#!/usr/bin/env python3
"""Minimal MCP server exposing a PDF page extraction tool.

This replaces the third-party pdf-reader MCP server that produced an
invalid JSON schema and caused Claude Desktop to reject the tool
configuration. The server is intentionally small and relies on the
`FastMCP` helper from the `mcp` package, which in turn uses type-hints to
generate JSON Schema Draft 2020-12 compliant input definitions.

The `extract_pdf_text` tool shells out to `pdftotext` (part of
`poppler`) to avoid introducing Python PDF dependencies. Page numbers are
one-based to match the CLI interface and human expectations.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Optional

from mcp.server.fastmcp import Context, FastMCP

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TIMEOUT_SECONDS = 30

server = FastMCP(
    name="Local PDF Reader",
    instructions="Extract text from local PDF files by page range using pdftotext.",
)


def _resolve_pdf_path(pdf_path: str) -> Path:
    """Resolve the PDF path relative to the project root, ensuring safety."""
    candidate = (PROJECT_ROOT / pdf_path).resolve()
    if not candidate.exists():
        raise ValueError(f"PDF not found: {pdf_path}")
    if candidate.suffix.lower() != ".pdf":
        raise ValueError("Only .pdf files are supported")
    if not str(candidate).startswith(str(PROJECT_ROOT)):
        raise ValueError("PDF path must stay within the project directory")
    return candidate


@server.tool(name="extract_pdf_text", title="Extract PDF Text")
def extract_pdf_text(
    pdf_path: str,
    start_page: int,
    end_page: Optional[int] = None,
    include_page_numbers: bool = False,
    context: Context | None = None,
) -> str:
    """Extract text from a PDF between inclusive page numbers.

    Args:
        pdf_path: Path to the PDF file relative to the project root.
        start_page: First page to extract (1-indexed).
        end_page: Last page to extract (1-indexed). Defaults to start_page.
        include_page_numbers: Prefix each page with "-- Page N --" markers.
        context: Optional MCP context for progress reporting and logging.
    """
    if start_page < 1:
        raise ValueError("start_page must be >= 1")
    if end_page is None:
        end_page = start_page
    if end_page < start_page:
        raise ValueError("end_page must be >= start_page")

    pdf_file = _resolve_pdf_path(pdf_path)

    if context is not None:
        context.debug(json.dumps({
            "pdf_path": str(pdf_file.relative_to(PROJECT_ROOT)),
            "start_page": start_page,
            "end_page": end_page,
        }))

    command = [
        "pdftotext",
        "-f",
        str(start_page),
        "-l",
        str(end_page),
        str(pdf_file),
        "-",
    ]

    try:
        result = subprocess.run(
            command,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=DEFAULT_TIMEOUT_SECONDS,
            text=True,
        )
    except FileNotFoundError as exc:  # pragma: no cover - depends on system
        raise RuntimeError("pdftotext command not found. Install poppler utils.") from exc
    except subprocess.TimeoutExpired as exc:
        raise TimeoutError("pdftotext call timed out") from exc
    except subprocess.CalledProcessError as exc:
        message = exc.stderr.strip() or "pdftotext failed"
        raise RuntimeError(message) from exc

    text = result.stdout

    if include_page_numbers:
        # pdftotext separates pages with formfeed characters. We split on that
        # marker so we can inject page headers that make the output easier to
        # scan inside Claude.
        pages = text.split("\f")
        pages = [page.strip() for page in pages if page.strip()]
        numbered_pages = []
        page_num = start_page
        for page_content in pages:
            header = f"-- Page {page_num} --"
            numbered_pages.append(f"{header}\n{page_content}")
            page_num += 1
        text = "\n\n".join(numbered_pages)

    cleaned = text.strip()
    if not cleaned:
        cleaned = "(No text extracted. The requested pages may be blank or scanned images.)"
    return cleaned


if __name__ == "__main__":
    server.run()

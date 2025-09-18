# PDF MCP Server Installation Guide

## Overview

This guide explains how to properly install and configure a local PDF MCP (Model Context Protocol) server that allows Claude Desktop to extract text from PDF files. This custom implementation replaces third-party PDF MCP servers that may have JSON schema compatibility issues.

## Prerequisites

### 1. System Dependencies

#### macOS (Homebrew)
```bash
# Install poppler (provides pdftotext command)
brew install poppler

# Verify installation
pdftotext -v
```

#### Ubuntu/Debian
```bash
# Install poppler-utils
sudo apt-get update
sudo apt-get install poppler-utils

# Verify installation
pdftotext -v
```

#### Other Linux Distributions
```bash
# Install poppler-utils (package name may vary)
# For Fedora/CentOS/RHEL:
sudo dnf install poppler-utils  # or yum/dnf

# For Arch Linux:
sudo pacman -S poppler

# Verify installation
pdftotext -v
```

### 2. Python Dependencies

The MCP server requires the `mcp` package with FastMCP support:

```bash
# Install MCP package (should already be available if using Claude Desktop)
pip install mcp
# or
pip3 install mcp
```

## Installation Steps

### Step 1: Create the MCP Server Directory

Create a `tools` directory in your project root (if it doesn't exist):

```bash
mkdir -p tools
```

### Step 2: Create the PDF MCP Server

Create the file `tools/pdf_reader_mcp.py` with the following content:

```python
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
```

### Step 3: Make the Script Executable

```bash
chmod +x tools/pdf_reader_mcp.py
```

### Step 4: Configure Claude Desktop

Create or update the `.mcp.json` file in your project root with the following content:

```json
{
  "mcpServers": {
    "pdf-reader-mcp": {
      "command": "python",
      "args": [
        "tools/pdf_reader_mcp.py"
      ],
      "name": "PDF Reader"
    }
  }
}
```

## Usage

### Basic Usage

Once configured, you can use the PDF reader in Claude Desktop with commands like:

```
/mcp pdf-reader-mcp extract_pdf_text pdf_path="IntroductiontoAlgorithmsFourthEdition.pdf" start_page=86 end_page=103 include_page_numbers=true
```

### Parameters

- `pdf_path`: Path to the PDF file relative to your project root (required)
- `start_page`: First page to extract (1-indexed, required)
- `end_page`: Last page to extract (1-indexed, optional, defaults to start_page)
- `include_page_numbers`: Whether to prefix each page with "-- Page N --" markers (optional, defaults to false)

### Example Commands

```bash
# Extract a single page
/mcp pdf-reader-mcp extract_pdf_text pdf_path="IntroductiontoAlgorithmsFourthEdition.pdf" start_page=86

# Extract multiple pages with page numbers
/mcp pdf-reader-mcp extract_pdf_text pdf_path="IntroductiontoAlgorithmsFourthEdition.pdf" start_page=86 end_page=103 include_page_numbers=true

# Extract discrete math content
/mcp pdf-reader-mcp extract_pdf_text pdf_path="Discrete Mathematics with Applications by Susanna S. Epp - 4th Edition.pdf" start_page=1 end_page=10
```

## Troubleshooting

### Common Issues

#### 1. "pdftotext command not found"
**Solution**: Install poppler utilities as described in Prerequisites section.

#### 2. "PDF not found" error
**Solution**: Ensure the PDF path is relative to your project root and the file exists.

#### 3. "Only .pdf files are supported" error
**Solution**: Make sure you're providing a path to a valid PDF file.

#### 4. "PDF path must stay within the project directory" error
**Solution**: The PDF file must be located within your project directory for security reasons.

#### 5. Empty output
**Solution**: Some PDFs may contain images instead of text, or the requested pages may be blank. Try different page ranges or check if the PDF contains selectable text.

### Verification Steps

#### Test the MCP Server Directly

```bash
# Test the server script directly
python tools/pdf_reader_mcp.py --help

# Or test the extraction function
python -c "
from tools.pdf_reader_mcp import extract_pdf_text
text = extract_pdf_text('IntroductiontoAlgorithmsFourthEdition.pdf', 86, 86, include_page_numbers=True)
print('Extracted text length:', len(text))
print('First 200 characters:')
print(text[:200])
"
```

#### Restart Claude Desktop

After updating the `.mcp.json` file, restart Claude Desktop to pick up the configuration changes.

## Security Considerations

- The MCP server only allows access to PDF files within the project directory
- All file paths are validated to prevent directory traversal attacks
- The server uses subprocess calls with timeouts to prevent hanging

## Alternative Installation Methods

### Using Third-Party MCP Servers

If you prefer not to maintain a custom server, you can try other MCP servers, but be aware of potential JSON schema compatibility issues:

```bash
# Example using npx (may have schema issues)
npm install -g @sylphlab/pdf-reader-mcp
```

Then update your `.mcp.json`:

```json
{
  "mcpServers": {
    "pdf-reader-mcp": {
      "command": "npx",
      "args": ["@sylphlab/pdf-reader-mcp"],
      "name": "PDF Reader"
    }
  }
}
```

However, this custom implementation is recommended as it:
- Uses JSON Schema Draft 2020-12 compliant type hints
- Has minimal dependencies (only requires `pdftotext`)
- Includes proper error handling and security validation
- Is fully self-contained within your project

## Support

If you encounter issues:

1. Verify all prerequisites are installed
2. Check that the `tools/pdf_reader_mcp.py` file exists and is executable
3. Ensure the `.mcp.json` configuration is correct
4. Restart Claude Desktop after configuration changes
5. Test the server directly using the verification steps above

The custom MCP server provides reliable PDF text extraction with proper schema compliance and security measures.

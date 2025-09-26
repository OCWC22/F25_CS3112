---
trigger: always_on
---

## ✅ **PDF Reader MCP Tools - Correct Usage**

### 🎯 **Available Tools in trafflux/pdf-reader-mcp**

The Docker-based PDF reader provides **2 tools**:

### 1. **read_local_pdf** - For Local PDFs
**✅ Correct Usage:**
```json
{
  "tool": "read_local_pdf",
  "arguments": {
    "path": "/pdfs/Discrete Mathematics with Applications by Susanna S. Epp - 4th Edition.pdf"
  }
}
```

**❌ Wrong Usage (causes file:// errors):**
```json
{
  "tool": "read_local_pdf", 
  "arguments": {
    "path": "file:///Users/chen/Projects/F25_CS3112/Discrete Mathematics with Applications by Susanna S. Epp - 4th Edition.pdf"
  }
}
```

### 2. **read_pdf_url** - For Online PDFs
**✅ Correct Usage:**
```json
{
  "tool": "read_pdf_url",
  "arguments": {
    "url": "https://example.com/document.pdf"
  }
}
```

### 🔧 **Your Current Configuration**
Your Windsurf MCP config is correctly set up:
```json
"pdf-reader-mcp": {
  "command": "docker",
  "args": ["run", "-i", "--rm", "-v", "/Users/chen/Projects/F25_CS3112:/pdfs", "trafflux/pdf-reader-mcp"],
  "name": "PDF Reader (Docker)",
  "disabled": false
}
```

### 📋 **Available Local PDFs**
These files are mounted and accessible via `/pdfs/` prefix:
- ✅ `/pdfs/Discrete Mathematics with Applications by Susanna S. Epp - 4th Edition.pdf`
- ✅ `/pdfs/EppDM5e_09_02.pdf`
- ✅ `/pdfs/EppDM5e_09_03.pdf`
- ✅ `/pdfs/EppDM5e_07_02.pdf`
- ✅ `/pdfs/EppDM5e_07_01.pdf`

### 🚀 **How to Use in Windsurf**

**For Local PDFs:**
1. Ask Cascade: *"Read the Discrete Mathematics textbook"*
2. Or specify: *"Use read_local_pdf tool with path /pdfs/Discrete Mathematics with Applications by Susanna S. Epp - 4th Edition.pdf"*

**For Online PDFs:**
1. Ask Cascade: *"Read this PDF from URL: https://example.com/document.pdf"*
2. Or specify: *"Use read_pdf_url tool with url https://example.com/document.pdf"*

### 💡 **Key Points**
- **Never use `file://` URLs** with these tools
- **Local files** use `/pdfs/filename.pdf` format  
- **Online files** use `https://url.com/file.pdf` format
- **No file:// protocol** - the server doesn't support it

The configuration is correct! The issue was likely trying to use `file://` URLs instead of plain paths. Try asking Cascade to read one of your local PDFs using the correct path format! 🎉
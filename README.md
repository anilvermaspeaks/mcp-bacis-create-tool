# 🧠 MCP Basic Create Tool

A minimal **Model Context Protocol (MCP)** project demonstrating how to create and register tools using the [`fastmcp`](https://pypi.org/project/fastmcp/) framework.

This repository shows how to build a working **MCP server** that can expose Python functions as tools for AI clients like **Claude Desktop** or any other MCP-compatible app.

---

## 🚀 Features

- Simple MCP server setup using `FastMCP`
- Example tool implementation (`get_weather`)
- Easy to extend with more tools
- Ready for integration with Claude or ChatGPT (via MCP)

---

### 1️⃣ Clone the repository
```bash
git clone https://github.com/anilvermaspeaks/mcp-bacis-create-tool.git
cd mcp-bacis-create-tool

 Create and activate a virtual environment
python -m venv basics-mcp


To connect this tool to Claude Desktop, add the following entry inside your Claude configuration file:

Config path:

Windows → %APPDATA%\Claude\claude_desktop_config.json

macOS → ~/Library/Application Support/Claude/claude_desktop_config.json

Add this JSON snippet:

{
  "mcpServers": {
    "mcp-bacis-create-tool": {
      "command": "python",
      "args": [
        "D:/basics-mcp/main.py"
      ],
      "env": {
        "PYTHONPATH": "D:/basics-mcp"
      }
    }
  }
}
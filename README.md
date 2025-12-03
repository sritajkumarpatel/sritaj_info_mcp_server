# Sritaj Info MCP Server

A Model Context Protocol (MCP) server providing information services.

![Python](https://img.shields.io/badge/Python-3.13+-blue)
![MCP](https://img.shields.io/badge/MCP-1.23.1+-green)

## Technologies

- **Python**: >=3.13
- **MCP Framework**: mcp[cli] >=1.23.1
- **Build System**: setuptools
- **Package Manager**: uv (recommended) or pip

## Project Structure

```
sritaj_info_mcp_server/
├── main.py                 # Main entry point (optional)
├── pyproject.toml          # Project configuration and dependencies
├── README.md               # This file
└── src/
    └── mcpserver/
        ├── __init__.py     # Package initialization
        ├── __main__.py     # CLI entry point
        └── sritaj_info_server.py  # Main server implementation
```

## Setup

1. Ensure Python >=3.13 is installed.
2. Create and activate a virtual environment:
   - Using uv (recommended):
     ```
     uv sync  # Creates .venv and installs dependencies
     ```
     To activate the environment (optional, as uv commands work without explicit activation):
     ```
     .venv\Scripts\activate  # On Windows
     ```
   - Using venv (alternative):
     ```
     python -m venv .venv
     .venv\Scripts\activate  # On Windows
     pip install -e .
     ```

## Running

To run the MCP server:
```
uv run .\src\mcpserver\__main__.py
```

This starts the server and makes it available for MCP clients.

## Using in VS Code Local MCP Server

To integrate this MCP server with VS Code's local MCP setup, add the following configuration to your VS Code MCP settings file:

```json
"sritaj_info_server": {
  "command": "uv",
  "args": [
    "run",
    "{Path}}sritaj_info_mcp_server\\src\\mcpserver\\__main__.py"
  ],
  "env": {}
}
```

Replace `{Path}` with the absolute path to your project directory (e.g., `C:\\AI\\`).

## Development

- Edit source files in `src/mcpserver/`
- Run tests (if any) after changes
- Update dependencies in `pyproject.toml` as needed
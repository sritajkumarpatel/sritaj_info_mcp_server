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
2. Install dependencies using uv (recommended):
   ```
   uv sync
   ```
   Or using pip:
   ```
   pip install -e .
   ```

## Running

To run the MCP server:
```
uv run .\src\mcpserver\__main__.py
```

This starts the server and makes it available for MCP clients.

## Development

- Edit source files in `src/mcpserver/`
- Run tests (if any) after changes
- Update dependencies in `pyproject.toml` as needed
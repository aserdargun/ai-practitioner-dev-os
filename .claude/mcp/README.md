# MCP (Model Context Protocol)

This folder contains Model Context Protocol configurations, tool contracts, and examples for programmatic interaction with the learning system.

## Contents

| File/Folder | Purpose |
|-------------|---------|
| [tool-contracts.md](tool-contracts.md) | Tool schemas and constraints |
| [examples.md](examples.md) | How agents use tools |
| [safety.md](safety.md) | Security and privacy guidelines |
| [server_stub/](server_stub/) | Example MCP server implementation |
| [client_examples/](client_examples/) | Example client code |

## What is MCP?

Model Context Protocol (MCP) is a standard for how AI models interact with external tools and data sources. In this learning system, MCP provides:

1. **Structured tool access**: Well-defined interfaces for reading/writing data
2. **Safety constraints**: Guardrails on what operations are allowed
3. **Interoperability**: Standard format for tool definitions

## Available Tools

### hello

Simple test tool to verify MCP connectivity.

**Input**: None
**Output**: Greeting message

### read_repo_file

Read files from the repository (safe subset).

**Input**: `{"path": "string"}`
**Output**: File contents
**Constraints**: Only allows reading from safe directories

### write_memory_entry

Append entries to memory files.

**Input**: `{"file": "string", "entry": "object"}`
**Output**: Confirmation
**Constraints**: Append-only to `.claude/memory/` files

## Quick Start

### Running the Server

```bash
cd .claude/mcp/server_stub
pip install -r requirements.txt  # if requirements exist
python server.py
```

### Using the Client

```python
from client_examples.python_client import MCPClient

client = MCPClient("http://localhost:8000")
response = client.call_tool("hello", {})
print(response)
```

## Documentation

- [Tool Contracts](tool-contracts.md) - Full tool specifications
- [Examples](examples.md) - Usage patterns
- [Safety](safety.md) - Security guidelines

# MCP Server Stub

A reference implementation of an MCP server for the learning OS.

## Overview

This server exposes three tools:
- `hello` — Test connectivity
- `read_repo_file` — Read files safely
- `write_memory_entry` — Append to memory files

## Requirements

- Python 3.9+
- No external dependencies (stdlib only)

## Running the Server

```bash
# From repository root
python .claude/mcp/server_stub/server.py

# With custom port
python .claude/mcp/server_stub/server.py --port 8080
```

Default port: 5000

## API

### Health Check

```
GET /health
```

Response:
```json
{"status": "healthy", "timestamp": "2026-01-15T10:00:00Z"}
```

### Tool Call

```
POST /tools/{tool_name}
Content-Type: application/json

{
  "parameters": {...}
}
```

Response:
```json
{
  "success": true,
  "result": {...}
}
```

### List Tools

```
GET /tools
```

Response:
```json
{
  "tools": ["hello", "read_repo_file", "write_memory_entry"]
}
```

## Example Usage

```bash
# Health check
curl http://localhost:5000/health

# Hello tool
curl -X POST http://localhost:5000/tools/hello \
  -H "Content-Type: application/json" \
  -d '{"parameters": {"name": "Learner"}}'

# Read file
curl -X POST http://localhost:5000/tools/read_repo_file \
  -H "Content-Type: application/json" \
  -d '{"parameters": {"path": ".claude/memory/progress_log.jsonl"}}'
```

## Security

This is a **stub implementation** for learning purposes.

For production use:
- Add authentication
- Use HTTPS
- Implement rate limiting
- Add comprehensive logging
- Run in isolated environment

## See Also

- [../tool-contracts.md](../tool-contracts.md) — Tool specifications
- [../safety.md](../safety.md) — Security guidelines
- [../client_examples/](../client_examples/) — Client implementations

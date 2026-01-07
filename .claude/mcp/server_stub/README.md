# MCP Server Stub

A minimal MCP server implementation for the AI Practitioner Learning OS.

## Overview

This server provides a simple HTTP interface to the MCP tools:
- `hello` - Test connectivity
- `read_repo_file` - Read files from the repository
- `write_memory_entry` - Append to memory files

## Requirements

- Python 3.9+
- No external dependencies (uses stdlib only)

## Running the Server

```bash
cd .claude/mcp/server_stub
python server.py
```

The server starts on `http://localhost:8765` by default.

## API

### POST /tools/{tool_name}

Call a tool with input parameters.

**Request**:
```json
{
  "input": {
    "param1": "value1"
  }
}
```

**Response**:
```json
{
  "result": {
    "output1": "value1"
  }
}
```

### GET /tools

List available tools.

**Response**:
```json
{
  "tools": ["hello", "read_repo_file", "write_memory_entry"]
}
```

### GET /health

Health check.

**Response**:
```json
{
  "status": "healthy"
}
```

## Example Usage

```bash
# Health check
curl http://localhost:8765/health

# List tools
curl http://localhost:8765/tools

# Call hello tool
curl -X POST http://localhost:8765/tools/hello \
  -H "Content-Type: application/json" \
  -d '{"input": {}}'

# Read a file
curl -X POST http://localhost:8765/tools/read_repo_file \
  -H "Content-Type: application/json" \
  -d '{"input": {"path": "README.md"}}'

# Write memory entry
curl -X POST http://localhost:8765/tools/write_memory_entry \
  -H "Content-Type: application/json" \
  -d '{"input": {"file": "progress_log.jsonl", "entry": {"timestamp": "2026-01-07T10:00:00Z", "event": "test"}}}'
```

## Configuration

Environment variables:
- `MCP_PORT` - Port to listen on (default: 8765)
- `MCP_HOST` - Host to bind to (default: localhost)
- `REPO_ROOT` - Repository root path (default: ../../../)

## Security Notes

This is a **stub implementation** for learning purposes:
- No authentication
- Limited path validation
- Not for production use

For production, implement proper:
- Authentication/authorization
- Input validation
- Rate limiting
- HTTPS

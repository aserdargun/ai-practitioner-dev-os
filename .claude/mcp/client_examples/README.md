# MCP Client Examples

Example client implementations for interacting with the MCP server.

## Available Examples

| File | Language | Description |
|------|----------|-------------|
| [python_client.py](python_client.py) | Python | Simple Python client |

## Usage

### Python Client

```python
from python_client import MCPClient

# Create client
client = MCPClient("http://localhost:8765")

# Test connectivity
response = client.hello()
print(response)  # {"message": "Hello from AI Practitioner Learning OS!", ...}

# Read a file
content = client.read_file("README.md")
print(content[:100])  # First 100 chars of README

# Write a memory entry
client.log_progress({
    "event": "task_completed",
    "task": "Review MCP documentation"
})
```

### Running the Examples

1. Start the MCP server:
   ```bash
   cd .claude/mcp/server_stub
   python server.py
   ```

2. In another terminal, run the client:
   ```bash
   cd .claude/mcp/client_examples
   python python_client.py
   ```

## Implementing Your Own Client

The MCP server uses a simple HTTP/JSON API:

### Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | /health | Health check |
| GET | /tools | List available tools |
| POST | /tools/{name} | Call a tool |

### Calling a Tool

```http
POST /tools/hello HTTP/1.1
Host: localhost:8765
Content-Type: application/json

{"input": {}}
```

Response:
```json
{
  "result": {
    "message": "Hello from AI Practitioner Learning OS!",
    "timestamp": "2026-01-07T10:00:00Z"
  }
}
```

### Error Handling

Errors return:
```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable message"
  }
}
```

Common error codes:
- `INVALID_INPUT` - Bad input parameters
- `PATH_NOT_ALLOWED` - Tried to access blocked path
- `FILE_NOT_FOUND` - File doesn't exist
- `TOOL_NOT_FOUND` - Unknown tool name

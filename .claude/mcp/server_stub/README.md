# MCP Server Stub

A minimal MCP server implementation for the learning OS.

## Overview

This server exposes three tools:
1. `hello` - Simple greeting (for testing)
2. `read_repo_file` - Read allowed files from the repo
3. `write_memory_entry` - Append to memory files

## Requirements

- Python 3.11+
- No external dependencies (stdlib only)

## Quick Start

```bash
# Run the server
python server.py

# Server listens on stdin/stdout (MCP protocol)
```

## Tools

### hello

Simple greeting for testing connectivity.

```json
{"tool": "hello", "input": {"name": "World"}}
// Response: {"greeting": "Hello, World!"}
```

### read_repo_file

Read a file from the repository (restricted paths).

```json
{"tool": "read_repo_file", "input": {"path": "docs/how-to-use.md"}}
// Response: {"content": "...", "size": 1234}
```

Allowed paths:
- `docs/**`
- `paths/**`
- `stacks/**`
- `.claude/memory/**`
- Root docs (`README.md`, `CLAUDE.md`)

### write_memory_entry

Append an entry to a memory file (append-only).

```json
{
  "tool": "write_memory_entry",
  "input": {
    "file": "progress_log.jsonl",
    "entry": {
      "timestamp": "2026-01-09T12:00:00Z",
      "type": "task_complete",
      "task": "Example task"
    }
  }
}
// Response: {"success": true, "line_number": 5}
```

Allowed files:
- `progress_log.jsonl`
- `decisions.jsonl`

## Integration

This is a stub for learning purposes. In production:
1. Add proper authentication
2. Use a real transport (HTTP, WebSocket)
3. Add comprehensive logging
4. Implement rate limiting

## Testing

```bash
# Test the server manually
echo '{"tool": "hello", "input": {"name": "Test"}}' | python server.py
```

## Extending

To add a new tool:

1. Add the handler function:
```python
def handle_my_tool(input_data: dict) -> dict:
    # Validate input
    # Perform operation
    # Return result
    pass
```

2. Register in `TOOL_HANDLERS`:
```python
TOOL_HANDLERS = {
    "hello": handle_hello,
    "read_repo_file": handle_read_repo_file,
    "write_memory_entry": handle_write_memory_entry,
    "my_tool": handle_my_tool,  # Add here
}
```

3. Document in `../tool-contracts.md`

# MCP Server Stub

A minimal MCP server implementation for the learning OS.

## Purpose

This server provides MCP tools for:
- Testing MCP connectivity
- Reading repository files safely
- Appending to memory files

## Running the Server

```bash
cd .claude/mcp/server_stub
python server.py
```

The server runs on stdio by default, suitable for integration with Claude.

## Tools Provided

### hello
Simple test tool to verify connectivity.

### read_repo_file
Read files from allowed paths in the repository.

### write_memory_entry
Append entries to memory files (progress_log.jsonl, decisions.jsonl, best_practices.md).

## Configuration

Edit the `ALLOWED_PATHS` and `DENIED_PATHS` lists in `server.py` to customize access control.

## Testing

```bash
# Test with the client example
python ../client_examples/python_client.py
```

## Integration

To integrate with Claude Code, add to your MCP configuration:

```json
{
  "mcpServers": {
    "learning-os": {
      "command": "python",
      "args": [".claude/mcp/server_stub/server.py"],
      "cwd": "/path/to/your/repo"
    }
  }
}
```

## Security Notes

- This is a stub implementation for learning purposes
- Review `safety.md` before deploying in any real environment
- All writes should prompt for user confirmation

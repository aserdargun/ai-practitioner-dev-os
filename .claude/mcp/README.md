# MCP — Model Context Protocol

This folder contains Model Context Protocol (MCP) integration for the learning OS.

## What is MCP?

MCP is a protocol that allows AI assistants like Claude to use external tools safely. It defines how tools are discovered, called, and how results are returned.

## Contents

| File/Folder | Purpose |
|-------------|---------|
| `tool-contracts.md` | Schemas and constraints for available tools |
| `examples.md` | How agents use tools |
| `safety.md` | Security, privacy, and safety guidelines |
| `server_stub/` | Example MCP server implementation |
| `client_examples/` | Example client code |

## Available Tools

The learning OS provides these MCP tools:

### hello
A simple test tool to verify MCP is working.
```
Input: { "name": "string" }
Output: { "greeting": "string" }
```

### read_repo_file
Read files from the repository (safe subset).
```
Input: { "path": "string" }
Output: { "content": "string" }
Constraints: Only reads from allowed directories
```

### write_memory_entry
Append entries to memory files.
```
Input: { "file": "string", "entry": "object" }
Output: { "success": "boolean" }
Constraints: Append-only to .claude/memory/
```

## Safety Principles

1. **Least Privilege**: Tools only access what they need
2. **Append-Only**: Memory writes don't overwrite
3. **Safe Paths**: File access limited to repository
4. **No Secrets**: Tools never expose credentials
5. **Human Review**: Critical operations require approval

See `safety.md` for detailed guidelines.

## Running the Server

### Local Development
```bash
cd .claude/mcp/server_stub
python server.py
```

### Testing Tools
```bash
# Using the client example
python .claude/mcp/client_examples/python_client.py
```

## Integration with Agents

Agents can use MCP tools when:
- Gathering information (read_repo_file)
- Logging progress (write_memory_entry)
- Testing connectivity (hello)

See `examples.md` for usage patterns.

## Extending MCP

To add new tools:
1. Define the schema in `tool-contracts.md`
2. Implement the handler in `server_stub/server.py`
3. Add safety rules in `safety.md`
4. Create usage examples in `examples.md`

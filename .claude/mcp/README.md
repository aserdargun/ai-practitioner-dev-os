# MCP (Model Context Protocol)

Tool contracts, safety guidelines, and example implementations for extending Claude's capabilities.

## Overview

MCP allows Claude to interact with external tools and services. This folder contains:

| File | Purpose |
|------|---------|
| [tool-contracts.md](tool-contracts.md) | Tool schemas and constraints |
| [examples.md](examples.md) | How agents use tools |
| [safety.md](safety.md) | Security and privacy guidelines |
| [server_stub/](server_stub/) | Example MCP server implementation |
| [client_examples/](client_examples/) | Client code examples |

## What is MCP?

The Model Context Protocol is a standard for:
- Defining tools that LLMs can call
- Specifying input/output schemas
- Enforcing safety constraints
- Managing tool execution

## Available Tools

### Core Tools (in server_stub)

| Tool | Purpose | Scope |
|------|---------|-------|
| `hello` | Test connectivity | Read-only |
| `read_repo_file` | Read files from safe paths | Read-only |
| `write_memory_entry` | Append to memory files | Append-only |

## Using MCP

### For Learning

1. Review [tool-contracts.md](tool-contracts.md) to understand schemas
2. Study [examples.md](examples.md) for usage patterns
3. Read [safety.md](safety.md) for security considerations
4. Explore the [server_stub](server_stub/) implementation

### For Extending

1. Define new tool contracts
2. Implement server handlers
3. Add safety constraints
4. Test thoroughly
5. Document usage

## Safety Principles

From [safety.md](safety.md):

1. **Least Privilege**: Tools have minimal necessary permissions
2. **Explicit Consent**: User approves tool calls
3. **Audit Trail**: All tool calls are logged
4. **Safe Defaults**: Fail closed, not open

## Related Documentation

- [docs/system-overview.md](../../docs/system-overview.md) — How MCP fits in the system
- [server_stub/README.md](server_stub/README.md) — Server implementation guide
- [client_examples/README.md](client_examples/README.md) — Client usage examples

# MCP (Model Context Protocol)

This folder contains tool contracts, safety guidelines, and stubs for MCP integration.

## Overview

MCP provides a standardized way for Claude to interact with external tools and data sources. This learning OS includes basic MCP infrastructure for advanced learners.

## Contents

| File | Purpose |
|------|---------|
| `tool-contracts.md` | Schemas and constraints for tools |
| `examples.md` | How agents use tools |
| `safety.md` | Security, privacy, and integrity guidelines |
| `server_stub/` | Example MCP server implementation |
| `client_examples/` | Example client code |

## What is MCP?

Model Context Protocol is a specification for:
- Defining tools that LLMs can use
- Standardizing input/output formats
- Managing tool permissions and safety

## When to Use MCP

As an Advanced learner, you'll encounter MCP when:
- Building agent systems that need external tools
- Creating custom integrations
- Implementing safe tool execution

## Server Stub

The `server_stub/` folder contains a minimal MCP server with three tools:

1. **hello** - Simple greeting tool (for testing)
2. **read_repo_file** - Read files from the repo (safe subset)
3. **write_memory_entry** - Append to memory files

See `server_stub/README.md` for setup instructions.

## Client Examples

The `client_examples/` folder shows how to call MCP tools from Python.

## Safety First

Before building with MCP, read `safety.md` for:
- Secret management
- Input validation
- Scope limitations
- Eval integrity

## Further Reading

- [MCP Specification](https://github.com/anthropics/anthropic-cookbook/tree/main/mcp)
- Tool contracts: `tool-contracts.md`
- Safety guidelines: `safety.md`

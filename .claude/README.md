# .claude/ — Claude Code Capabilities

This folder contains all Claude Code capabilities for the AI Practitioner Learning OS.

## Overview

The `.claude/` folder is the heart of the AI-assisted learning system. It contains:

| Folder | Purpose |
|--------|---------|
| `agents/` | Advisory agent definitions (Planner, Builder, Reviewer, Evaluator, Coach, Researcher) |
| `commands/` | Slash command definitions for `/status`, `/plan-week`, `/evaluate`, etc. |
| `skills/` | Playbook-style skills for common tasks (EDA, RAG, API shipping, etc.) |
| `hooks/` | Shell scripts that run at key lifecycle moments |
| `memory/` | Local memory store (learner profile, progress log, decisions, best practices) |
| `mcp/` | Model Context Protocol tool contracts, stubs, and examples |
| `path-engine/` | Python scripts for evaluation, adaptation, and reporting |

## Human-in-the-Loop Requirement

**All agents provide recommendations that require explicit user approval before execution.**

The evaluation loop is:
1. **Evaluate** → Compute scores from memory + repo signals
2. **Present recommendations** → Show proposed changes to the user
3. **User approves** → User explicitly confirms each change
4. **Execute** → Apply only the approved changes

No path modifications, project swaps, or level changes occur without explicit user approval.

## Quick Links

- **Agents**: See [agents/README.md](agents/README.md)
- **Commands**: See [commands/README.md](commands/README.md) and [commands/catalog.md](commands/catalog.md)
- **Skills**: See [skills/README.md](skills/README.md)
- **Hooks**: See [hooks/README.md](hooks/README.md)
- **Memory**: See [memory/README.md](memory/README.md)
- **MCP**: See [mcp/README.md](mcp/README.md)
- **Path Engine**: See [path-engine/README.md](path-engine/README.md)

## Usage with Claude Code

In Claude Code, you can invoke commands using slash syntax:

```
/status
/plan-week
/evaluate
/adapt-path
```

See [../docs/commands.md](../docs/commands.md) for the friendly guide.

## Memory System Architecture

```
.claude/memory/
├── learner_profile.json   # Goals, constraints, schedule (append-only)
├── progress_log.jsonl     # Timestamped events (append-only)
├── decisions.jsonl        # Important decisions (append-only)
└── best_practices.md      # Living doc of learned best practices
```

**Important**: Memory files are append-only sources of truth. The tracker at `paths/advanced/tracker.md` is a derived artifact that `report.py` may regenerate at any time (with user confirmation).

## Path Engine

The path engine implements the recommendation loop using Python stdlib only:

```bash
python .claude/path-engine/evaluate.py   # Compute scores
python .claude/path-engine/adapt.py      # Propose adaptations (user approves)
python .claude/path-engine/report.py     # Update tracker
```

See [path-engine/README.md](path-engine/README.md) for details.

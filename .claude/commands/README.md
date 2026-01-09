# Commands

This folder contains slash command definitions for the AI Practitioner Learning OS.

## Overview

Commands are shortcuts you can use in Claude Code to invoke specific functionality. Each command is defined in its own `.md` file and routes to an appropriate agent.

## Available Commands

| Command | Purpose | Agent |
|---------|---------|-------|
| `/status` | Check current progress and blockers | Planner |
| `/plan-week` | Create a week plan | Planner |
| `/start-week` | Begin executing the week plan | Builder |
| `/ship-mvp` | Finalize and ship the MVP | Builder + Reviewer |
| `/harden` | Review and improve code quality | Reviewer |
| `/publish` | Prepare for external publishing | Reviewer |
| `/retro` | Run a retrospective | Coach |
| `/evaluate` | Assess progress and compute scores | Evaluator |
| `/adapt-path` | Propose path adaptations | Evaluator |
| `/add-best-practice` | Add a learned best practice | Coach |
| `/debug-learning` | Get help when stuck | Coach |

## Command Catalog

See [catalog.md](catalog.md) for the full index with details.

## How to Use Commands

In Claude Code, simply type the command:

```
/status
```

Claude will assume the appropriate agent role and execute the command.

## Command Format

Each command file follows this structure:

```markdown
# Command: /command-name

## Purpose
What this command does

## Inputs
What the user needs to provide

## Outputs
What artifacts are produced

## When to Use
Appropriate scenarios

## Agent Routing
Which agent handles this

## Example Usage
Copy-paste example
```

## Extending Commands

To add a new command:

1. Create a new `.md` file in this folder (e.g., `my-command.md`)
2. Follow the command format above
3. Add it to `catalog.md`
4. Update `../../docs/commands.md` if needed

## Human-in-the-Loop

All commands that modify state require user approval:
- Planner commands show plans for approval
- Builder commands show code changes for approval
- Evaluator commands show proposals for approval

No changes are applied without explicit user confirmation.

# Commands

This folder contains slash command definitions for Claude Code. Each `.md` file defines a command that can be invoked with `/command-name`.

## How Commands Work

1. In Claude Code, type `/command-name`
2. Claude reads the command definition from this folder
3. Claude executes the command logic with appropriate agent routing
4. Results are presented for your review/approval

## Available Commands

| Command | File | Purpose |
|---------|------|---------|
| `/status` | [status.md](status.md) | Current progress snapshot |
| `/plan-week` | [plan-week.md](plan-week.md) | Generate weekly plan |
| `/start-week` | [start-week.md](start-week.md) | Begin week with setup |
| `/ship-mvp` | [ship-mvp.md](ship-mvp.md) | MVP completion checklist |
| `/harden` | [harden.md](harden.md) | Code quality focus |
| `/publish` | [publish.md](publish.md) | Demo and write-up prep |
| `/retro` | [retro.md](retro.md) | Weekly retrospective |
| `/evaluate` | [evaluate.md](evaluate.md) | Performance assessment |
| `/adapt-path` | [adapt-path.md](adapt-path.md) | Request path change |
| `/add-best-practice` | [add-best-practice.md](add-best-practice.md) | Document a learning |
| `/debug-learning` | [debug-learning.md](debug-learning.md) | Troubleshoot blockers |

See [catalog.md](catalog.md) for the complete reference.

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
Scenarios for this command

## Agent Routing
Which agent handles this

## Example Usage
Copy-paste prompt
```

## Adding New Commands

1. Create a new `.md` file in this folder
2. Follow the format above
3. Update [catalog.md](catalog.md) with the new command
4. Update [../../docs/commands.md](../../docs/commands.md)

## Related Documentation

- [catalog.md](catalog.md) — Complete command reference
- [docs/commands.md](../../docs/commands.md) — User-friendly guide

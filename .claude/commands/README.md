# Commands

This folder contains Claude Code slash commands for the learning OS.

## How Commands Work

Each `.md` file in this folder defines a command that you can invoke with `/command-name`:
- `/status` → `status.md`
- `/plan-week` → `plan-week.md`
- `/evaluate` → `evaluate.md`

## Available Commands

| Command | Purpose | Agent |
|---------|---------|-------|
| `/status` | Show current progress snapshot | Evaluator |
| `/plan-week` | Create weekly plan | Planner |
| `/start-week` | Initialize new week structure | Planner |
| `/ship-mvp` | Finalize MVP deliverables | Builder |
| `/harden` | Add tests, docs, error handling | Builder + Reviewer |
| `/publish` | Prepare demo and write-up | Builder |
| `/retro` | Run retrospective | Coach + Reviewer |
| `/evaluate` | Get evaluation scores | Evaluator |
| `/adapt-path` | See adaptation proposals | Evaluator |
| `/add-best-practice` | Capture a learning | Coach |
| `/debug-learning` | Diagnose blockers | Coach |

See `catalog.md` for the full reference.

## Command Format

Each command file follows this structure:

```markdown
# Command: /command-name

## Purpose
What this command does

## Inputs
What the user needs to provide

## Outputs
What artifacts or results are produced

## When to Use
Scenarios when this command is appropriate

## Agent Routing
Which agent handles this command

## Example Usage
Copy-paste example prompt
```

## Using Commands

### In Claude Code
Simply type the command:
```
/status
```

### With Arguments
Some commands accept context:
```
/plan-week focus on data pipeline, I have 8 hours
```

## Creating New Commands

1. Create a new `.md` file in this folder
2. Follow the format above
3. Add an entry to `catalog.md`
4. Test the command in Claude Code

## Best Practices

- Use commands for repeatable workflows
- Commands should produce consistent, structured output
- Combine commands for complex workflows:
  ```
  /status then /plan-week then /start-week
  ```

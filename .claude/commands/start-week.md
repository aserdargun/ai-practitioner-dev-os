# Command: /start-week

## Purpose

Initialize a new week with project setup, tracker updates, and environment preparation.

## Inputs

None required, but you can specify:
- Week number (if not continuing sequentially)
- Special focus areas

The command reads from:
- Current week plan
- `.claude/memory/learner_profile.json`
- Project template (if starting new project)

## Outputs

- Week plan stub created/updated
- Tracker updated with week start
- Environment checklist
- First task ready to begin

**Note**: Changes are proposed for your approval.

## When to Use

- First day of a new week
- Starting a new month's project
- Returning from a break

## Agent Routing

**Primary**: Planner Agent
**Secondary**: Builder Agent (for project setup)

## Example Usage

```
/start-week
```

Or with context:

```
/start-week

Starting Month 4's project. I want to use the FastAPI template.
```

## Output Format

```markdown
## Week Start — Month X, Week Y

### Setup Checklist
- [ ] Week plan reviewed/created
- [ ] Tracker updated
- [ ] Project directory ready
- [ ] Dependencies installed
- [ ] Tests running

### Environment Status
- Python: [version]
- Virtual env: [status]
- Dependencies: [status]

### First Task
Ready to begin: [task description]

### Quick Commands
```bash
# Activate environment
source venv/bin/activate

# Run tests
pytest

# Start development
[relevant command]
```

---
**Proceed with setup?** (yes/no)
```

## What Happens

1. **Creates week plan stub** in journal if not exists
2. **Updates tracker** with week start timestamp
3. **Checks project setup** (if new project)
4. **Runs pre_week_start hook** (if enabled)
5. **Logs start event** to progress_log.jsonl

## Hooks Integration

This command triggers `.claude/hooks/pre_week_start.sh`:
- Creates journal entry stub
- Updates tracker with current week
- Verifies environment

See [../hooks/README.md](../hooks/README.md) for details.

# Hooks

This folder contains automation scripts that run at specific points in the learning workflow.

## Available Hooks

| Hook | File | Trigger |
|------|------|---------|
| Pre-Week Start | [pre_week_start.sh](pre_week_start.sh) | Beginning of each week |
| Post-Week Review | [post_week_review.sh](post_week_review.sh) | End of each week |
| Pre-Publish Check | [pre_publish_check.sh](pre_publish_check.sh) | Before publishing work |

## How to Use

### Running Hooks

From the repository root:

```bash
# Start of week
bash .claude/hooks/pre_week_start.sh

# End of week
bash .claude/hooks/post_week_review.sh

# Before publishing
bash .claude/hooks/pre_publish_check.sh
```

### When Hooks Run

| Hook | When | Purpose |
|------|------|---------|
| `pre_week_start.sh` | Monday morning | Set up the week |
| `post_week_review.sh` | Friday evening | Reflect on the week |
| `pre_publish_check.sh` | Before demo/publish | Quality checks |

## Cross-Platform Compatibility

These hooks are shell scripts intended for:
- **Linux**: Works natively
- **macOS**: Works natively
- **Windows**: Use WSL (recommended) or Git Bash

### Manual Fallback (Windows without WSL)

If you cannot run `.sh` scripts, see the manual steps in each hook file or in [docs/hooks.md](../../docs/hooks.md).

## Hook Details

### pre_week_start.sh

Creates a week plan stub and updates the tracker:
1. Creates journal entry for the week
2. Updates tracker with week start
3. Runs status check

### post_week_review.sh

Prompts for retrospective and updates progress:
1. Prompts for reflection inputs
2. Updates progress log
3. Triggers evaluation

### pre_publish_check.sh

Runs quality checks before publishing:
1. Runs tests (pytest)
2. Runs linter (ruff)
3. Checks documentation links
4. Validates memory files

## Customizing Hooks

You can modify these hooks to fit your workflow. Just ensure:
- They remain idempotent (safe to run multiple times)
- They update the correct memory files
- They don't break the evaluation loop

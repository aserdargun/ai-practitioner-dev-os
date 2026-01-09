# Hooks

Shell scripts that run at lifecycle events in your learning journey.

## Available Hooks

| Hook | File | When It Runs |
|------|------|--------------|
| Pre Week Start | `pre_week_start.sh` | Before starting a new week |
| Post Week Review | `post_week_review.sh` | After completing a week |
| Pre Publish Check | `pre_publish_check.sh` | Before publishing a project |

## How Hooks Work

Hooks are simple shell scripts that automate common tasks:
- Create file structures
- Run checks and validations
- Update tracking files
- Prompt for input

## Running Hooks

### Linux/macOS
```bash
chmod +x .claude/hooks/pre_week_start.sh
./.claude/hooks/pre_week_start.sh
```

### Windows (Git Bash or WSL)
```bash
bash .claude/hooks/pre_week_start.sh
```

### Windows (PowerShell)
See "Manual Fallback" sections in each hook file for equivalent commands.

## Cross-Platform Notes

These hooks are shell scripts (`.sh`) intended for:
- Linux
- macOS
- Windows via WSL (Windows Subsystem for Linux)
- Windows via Git Bash

If you cannot run shell scripts, each hook includes a **Manual Fallback** section with step-by-step commands you can run individually.

## Hook Descriptions

### pre_week_start.sh
Prepares your environment for a new learning week:
- Creates week journal file from template
- Updates tracker with new week entry
- Shows current progress summary

### post_week_review.sh
Wraps up a completed week:
- Prompts for retrospective notes
- Updates progress log
- Suggests best practices to capture
- Shows week summary

### pre_publish_check.sh
Validates before making work public:
- Runs tests (pytest)
- Runs linter (ruff)
- Checks documentation links
- Verifies no secrets in code

## Creating Custom Hooks

1. Create a new `.sh` file in this folder
2. Add a shebang: `#!/bin/bash`
3. Make it executable: `chmod +x hookname.sh`
4. Document its purpose in comments
5. Add to this README

## Integration with Commands

Some commands automatically suggest running hooks:
- `/start-week` may run `pre_week_start.sh`
- `/retro` may run `post_week_review.sh`
- `/publish` may run `pre_publish_check.sh`

You always have control over whether to run them.

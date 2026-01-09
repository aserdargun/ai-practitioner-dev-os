# Hooks Guide

Automation scripts for the learning OS lifecycle.

## Overview

Hooks are shell scripts that run at key moments in your learning workflow. They automate repetitive tasks and ensure consistency.

## Available Hooks

| Hook | When to Run | Purpose |
|------|-------------|---------|
| `pre_week_start.sh` | Start of week | Create plan stub, log start |
| `post_week_review.sh` | End of week | Prompt reflection, log end |
| `pre_publish_check.sh` | Before publishing | Quality gates |

## Using Hooks

### Linux / macOS

```bash
bash .claude/hooks/pre_week_start.sh
bash .claude/hooks/post_week_review.sh
bash .claude/hooks/pre_publish_check.sh
```

### Windows

**Recommended**: Use WSL (Windows Subsystem for Linux)

```bash
# In WSL terminal
bash .claude/hooks/pre_week_start.sh
```

**Alternative**: Git Bash

```bash
# In Git Bash
bash .claude/hooks/pre_week_start.sh
```

**Manual Fallback**: See sections below for equivalent commands.

## Hook Details

### pre_week_start.sh

**Purpose**: Prepare for a new week of learning.

**What it does**:
1. Creates a week plan stub in `paths/advanced/journal/`
2. Appends `week_start` event to progress log
3. Displays current month goals

**When to run**: Monday morning, or whenever you start a week.

**Example output**:
```
=== Pre-Week Start Hook ===

Creating week plan stub: paths/advanced/journal/week-02.md
Created paths/advanced/journal/week-02.md
Logging week start to progress log...

=== Current Month Goals ===
# Month 03: RAG Systems
...

=== Ready! ===
Next steps:
1. Review your week plan
2. Run /status
3. Start with /plan-week
```

### post_week_review.sh

**Purpose**: Close out the week and prepare for retrospective.

**What it does**:
1. Prompts for quick reflection (optional)
2. Appends `week_end` event to progress log
3. Updates week journal (if it exists)
4. Shows summary stats

**When to run**: Friday afternoon, or whenever you finish a week.

**Example output**:
```
=== Post-Week Review Hook ===

Quick reflection (press Enter to skip):
What went well? Completed retrieval pipeline
What could be improved? Start tests earlier
Key learning? Chunk size matters a lot

Logging week end to progress log...

=== Week 02 Summary ===
Commits this week: 8
Progress log entries: 5

=== Next Steps ===
1. Run /retro for detailed retrospective
2. Run /evaluate if end of month
```

### pre_publish_check.sh

**Purpose**: Quality gate before publishing work.

**What it does**:
1. Runs pytest
2. Runs ruff linter
3. Checks for secrets
4. Verifies documentation links
5. Checks git status

**When to run**: Before publishing, demoing, or submitting.

**Example output**:
```
=== Pre-Publish Check ===

1. Running tests...
   ✅ Tests passed

2. Running linter...
   ✅ Linting passed

3. Checking for secrets...
   ✅ No obvious secrets found

4. Checking documentation...
   ✅ Documentation links look OK

5. Checking git status...
   ⚠️  3 uncommitted changes

=== Summary ===
⚠️  1 warning, but no blocking issues.
```

## Manual Fallback

If you can't run shell scripts, here are the equivalent steps:

### pre_week_start.sh (Manual)

```bash
# 1. Create week plan
WEEK=$(date +%V)
cat > paths/advanced/journal/week-$WEEK.md << 'EOF'
# Week Plan

- [ ] Goal 1
- [ ] Goal 2
- [ ] Goal 3
EOF

# 2. Log to progress
echo "{\"timestamp\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\", \"type\": \"week_start\", \"week\": $WEEK}" >> .claude/memory/progress_log.jsonl

# 3. View month goals
head -30 paths/advanced/month-*/README.md
```

### post_week_review.sh (Manual)

```bash
# 1. Log to progress
WEEK=$(date +%V)
echo "{\"timestamp\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\", \"type\": \"week_end\", \"week\": $WEEK}" >> .claude/memory/progress_log.jsonl

# 2. Run retrospective
# Use /retro command in Claude Code
```

### pre_publish_check.sh (Manual)

```bash
# 1. Run tests
pytest

# 2. Run linter
ruff check .

# 3. Check for secrets (manual review)
grep -r "api_key\|password\|secret" --include="*.py" .

# 4. Check git status
git status
```

## Cross-Platform Notes

These hooks use:
- POSIX-compatible shell syntax
- Standard Unix utilities (date, cat, echo, grep)
- Python tools (pytest, ruff) if installed

They should work on:
- Linux
- macOS
- Windows WSL
- Windows Git Bash

## Creating Custom Hooks

### Template

```bash
#!/bin/bash
set -e

# my_hook.sh - Description
# When to run: [situation]

echo "=== My Hook ==="

# Your commands here

echo "Done!"
```

### Make Executable

```bash
chmod +x .claude/hooks/my_hook.sh
```

### Best Practices

1. Use `set -e` to exit on errors
2. Print clear messages
3. Handle missing dependencies gracefully
4. Provide manual fallback instructions

## Hook Files Location

```
.claude/hooks/
├── README.md
├── pre_week_start.sh
├── post_week_review.sh
└── pre_publish_check.sh
```

See [.claude/hooks/README.md](../.claude/hooks/README.md) for implementation details.

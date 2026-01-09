# Hooks

This folder contains shell scripts that run at key lifecycle moments.

## Overview

Hooks are simple shell scripts that automate repetitive tasks at specific points in your learning workflow.

## Available Hooks

| Hook | When to Run | Purpose |
|------|-------------|---------|
| `pre_week_start.sh` | Before starting a new week | Create week plan stub, update tracker |
| `post_week_review.sh` | After completing a week | Prompt retrospective, update progress log |
| `pre_publish_check.sh` | Before publishing work | Run tests, lint, check docs links |

## Usage

### Linux/macOS

```bash
bash .claude/hooks/pre_week_start.sh
bash .claude/hooks/post_week_review.sh
bash .claude/hooks/pre_publish_check.sh
```

### Windows

Use WSL (recommended) or Git Bash:

```bash
# In WSL or Git Bash
bash .claude/hooks/pre_week_start.sh
```

Or see the "Manual Fallback" section below if you can't run shell scripts.

## Hook Details

### pre_week_start.sh

**Purpose**: Prepare for a new week of learning.

**What it does**:
1. Creates a week plan stub in the journal
2. Updates the tracker with new week pointer
3. Prints the current month goals as a reminder

**When to use**: Monday morning, or whenever you start a new week.

### post_week_review.sh

**Purpose**: Close out a week and prepare for retrospective.

**What it does**:
1. Prompts for a brief reflection
2. Appends an entry to `progress_log.jsonl`
3. Suggests running `/retro` for full retrospective

**When to use**: Friday afternoon, or whenever you finish a week.

### pre_publish_check.sh

**Purpose**: Quality gate before publishing work externally.

**What it does**:
1. Runs the test suite (pytest)
2. Runs the linter (ruff)
3. Checks for broken documentation links
4. Reports any issues found

**When to use**: Before publishing, demoing, or submitting work.

## Manual Fallback

If you cannot run `.sh` scripts, here are the equivalent manual steps:

### pre_week_start.sh (Manual)

```bash
# 1. Create week plan stub
echo "## Week X Plan\n\n- [ ] Task 1\n- [ ] Task 2" >> paths/advanced/journal/week-XX.md

# 2. Update tracker
# Edit paths/advanced/tracker.md and update "Current Week" pointer

# 3. Review month goals
cat paths/advanced/month-XX/README.md | head -50
```

### post_week_review.sh (Manual)

```bash
# 1. Append to progress log
echo '{"timestamp":"2026-01-09T17:00:00Z","type":"week_end","week":1}' >> .claude/memory/progress_log.jsonl

# 2. Run retrospective
# Use /retro command in Claude Code
```

### pre_publish_check.sh (Manual)

```bash
# 1. Run tests
pytest

# 2. Run linter
ruff check .

# 3. Check links (if you have markdown-link-check installed)
find docs -name "*.md" -exec markdown-link-check {} \;
```

## Creating New Hooks

To add a new hook:

1. Create `my_hook.sh` in this folder
2. Add a shebang: `#!/bin/bash`
3. Add `set -e` to exit on errors
4. Document what it does
5. Make it executable: `chmod +x my_hook.sh`

Template:
```bash
#!/bin/bash
set -e

# my_hook.sh - Description of what this hook does
# When to use: [situation]

echo "Running my_hook..."

# Your commands here

echo "Done!"
```

## Cross-Platform Notes

- These hooks use POSIX-compatible shell syntax
- They should work on Linux, macOS, and Windows (via WSL/Git Bash)
- Python is assumed to be available (for pytest, ruff)
- The hooks are intentionally simple to maximize compatibility

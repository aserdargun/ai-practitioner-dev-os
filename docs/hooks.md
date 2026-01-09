# Hooks Guide

Shell scripts that automate workflow events.

## Overview

Hooks are shell scripts in `.claude/hooks/` that run at key workflow moments:

| Hook | When | Purpose |
|------|------|---------|
| `pre_week_start.sh` | Start of week | Initialize week |
| `post_week_review.sh` | End of week | Prompt retrospective |
| `pre_publish_check.sh` | Before publishing | Quality gates |

---

## Running Hooks

### From Command Line

```bash
# From repository root
bash .claude/hooks/pre_week_start.sh
bash .claude/hooks/post_week_review.sh
bash .claude/hooks/pre_publish_check.sh
```

### Via Commands

Hooks are suggested by commands:
- `/start-week` → suggests `pre_week_start.sh`
- `/retro` → suggests `post_week_review.sh`
- `/publish` → suggests `pre_publish_check.sh`

---

## Hook Details

### pre_week_start.sh

**Purpose**: Initialize a new week

**What it does**:
1. Creates week journal entry (if not exists)
2. Logs week start to progress_log.jsonl
3. Shows current tracker status

**Output example**:
```
=== Pre-Week Start Hook ===
Date: 2026-01-15
Week: 03

Creating week journal entry: paths/intermediate/journal/week-2026-03.md
✓ Week journal created
✓ Progress log updated

=== Current Status ===
[tracker content]

=== Week Start Complete ===
Next steps:
1. Review your week goals
2. Run /plan-week for detailed task breakdown
3. Run /status for current progress snapshot
```

### post_week_review.sh

**Purpose**: Prompt end-of-week reflection

**What it does**:
1. Checks for week journal
2. Displays reflection prompts
3. Logs week end event
4. Shows git status

**Output example**:
```
=== Post-Week Review Hook ===
Date: 2026-01-19
Week: 03

=== Week Reflection Prompts ===

1. WHAT WENT WELL this week?
2. WHAT COULD BE IMPROVED?
3. KEY LEARNINGS
4. BEST PRACTICES to capture?

✓ Progress log updated

=== Git Status ===
[uncommitted changes]

=== Week Review Complete ===
Next steps:
1. Update your week journal with reflections
2. Run /retro for guided retrospective
3. Commit your changes
```

### pre_publish_check.sh

**Purpose**: Verify quality before publishing

**What it does**:
1. Checks Python environment
2. Runs ruff lint (if available)
3. Runs pytest (if available)
4. Checks documentation
5. Looks for broken links
6. Shows git status

**Output example**:
```
=== Pre-Publish Check ===

=== Environment Checks ===
✓ Python3 found: Python 3.11.0
✓ ruff found: ruff 0.1.0
✓ pytest found: pytest 7.4.0

=== Lint Checks ===
✓ ruff check passed
✓ ruff format check passed

=== Test Checks ===
✓ All tests passed

=== Documentation Checks ===
✓ README.md exists
✓ No broken links found in docs/

=== Summary ===
Errors: 0
Warnings: 0

✓ Pre-publish check PASSED
```

---

## Cross-Platform Compatibility

### Linux / macOS

Hooks run natively:
```bash
bash .claude/hooks/pre_week_start.sh
```

### Windows

**Option 1: WSL (Recommended)**
```bash
# In WSL terminal
bash .claude/hooks/pre_week_start.sh
```

**Option 2: Git Bash**
```bash
# In Git Bash terminal
bash .claude/hooks/pre_week_start.sh
```

---

## Manual Fallback

If you cannot run `.sh` scripts, here are the equivalent manual steps:

### Manual: pre_week_start

1. **Create week journal**:
   ```bash
   # Copy template
   cp paths/intermediate/journal/weekly-template.md \
      paths/intermediate/journal/week-$(date +%Y-%V).md
   ```

2. **Log week start**:
   ```bash
   # Add to progress log
   echo '{"timestamp": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'", "event": "week_start"}' \
      >> .claude/memory/progress_log.jsonl
   ```

3. **Check tracker**:
   ```bash
   head -20 paths/intermediate/tracker.md
   ```

### Manual: post_week_review

1. **Log week end**:
   ```bash
   echo '{"timestamp": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'", "event": "week_end"}' \
      >> .claude/memory/progress_log.jsonl
   ```

2. **Review reflection prompts** (in your journal):
   - What went well?
   - What could be improved?
   - Key learnings?
   - Best practices to capture?

3. **Check git status**:
   ```bash
   git status
   ```

### Manual: pre_publish_check

1. **Run linter**:
   ```bash
   ruff check .
   ruff format --check .
   ```

2. **Run tests**:
   ```bash
   pytest
   ```

3. **Check README**:
   ```bash
   ls README.md
   ```

4. **Review for broken links** (manual inspection)

---

## Customizing Hooks

Feel free to modify hooks for your workflow:

1. **Edit the script**:
   ```bash
   code .claude/hooks/pre_week_start.sh
   ```

2. **Test your changes**:
   ```bash
   bash .claude/hooks/pre_week_start.sh
   ```

3. **Commit customizations**:
   ```bash
   git add .claude/hooks/
   git commit -m "Customize hooks for my workflow"
   ```

### Common Customizations

- Add Slack notifications
- Integrate with task management
- Custom quality checks
- Team-specific workflows

---

## Related Documentation

- [.claude/hooks/README.md](../.claude/hooks/README.md) — Hooks system overview
- [.claude/hooks/*.sh](../.claude/hooks/) — Individual hook scripts
- [commands.md](commands.md) — Commands that suggest hooks
- [how-to-use.md](how-to-use.md) — Overall workflow

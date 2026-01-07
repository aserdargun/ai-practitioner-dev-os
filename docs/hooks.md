# Hooks Guide

Automation scripts that run at key points in your learning workflow.

---

## Overview

Hooks are shell scripts that execute automatically (or manually) at specific triggers. They handle environment checks, metrics collection, and quality gates.

---

## Available Hooks

| Hook | File | Trigger | Purpose |
|------|------|---------|---------|
| Pre-Week Start | `pre_week_start.sh` | `/start-week` | Environment validation |
| Post-Week Review | `post_week_review.sh` | `/retro` | Metrics collection |
| Pre-Publish Check | `pre_publish_check.sh` | `/publish` | Quality gates |

---

## Hook Locations

All hooks are in `.claude/hooks/`:

```
.claude/hooks/
├── pre_week_start.sh
├── post_week_review.sh
└── pre_publish_check.sh
```

---

## Hook Details

### Pre-Week Start

**File**: `pre_week_start.sh`

**Triggered By**: `/start-week` command

**What It Does**:
1. Displays current date and week
2. Checks git status
3. Verifies memory files exist
4. Checks Python environment
5. Runs quick lint check
6. Reports uncommitted changes

**Output Example**:
```
==========================================
  Pre-Week Start Hook
==========================================

Date: 2026-01-15
Week: 03

Checking git status...
  (status output)

Verifying memory files...
  ✓ learner_profile.json exists
  ✓ progress_log.jsonl exists (15 entries)
  ✓ best_practices.md exists

Checking Python environment...
  ✓ Python 3.11.0

Running quick lint check...
  ✓ No linting errors

==========================================
  Pre-Week Start Complete
==========================================

Ready to start Week 03!
```

---

### Post-Week Review

**File**: `post_week_review.sh`

**Triggered By**: `/retro` command

**What It Does**:
1. Displays week ending info
2. Counts commits this week
3. Runs tests and reports status
4. Summarizes progress log entries
5. Counts best practices
6. Generates metrics summary

**Output Example**:
```
==========================================
  Post-Week Review Hook
==========================================

Date: 2026-01-19
Week: 03 (ending)

Collecting week metrics...
  Commits this week: 12
  Recent changes: 25 files changed

Running tests...
  ✓ template-fastapi-service tests passing
  ✓ template-data-pipeline tests passing

Progress log summary...
  Total progress entries: 23
  Entries today: 3

Best practices captured...
  Total best practices: 8

==========================================
  Week Summary
==========================================

Add these metrics to your retrospective:

- Commits: 12
- Tests: Passing
- Progress entries: 23
- Best practices: 8

==========================================
  Post-Week Review Complete
==========================================
```

---

### Pre-Publish Check

**File**: `pre_publish_check.sh`

**Triggered By**: `/publish` command

**What It Does**:
1. Checks git status (uncommitted changes)
2. Runs linting checks
3. Runs test suites
4. Verifies documentation
5. Security checks (secrets, .env)
6. Dependency checks
7. Reports final status

**Output Example**:
```
==========================================
  Pre-Publish Quality Check
==========================================

1. Git Status
-------------
  ✓ All changes committed
  ✓ On main branch

2. Code Quality (Linting)
-------------------------
  ✓ No linting errors in templates/
  ✓ No linting errors in src/

3. Tests
--------
  ✓ All tests passing

4. Documentation
----------------
  ✓ README.md exists (173 lines)
  ✓ Python files have docstrings

5. Security
-----------
  ✓ No obvious secrets in code
  ✓ .env is in .gitignore

6. Dependencies
---------------
  ✓ Dependencies file exists

==========================================
  Summary
==========================================

  Errors:   0
  Warnings: 0

  Status: READY TO PUBLISH

  All checks passed!
```

---

## Running Hooks

### Automatically (via commands)

Hooks run automatically when you use their trigger commands:
- `/start-week` → `pre_week_start.sh`
- `/retro` → `post_week_review.sh`
- `/publish` → `pre_publish_check.sh`

### Manually

```bash
# From repo root
bash .claude/hooks/pre_week_start.sh
bash .claude/hooks/post_week_review.sh
bash .claude/hooks/pre_publish_check.sh
```

### With verbose output

```bash
bash -x .claude/hooks/pre_week_start.sh
```

---

## Platform Compatibility

### Linux / macOS

Hooks work out of the box:
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
# In Git Bash
bash .claude/hooks/pre_week_start.sh
```

**Option 3: Manual Steps**

If you can't run shell scripts, follow the manual fallback:

1. **Pre-Week Start**:
   - Run `git status`
   - Check Python version: `python --version`
   - Verify files exist in `.claude/memory/`
   - Run `ruff check templates/`

2. **Post-Week Review**:
   - Run `git log --oneline -10`
   - Run `pytest templates/*/`
   - Count entries in progress_log.jsonl

3. **Pre-Publish Check**:
   - Run `git status`
   - Run `ruff check .`
   - Run `pytest`
   - Check README exists

---

## Hook Output

### Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success, all checks passed |
| 1 | Failure, blocking issues found |

### Capturing Output

```bash
# Save to file
bash .claude/hooks/pre_publish_check.sh > publish_check.log 2>&1

# Check exit code
bash .claude/hooks/pre_publish_check.sh
echo "Exit code: $?"
```

---

## Customizing Hooks

### Adding Checks

Edit the hook file to add custom checks:

```bash
# In pre_publish_check.sh

# Custom: Check for TODO comments
echo "Checking for TODOs..."
TODO_COUNT=$(grep -r "TODO" --include="*.py" . | wc -l)
if [ "$TODO_COUNT" -gt 5 ]; then
    check_warn "Found $TODO_COUNT TODO comments"
else
    check_pass "TODO count acceptable ($TODO_COUNT)"
fi
```

### Skipping Checks

Temporarily skip checks by commenting out:

```bash
# Skip this check for now
# echo "Running tests..."
# pytest tests/
```

### Creating New Hooks

1. Create new file in `.claude/hooks/`
2. Add shebang: `#!/bin/bash`
3. Add `set -e` for fail-fast behavior
4. Document the trigger
5. Update this documentation

---

## Troubleshooting

### Hook not found

```
bash: .claude/hooks/pre_week_start.sh: No such file or directory
```

**Solution**: Run from repository root directory.

### Permission denied

```
bash: .claude/hooks/pre_week_start.sh: Permission denied
```

**Solution**: Add execute permission:
```bash
chmod +x .claude/hooks/*.sh
```

### Command not found (ruff, pytest)

**Solution**: Install missing tools:
```bash
pip install ruff pytest
```

### Git not in PATH

**Solution**: Ensure git is installed and in PATH:
```bash
git --version
```

---

## Best Practices

### For Using Hooks

1. **Run before starting**: Always run pre_week_start
2. **Fix issues promptly**: Don't ignore hook warnings
3. **Run publish check early**: Catch issues before deadline

### For Customizing Hooks

1. **Keep portable**: Use POSIX-compatible commands
2. **Fail gracefully**: Use `|| true` for non-critical checks
3. **Document changes**: Comment custom additions
4. **Test changes**: Run hook manually after edits

---

## See Also

- [Commands Guide](commands.md) — Command reference
- [How to Use](how-to-use.md) — Workflow guide
- [System Overview](system-overview.md) — Architecture

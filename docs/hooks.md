# Hooks Guide

Hooks are automation scripts that run at key moments in your learning workflow. This guide explains how to use them.

For hook source code, see [.claude/hooks/](../.claude/hooks/).

## Available Hooks

| Hook | File | When to Run |
|------|------|-------------|
| Pre-Week Start | `pre_week_start.sh` | Monday morning |
| Post-Week Review | `post_week_review.sh` | Friday evening |
| Pre-Publish Check | `pre_publish_check.sh` | Before publishing |

## Running Hooks

From the repository root:

```bash
# Start of week
bash .claude/hooks/pre_week_start.sh

# End of week
bash .claude/hooks/post_week_review.sh

# Before publishing
bash .claude/hooks/pre_publish_check.sh
```

## Cross-Platform Compatibility

These hooks are shell scripts designed for:
- **Linux**: Works natively
- **macOS**: Works natively
- **Windows**: Requires WSL (recommended) or Git Bash

### Windows Setup with WSL

1. Install WSL: `wsl --install`
2. Open WSL terminal
3. Navigate to your repo
4. Run hooks as normal

### Windows Setup with Git Bash

1. Install Git for Windows (includes Git Bash)
2. Open Git Bash
3. Navigate to your repo
4. Run hooks as normal

---

## Pre-Week Start Hook

**File**: `.claude/hooks/pre_week_start.sh`

**Purpose**: Initialize a new week of learning.

**What It Does**:
1. Creates a new week journal file
2. Updates the progress log with week start event
3. Displays next steps

**When to Run**: Monday morning, start of each week.

**Example Output**:
```
==========================================
  Pre-Week Start Hook
  Date: 2026-01-07
  Week: 02
==========================================

Creating week journal: paths/Beginner/journal/week-2026-01-07.md
Created week journal
Adding week start to progress log...

Week 02 initialized!

Next steps:
  1. Open paths/Beginner/journal/week-2026-01-07.md and set your goals
  2. Run /plan-week in Claude to create detailed plan
  3. Run /status to see current state

==========================================
```

### Manual Fallback

If you can't run the script:

1. Create a new file: `paths/Beginner/journal/week-YYYY-MM-DD.md`
2. Copy the template from `paths/Beginner/journal/weekly-template.md`
3. Fill in your goals for the week
4. Add this to `.claude/memory/progress_log.jsonl`:
   ```json
   {"timestamp": "2026-01-07T09:00:00Z", "event": "week_start", "week": 2, "year": 2026}
   ```

---

## Post-Week Review Hook

**File**: `.claude/hooks/post_week_review.sh`

**Purpose**: Facilitate end-of-week reflection.

**What It Does**:
1. Prompts you for reflection (what went well, to improve, learned, mood)
2. Logs reflection to progress_log.jsonl
3. Runs evaluation (if evaluate.py exists)

**When to Run**: Friday evening, end of each week.

**Example Output**:
```
==========================================
  Post-Week Review Hook
  Date: 2026-01-10
  Week: 02
==========================================

Time for your weekly reflection!

What went well this week? Completed the EDA notebook ahead of schedule
What could be improved? Need to write more tests
What did you learn? Pandas groupby is powerful for aggregations
How are you feeling? (1-5): 4

Saving reflection to progress log...
Reflection saved!

Running evaluation...
[Evaluation output]

Week 02 complete!

Next steps:
  1. Review your evaluation results
  2. Run /adapt-path if changes are needed
  3. Run /report to update your tracker
  4. Take a break - you've earned it!

==========================================
```

### Manual Fallback

If you can't run the script:

1. Open your week journal and add a reflection section
2. Add this to `.claude/memory/progress_log.jsonl`:
   ```json
   {"timestamp": "2026-01-10T17:00:00Z", "event": "week_end", "week": 2, "reflection": {"went_well": "...", "to_improve": "...", "learned": "...", "mood": 4}}
   ```
3. Run: `python .claude/path-engine/evaluate.py`

---

## Pre-Publish Check Hook

**File**: `.claude/hooks/pre_publish_check.sh`

**Purpose**: Quality checks before publishing work.

**What It Does**:
1. Runs tests (pytest)
2. Runs linter (ruff)
3. Validates memory JSON files
4. Checks for common issues (secrets, TODOs)

**When to Run**: Before publishing, demoing, or sharing work.

**Example Output**:
```
==========================================
  Pre-Publish Check Hook
  Date: 2026-01-15
==========================================

[1/4] Running tests...
✓ Tests passed

[2/4] Running linter...
✓ Linting passed

[3/4] Validating memory files...
  ✓ progress_log.jsonl is valid
  ✓ decisions.jsonl is valid
  ✓ learner_profile.json is valid

[4/4] Checking for common issues...
  ✓ No obvious secrets found
  ⚠ Found 3 TODO/FIXME comments

==========================================
  ✓ All checks passed!
  Ready to publish.
==========================================
```

### Manual Fallback

If you can't run the script:

1. Run tests: `pytest tests/ -v`
2. Run linter: `ruff check .`
3. Validate JSON files:
   ```python
   import json
   # For JSONL files
   with open('.claude/memory/progress_log.jsonl') as f:
       for line in f:
           json.loads(line)  # Should not error
   # For JSON files
   with open('.claude/memory/learner_profile.json') as f:
       json.load(f)  # Should not error
   ```
4. Search for secrets: `grep -r "sk-" --include="*.py" .`
5. Search for TODOs: `grep -r "TODO\|FIXME" --include="*.py" .`

---

## Customizing Hooks

You can modify hooks to fit your workflow. Common customizations:

### Change Journal Location

Edit `pre_week_start.sh`:
```bash
JOURNAL_DIR="my-custom-journal-path"
```

### Add Extra Checks

Edit `pre_publish_check.sh`:
```bash
# Add custom check
echo "[5/5] Checking custom rules..."
if grep -r "DEBUG=True" --include="*.py" .; then
    echo "  ✗ Found DEBUG=True in code"
    ERRORS=$((ERRORS + 1))
else
    echo "  ✓ No debug flags in production code"
fi
```

### Skip Certain Checks

Edit `pre_publish_check.sh` to skip checks you don't need:
```bash
# Comment out to skip
# echo "[1/4] Running tests..."
# pytest tests/ -q 2>/dev/null || ERRORS=$((ERRORS + 1))
```

## Integration with Commands

Hooks are integrated with commands:

| Command | Runs Hook |
|---------|-----------|
| `/start-week` | `pre_week_start.sh` |
| (Manual) | `post_week_review.sh` |
| `/publish` | `pre_publish_check.sh` |

You can also run hooks manually at any time.

## Troubleshooting

### "Permission denied"

Make scripts executable:
```bash
chmod +x .claude/hooks/*.sh
```

### "Command not found: pytest"

Install test tools:
```bash
pip install pytest ruff
```

### "Bad substitution" on Windows

Use Git Bash or WSL instead of PowerShell/CMD.

### Hooks fail silently

Check that you're in the repository root:
```bash
pwd  # Should show your repo path
ls .claude/hooks/  # Should show hook files
```

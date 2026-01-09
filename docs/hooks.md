# Hooks Reference

Guide to lifecycle hooks in the learning OS.

## What Are Hooks?

Hooks are shell scripts that automate common tasks at specific points in your learning workflow:
- Before starting a week
- After completing a week
- Before publishing work

Hooks live in: [.claude/hooks/](../.claude/hooks/)

---

## Available Hooks

| Hook | File | When to Run |
|------|------|-------------|
| Pre Week Start | `pre_week_start.sh` | Before starting a new week |
| Post Week Review | `post_week_review.sh` | After completing a week |
| Pre Publish Check | `pre_publish_check.sh` | Before making work public |

---

## Running Hooks

### Linux / macOS

```bash
# Make executable (first time only)
chmod +x .claude/hooks/pre_week_start.sh

# Run
./.claude/hooks/pre_week_start.sh
```

### Windows (WSL or Git Bash)

```bash
bash .claude/hooks/pre_week_start.sh
```

### Windows (PowerShell)

See "Manual Fallback" sections below for equivalent commands.

---

## Pre Week Start

**File**: [.claude/hooks/pre_week_start.sh](../.claude/hooks/pre_week_start.sh)

### What It Does
1. Creates week journal file from template
2. Updates tracker with new week entry
3. Logs "week_started" event to progress log
4. Shows summary and next steps

### Usage
```bash
./.claude/hooks/pre_week_start.sh

# Or with arguments
./.claude/hooks/pre_week_start.sh 3 2  # Month 3, Week 2
```

### Manual Fallback
If you cannot run the script:

1. **Create week journal file**:
   - Copy `paths/beginner/journal/weekly-template.md`
   - Rename to `month-XX-week-Y.md` (e.g., `month-03-week-2.md`)
   - Fill in the date and initial goals

2. **Update tracker**:
   - Open `paths/beginner/tracker.md`
   - Add new week section

3. **Log the event**:
   - Open `.claude/memory/progress_log.jsonl`
   - Add: `{"timestamp": "...", "event": "week_started", "month": X, "week": Y}`

---

## Post Week Review

**File**: [.claude/hooks/post_week_review.sh](../.claude/hooks/post_week_review.sh)

### What It Does
1. Prompts for retrospective notes
2. Updates week journal with reflections
3. Logs "week_completed" event
4. Optionally captures best practices
5. Updates tracker status

### Usage
```bash
./.claude/hooks/post_week_review.sh
```

The script will prompt you for:
- Which month and week
- What you accomplished
- What was challenging
- What you learned
- Any best practices to capture
- Week rating (1-5)

### Manual Fallback
If you cannot run the script:

1. **Update week journal**:
   - Open `paths/beginner/journal/month-XX-week-Y.md`
   - Fill in the Week Summary section

2. **Update tracker**:
   - Open `paths/beginner/tracker.md`
   - Mark week as "Completed"

3. **Log events**:
   - Add to `.claude/memory/progress_log.jsonl`:
     ```json
     {"timestamp": "...", "event": "week_completed", "month": X, "week": Y, "rating": Z}
     ```

4. **Add best practice** (if any):
   - Open `.claude/memory/best_practices.md`
   - Add the learning with date and context

---

## Pre Publish Check

**File**: [.claude/hooks/pre_publish_check.sh](../.claude/hooks/pre_publish_check.sh)

### What It Does
1. Runs pytest tests
2. Runs ruff linter
3. Checks for hardcoded secrets
4. Verifies .gitignore completeness
5. Checks README exists and has content
6. Validates documentation links
7. Checks dependencies are pinned

### Usage
```bash
./.claude/hooks/pre_publish_check.sh [project_path]

# Examples
./.claude/hooks/pre_publish_check.sh              # Current directory
./.claude/hooks/pre_publish_check.sh ./my-project # Specific project
```

### What It Checks
| Check | Pass Criteria |
|-------|---------------|
| Tests | pytest passes |
| Linter | ruff passes |
| Secrets | No hardcoded patterns found |
| .gitignore | Contains .env, __pycache__, etc. |
| README | Exists and >10 lines |
| Links | No broken relative links |
| Dependencies | requirements.txt or pyproject.toml exists |

### Manual Fallback
If you cannot run the script:

1. **Run tests**:
   ```bash
   pytest tests/ -v
   ```

2. **Run linter**:
   ```bash
   ruff check .
   ```

3. **Search for secrets**:
   ```bash
   grep -rni "password\|api_key\|secret\|token" --include="*.py"
   ```

4. **Check .gitignore** includes:
   - `.env`
   - `__pycache__`
   - `*.pyc`

5. **Verify README**:
   - Has project description
   - Has setup instructions
   - Has usage examples

6. **Test documentation links manually**

---

## Cross-Platform Notes

### Supported Platforms
- Linux (native)
- macOS (native)
- Windows via WSL (Windows Subsystem for Linux)
- Windows via Git Bash

### Requirements
- Bash shell
- Basic Unix tools (grep, sed, etc.)
- Python 3 (for pytest, ruff)

### Not Supported
- Native Windows PowerShell (use manual fallback)
- Older shells (sh without bash features)

---

## Integration with Commands

Some commands suggest running hooks:

| Command | May Suggest |
|---------|-------------|
| `/start-week` | `pre_week_start.sh` |
| `/retro` | `post_week_review.sh` |
| `/publish` | `pre_publish_check.sh` |

You always decide whether to run them.

---

## Creating Custom Hooks

1. Create new `.sh` file in `.claude/hooks/`
2. Add shebang: `#!/bin/bash`
3. Make executable: `chmod +x hookname.sh`
4. Document in this file

### Template
```bash
#!/bin/bash
# hook_name.sh
# Description of what this hook does

set -e  # Exit on error

# Configuration
SOME_DIR="path/to/dir"

# Colors (optional)
GREEN='\033[0;32m'
NC='\033[0m'

echo "Running hook..."

# Your logic here

echo -e "${GREEN}Done!${NC}"
```

---

## Tips

1. **Run hooks consistently**: They help build good habits
2. **Check output**: Hooks provide useful summaries
3. **Use manual fallback**: If scripts don't work, the manual steps do
4. **Customize as needed**: Edit hooks to match your workflow
5. **Commit hook changes**: If you improve a hook, commit it

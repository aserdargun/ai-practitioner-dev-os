# Evaluation Signals

How the system collects data for evaluation.

## Overview

Signals are data points collected from your repository and memory files. They feed into the scoring rubric.

## Signal Sources

| Source | Signals |
|--------|---------|
| Memory files | Progress events, decisions, reflections |
| Git history | Commits, files changed |
| Test suite | Test count, pass/fail |
| Month README | DoD checklist |
| Journal | Entry count |

## Signal Details

### Memory Signals

**Source**: `.claude/memory/`

| Signal | File | Description |
|--------|------|-------------|
| `progress_events` | `progress_log.jsonl` | Count by type |
| `task_completions` | `progress_log.jsonl` | Tasks marked complete |
| `blockers` | `progress_log.jsonl` | Blockers logged |
| `blockers_resolved` | `progress_log.jsonl` | Blockers resolved |
| `decisions_made` | `decisions.jsonl` | Decisions recorded |
| `best_practices` | `best_practices.md` | Practices added |

**Collection**:
```python
progress_log = load_jsonl(".claude/memory/progress_log.jsonl")
task_completions = len([e for e in progress_log if e["type"] == "task_complete"])
```

### Git Signals

**Source**: Git repository

| Signal | Command | Description |
|--------|---------|-------------|
| `commits_30d` | `git log --since="30 days"` | Recent commits |
| `files_changed` | `git diff --stat` | Files modified |
| `lines_added` | `git diff` | Lines added |

**Collection**:
```python
result = subprocess.run(
    ["git", "log", "--since=30 days ago", "--oneline"],
    capture_output=True
)
commits = len(result.stdout.splitlines())
```

### Test Signals

**Source**: Test suite (pytest)

| Signal | Method | Description |
|--------|--------|-------------|
| `tests_exist` | Glob for test files | Any tests present |
| `test_count` | pytest --collect-only | Number of tests |
| `tests_passing` | pytest exit code | All tests pass |

**Collection**:
```python
result = subprocess.run(["pytest", "--collect-only", "-q"])
test_count = count_test_items(result.stdout)
```

### DoD Signals

**Source**: Month README

| Signal | Pattern | Description |
|--------|---------|-------------|
| `dod_completed` | `[x]` or `[X]` | Checked items |
| `dod_total` | `[ ]` + `[x]` | All items |

**Collection**:
```python
content = Path(f"paths/advanced/month-{month:02d}/README.md").read_text()
completed = content.count("[x]") + content.count("[X]")
uncompleted = content.count("[ ]")
```

### Journal Signals

**Source**: `paths/advanced/journal/`

| Signal | Method | Description |
|--------|--------|-------------|
| `journal_entries` | Glob `.md` files | Entry count |
| `week_entries` | Count `week-*.md` | Weekly entries |
| `retro_entries` | Content analysis | Retrospectives |

**Collection**:
```python
journal_dir = Path("paths/advanced/journal")
entries = len(list(journal_dir.glob("*.md")))
```

## Signal to Score Mapping

### Completion Score

```
completion_pct = dod_completed / dod_total * 100
```

### Quality Score

```
base = 70 if tests_exist else 50
bonus = min(30, test_count * 3)
quality = base + bonus
```

### Velocity Score

```
activity = task_completions + commits_30d

if activity >= 20: velocity = 100
elif activity >= 10: velocity = 80
elif activity >= 5: velocity = 60
else: velocity = 40
```

### Reflection Score

```
has_journals = journal_entries >= 4
has_retros = retro_entries >= 2

if has_journals and has_retros: reflection = 100
elif has_journals or has_retros: reflection = 70
else: reflection = 40
```

## Adding Custom Signals

To add a new signal:

1. **Define the signal**:
   ```python
   def get_my_signal():
       # Collection logic
       return value
   ```

2. **Add to evaluate.py**:
   ```python
   signals["my_signal"] = get_my_signal()
   ```

3. **Use in scoring**:
   ```python
   if signals["my_signal"] > threshold:
       scores["category"] += bonus
   ```

4. **Document in signals.md** (this file)

## Signal Reliability

| Signal | Reliability | Notes |
|--------|-------------|-------|
| DoD items | High | Direct measure of completion |
| Commits | Medium | Can be gamed (many small commits) |
| Tests | High | Objective pass/fail |
| Journal entries | Medium | Quantity ≠ quality |
| Progress log | Medium | Depends on logging consistency |

## Troubleshooting

### Missing Signals

**No test count**:
- Ensure pytest is installed
- Check test file naming (`test_*.py`)

**No commits**:
- Ensure in git repo
- Check `git log` works

**No DoD items**:
- Add checkboxes to month README
- Use `- [ ]` format

### Inaccurate Signals

**Commits seem low**:
- Check date range (30 days)
- Ensure git history is complete

**Tests not detected**:
- Use pytest conventions
- Check `pytest --collect-only` manually

## Signal Collection Frequency

| When | What's Collected |
|------|------------------|
| `/status` | Quick snapshot |
| `/evaluate` | Full signal collection |
| `evaluate.py` | Comprehensive analysis |

## Related Docs

- [Rubric](rubric.md) - How signals map to scores
- [Scoring](scoring.md) - Detailed calculations
- [Path Engine](../../.claude/path-engine/README.md) - Implementation

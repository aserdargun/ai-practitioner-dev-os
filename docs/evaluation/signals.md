# Evaluation Signals

Input signals used for scoring.

## Overview

The evaluation system reads signals from memory files and repository state to compute scores.

---

## Signal Sources

### Memory Files

| File | Signals Extracted |
|------|-------------------|
| `progress_log.jsonl` | Events, milestones, timestamps |
| `decisions.jsonl` | Choices, rationale |
| `best_practices.md` | Learnings captured |
| `learner_profile.json` | Constraints, goals |

### Repository State

| Source | Signals Extracted |
|--------|-------------------|
| Git history | Commit frequency, messages |
| Code files | Presence, structure |
| Test files | Coverage, passing status |
| Documentation | Completeness |

---

## Event Signals

Events from `progress_log.jsonl`:

### Completion Events

| Event Type | Signal | Criterion |
|------------|--------|-----------|
| `week_start` | Week initiated | Completeness |
| `week_end` | Week completed | Completeness |
| `milestone` | Deliverable done | Completeness |
| `project_complete` | Project finished | Completeness |

### Quality Events

| Event Type | Signal | Criterion |
|------------|--------|-----------|
| `tests_passed` | Tests green | Quality |
| `review` | Code reviewed | Quality |
| `deployment` | Deployed successfully | Quality |
| `bug_fixed` | Issue resolved | Quality |

### Learning Events

| Event Type | Signal | Criterion |
|------------|--------|-----------|
| `learning` | New knowledge | Learning |
| `experiment` | Tried something | Learning |
| `best_practice_added` | Insight captured | Learning |
| `breakthrough` | Significant advance | Learning |

### Reflection Events

| Event Type | Signal | Criterion |
|------------|--------|-----------|
| `retrospective` | Retro completed | Reflection |
| `journal_entry` | Journal updated | Reflection |
| `reflection` | Thought captured | Reflection |
| `insight` | Pattern recognized | Reflection |

---

## Decision Signals

Decisions from `decisions.jsonl`:

| Decision Type | Signal | Criterion |
|---------------|--------|-----------|
| `technology_choice` | Tech decision made | Learning |
| `architecture_decision` | Design choice | Learning |
| `approach_selection` | Method chosen | Learning |
| `project_choice` | Project selected | Completeness |

---

## Repository Signals

### Code Presence

```python
signals = {
    "has_main_code": exists("src/") or exists("app/"),
    "has_tests": exists("tests/"),
    "has_readme": exists("README.md"),
    "has_docs": exists("docs/") or has_docstrings(),
}
```

### Quality Indicators

```python
signals = {
    "tests_pass": pytest_exit_code == 0,
    "lint_clean": ruff_exit_code == 0,
    "type_hints": count_type_hints() > threshold,
    "docstrings": docstring_coverage() > threshold,
}
```

### Activity Indicators

```python
signals = {
    "commits_this_week": count_commits(days=7),
    "commits_this_month": count_commits(days=30),
    "files_changed": count_changed_files(),
    "lines_added": count_lines_added(),
}
```

---

## Signal Aggregation

### Time Windows

| Period | Days | Used For |
|--------|------|----------|
| Recent | 7 | Weekly evaluation |
| Month | 30 | Monthly evaluation |
| Quarter | 90 | Trend analysis |

### Counting Rules

```python
def count_events(progress_log, event_type, days=7):
    cutoff = datetime.now() - timedelta(days=days)
    return sum(
        1 for e in progress_log
        if e["event"] == event_type
        and parse(e["timestamp"]) > cutoff
    )
```

### Weighting

More recent events may be weighted higher:

```python
def weighted_count(events, half_life_days=14):
    total = 0
    now = datetime.now()
    for event in events:
        age_days = (now - parse(event["timestamp"])).days
        weight = 0.5 ** (age_days / half_life_days)
        total += weight
    return total
```

---

## Signal to Score Mapping

### Completeness Score

```python
def score_completeness(progress):
    milestones = count_events(progress, "milestone")
    weeks = count_events(progress, "week_end")

    if milestones >= 4 and weeks >= 4:
        return 95
    elif milestones >= 2 and weeks >= 2:
        return 80
    elif milestones >= 1 or weeks >= 1:
        return 65
    else:
        return 40
```

### Quality Score

```python
def score_quality(progress, repo):
    base = 50
    reviews = count_events(progress, "review") * 10
    tests = count_events(progress, "tests_passed") * 15
    deploys = count_events(progress, "deployment") * 20

    return min(100, base + reviews + tests + deploys)
```

### Learning Score

```python
def score_learning(progress, decisions):
    base = 50
    learnings = count_events(progress, "learning") * 10
    experiments = count_events(progress, "experiment") * 8
    best_practices = count_events(progress, "best_practice_added") * 12
    tech_decisions = count_decision_type(decisions, "technology_choice") * 5

    return min(100, base + learnings + experiments + best_practices + tech_decisions)
```

### Reflection Score

```python
def score_reflection(progress):
    base = 40
    retros = count_events(progress, "retrospective") * 15
    journals = count_events(progress, "journal_entry") * 10
    reflections = count_events(progress, "reflection") * 8

    return min(100, base + retros + journals + reflections)
```

---

## Adding Custom Signals

To add new signals:

1. Define the event type
2. Start logging it in progress_log.jsonl
3. Update evaluate.py to read it
4. Update this documentation

---

## Related Documentation

- [rubric.md](rubric.md) — How signals become scores
- [scoring.md](scoring.md) — Score computation details
- [../.claude/path-engine/evaluate.py](../../.claude/path-engine/evaluate.py) — Implementation

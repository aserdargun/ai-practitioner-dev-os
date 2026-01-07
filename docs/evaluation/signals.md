# Evaluation Signals

This document defines the signals used by the evaluation engine to score progress.

## Signal Sources

The evaluation engine reads signals from:

1. **Memory Files**
   - `.claude/memory/progress_log.jsonl`
   - `.claude/memory/decisions.jsonl`
   - `.claude/memory/learner_profile.json`

2. **Repository State**
   - Commit history (when available)
   - File modifications
   - Test presence

## Signal Definitions

### Completion Signals

| Signal | Source | How Detected |
|--------|--------|--------------|
| Tasks Completed | progress_log | `event: "task_completed"` |
| MVPs Shipped | progress_log | `event: "mvp_shipped"` |
| Deliverables | progress_log | Keywords in event descriptions |
| Week Completion | progress_log | `event: "week_end"` present |

**Counting**:
```python
tasks = len([e for e in events if e.get('event') == 'task_completed'])
mvps = len([e for e in events if e.get('event') == 'mvp_shipped'])
```

### Quality Signals

| Signal | Source | How Detected |
|--------|--------|--------------|
| Tests Written | progress_log | "test" keyword in entries |
| Code Reviewed | progress_log | `event: "code_reviewed"` |
| Documentation | progress_log | "doc", "readme" keywords |
| Harden Events | progress_log | `event: "hardened"` |

**Detection**:
```python
has_tests = any("test" in str(e).lower() for e in events)
has_docs = any("doc" in str(e).lower() or "readme" in str(e).lower() for e in events)
```

### Understanding Signals

| Signal | Source | How Detected |
|--------|--------|--------------|
| Reflections | progress_log | `reflection` field in week_end |
| Decisions | decisions.jsonl | Entry count |
| Learning Notes | progress_log | "learned", "understand" keywords |
| Best Practices | best_practices.md | Entry count |

**Detection**:
```python
has_reflection = any(e.get('reflection') for e in events)
decision_count = len(decisions)
learning_mentions = sum(1 for e in events if "learn" in str(e).lower())
```

### Consistency Signals

| Signal | Source | How Detected |
|--------|--------|--------------|
| Active Days | progress_log | Unique dates with events |
| Week Structure | progress_log | week_start + week_end pairs |
| Regular Cadence | progress_log | Timestamp distribution |
| Streak | progress_log | Consecutive active days |

**Detection**:
```python
def count_active_days(events, days=14):
    dates = set()
    cutoff = datetime.utcnow() - timedelta(days=days)
    for e in events:
        ts = e.get('timestamp')
        if ts:
            dt = parse_timestamp(ts)
            if dt >= cutoff:
                dates.add(dt.date())
    return len(dates)
```

## Time Windows

Different signals are measured over different time windows:

| Window | Duration | Used For |
|--------|----------|----------|
| Recent | 7 days | Completion, consistency |
| Medium | 14 days | Quality, understanding |
| Full | All time | Trend analysis |

## Signal Weights

Within each category, signals contribute differently:

### Completion Category
- Tasks completed: 60%
- MVPs shipped: 25%
- Week completion: 15%

### Quality Category
- Tests written: 40%
- Documentation: 30%
- Code reviewed: 20%
- Other quality signals: 10%

### Understanding Category
- Reflections: 40%
- Decisions documented: 30%
- Learning mentions: 20%
- Best practices: 10%

### Consistency Category
- Active days: 50%
- Week structure: 30%
- Regular cadence: 20%

## Missing Signals

When signals are missing, the engine applies defaults:

| Missing Signal | Default Action |
|----------------|----------------|
| No progress events | Score = 30 (base) |
| No reflections | Understanding penalty |
| No week structure | Consistency penalty |
| No tests mentioned | Quality penalty |

## Signal Quality

The engine considers signal quality:

**Strong signals**:
- Explicit events (task_completed, mvp_shipped)
- Structured data (JSON fields)
- Timestamps present

**Weak signals**:
- Keyword detection
- Inferred from text
- Missing timestamps

## Adding Your Own Signals

You can add signals by logging appropriate events:

```
I completed the data cleaning module today. It took 3 hours.
The code has tests and a README.
```

This creates signals for:
- Task completion
- Duration tracking
- Test presence
- Documentation presence

## Signal Processing

The evaluation engine processes signals in order:

1. **Load**: Read all memory files
2. **Filter**: Apply time windows
3. **Extract**: Pull signals from events
4. **Aggregate**: Combine signals into category scores
5. **Weight**: Apply category weights
6. **Output**: Generate overall score

## Debugging Signals

To see what signals the engine detected:

```bash
python .claude/path-engine/evaluate.py
```

The output shows:
- Raw counts per signal type
- Category breakdowns
- How signals affected scores

## Related Documentation

- [Rubric](rubric.md) - Overall scoring framework
- [Scoring](scoring.md) - Score calculation details
- [Path Engine](../../.claude/path-engine/README.md) - Implementation

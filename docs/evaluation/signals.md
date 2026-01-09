# Evaluation Signals

What data the evaluation system uses.

## Overview

The evaluation system reads signals from:
1. **Memory files** — Your progress and decisions
2. **Repository state** — What exists in the codebase
3. **Activity patterns** — When and how you work

---

## Memory Signals

### From `progress_log.jsonl`

| Signal | Event Types | Used For |
|--------|-------------|----------|
| Tasks completed | `task_completed` | Completion score |
| Weeks started | `week_started` | Velocity baseline |
| Weeks completed | `week_completed` | Completion, Velocity |
| Ratings | `week_completed.rating` | Quality indicator |
| Retros done | `retro_completed` | Learning score |
| Recent activity | All events (last 14-30 days) | Velocity trend |

### From `learner_profile.json`

| Signal | Field | Used For |
|--------|-------|----------|
| Expected hours | `constraints.hours_per_week` | Velocity baseline |
| Level | `level` | Tier expectations |
| Start date | `start_date` | Timeline calculations |

### From `decisions.jsonl`

| Signal | Decision Types | Used For |
|--------|----------------|----------|
| Path changes | All decisions | Context for evaluation |
| Approved adaptations | `approved_by: learner` | Valid changes |

### From `best_practices.md`

| Signal | How Measured | Used For |
|--------|--------------|----------|
| Practices captured | Count of `### ` headers | Learning score |
| Recent captures | Headers with recent dates | Learning trend |

---

## Repository Signals

### File Existence
| Signal | What We Check | Used For |
|--------|---------------|----------|
| Tests exist | `tests/` directories, `test_*.py` files | Quality score |
| Docs exist | `README.md`, docstrings | Quality score |
| Config exists | `pyproject.toml`, etc. | Quality indicator |

### Activity Patterns
| Signal | What We Measure | Used For |
|--------|-----------------|----------|
| Recent modifications | File timestamps | Velocity |
| Commit frequency | Git history (if available) | Velocity |

---

## Derived Signals

### Trends
```python
# Recent activity (last 14 days)
recent_count = count_events(last_14_days)

# Older activity (14-28 days ago)
older_count = count_events(days_14_to_28)

# Trend
trend = (recent_count - older_count) / older_count
# Positive = improving, Negative = declining
```

### Velocity Indicators
```python
# Events per week (rolling)
events_per_week = total_events / weeks_elapsed

# Task completion rate
completion_rate = tasks_completed / tasks_planned
```

---

## Signal Collection

### When Signals Are Read
- `/status` — Quick read of recent signals
- `/evaluate` — Full signal collection
- `evaluate.py` — Comprehensive analysis

### What Gets Logged
Every time you:
- Start a week → `week_started` event
- Complete a task → `task_completed` event
- Finish a week → `week_completed` event
- Run a retro → `retro_completed` event
- Add a practice → File modification

---

## Signal Weights

Not all signals are equal:

| Signal Category | Weight | Rationale |
|-----------------|--------|-----------|
| Task completions | High | Direct progress indicator |
| Week completions | High | Milestone achievement |
| Retros completed | Medium | Learning behavior |
| Best practices | Medium | Reflection indicator |
| File existence | Low | Proxy for quality |
| Timestamps | Low | Activity indicator |

---

## Missing Signals

### What Happens If No Data
- Empty progress log → Low scores, but not zero
- No profile → Defaults assumed
- No best practices → Learning score impacted

### Bootstrapping
First-time users start with neutral scores:
- Initial scores around 50
- Trends show "insufficient data"
- Recommendations focus on getting started

---

## Signal Privacy

### What's NOT Collected
- File contents (beyond existence)
- Code analysis
- External API calls
- Personal information beyond profile

### Local Only
All signals come from local files. Nothing is sent externally.

---

## Improving Your Signals

### For Completion
- Log task completions explicitly
- Mark weeks as started and completed
- Keep task descriptions specific

### For Quality
- Run `/harden` regularly
- Add tests to projects
- Write documentation

### For Velocity
- Maintain regular activity
- Log events as they happen
- Don't batch updates

### For Learning
- Run `/retro` weekly
- Capture best practices
- Write journal entries

---

## Debugging Signals

### View Raw Data
```bash
# See progress log
cat .claude/memory/progress_log.jsonl

# Count events
wc -l .claude/memory/progress_log.jsonl

# Recent events
tail -20 .claude/memory/progress_log.jsonl
```

### Check What Evaluation Sees
```bash
python .claude/path-engine/evaluate.py --json
```

---

## Related

- [Rubric](rubric.md) — How signals become scores
- [Scoring](scoring.md) — Score calculation details
- [Adaptation Rules](adaptation-rules.md) — How scores trigger changes

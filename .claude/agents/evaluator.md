# Evaluator Agent

## Role

The Evaluator agent scores progress, identifies gaps, and triggers the adaptation engine. This agent is responsible for the "Evaluate" phase of the learning loop.

## Responsibilities

1. **Progress Scoring**: Calculate scores based on rubric
2. **Gap Analysis**: Identify areas needing improvement
3. **Signal Reading**: Parse repo signals (commits, tests, etc.)
4. **Adaptation Triggers**: Recommend when path changes are needed

## Triggers

The Evaluator is invoked by these commands:

| Command | Action |
|---------|--------|
| `/status` | Quick status check |
| `/evaluate` | Full evaluation run |
| `/adapt-path` | Propose path changes |

## Input Context

When activated, the Evaluator reads:

- `.claude/memory/progress_log.jsonl` — All progress entries
- `.claude/memory/decisions.jsonl` — Past adaptation decisions
- `paths/Advanced/tracker.md` — Current tracker state
- Git history — Commit frequency and content
- Test results — pytest outcomes

## Output Artifacts

The Evaluator produces:

1. **Score Report**: Numerical scores per rubric dimension
2. **Gap Analysis**: List of identified gaps
3. **Recommendations**: Suggested actions
4. **Adaptation Proposals**: Specific path mutations (if needed)

## Evaluation Dimensions

| Dimension | Weight | Signals |
|-----------|--------|---------|
| **Completion** | 30% | Tasks done, deliverables shipped |
| **Quality** | 25% | Test coverage, code review scores |
| **Consistency** | 20% | Regular commits, journal entries |
| **Growth** | 15% | Best practices captured, skills applied |
| **Engagement** | 10% | Questions asked, blockers resolved |

## Scoring Process

```python
# Pseudo-code for evaluation
def evaluate():
    progress = read_progress_log()
    signals = read_repo_signals()

    scores = {
        "completion": score_completion(progress),
        "quality": score_quality(signals),
        "consistency": score_consistency(progress),
        "growth": score_growth(progress),
        "engagement": score_engagement(progress)
    }

    overall = weighted_average(scores)

    if overall < 0.6:
        recommend_remediation()
    elif overall > 0.9:
        recommend_acceleration()

    return EvaluationReport(scores, recommendations)
```

## Adaptation Thresholds

| Score Range | Recommendation |
|-------------|----------------|
| 0.0 - 0.4 | Level downgrade consideration |
| 0.4 - 0.6 | Remediation week insertion |
| 0.6 - 0.8 | On track, continue |
| 0.8 - 0.9 | Consider acceleration |
| 0.9 - 1.0 | Level upgrade consideration |

## Collaboration

- Reads input from all other agents
- Triggers **Coach** for guidance
- Feeds into **Planner** for next cycle

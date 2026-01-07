# Path Engine

The Path Engine implements the evaluation and adaptation loop for the AI Practitioner Learning OS. It uses Python stdlib only - no external dependencies required.

## Scripts

| Script | Purpose | Command |
|--------|---------|---------|
| [evaluate.py](evaluate.py) | Score learner progress | `/evaluate` |
| [adapt.py](adapt.py) | Propose path modifications | `/adapt-path` |
| [report.py](report.py) | Generate tracker report | `/report` |

## Usage

From the repository root:

```bash
# Run evaluation
python .claude/path-engine/evaluate.py

# Propose adaptations
python .claude/path-engine/adapt.py

# Generate report
python .claude/path-engine/report.py
```

## How It Works

### 1. Evaluate

`evaluate.py` reads:
- `.claude/memory/learner_profile.json` - Current level and goals
- `.claude/memory/progress_log.jsonl` - Progress events
- `.claude/memory/decisions.jsonl` - Past decisions

It outputs:
- Overall score (0-100)
- Category scores (completion, quality, understanding, consistency)
- Strengths and gaps
- Recommendations

### 2. Adapt

`adapt.py` reads evaluation results and proposes modifications:
- Level changes (upgrade/downgrade)
- Month reordering
- Remediation weeks
- Project swaps

**Important**: Only allowed adaptations are proposed. See [docs/evaluation/adaptation-rules.md](../../docs/evaluation/adaptation-rules.md).

### 3. Report

`report.py` generates/updates:
- `paths/Beginner/tracker.md` - Progress tracker

**Important**: The tracker is a derived artifact. It can be regenerated at any time from memory files.

## Scoring Rubric

| Category | Weight | Measures |
|----------|--------|----------|
| Completion | 30% | Tasks completed, deliverables shipped |
| Quality | 25% | Code quality, test coverage |
| Understanding | 25% | Explanations, decisions documented |
| Consistency | 20% | Regular progress, habit formation |

See [docs/evaluation/scoring.md](../../docs/evaluation/scoring.md) for details.

## Allowed Adaptations

The engine can only propose these modifications:

1. **Level Change**
   ```json
   {"type": "level_change", "from": "Beginner", "to": "Intermediate"}
   ```

2. **Month Reorder**
   ```json
   {"type": "month_reorder", "swap": [5, 6]}
   ```

3. **Remediation Week**
   ```json
   {"type": "remediation_week", "month": 3, "week": 3, "focus": "pandas"}
   ```

4. **Project Swap**
   ```json
   {"type": "project_swap", "month": 4, "from": "projectA", "to": "projectB"}
   ```

## Output Format

### Evaluation Output

```json
{
  "timestamp": "2026-01-07T18:00:00Z",
  "overall_score": 75,
  "categories": {
    "completion": 80,
    "quality": 70,
    "understanding": 75,
    "consistency": 75
  },
  "strengths": ["Regular commits", "Good test coverage"],
  "gaps": ["Documentation incomplete", "Missing retros"],
  "recommendations": ["Add docstrings", "Complete weekly retros"]
}
```

### Adaptation Output

```json
{
  "timestamp": "2026-01-07T18:05:00Z",
  "needs_adaptation": true,
  "proposals": [
    {
      "type": "remediation_week",
      "month": 3,
      "week": 3,
      "focus": "pandas fundamentals",
      "rationale": "Struggling with data manipulation"
    }
  ]
}
```

## Documentation

- [Evaluation Rubric](../../docs/evaluation/rubric.md)
- [Scoring Details](../../docs/evaluation/scoring.md)
- [Signals](../../docs/evaluation/signals.md)
- [Adaptation Rules](../../docs/evaluation/adaptation-rules.md)

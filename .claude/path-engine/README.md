# Path Engine

Python scripts for the evaluation and adaptation loop.

## Overview

The path engine implements the core learning OS loop:
1. **Evaluate** — Compute scores from memory and signals
2. **Adapt** — Propose path changes based on evaluation
3. **Report** — Generate tracker updates

## Scripts

| Script | Purpose | Command |
|--------|---------|---------|
| `evaluate.py` | Compute evaluation scores | `python evaluate.py` |
| `adapt.py` | Propose adaptations | `python adapt.py` |
| `report.py` | Update tracker | `python report.py` |

## Usage

### Run Evaluation
```bash
cd .claude/path-engine
python evaluate.py

# Output: JSON with scores by dimension
```

### See Adaptation Proposals
```bash
python adapt.py

# Output: Proposed changes (require approval)
```

### Generate Tracker Report
```bash
python report.py

# Output: Updates paths/beginner/tracker.md
```

## Human-in-the-Loop

**Critical**: The path engine provides recommendations, not automatic changes.

- `evaluate.py` outputs scores for your review
- `adapt.py` outputs **proposals** — you approve before any changes
- `report.py` updates tracker — you can review/edit the output

## How It Works

### Evaluation Dimensions

The engine scores four dimensions (0-100):

| Dimension | Signals |
|-----------|---------|
| Completion | Tasks done, deliverables shipped, DoD progress |
| Quality | Test coverage (if detectable), docs completeness |
| Velocity | Tasks per week, blocker resolution |
| Learning | Journal entries, best practices, retros |

### Scoring Logic

```python
# Simplified scoring
completion = (completed_tasks / planned_tasks) * 100
quality = evidence_score * 100  # Based on observable signals
velocity = trend_score * 100    # Based on recent pattern
learning = (journal_entries + best_practices + retros) / expected * 100
```

### Adaptation Rules

Proposals are generated based on gaps:
- Large quality gap → Suggest remediation week
- Completion behind → Suggest scope reduction
- Consistent struggle → Suggest level change (at month boundary)
- Ahead of schedule → Suggest acceleration

## Memory Files Used

The engine reads:
- `.claude/memory/learner_profile.json` — Goals and constraints
- `.claude/memory/progress_log.jsonl` — Events and history
- `.claude/memory/decisions.jsonl` — Past decisions
- `.claude/memory/best_practices.md` — Captured learnings

The engine may propose updates to:
- `paths/beginner/tracker.md` — Via `report.py`
- `.claude/memory/decisions.jsonl` — Via approved adaptations

## Implementation Notes

- **Stdlib only**: No external dependencies
- **Reproducible**: Same input → same output
- **Transparent**: Scores explained, not black-box
- **Safe**: Never modifies files without approval

## Extending

To add new signals or rules:
1. Add signal extraction in `evaluate.py`
2. Add adaptation rule in `adapt.py`
3. Update report format in `report.py`
4. Document in `docs/evaluation/`

## Integration with Commands

| Command | Uses |
|---------|------|
| `/status` | Calls evaluate for quick status |
| `/evaluate` | Full evaluation output |
| `/adapt-path` | Calls adapt for proposals |

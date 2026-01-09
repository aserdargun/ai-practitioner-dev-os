# Path Engine

Python scripts for evaluating progress and proposing learning path adaptations.

## Overview

The path engine implements the evaluation → recommendation → approval loop:

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   evaluate.py  →  adapt.py  →  USER APPROVES  →  Apply │
│       ↓            ↓                                    │
│    Scores      Proposals                                │
│       ↓            ↓                                    │
│   report.py    (only if approved)                       │
│       ↓                                                 │
│   tracker.md                                            │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Scripts

| Script | Purpose | Output |
|--------|---------|--------|
| [evaluate.py](evaluate.py) | Compute scores from progress | Evaluation report |
| [adapt.py](adapt.py) | Propose path adaptations | Adaptation proposals |
| [report.py](report.py) | Generate tracker document | tracker.md |

## Usage

```bash
# From repository root

# 1. Run evaluation
python .claude/path-engine/evaluate.py

# 2. Get adaptation proposals
python .claude/path-engine/adapt.py

# 3. Generate tracker (after approving adaptations)
python .claude/path-engine/report.py
```

## Requirements

- Python 3.9+
- No external dependencies (stdlib only)

## Critical: Human Approval

**adapt.py outputs proposals only**. It does not automatically apply changes.

The workflow is:
1. Run evaluate.py → see scores
2. Run adapt.py → see proposals
3. **You review and approve** each proposal
4. Apply approved changes manually or via Claude
5. Run report.py → update tracker

## Input Files

The engine reads from:
- `.claude/memory/learner_profile.json` — Learner configuration
- `.claude/memory/progress_log.jsonl` — Progress events
- `.claude/memory/decisions.jsonl` — Past decisions
- `paths/intermediate/` — Current month content

## Output Files

The engine writes to:
- `paths/intermediate/tracker.md` — Progress tracker (derived, regeneratable)
- stdout — Evaluation reports and proposals

## Scoring Criteria

From `docs/evaluation/rubric.md`:

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Completeness | 25% | Deliverables present |
| Quality | 25% | Code quality, tests |
| Learning | 25% | Skill demonstration |
| Reflection | 25% | Journal entries |

## Allowed Adaptations

From `docs/evaluation/adaptation-rules.md`:

1. **Level Change**: Beginner ↔ Intermediate ↔ Advanced
2. **Month Reorder**: Swap upcoming months
3. **Remediation**: Insert review week
4. **Project Swap**: Replace with equivalent project

## Related Documentation

- [docs/evaluation/rubric.md](../../docs/evaluation/rubric.md) — Scoring rubric
- [docs/evaluation/signals.md](../../docs/evaluation/signals.md) — Input signals
- [docs/evaluation/scoring.md](../../docs/evaluation/scoring.md) — Score computation
- [docs/evaluation/adaptation-rules.md](../../docs/evaluation/adaptation-rules.md) — Adaptation rules

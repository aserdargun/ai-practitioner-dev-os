# Path Engine

Python scripts for evaluation, adaptation, and reporting in the learning OS.

## Overview

The path engine implements the recommendation loop using Python stdlib only. No external dependencies are required.

## Scripts

| Script | Purpose | Output |
|--------|---------|--------|
| `evaluate.py` | Compute progress scores | Evaluation report |
| `adapt.py` | Propose path adaptations | Adaptation proposals |
| `report.py` | Generate/update tracker | Updated tracker.md |

## Usage

From the repository root:

```bash
# 1. Evaluate current progress
python .claude/path-engine/evaluate.py

# 2. Get adaptation proposals (if needed)
python .claude/path-engine/adapt.py

# 3. Update the tracker
python .claude/path-engine/report.py
```

## Workflow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  evaluate   │ ──> │    adapt    │ ──> │   report    │
│             │     │             │     │             │
│ Reads:      │     │ Reads:      │     │ Reads:      │
│ - memory/   │     │ - eval      │     │ - memory/   │
│ - signals   │     │ - rules     │     │ - eval      │
│             │     │             │     │             │
│ Outputs:    │     │ Outputs:    │     │ Outputs:    │
│ - scores    │     │ - proposals │     │ - tracker   │
└─────────────┘     └─────────────┘     └─────────────┘
```

## Human-in-the-Loop

**Critical**: These scripts produce recommendations, not automatic changes.

- `evaluate.py` outputs scores for you to review
- `adapt.py` outputs proposals that require your explicit approval
- `report.py` regenerates the tracker (with confirmation)

## Scoring Categories

| Category | Weight | Description |
|----------|--------|-------------|
| Completion | 40% | DoD items completed |
| Quality | 25% | Tests passing, review feedback |
| Velocity | 20% | Tasks completed vs planned |
| Reflection | 15% | Journal entries, retrospectives |

## Allowed Adaptations

The path engine can only propose these mutations:

1. **Level Change**: Beginner ↔ Intermediate ↔ Advanced
2. **Month Reorder**: Swap upcoming months within tier scope
3. **Remediation Week**: Insert 1-week remediation block
4. **Project Swap**: Replace project with equivalent scope alternative

See `../docs/evaluation/adaptation-rules.md` for the full schema.

## Configuration

The engine reads from:
- `.claude/memory/learner_profile.json` - Learner settings
- `.claude/memory/progress_log.jsonl` - Progress history
- `.claude/memory/decisions.jsonl` - Past decisions
- `paths/advanced/month-XX/README.md` - Month goals

## Output Locations

- Evaluation reports: stdout (review before saving)
- Adaptation proposals: stdout (approve before applying)
- Tracker: `paths/advanced/tracker.md` (regenerated)

## Extending

To add new signals or scoring:

1. Edit `evaluate.py` to collect new signals
2. Add to `_compute_scores()` function
3. Update documentation

To add new adaptation types:

1. Edit `adapt.py` to propose new mutations
2. Add to `ALLOWED_ADAPTATIONS` list
3. Update `../docs/evaluation/adaptation-rules.md`

# Adaptation Rules

How evaluation scores trigger path change proposals.

## Overview

The adaptation system proposes changes based on evaluation results. **All proposals require your explicit approval** before any changes are applied.

Workflow:
```
Evaluate → Propose → YOU APPROVE → Execute
```

---

## Allowed Adaptations

The system can ONLY propose these types of changes:

| Type | Description | When Allowed |
|------|-------------|--------------|
| Remediation Week | Insert focused learning block | Anytime |
| Scope Adjustment | Reduce/expand project scope | Anytime |
| Month Reorder | Swap upcoming months | Anytime |
| Project Swap | Replace project with equivalent | Anytime |
| Level Change | Beginner ↔ Intermediate ↔ Advanced | Month boundaries only |

---

## Proposal Triggers

### Remediation Week

**Triggered when**: Quality score below 55

```python
if quality_score < 55:
    propose("remediation_week", {
        "focus": "testing and quality",
        "duration": "1 week",
        "rationale": f"Quality score ({quality_score}) below target"
    })
```

**What it does**:
- Inserts a focused week on specific skills
- Shifts remaining tasks (uses buffer time)
- No change to month-end deadline

---

### Scope Adjustment

**Triggered when**: Completion score below 50

```python
if completion_score < 50:
    propose("scope_adjustment", {
        "action": "reduce",
        "rationale": f"Completion score ({completion_score}) indicates falling behind"
    })
```

**What it does**:
- Moves non-essential features to stretch goals
- Focuses on core MVP functionality
- Maintains quality on smaller scope

---

### Velocity Investigation

**Triggered when**: Velocity trend is declining

```python
if velocity_trend == "declining":
    propose("process_change", {
        "action": "investigate blockers",
        "rationale": f"Velocity declining (trend: {trend_value})"
    })
```

**What it does**:
- Prompts blocker investigation
- Suggests `/debug-learning`
- Reviews time allocation

---

### Learning Focus

**Triggered when**: Learning score below 50

```python
if learning_score < 50:
    propose("process_change", {
        "action": "increase reflection",
        "rationale": f"Learning score ({learning_score}) is low"
    })
```

**What it does**:
- Suggests regular retrospectives
- Prompts best practice capture
- Encourages journaling

---

### Level Change (Down)

**Triggered when**: Overall score consistently below 40

```python
if overall_score < 40:
    propose("level_change", {
        "direction": "consider_down",
        "requires_month_boundary": True,
        "rationale": f"Overall score ({overall_score}) suggests significant challenges"
    })
```

**Constraints**:
- Only at month boundaries
- User must explicitly approve
- Not automatic

---

### Level Change (Up)

**Triggered when**: Overall score consistently above 85

```python
if overall_score >= 85 and velocity_trend != "declining":
    propose("level_change", {
        "direction": "consider_up",
        "requires_month_boundary": True,
        "rationale": f"Overall score ({overall_score}) is excellent"
    })
```

**Constraints**:
- Only at month boundaries
- User must explicitly approve
- Optional acceleration

---

## Proposal Schema

All proposals follow this format:

```json
{
  "id": "unique_identifier",
  "type": "remediation_week | scope_adjustment | month_reorder | project_swap | level_change | process_change",
  "title": "Human-readable title",
  "description": "What the change involves",
  "rationale": "Why this is proposed",
  "impact": ["List of", "impacts"],
  "priority": "high | medium | low",
  "requires_month_boundary": false
}
```

---

## Approval Workflow

### Step 1: Review Proposals
```
/adapt-path
```

Output shows each proposal with rationale.

### Step 2: Approve or Reject
For each proposal:
- **Approve (Y)**: Change will be applied
- **Reject (N)**: No change, continue as-is
- **Ask Questions**: Get more details before deciding

### Step 3: Apply Approved Changes
Only approved changes are applied:
- Tracker updated
- Decision logged to `decisions.jsonl`
- Plan adjusted accordingly

---

## What Gets Updated

When adaptations are approved:

| Adaptation | Files Updated |
|------------|---------------|
| Remediation Week | `tracker.md`, `decisions.jsonl` |
| Scope Adjustment | `month-XX/README.md`, `decisions.jsonl` |
| Month Reorder | `tracker.md`, `decisions.jsonl` |
| Project Swap | `month-XX/README.md`, `decisions.jsonl` |
| Level Change | `learner_profile.json`, `decisions.jsonl` |

---

## Decision Logging

All approved adaptations are logged:

```json
{
  "timestamp": "2026-03-15T15:00:00Z",
  "decision": "Insert remediation week",
  "rationale": "Quality score (52) below target (55)",
  "approved_by": "learner",
  "category": "path_adaptation",
  "proposal_id": "remediation_quality"
}
```

---

## Thresholds

Current thresholds (can be adjusted):

| Threshold | Value | Triggers |
|-----------|-------|----------|
| `remediation_quality` | 55 | Quality remediation |
| `remediation_completion` | 50 | Scope reduction |
| `scope_reduction` | 45 | Aggressive scope cut |
| `level_down` | 40 | Level change consideration |
| `acceleration` | 85 | Acceleration consideration |

---

## Manual Adaptations

You can also request adaptations manually:

```
I'd like to swap the Month 4 project for something more focused on APIs
```

Claude will:
1. Verify it's an allowed adaptation
2. Propose equivalent alternatives
3. Wait for your approval
4. Apply if approved

---

## What's NOT Allowed

The system cannot propose:
- Skipping entire months
- Reducing tier scope (e.g., dropping Tier 1 items)
- External dependencies
- Permanent changes without approval
- Changes that break prerequisites

---

## Running Adapt

### Command Line
```bash
python .claude/path-engine/adapt.py

# JSON output
python .claude/path-engine/adapt.py --json

# Save proposals for later
python .claude/path-engine/adapt.py --save
```

### Via Claude
```
/adapt-path
```

---

## Related

- [Rubric](rubric.md) — How scores are interpreted
- [Signals](signals.md) — What data triggers adaptations
- [Scoring](scoring.md) — Score calculation details
- [adapt.py](../../.claude/path-engine/adapt.py) — Implementation

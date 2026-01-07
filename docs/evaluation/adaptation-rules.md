# Adaptation Rules

How the learning path can be modified based on your progress.

---

## Overview

The adaptation system can propose changes to your learning path based on evaluation results. All changes follow strict rules and most require your approval.

---

## Allowed Adaptations

The system can **only** propose these four types of changes:

### 1. Level Change

**Description**: Upgrade or downgrade your learner level.

**When Triggered**:
- Downgrade: Overall score < 40% for 2+ consecutive evaluations
- Upgrade: Overall score > 90% for 2+ consecutive evaluations

**What Changes**:
- Level moves between: Beginner ↔ Intermediate ↔ Advanced
- Tier scope adjusts accordingly
- Pace expectations change

**Constraints**:
- Only at month boundaries
- Requires manual approval
- Cannot skip levels

**Example**:
```json
{
  "type": "level_change",
  "description": "Consider moving from Advanced to Intermediate",
  "details": {
    "current_level": "Advanced",
    "proposed_level": "Intermediate",
    "reason": "Overall score below 40% for 2 weeks"
  },
  "requires_approval": true
}
```

---

### 2. Month Reorder

**Description**: Swap the order of upcoming months.

**When Triggered**:
- Specific skill gaps that could be addressed earlier
- Prerequisites not met for current month
- Learner interest alignment

**What Changes**:
- Order of months 2-12 (month 1 is always first)
- Must preserve tier scope

**Constraints**:
- Only future months can be reordered
- Current month cannot be swapped
- Tiers must stay intact

**Example**:
```json
{
  "type": "month_reorder",
  "description": "Swap Month 05 and Month 06",
  "details": {
    "original_order": [5, 6],
    "proposed_order": [6, 5],
    "reason": "Computer Vision skills needed for current project"
  },
  "requires_approval": true
}
```

---

### 3. Remediation Week

**Description**: Insert a 1-week remediation block.

**When Triggered**:
- Overall score between 40-60%
- Specific dimension severely underperforming
- Blocker preventing progress

**What Changes**:
- Adds a catch-up week to current month
- Focuses on weak areas
- Adjusts timeline

**Constraints**:
- Maximum 2 remediation weeks per month
- Must specify focus areas
- Usually auto-approved

**Example**:
```json
{
  "type": "remediation_week",
  "description": "Insert catch-up week focusing on testing",
  "details": {
    "focus_areas": ["quality", "testing"],
    "duration": "1 week",
    "reason": "Quality score at 45%"
  },
  "requires_approval": false
}
```

---

### 4. Project Swap

**Description**: Replace the current project with an equivalent alternative.

**When Triggered**:
- Very low engagement with current project
- Technical blockers preventing completion
- Better alignment with learner goals

**What Changes**:
- Main project for the month
- Deliverables list
- Resources and references

**Constraints**:
- Replacement must be equivalent scope
- Must serve same learning objectives
- Requires manual approval

**Example**:
```json
{
  "type": "project_swap",
  "description": "Replace recommendation system with search engine project",
  "details": {
    "original_project": "Movie Recommendation System",
    "proposed_project": "Semantic Search Engine",
    "reason": "Better alignment with learner's domain interest"
  },
  "requires_approval": true
}
```

---

## Adaptation Thresholds

| Threshold | Value | Action |
|-----------|-------|--------|
| Level Downgrade | < 40% | Consider level change down |
| Remediation | 40-60% | Insert remediation week |
| On Track | 60-80% | No changes |
| Acceleration | > 90% | Consider advanced challenges |

---

## Approval Process

### Auto-Approved Adaptations

These changes can be applied automatically:
- Remediation weeks (when score 40-60%)
- Minor schedule adjustments

### Manual Approval Required

These changes require your explicit approval:
- Level changes
- Month reorders
- Project swaps

### Reviewing Proposals

```
/adapt-path

🔄 Adaptation Proposal
───────────────────────────────

1. [REMEDIATION_WEEK] ✓ Auto-approved
   Insert 1-week catch-up for quality improvement

2. [PROJECT_SWAP] ⚠️ Requires Approval
   Replace current project with alternative

   [A]pprove / [R]eject / [D]efer
```

---

## Decision Logging

All adaptation decisions are logged to `decisions.jsonl`:

```json
{
  "timestamp": "2026-02-15T18:00:00Z",
  "decision_type": "remediation_week",
  "value": true,
  "reason": "Quality score at 52%",
  "proposed_by": "adapt.py",
  "approved": true,
  "approved_by": "auto",
  "applied": true
}
```

---

## Overriding Adaptations

You can always override system proposals:

### Rejecting a Proposal

```
/adapt-path
...
[R]eject

Reason: I prefer to continue with current pace
```

### Deferring a Decision

```
/adapt-path
...
[D]efer

Will be proposed again next evaluation
```

### Manual Override

Edit profile or path files directly:
- Risky: Can break assumptions
- Document: Note changes in decisions.jsonl
- Verify: Run evaluation after changes

---

## Best Practices

### When to Accept Adaptations

- Score consistently below threshold
- Feeling overwhelmed or bored
- Blockers preventing progress
- Clear skill gaps

### When to Reject Adaptations

- Temporary dip (e.g., busy week)
- About to finish current work
- Know the cause and it's resolved
- Prefer current project

### Monitoring Adaptations

1. Review proposals thoughtfully
2. Check decision history periodically
3. Notice patterns in adaptations
4. Discuss with Claude if unsure

---

## Technical Details

### Adaptation Algorithm

```python
def propose_adaptations(evaluation):
    proposals = []

    if evaluation.overall < 0.4:
        proposals.append(level_downgrade())
    elif evaluation.overall < 0.6:
        proposals.append(remediation_week())
    elif evaluation.overall > 0.9:
        proposals.append(acceleration())

    # Check specific dimensions
    if evaluation.quality < 0.5:
        proposals.append(quality_focus())

    return filter_valid(proposals)
```

### Validation Rules

All proposals are validated:
- Type must be one of four allowed
- Constraints must be satisfied
- Cannot conflict with existing changes

---

## See Also

- [Evaluation Rubric](rubric.md) — How scores are calculated
- [Memory System](../memory-system.md) — Decision logging
- [How to Use](../how-to-use.md) — Workflow guide

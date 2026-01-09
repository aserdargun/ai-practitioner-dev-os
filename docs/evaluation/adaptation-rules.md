# Adaptation Rules

What changes are allowed and how they're approved.

## Overview

The path engine can only propose specific types of adaptations. All proposals require explicit user approval before being applied.

## Allowed Adaptations

Only these four mutations are permitted:

| Type | Description |
|------|-------------|
| `level_change` | Change learner level (Beginner ↔ Intermediate ↔ Advanced) |
| `month_reorder` | Swap upcoming months within tier scope |
| `remediation_week` | Insert 1-week remediation block |
| `project_swap` | Replace project with equivalent scope alternative |

## Human Approval Requirement

**Critical**: No adaptations are applied automatically.

The workflow is:
1. `evaluate.py` computes scores
2. `adapt.py` proposes changes
3. **You review each proposal**
4. **You approve, modify, or reject**
5. Only approved changes are applied

## Adaptation Schemas

### Level Change

```json
{
  "type": "level_change",
  "from": "advanced",
  "to": "intermediate",
  "rationale": "3 consecutive months below threshold",
  "reversible": true,
  "review_at_month": 6
}
```

**When triggered**:
- Overall score <55% for 2+ months
- Consistent struggle with tier scope
- User requests level change

**Impact**:
- Changes tier scope (what technologies are included)
- Adjusts month project complexity
- Updates learner profile

### Month Reorder

```json
{
  "type": "month_reorder",
  "swap": [4, 5],
  "rationale": "Month 05 has better prerequisites for current situation",
  "impact": "Different order, same content coverage",
  "tier_scope": "unchanged"
}
```

**When triggered**:
- Prerequisites not met for upcoming month
- Interest alignment (user wants different order)
- Performance suggests different sequencing

**Constraints**:
- Must preserve tier scope
- Only swap upcoming months (not past)
- Month 12 cannot be moved earlier

### Remediation Week

```json
{
  "type": "remediation_week",
  "month": 3,
  "insert_after_week": 4,
  "focus": "Complete remaining RAG deliverables",
  "rationale": "Completion at 60%, extra time needed",
  "impact": "Month 04 starts 1 week later"
}
```

**When triggered**:
- Completion <70% at month end
- Velocity drop mid-month
- Specific skill gap identified

**Constraints**:
- Maximum 2 remediation weeks per month
- Does not change tier scope
- Must specify focus area

### Project Swap

```json
{
  "type": "project_swap",
  "month": 4,
  "original": "Full RAG with Kubernetes",
  "replacement": "RAG with Docker Compose",
  "rationale": "K8s complexity causing delays, Docker achieves same learning goals",
  "tier_scope": "unchanged",
  "dod_equivalent": true
}
```

**When triggered**:
- Project is significantly harder than expected
- User has constraints that make original infeasible
- Better project fit for learning goals

**Constraints**:
- Must maintain equivalent scope
- Same core skills covered
- DoD should be comparable

## Triggering Conditions

### Automatic Triggers (Proposals Generated)

| Condition | Proposed Adaptation |
|-----------|---------------------|
| Overall <50% | Level change |
| Completion <60% | Remediation week |
| Velocity <50% | Remediation week |
| 3+ blockers same topic | Project swap |
| Overall >90% | Acceleration (month reorder) |

### Manual Triggers (User Request)

You can request adaptations at any time:
```
/adapt-path "I want to swap Month 04 and 05"
```

## Approval Process

### Step 1: Generate Proposals

```bash
python .claude/path-engine/adapt.py
```

### Step 2: Review Output

```
## Adaptation Proposals

### Proposal 1: Remediation Week
...

**Approve?** (1/none)
```

### Step 3: Approve or Reject

- Approve: Apply the change
- Modify: Adjust the proposal
- Reject: Continue as planned

### Step 4: Apply Changes

After approval:
1. Update relevant files (profile, month READMEs)
2. Log to decisions.jsonl
3. Update tracker

### Step 5: Verify

Run `/status` to confirm changes applied.

## Logging Adaptations

All adaptations must be logged:

```json
{
  "timestamp": "2026-01-09T15:00:00Z",
  "type": "adaptation_applied",
  "adaptation": "remediation_week",
  "details": {
    "month": 3,
    "focus": "RAG completion"
  },
  "approved_by": "user"
}
```

## Forbidden Mutations

The system cannot propose:
- ❌ Removing months
- ❌ Adding technologies outside tier scope
- ❌ Changing past month records
- ❌ Modifying memory files automatically
- ❌ Skipping evaluation/approval

## Edge Cases

### Multiple Proposals

If multiple adaptations are proposed:
- Review each independently
- May approve some, reject others
- Consider combined impact

### Conflicting Proposals

If proposals conflict:
- System flags the conflict
- User chooses which to apply
- Or rejects both

### Undoing Adaptations

Most adaptations are reversible:
- Level changes can be reversed
- Month reorders can be re-swapped
- Remediation weeks are additions (no undo needed)
- Project swaps can be reverted

Log all reversals to decisions.jsonl.

## Implementation

Adaptations are proposed by:
```
.claude/path-engine/adapt.py
```

Applied by:
- Manual file edits (recommended)
- Or Claude with approval

Tracked in:
```
.claude/memory/decisions.jsonl
```

## Related Docs

- [Rubric](rubric.md) - What triggers proposals
- [Scoring](scoring.md) - How scores are computed
- [Path Engine](../../.claude/path-engine/README.md) - Technical implementation

# Adaptation Rules

This document defines the allowed adaptations and their schemas. The adaptation engine (`adapt.py`) can ONLY propose these modifications.

## Allowed Adaptations

The system can propose exactly four types of modifications:

1. **Level Change** - Upgrade or downgrade learner level
2. **Month Reorder** - Swap upcoming month modules
3. **Remediation Week** - Insert a focused remediation block
4. **Project Swap** - Replace a project with equivalent alternative

## Adaptation Schemas

### 1. Level Change

Change the learner's level (Beginner ↔ Intermediate ↔ Advanced).

**Schema**:
```json
{
  "type": "level_change",
  "from": "Beginner",
  "to": "Intermediate",
  "effective": "next_month_boundary",
  "rationale": "Consistently scoring 90+ with strong understanding"
}
```

**Fields**:
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| type | string | yes | Always "level_change" |
| from | string | yes | Current level |
| to | string | yes | Target level |
| effective | string | yes | When change takes effect |
| rationale | string | yes | Why this change is proposed |

**Constraints**:
- Can only change at month boundaries (unless rubric override)
- Cannot skip levels (Beginner → Advanced not allowed)
- Requires learner consent

**Triggers**:
- Upgrade: Score ≥ 90 for 2+ consecutive evaluations
- Downgrade: Score < 50 for 2+ consecutive evaluations

### 2. Month Reorder

Swap the order of upcoming months within tier scope.

**Schema**:
```json
{
  "type": "month_reorder",
  "swap": [5, 6],
  "rationale": "Month 6 topic better prepares for current project"
}
```

**Fields**:
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| type | string | yes | Always "month_reorder" |
| swap | array[int] | yes | Two month numbers to swap |
| rationale | string | yes | Why this reorder helps |

**Constraints**:
- Can only swap upcoming months (not current or past)
- Must preserve tier scope (Beginner stays in Tier 1)
- Maximum one swap per adaptation cycle

**Triggers**:
- Learner interest alignment
- Prerequisite optimization
- Project dependencies

### 3. Remediation Week

Insert a 1-week focused remediation block.

**Schema**:
```json
{
  "type": "remediation_week",
  "month": 3,
  "week": 3,
  "focus": "pandas fundamentals",
  "rationale": "Struggling with groupby and merge operations"
}
```

**Fields**:
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| type | string | yes | Always "remediation_week" |
| month | int | yes | Current month |
| week | int | yes | Week to insert remediation |
| focus | string | yes | What to focus on |
| rationale | string | yes | Why remediation is needed |

**Constraints**:
- Maximum 2 remediation weeks per month
- Cannot remediate past months
- Does not change tier scope

**Triggers**:
- Category score < 60
- Multiple failed attempts on same topic
- Learner request

### 4. Project Swap

Replace a month's project with an equivalent alternative.

**Schema**:
```json
{
  "type": "project_swap",
  "month": 4,
  "original": "sentiment-analysis",
  "replacement": "topic-modeling",
  "rationale": "Better aligned with learner's NLP interests"
}
```

**Fields**:
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| type | string | yes | Always "project_swap" |
| month | int | yes | Month to swap project |
| original | string | yes | Current project name |
| replacement | string | yes | Alternative project name |
| rationale | string | yes | Why swap is beneficial |

**Constraints**:
- Replacement must be equivalent scope/skills
- Must stay within tier
- Deliverables and DoD must be comparable
- Can only swap upcoming months

**Triggers**:
- Learner interest alignment
- Resource availability
- Industry relevance

## Decision Process

### Evaluation → Adaptation Flow

```
1. Run evaluation (evaluate.py)
   ↓
2. Check score against thresholds
   ↓
3. If adaptation needed, propose changes
   ↓
4. Log proposal to decisions.jsonl
   ↓
5. Present to learner for approval
   ↓
6. If approved, update learner_profile.json
```

### Threshold Rules

| Condition | Possible Adaptation |
|-----------|---------------------|
| Score ≥ 90 (2+ times) | Level upgrade |
| Score < 60 | Remediation week |
| Score < 50 (2+ times) | Level downgrade |
| Category < 50 | Remediation for that area |

### Priority Order

When multiple adaptations are possible:

1. **Level change** (most significant)
2. **Remediation week** (immediate help)
3. **Project swap** (alignment)
4. **Month reorder** (optimization)

## Learner Consent

All adaptations require explicit learner consent:

```
Proposed Adaptation:
  Type: remediation_week
  Month: 3, Week: 3
  Focus: pandas fundamentals
  Rationale: Struggling with data manipulation

Do you accept this adaptation? (yes/no)
```

The system will:
- Explain the proposal clearly
- Show expected impact
- Wait for confirmation
- Log the decision either way

## Logging

All proposals are logged to `decisions.jsonl`:

```json
{
  "timestamp": "2026-02-01T09:00:00Z",
  "decision": "remediation_week",
  "status": "proposed",
  "month": 3,
  "week": 3,
  "focus": "pandas fundamentals",
  "rationale": "Struggling with groupby operations"
}
```

After learner response:

```json
{
  "timestamp": "2026-02-01T09:05:00Z",
  "decision": "remediation_week",
  "status": "accepted",
  "month": 3,
  "week": 3,
  "focus": "pandas fundamentals"
}
```

## Implementation

The adaptation logic is in:
- `.claude/path-engine/adapt.py`

To check for adaptations:
```bash
python .claude/path-engine/adapt.py
```

## Forbidden Adaptations

The system CANNOT:
- Skip months entirely
- Remove required deliverables
- Change tier scope mid-month
- Reduce quality requirements
- Bypass prerequisites
- Auto-accept adaptations

## Related Documentation

- [Rubric](rubric.md) - What triggers adaptations
- [Scoring](scoring.md) - How scores are calculated
- [Signals](signals.md) - Input data
- [Path Engine](../../.claude/path-engine/README.md) - Implementation

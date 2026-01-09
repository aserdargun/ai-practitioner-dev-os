# Adaptation Rules

Rules governing how the learning path can be adapted.

## Core Principle

**All adaptations require explicit user approval.**

The system:
1. Evaluates progress
2. Proposes adaptations
3. **Waits for your approval**
4. Applies only what you approve

---

## Allowed Adaptations

The system can ONLY propose these four types of changes:

### 1. Level Change

Move between learner levels.

| Change | Trigger | Impact |
|--------|---------|--------|
| Beginner → Intermediate | Sustained 90+ scores | Add Tier 2 technologies |
| Intermediate → Advanced | Sustained 90+ scores | Add Tier 3 technologies |
| Advanced → Intermediate | Sustained below 60 | Remove Tier 3 focus |
| Intermediate → Beginner | Sustained below 60 | Focus on Tier 1 only |

**Constraints**:
- Only at month boundaries (unless override)
- Requires 3+ consecutive evaluations showing pattern
- User must explicitly approve

### 2. Month Reorder

Swap upcoming months within curriculum.

| Example | Reason |
|---------|--------|
| Swap Month 5 ↔ 6 | Better prerequisite ordering |
| Move Month 8 earlier | More relevant to current work |

**Constraints**:
- Only affects upcoming months (not completed)
- Must maintain tier scope
- Cannot skip required foundations

### 3. Remediation Week

Insert a 1-week review block.

| Trigger | Action |
|---------|--------|
| Struggling with concepts | Add review week |
| Knowledge gap identified | Focused practice week |
| Low scores in specific area | Targeted remediation |

**Constraints**:
- Maximum 1 remediation per month
- Does not change tier scope
- Week is inserted, not replaced

### 4. Project Swap

Replace a month's project with an equivalent.

| Original | Swap | Reason |
|----------|------|--------|
| NER System | Sentiment API | Better domain fit |
| E-commerce ML | Healthcare ML | Work relevance |

**Constraints**:
- Same tier scope requirements
- Equivalent learning outcomes
- Comparable deliverables and DoD

---

## Proposal Schema

All proposals follow this schema:

```json
{
  "type": "level_change | month_reorder | remediation_week | project_swap",
  "timestamp": "ISO-8601 timestamp",
  "rationale": "Why this is proposed",
  "details": {
    // Type-specific details
  },
  "impact": "What changes",
  "risk": "Potential downsides",
  "requires_approval": true
}
```

### Level Change Schema

```json
{
  "type": "level_change",
  "from_level": "intermediate",
  "to_level": "advanced",
  "rationale": "Sustained 90+ scores for 4 weeks",
  "impact": "Tier 3 technologies will be added",
  "risk": "Increased complexity"
}
```

### Month Reorder Schema

```json
{
  "type": "month_reorder",
  "from_order": [5, 6],
  "to_order": [6, 5],
  "rationale": "Month 6 content is prerequisite for month 5 project",
  "impact": "Swap delivery order of these months",
  "risk": "None identified"
}
```

### Remediation Schema

```json
{
  "type": "remediation_week",
  "focus_areas": ["data_quality", "feature_engineering"],
  "insert_at": "Month 4, Week 2",
  "rationale": "Quality scores below 60 for 2 weeks",
  "impact": "Month 4 extends by 1 week",
  "risk": "Delays subsequent timeline"
}
```

### Project Swap Schema

```json
{
  "type": "project_swap",
  "from_project": "Custom NER System",
  "to_project": "Sentiment Analysis API",
  "month": 4,
  "rationale": "Better alignment with learner's work domain",
  "impact": "Different project, same learning outcomes",
  "risk": "May require some research ramp-up"
}
```

---

## Approval Workflow

### 1. Proposal Generation

```bash
python .claude/path-engine/adapt.py
```

Output:
```
=== ADAPTATION PROPOSALS ===

PROPOSAL 1: Level Change
  From: intermediate
  To: advanced
  Rationale: Sustained 90+ scores for 4 weeks
  Impact: Tier 3 technologies will be added
  Risk: Increased complexity

Choose:
- A: Approve Proposal 1
- N: No adaptation needed
- D: Discuss further
```

### 2. User Decision

You review and choose:
- **Approve**: The change will be applied
- **Reject**: No change made
- **Discuss**: Ask for more information

### 3. Recording

Approved adaptations are recorded in `decisions.jsonl`:

```json
{
  "timestamp": "2026-03-15T10:00:00Z",
  "type": "path_adaptation",
  "adaptation": "level_change",
  "details": {
    "from": "intermediate",
    "to": "advanced"
  },
  "rationale": "Sustained high performance",
  "approved_by": "learner"
}
```

### 4. Application

Only after approval:
- Memory files updated
- Profile adjusted (if level change)
- Tracker regenerated

---

## What adapt.py Cannot Do

The script is constrained to **never**:

- Auto-apply any changes
- Skip required content
- Change evaluation criteria
- Modify without approval
- Access external systems
- Delete memory entries

---

## Edge Cases

### Multiple Proposals

If multiple adaptations are proposed:
- Each is presented separately
- You approve each independently
- Conflicting proposals are flagged

### Rejected Proposals

If you reject a proposal:
- No change is made
- Rejection is logged (optional)
- System continues with current path

### Override Requests

You can request adaptations manually:
```
/adapt-path

I want to swap Month 5's project to something related to NLP.
Can you propose alternatives?
```

---

## Thresholds

| Threshold | Value | Triggers |
|-----------|-------|----------|
| Upgrade consideration | 90+ | Level up proposal |
| Downgrade consideration | Below 60 | Level down proposal |
| Remediation trigger | Below 60 in criterion | Remediation proposal |
| Trend window | 3+ evaluations | Pattern recognition |

---

## Related Documentation

- [rubric.md](rubric.md) — Scoring criteria
- [scoring.md](scoring.md) — Score computation
- [../.claude/path-engine/adapt.py](../../.claude/path-engine/adapt.py) — Implementation
- [../memory-system.md](../memory-system.md) — How decisions are stored

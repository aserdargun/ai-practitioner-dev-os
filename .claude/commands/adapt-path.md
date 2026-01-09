# Command: /adapt-path

## Purpose

Propose path adaptations based on evaluation results. This command suggests changes to your learning path when needed.

## Inputs

- Evaluation results (run `/evaluate` first)
- Current path state
- Allowed adaptations schema

## Outputs

- Proposed adaptations with rationale
- Impact analysis
- **User must explicitly approve each change**
- No changes are applied automatically

## When to Use

- After `/evaluate` shows concerning scores
- When feeling off-track
- At month boundaries
- When circumstances change (schedule, goals)

## Agent Routing

**Primary**: Evaluator Agent

The Evaluator proposes adaptations using only the allowed mutation types.

## Allowed Adaptations

Only these changes can be proposed:

| Type | Description | When Appropriate |
|------|-------------|------------------|
| `level_change` | Beginner ↔ Intermediate ↔ Advanced | Sustained over/under performance |
| `month_reorder` | Swap upcoming month modules | Prerequisites, interest, circumstances |
| `remediation_week` | Insert 1-week remediation | Specific skill gap |
| `project_swap` | Replace project with equivalent | Better fit for goals/constraints |

## Example Usage

**User Input**:
```
/adapt-path
```

**Expected Output**:
```
## Path Adaptation Proposals

Based on Month 03 evaluation (score: 68%, below 70% threshold):

---

### Proposal 1: Remediation Week

**Type**: `remediation_week`

**Details**:
```json
{
  "type": "remediation_week",
  "month": 3,
  "insert_after_week": 4,
  "focus": "RAG evaluation and chunking optimization",
  "rationale": "Quality score strong (90%) but completion lagging (60%). Extra week to finish DoD items without rushing.",
  "impact": "Month 04 starts 1 week later"
}
```

**Approve this adaptation?** (yes/no)

---

### Proposal 2: Month Reorder (Alternative)

**Type**: `month_reorder`

**Details**:
```json
{
  "type": "month_reorder",
  "swap": [4, 5],
  "rationale": "Month 05 (API Development) may be easier momentum-builder before Month 04 (Advanced RAG). Tier scope unchanged.",
  "impact": "Different order, same content coverage"
}
```

**Approve this adaptation?** (yes/no)

---

### No Mandatory Changes

Your score is close to threshold. These are suggestions, not requirements.

Options:
1. Apply Proposal 1 (remediation week)
2. Apply Proposal 2 (reorder months)
3. Apply both
4. Continue as planned (no changes)

**Your choice?**
```

## Level Change Example

For significant under/over performance:

```json
{
  "type": "level_change",
  "from": "Advanced",
  "to": "Intermediate",
  "rationale": "3 consecutive months below threshold. Reducing scope to Tier 1 + Tier 2 only may help build momentum.",
  "reversible": true,
  "review_at": "Month 06"
}
```

## Project Swap Example

```json
{
  "type": "project_swap",
  "month": 4,
  "original": "Full RAG System with Kubernetes",
  "replacement": "RAG System with Docker Compose",
  "rationale": "K8s complexity causing delays. Docker Compose achieves same learning goals at lower infra cost.",
  "tier_scope": "unchanged"
}
```

## Human Approval Requirement

**Critical**: `adapt.py` and this command ONLY propose changes. They are NEVER applied automatically.

The flow is:
1. `/evaluate` computes scores
2. `/adapt-path` proposes changes
3. **You review and approve/reject each proposal**
4. Only approved changes are applied

## Related Commands

- `/evaluate` - Run this first
- `/plan-week` - After adaptations approved
- `/status` - Check new path state

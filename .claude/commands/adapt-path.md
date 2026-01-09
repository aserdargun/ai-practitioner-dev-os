# Command: /adapt-path

## Purpose
Get proposed path adaptations based on evaluation results. Proposals require your explicit approval before any changes are applied.

## Inputs
- Recent evaluation results (from `/evaluate`)
- Current progress and blockers
- Learner profile and constraints

## Outputs
- **Adaptation Proposals**: Specific changes recommended
- **Rationale**: Why each adaptation is suggested
- **Impact Assessment**: What changes if you approve
- **Approval Prompt**: Clear yes/no decision for each proposal

## When to Use
- After running `/evaluate` and seeing gaps
- When feeling off-track or overwhelmed
- At month boundaries
- When circumstances change significantly

## Agent Routing
**Evaluator** — generates proposals based on evaluation

## Example Usage

### Get Recommendations
```
/adapt-path
```

### After Evaluation
```
/evaluate
then
/adapt-path
```

### With Context
```
/adapt-path
My situation has changed — I have less time for the next 2 months
```

## Sample Output

```
🔄 ADAPTATION PROPOSALS — Month 3

Based on your evaluation (67/100) and current context,
here are proposed adaptations:

───────────────────────────────────────────────────
PROPOSAL 1: Insert Remediation Week
───────────────────────────────────────────────────

What: Add a 1-week focused remediation block for testing skills

Why: Quality score (58) is below target (70). Test coverage
gap is the primary driver. A focused week can close this gap.

Impact:
- Week 3 becomes "Testing Fundamentals" week
- Current Week 3-4 tasks shift to Week 4-5
- Month end date unchanged (buffer absorbed)

Approve this proposal? [Y/N]

───────────────────────────────────────────────────
PROPOSAL 2: Project Scope Adjustment
───────────────────────────────────────────────────

What: Reduce Month 3 project scope to core features only

Why: Velocity is good (75) but you're at risk of burnout
with current scope. Reducing scope maintains quality.

Impact:
- Remove "advanced filtering" feature from DoD
- Focus on core data pipeline functionality
- Stretch goals become Month 4 candidates

Approve this proposal? [Y/N]

───────────────────────────────────────────────────
NO PROPOSALS FOR:
───────────────────────────────────────────────────

- Level Change: Not recommended (scores in range)
- Month Reorder: Not applicable (current sequence optimal)
- Project Swap: Not needed (current project appropriate)

───────────────────────────────────────────────────

To apply approved proposals, I'll update:
- paths/beginner/tracker.md
- paths/beginner/month-03/README.md
- .claude/memory/decisions.jsonl

No changes will be made until you explicitly approve.
```

## Allowed Adaptations

The system can only propose these types of changes:

| Adaptation | Description | When Applied |
|------------|-------------|--------------|
| Level Change | Beginner ↔ Intermediate ↔ Advanced | Month boundaries |
| Month Reorder | Swap upcoming month modules | Anytime |
| Remediation Week | Insert 1-week focused block | Anytime |
| Project Swap | Replace project with equivalent | Anytime |

## Approval Workflow

1. Review each proposal carefully
2. Ask clarifying questions if needed
3. Approve (Y) or Reject (N) each proposal
4. Only approved changes are applied
5. Changes logged to `decisions.jsonl`

## Related Commands
- `/evaluate` — Get scores before adaptations
- `/status` — Check current state
- `/plan-week` — Re-plan after adaptations

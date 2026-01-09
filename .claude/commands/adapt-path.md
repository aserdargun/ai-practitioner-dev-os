# Command: /adapt-path

## Purpose

Request or review learning path adaptations based on your progress and evaluation results.

## Inputs

Optional context:
- Specific adaptation you're considering
- Challenges you're facing
- Goals that have changed

The command reads from:
- `.claude/memory/progress_log.jsonl`
- `.claude/memory/decisions.jsonl`
- Recent evaluation results
- `docs/evaluation/adaptation-rules.md`

## Outputs

- Current path assessment
- Proposed adaptations (if any)
- Impact analysis
- Implementation plan

**Critical**: All adaptations require your explicit approval.

## When to Use

- After evaluation shows consistent patterns
- When significantly ahead or behind
- At month boundaries
- When circumstances change

## Agent Routing

**Primary**: Evaluator Agent
**Secondary**: Coach Agent

Evaluator proposes adaptations based on data; Coach provides perspective.

## Example Usage

```
/adapt-path
```

Or with context:

```
/adapt-path

I've been consistently scoring above 90% and finding the material
too easy. Should I consider moving to Advanced?
```

## Allowed Adaptations

From `docs/evaluation/adaptation-rules.md`:

| Adaptation | Description | Trigger |
|------------|-------------|---------|
| Level Change | Beginner ↔ Intermediate ↔ Advanced | Consistent over/under performance |
| Month Reorder | Swap upcoming months | Prerequisites or interest |
| Remediation | Insert 1-week review block | Struggling with concepts |
| Project Swap | Replace project with equivalent | Better fit for goals |

## Output Format

```markdown
## Path Adaptation Analysis

### Current Status
- Level: Intermediate
- Month: 5 of 12
- Recent scores: [list]
- Trend: [improving/stable/declining]

### Assessment
[Analysis of your progress patterns]

### Proposed Adaptations

#### Option 1: [Adaptation Type]
- **What**: [description]
- **Why**: [rationale based on data]
- **Impact**: [what changes]
- **Risk**: [potential downsides]

#### Option 2: [Adaptation Type]
- ...

### Recommendation
Based on the data, I recommend: [specific recommendation]

### If You Approve

Implementation steps:
1. [Step 1]
2. [Step 2]
3. [Step 3]

Files that will be updated:
- `.claude/memory/decisions.jsonl` (record decision)
- `paths/intermediate/tracker.md` (update path)
- [other affected files]

---
**Choose an option:**
- A: Approve Option 1
- B: Approve Option 2
- N: No adaptation needed
- D: Discuss further
```

## Decision Recording

Approved adaptations are logged to `.claude/memory/decisions.jsonl`:
```json
{
  "timestamp": "2026-03-15T10:30:00Z",
  "type": "path_adaptation",
  "adaptation": "month_reorder",
  "details": {"from": [5,6], "to": [6,5]},
  "rationale": "Better prerequisite ordering",
  "approved_by": "learner"
}
```

## Integration with Path Engine

This command wraps `.claude/path-engine/adapt.py`:
```bash
python .claude/path-engine/adapt.py
```

The script outputs proposals only; actual changes require your approval.

# Command: /ship-mvp

## Purpose

Get a checklist and guidance for completing the Minimum Viable Product for your current project.

## Inputs

Optional context:
- Current state of your implementation
- Specific concerns or blockers

The command reads from:
- Current month's README (for DoD criteria)
- Your codebase
- `.claude/skills/` for relevant playbooks

## Outputs

- MVP completion checklist
- Gap analysis (what's done vs. what's needed)
- Implementation guidance for missing pieces
- Quality gates before "done"

## When to Use

- Week 2 of monthly cycle
- When core features are mostly implemented
- Before moving to hardening phase

## Agent Routing

**Primary**: Builder Agent

The Builder reviews your current implementation against MVP requirements and provides actionable guidance.

## Example Usage

```
/ship-mvp
```

Or with context:

```
/ship-mvp

I've implemented the data ingestion and basic retrieval. Still need to
add the answer generation step.
```

## Output Format

```markdown
## MVP Checklist — [Project Name]

### Core Requirements
From the Definition of Done:
- [x] Requirement 1 — implemented in `file.py`
- [ ] Requirement 2 — **missing**
- [x] Requirement 3 — implemented

### Gap Analysis

#### Missing Components
1. **[Component name]**
   - What: [description]
   - Where: [suggested location]
   - How: [brief approach]

#### Incomplete Components
1. **[Component name]**
   - Status: [what exists]
   - Needed: [what's missing]

### Implementation Guidance

For [missing component]:
```python
# Suggested approach
[code snippet]
```

### Quality Gates
Before considering MVP complete:
- [ ] Core functionality works end-to-end
- [ ] Basic error handling in place
- [ ] At least one test per component
- [ ] README updated with usage

### Recommended Next Steps
1. [First priority]
2. [Second priority]
3. [Third priority]

---
**Ready to implement? Approve to proceed.**
```

## MVP Definition

For Intermediate level, MVP means:
- Core functionality working
- Basic tests passing
- Minimal documentation
- Can be demonstrated

Hardening (tests, edge cases, polish) comes in Week 3 with `/harden`.

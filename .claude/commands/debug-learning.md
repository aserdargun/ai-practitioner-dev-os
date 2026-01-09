# Command: /debug-learning

## Purpose

Troubleshoot blockers in your learning journey — whether conceptual confusion, technical issues, or motivation challenges.

## Inputs

Required:
- Description of what you're stuck on

Optional:
- What you've already tried
- How long you've been stuck
- Related context

## Outputs

- Problem diagnosis
- Potential root causes
- Solution approaches
- Resources for help
- Action plan

## When to Use

- Stuck for more than one session
- Confused about concepts
- Technical issues blocking progress
- Feeling overwhelmed or unmotivated
- Not sure what's wrong

## Agent Routing

**Primary**: Coach Agent
**Secondary**: Researcher Agent

Coach diagnoses the issue; Researcher finds relevant resources.

## Example Usage

```
/debug-learning

I've been trying to understand attention mechanisms for three days.
I've read the original paper and watched videos but it's not clicking.
```

Or for technical issues:

```
/debug-learning

My model training keeps running out of memory. I've tried reducing
batch size but it's still crashing.
```

## Output Format

```markdown
## Learning Debug — [Topic/Issue]

### Understanding the Blocker

**What I hear**: [restating the problem]

**Type of blocker**:
- [ ] Conceptual — don't understand the idea
- [ ] Technical — code/tool not working
- [ ] Process — not sure how to proceed
- [ ] Motivation — struggling to engage
- [ ] Resource — missing something needed

### Diagnosis

[Analysis of likely root causes]

### Potential Causes
1. **[Cause 1]**
   - Why this might be it: [explanation]
   - Check: [how to verify]

2. **[Cause 2]**
   - ...

### Solution Approaches

#### Approach 1: [Name]
[Description and steps]

#### Approach 2: [Name]
[Description and steps]

### Resources
- [Resource 1] — for [specific aspect]
- [Resource 2] — for [specific aspect]

### Recommended Action Plan
1. First, try: [immediate action]
2. Then: [next step]
3. If still stuck: [escalation]

### Questions for Clarification
- [Question that might help narrow down the issue]
- [Another question]

---
**Would you like to explore any of these approaches?**
```

## Common Blocker Types

### Conceptual
- Missing prerequisite knowledge
- Abstract concept needs concrete example
- Multiple explanations help different learners

### Technical
- Environment issues
- Configuration problems
- Bug in code
- Resource constraints

### Process
- Unclear next steps
- Too many options
- Perfectionism paralysis

### Motivation
- Burnout
- Imposter syndrome
- Unclear purpose
- Isolation

## Escalation Path

If `/debug-learning` doesn't resolve:
1. Try breaking the problem smaller
2. Seek external help (community, mentor)
3. Consider path adaptation (`/adapt-path`)
4. Take a strategic break

## Related Commands

- `/status` — Check overall progress context
- `/coach` — General guidance and support
- `/adapt-path` — If consistent struggles suggest path change

# Command: /add-best-practice

## Purpose

Document a learning, insight, or best practice for future reference in your growing knowledge base.

## Inputs

Required:
- The learning or insight to capture

Optional:
- Context where it applies
- Category/tags
- Related resources

## Outputs

- Formatted best practice entry
- Updated `.claude/memory/best_practices.md`

**Note**: Entry is proposed for your approval before saving.

## When to Use

- After a breakthrough or "aha" moment
- When you solve a tricky problem
- When you discover a useful pattern
- After making a mistake worth remembering
- When a retrospective surfaces key insights

## Agent Routing

**Primary**: Coach Agent

The Coach helps structure your learning into a reusable format.

## Example Usage

```
/add-best-practice

I learned that when building RAG systems, it's crucial to evaluate
retrieval quality separately from generation quality. I spent hours
debugging generation when the real problem was retrieval.
```

## Output Format

```markdown
## Proposed Best Practice Entry

### Title
[Concise title for the learning]

### Category
[e.g., RAG, Testing, Debugging, MLOps, etc.]

### The Learning
[Clear statement of the insight]

### Context
[When this applies]

### Example
[Concrete example or story]

### Action
[How to apply this in the future]

### Related
- [Related topics or resources]

---

**Preview in best_practices.md:**

```markdown
### [Title]
**Category**: [category] | **Added**: [date]

[The learning]

**When to apply**: [context]

**Example**: [example]
```

---
**Add this entry?** (yes/no/modify)
```

## Best Practices File

Location: `.claude/memory/best_practices.md`

Structure:
```markdown
# Best Practices

A living document of learnings accumulated during the AI Practitioner journey.

## How to Use
- Review before starting new projects
- Search when facing similar challenges
- Update as you learn more

---

## Entries

### [Entry 1 Title]
...

### [Entry 2 Title]
...
```

## Categories

Common categories:
- **Data**: Data handling, quality, pipelines
- **ML**: Model training, evaluation, deployment
- **RAG**: Retrieval, generation, evaluation
- **Code**: Coding patterns, debugging, testing
- **MLOps**: CI/CD, monitoring, deployment
- **Process**: Workflow, planning, retrospectives
- **Tools**: Specific tool tips and tricks

## Related Commands

- `/retro` — Often surfaces learnings to capture
- `/debug-learning` — Problem-solving may yield insights
- `/evaluate` — Evaluation may reveal patterns

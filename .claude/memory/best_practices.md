# Best Practices

This file contains accumulated learnings and best practices captured during the learning journey. Each entry is append-only—never delete existing entries.

---

## How to Add Entries

Use the `/add-best-practice` command or manually append entries in this format:

```markdown
### [Date] - [Title]

**Context**: [When does this apply?]

**Practice**: [What to do]

**Why**: [Reasoning/evidence]

**Example**:
[Code or process example if applicable]
```

---

## Entries

### 2026-01-01 - Start with Working Code

**Context**: Beginning any new project or feature

**Practice**: Always start with the simplest working version before adding complexity.

**Why**: It's easier to iterate on something that works than to debug something complex that doesn't.

**Example**:
```python
# Start simple
def process_data(data):
    return data

# Then iterate
def process_data(data):
    validated = validate(data)
    transformed = transform(validated)
    return transformed
```

---

### 2026-01-01 - Commit Early and Often

**Context**: During any development work

**Practice**: Make small, focused commits with clear messages. Commit working states frequently.

**Why**: Small commits are easier to review, revert, and understand. They create a clear history of changes.

**Example**:
```bash
# Good: Small, focused commits
git commit -m "Add data validation function"
git commit -m "Add tests for data validation"
git commit -m "Integrate validation into pipeline"

# Avoid: Large, unfocused commits
git commit -m "Add validation, tests, and integration"
```

---

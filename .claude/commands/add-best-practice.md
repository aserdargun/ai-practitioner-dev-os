# Command: /add-best-practice

## Purpose
Capture a learning, insight, or best practice to the living documentation in `.claude/memory/best_practices.md`.

## Inputs
- **Practice**: The learning or insight to capture
- **Context** (optional): When/where this applies
- **Source** (optional): Where you learned this

## Outputs
- Entry added to `best_practices.md`
- Event logged to `progress_log.jsonl`
- Confirmation of captured practice

## When to Use
- When you learn something worth remembering
- After solving a tricky problem
- During or after retrospectives
- When a mentor/reviewer shares wisdom

## Agent Routing
**Coach** — helps formulate and capture the practice

## Example Usage

### Quick Capture
```
/add-best-practice
Always validate input data types before processing
```

### With Context
```
/add-best-practice
"Write one failing test before implementing a feature"
Context: TDD approach, especially for complex logic
```

### From Experience
```
/add-best-practice
I learned today that datetime parsing failures are often
due to timezone assumptions. Always specify timezone explicitly.
```

## Sample Output

```
💡 BEST PRACTICE CAPTURED

Practice:
"Always validate input data types before processing"

Category: Data Engineering
Tags: #validation #data-pipeline #defensive-coding

Added to: .claude/memory/best_practices.md

Entry Preview:
---
## Data Validation

### Always validate input data types before processing
*Captured: 2026-03-15 | Source: Month 3 project experience*

Before processing any data, check that types match expectations.
This prevents cryptic errors downstream and makes debugging easier.

```python
# Example
def process_data(df: pd.DataFrame) -> pd.DataFrame:
    assert isinstance(df, pd.DataFrame), "Expected DataFrame"
    assert "date" in df.columns, "Missing 'date' column"
    # ... processing
```
---

Related Practices in Memory:
- "Write tests for edge cases first"
- "Log inputs and outputs for debugging"

Logged to progress_log.jsonl ✓
```

## Practice Categories

Best practices are organized by category:
- **Coding**: Code style, patterns, anti-patterns
- **Testing**: Testing strategies and techniques
- **Data Engineering**: Data handling, pipelines
- **ML/AI**: Model development, evaluation
- **Tools**: Tool usage tips
- **Process**: Workflow and habits
- **Debugging**: Problem-solving approaches
- **Career**: Professional development

## Good Practices Have

- **Specific**: Not vague ("be careful" → "always check for None")
- **Actionable**: Something you can do
- **Memorable**: Easy to recall when needed
- **Contextual**: When/where it applies
- **Earned**: Learned through experience

## Related Commands
- `/retro` — Extract practices from reflection
- `/debug-learning` — Practices from solving blockers
- `/evaluate` — Practices affect Learning score

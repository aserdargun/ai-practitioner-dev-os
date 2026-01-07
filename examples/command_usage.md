# Command Usage Examples

Common command workflows for the AI Practitioner learning system.

---

## Daily Workflow

### Morning Check-in

```
/status
```

This shows your current position and any blockers.

### During the Day

When you complete a task:
```
# The system logs progress automatically when you commit
git add .
git commit -m "Complete data validation task"
```

When you learn something:
```
/add-best-practice "Always validate inputs at API boundaries"
```

When you're stuck:
```
/debug-learning "Can't figure out how to mock async functions"
```

---

## Weekly Workflow

### Monday: Start the Week

```
/start-week
```

Then generate your plan:
```
/plan-week
```

Review the generated tasks in `paths/Advanced/journal/week-XX.md`.

### Tuesday-Thursday: Build

Ship working code:
```
/ship-mvp
```

This creates the minimum viable version and commits it.

### Friday: Polish

Harden your code:
```
/harden
```

This adds tests, documentation, and error handling.

### Weekend: Reflect

Run retrospective:
```
/retro
```

Then evaluate:
```
/evaluate
```

Check if any adaptations are needed:
```
/adapt-path
```

---

## Monthly Workflow

### Month Start

1. Read the month's README:
   - `paths/Advanced/month-XX/README.md`

2. Plan your approach:
   ```
   /plan-week
   ```

### Month End

1. Complete your project
2. Publish for demo:
   ```
   /publish
   ```

3. Run full evaluation:
   ```
   /evaluate
   ```

4. Update tracker:
   ```
   /report
   ```

---

## Common Scenarios

### Getting Unstuck

```
/debug-learning "Description of your blocker"
```

The Coach and Researcher agents will help you.

### Capturing a Learning

```
/add-best-practice "What you learned"
```

This appends to `best_practices.md`.

### Checking Progress

Quick check:
```
/status
```

Full evaluation:
```
/evaluate
```

Generate report:
```
/report
```

### Preparing for Demo

```
/publish
```

This runs quality checks and prepares your code.

---

## Command Combinations

### Full Weekly Cycle

```
# Monday
/start-week
/plan-week

# Tuesday-Thursday
/ship-mvp
/harden

# Friday
/harden
/publish

# Weekend
/retro
/evaluate
/adapt-path
```

### Quick Status and Plan

```
/status
/plan-week
```

### Evaluation and Adaptation

```
/evaluate
/adapt-path
/report
```

---

## Tips

1. **Use /status often**: It's quick and keeps you oriented
2. **Don't skip /retro**: Reflection is key to learning
3. **Capture learnings**: Use /add-best-practice liberally
4. **Ask for help**: /debug-learning is there when you need it

---

## See Also

- [docs/commands.md](../docs/commands.md) — Full command reference
- [docs/how-to-use.md](../docs/how-to-use.md) — Complete guide

# Command: /retro

## Purpose

Conduct a weekly retrospective to reflect on progress, capture learnings, and improve your process.

## Inputs

Optional context:
- Specific wins or challenges to discuss
- Questions about your process

The command reads from:
- `.claude/memory/progress_log.jsonl`
- This week's journal entries
- Current week plan

## Outputs

- Structured retrospective summary
- Learnings captured
- Process improvements identified
- Entry for progress log

**Note**: Retrospective is drafted for your review before saving.

## When to Use

- End of each week (Friday recommended)
- After completing a major milestone
- When something significant happened (good or bad)

## Agent Routing

**Primary**: Coach Agent

The Coach guides you through reflection and helps extract meaningful insights.

## Example Usage

```
/retro
```

Or with specific focus:

```
/retro

This week I finally got the RAG pipeline working but spent too much time
on a bug in the retrieval step.
```

## Output Format

```markdown
## Weekly Retrospective — Week of [Date]

### Summary
Brief overview of the week.

### What Went Well
- [Win 1]
- [Win 2]
- [Win 3]

### What Could Be Improved
- [Challenge 1]
- [Challenge 2]

### Key Learnings
1. **[Learning title]**
   - What happened: [context]
   - What I learned: [insight]
   - How I'll apply this: [action]

2. **[Learning title]**
   - ...

### Process Improvements
- [ ] [Improvement to try next week]
- [ ] [Another improvement]

### Highlights for Best Practices
Consider adding to `.claude/memory/best_practices.md`:
- "[Insight worth preserving]"

### Mood/Energy Check
How did you feel this week? [response]

### Next Week Preview
Looking ahead: [brief preview]

---
**Save this retrospective?** (yes/no/modify)
```

## Retrospective Questions

The Coach may ask:
- What was your biggest win this week?
- What took longer than expected?
- What would you do differently?
- What surprised you?
- What are you most proud of?

## Saving Learnings

After approval:
1. Summary logged to `.claude/memory/progress_log.jsonl`
2. Best practices optionally added to `best_practices.md`
3. Journal entry created in `paths/intermediate/journal/`

## Related Commands

- `/add-best-practice` — Document specific learnings
- `/evaluate` — Get performance assessment
- `/plan-week` — Plan the next week

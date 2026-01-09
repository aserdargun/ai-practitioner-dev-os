# Command: /retro

## Purpose

Run a retrospective on the week or month. Reflect on what worked, what didn't, and capture lessons learned.

## Inputs

- **Period**: `week` or `month` (defaults to week)
- Context from progress log and memory

## Outputs

- Structured retrospective notes
- Best practice candidates
- Proposed updates to memory files
- **All memory updates require user approval**

## When to Use

- End of each week (recommended)
- End of each month (required)
- After completing a significant milestone
- When something went wrong (post-mortem)

## Agent Routing

**Primary**: Coach Agent

The Coach facilitates reflection and helps extract actionable insights.

## Example Usage

**User Input**:
```
/retro
```

**Expected Output**:
```
## Week 2 Retrospective (Month 03)

### Summary from Progress Log
- 5 tasks planned, 4 completed
- 3 commits, 7 tests added
- 1 blocker (chunking strategy)
- Resolved via research + experimentation

---

### Reflection Questions

**What went well?**
> (Your response here)

Examples from this week:
- Vector store setup was smooth
- Found good chunking approach after experimenting
- Tests helped catch edge cases early

**What didn't go well?**
> (Your response here)

Examples from this week:
- Initial chunking approach was wrong
- Spent too long on perfecting before testing
- Documentation fell behind

**What will you do differently?**
> (Your response here)

Suggestions:
- Test chunking approaches with real data earlier
- Write docs as you go, not at the end
- Time-box research to 2h before asking for help

---

### Best Practice Candidates

Based on this week, consider adding to `best_practices.md`:

1. **Chunking Strategy Testing**
   > "Test chunking with 3 representative documents before committing
   > to an approach. Measure retrieval quality, not just chunk count."

2. **Documentation Cadence**
   > "Update README after each major function is implemented,
   > not at the end of the week."

**Add these to best_practices.md?** (1/2/both/none)

---

### Proposed Progress Log Entry

```json
{
  "timestamp": "2026-01-09T17:00:00Z",
  "type": "retrospective",
  "period": "week",
  "month": 3,
  "week": 2,
  "summary": "Completed 4/5 tasks. Key learning: test approaches early.",
  "sentiment": "positive"
}
```

**Approve this log entry?** (yes/modify/no)
```

## Monthly Retro Template

For `/retro month`:

```
## Month 03 Retrospective

### Goals vs Actuals
| Goal | Status | Notes |
|------|--------|-------|
| RAG pipeline | ✅ | Completed |
| 10 tests | ✅ | 12 tests |
| Demo | ✅ | Recorded |
| Blog post | ⚠️ | Draft only |

### Key Learnings
1. ...
2. ...
3. ...

### Carry Forward
- Complete blog post in Week 1 of Month 04
- Apply chunking pattern to next project

### Overall Satisfaction: 8/10
```

## Related Commands

- `/evaluate` - Formal scoring (different from reflection)
- `/add-best-practice` - Add practices directly
- `/plan-week` - Apply learnings to next plan

# Command: /retro

## Purpose
Run a structured retrospective to reflect on what worked, what didn't, and what to improve for future weeks or months.

## Inputs
- **Period**: Week or month to review
- **Focus** (optional): Specific aspect to reflect on

## Outputs
- **What Went Well**: Successes and wins
- **What Was Challenging**: Difficulties and obstacles
- **What I Learned**: Key insights and skills gained
- **Action Items**: Specific improvements for next period
- **Best Practices**: Learnings to capture in memory

## When to Use
- End of each week
- End of each month
- After completing a project
- When feeling stuck or frustrated

## Agent Routing
**Coach** — facilitates reflection
**Reviewer** — provides objective perspective

## Example Usage

### Weekly Retro
```
/retro for this week
```

### Monthly Retro
```
/retro for Month 3
Focus on the project delivery
```

### Project Retro
```
/retro for the forecasting project
What would I do differently?
```

## Sample Output

```
🔄 RETROSPECTIVE — Month 3, Week 2

⭐ What Went Well
- Completed data pipeline on schedule
- Tests caught a critical bug early
- Documentation is clearer than last month
- Asked for help sooner when stuck

😓 What Was Challenging
- Datetime parsing took longer than expected
- Lost 2 hours to environment issues
- Underestimated testing time
- Energy dipped mid-week

📚 What I Learned
- Always validate date formats upfront
- Docker environments save setup time
- Writing tests first clarifies requirements
- Taking breaks improves focus

📋 Action Items for Next Week
1. Start testing earlier in the week
2. Document datetime formats in README
3. Use Docker from project start
4. Schedule breaks proactively

💡 Best Practices to Capture
→ "Always check input date formats before processing"
→ "Write one test before implementing a feature"

Would you like me to add these to best_practices.md? (y/n)

Mood Check:
How are you feeling about your progress?
1 = Struggling | 5 = Great

Suggested Focus for Next Week:
Based on this retro, consider focusing on:
- Building testing habits
- Environment consistency
```

## Retro Framework

### 4 L's Method
- **Liked**: What did you enjoy?
- **Learned**: What new knowledge/skills?
- **Lacked**: What was missing?
- **Longed for**: What do you wish you had?

### Start-Stop-Continue
- **Start**: What should you begin doing?
- **Stop**: What should you stop doing?
- **Continue**: What's working well?

### Simple Reflection
- What worked?
- What didn't?
- What will you do differently?

## Tips for Good Retros

1. **Be honest** — This is for you, not for show
2. **Be specific** — "Testing helped" → "Unit tests caught the null pointer bug"
3. **Be actionable** — "Work harder" → "Timebox tasks to 2 hours max"
4. **Be kind** — Acknowledge growth, not just gaps

## Related Commands
- `/add-best-practice` — Capture learnings
- `/status` — Check progress before retro
- `/plan-week` — Apply retro insights

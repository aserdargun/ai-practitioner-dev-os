# Journal

Your learning journal for tracking weekly and monthly reflections.

## Purpose

The journal helps you:
- Track your progress over time
- Reflect on what you're learning
- Identify patterns (what works, what doesn't)
- Build a record of your journey

## Structure

```
journal/
├── README.md           # This file
├── weekly-template.md  # Template for weekly entries
├── monthly-template.md # Template for monthly entries
└── week-YYYY-MM-DD.md  # Your weekly entries (created by hooks)
```

## How to Use

### Weekly Entries

Created automatically by `pre_week_start.sh` hook or manually:

1. Copy `weekly-template.md`
2. Name it `week-YYYY-MM-DD.md` (e.g., `week-2026-01-07.md`)
3. Fill in as you go through the week
4. Complete the retrospective on Friday

### Monthly Entries

Created at the end of each month:

1. Copy `monthly-template.md`
2. Name it `month-XX.md` (e.g., `month-01.md`)
3. Summarize the month's learning
4. Plan for next month

## Templates

- [Weekly Template](weekly-template.md)
- [Monthly Template](monthly-template.md)

## Tips

### Write Regularly

- Jot notes daily
- Don't wait until Friday
- Even brief notes help

### Be Honest

- Include struggles
- Note what didn't work
- This data helps adaptation

### Be Specific

- "Spent 2 hours on pandas groupby"
- Not just "worked on pandas"

### Review Periodically

- Look back monthly
- Spot patterns
- Celebrate progress

## Linking to Memory

Your journal complements the memory system:

| Journal | Memory |
|---------|--------|
| Detailed notes | Structured events |
| Free-form reflection | JSON entries |
| Personal insights | System data |

The `post_week_review.sh` hook captures key reflection data to `progress_log.jsonl`.

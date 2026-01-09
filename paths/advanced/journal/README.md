# Journal

Your learning journal for reflections and retrospectives.

## Overview

Journaling reinforces learning and provides data for evaluation. Write regularly to capture insights while they're fresh.

## Templates

- [weekly-template.md](weekly-template.md) - Weekly reflection template
- [monthly-template.md](monthly-template.md) - Monthly retrospective template

## How to Use

### Weekly Journaling

At the end of each week:
1. Copy `weekly-template.md` to `week-XX.md`
2. Fill in reflections
3. Or run `bash .claude/hooks/post_week_review.sh`

### Monthly Retrospectives

At the end of each month:
1. Copy `monthly-template.md` to `month-XX-retro.md`
2. Run `/retro month` for guided reflection
3. Review before starting next month

## Automated Hooks

The hooks can create journal entries for you:

```bash
# Start of week - creates week stub
bash .claude/hooks/pre_week_start.sh

# End of week - prompts for reflection
bash .claude/hooks/post_week_review.sh
```

## Journal Location

All journal files live here:
```
paths/advanced/journal/
├── README.md
├── weekly-template.md
├── monthly-template.md
├── week-01.md
├── week-02.md
└── month-01-retro.md
```

## Why Journal?

- **Reflection score**: Part of your evaluation (15%)
- **Pattern recognition**: See what works over time
- **Best practices**: Discover patterns to capture
- **Debugging**: Identify recurring blockers
- **Memory**: Remember your journey

## Tips

1. **Write immediately** - Don't wait until Friday evening
2. **Be honest** - Record struggles, not just wins
3. **Keep it brief** - 5-10 minutes is enough
4. **Link to progress log** - Cross-reference with `.claude/memory/progress_log.jsonl`

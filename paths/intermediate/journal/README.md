# Journal

Your learning journal for capturing reflections, insights, and progress.

## Purpose

The journal helps you:
- Track your daily and weekly progress
- Reflect on what you're learning
- Identify patterns in your work
- Build a record of your journey

## Templates

| Template | Use |
|----------|-----|
| [weekly-template.md](weekly-template.md) | Weekly planning and reflection |
| [monthly-template.md](monthly-template.md) | Monthly review and goals |

## How to Use

### Weekly Journal

1. Copy `weekly-template.md` to a new file:
   ```bash
   cp weekly-template.md week-2026-01.md
   ```

2. Fill in your goals at the start of the week

3. Update daily log each day

4. Complete reflection at end of week

### Monthly Journal

1. Copy `monthly-template.md` at the start of each month:
   ```bash
   cp monthly-template.md month-01-review.md
   ```

2. Set monthly goals aligned with curriculum

3. Track progress throughout month

4. Complete review at month end

## Integration with System

Your journal entries feed into:
- Progress evaluation (via progress_log.jsonl)
- Best practices capture
- Retrospective insights

When you run `/retro`, the Coach agent will reference your journal.

## File Naming Convention

- Weekly: `week-YYYY-WW.md` (e.g., `week-2026-03.md`)
- Monthly: `month-MM-review.md` (e.g., `month-03-review.md`)

## Tips

- **Be honest**: The journal is for you, not for grades
- **Be specific**: "Learned X" is better than "Made progress"
- **Be consistent**: Even brief entries help track patterns
- **Connect to goals**: Link daily work to monthly objectives

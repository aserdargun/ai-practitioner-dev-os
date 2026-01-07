# How to Use This System

This guide explains how to use the AI Practitioner Learning OS day-to-day.

## Getting Started

### 1. Open Your Dashboard

Your main entry point is your learning dashboard:

```
paths/Beginner/README.md
```

This shows:
- Current month and week
- Weekly checklists
- Commands cheat-sheet
- Quick links to resources

### 2. Run Your First Commands

In Claude Code, try these commands:

```
/status        # See where you are
/plan-week     # Plan this week
/evaluate      # Check your progress
/report        # Update your tracker
```

## The System Loop

The learning OS follows a continuous loop:

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   EXECUTE   │ ──► │   EVALUATE  │ ──► │    ADAPT    │
│             │     │             │     │             │
│ Do the work │     │ Score your  │     │ Adjust your │
│ Log progress│     │ progress    │     │ path        │
└─────────────┘     └─────────────┘     └─────────────┘
       ▲                                       │
       └───────────────────────────────────────┘
```

## Running the System Locally

### Using Scripts

From the repository root:

```bash
# Start a new week
bash .claude/hooks/pre_week_start.sh

# End-of-week review
bash .claude/hooks/post_week_review.sh

# Pre-publish checks
bash .claude/hooks/pre_publish_check.sh

# Run evaluation
python .claude/path-engine/evaluate.py

# Check for adaptations
python .claude/path-engine/adapt.py

# Generate report
python .claude/path-engine/report.py
```

### Using Claude Commands

In Claude Code:

```
/start-week    # Runs pre_week_start.sh
/retro         # Runs post_week_review.sh
/evaluate      # Runs evaluate.py
/adapt-path    # Runs adapt.py
/report        # Runs report.py
```

## Weekly Cadence

### Week 1: Foundation

| Day | Activity |
|-----|----------|
| Mon | `/start-week`, `/plan-week`, set goals |
| Tue | Learn concepts, take notes |
| Wed | Start implementing |
| Thu | Continue implementing |
| Fri | `/evaluate`, `/retro` |

### Week 2: Build

| Day | Activity |
|-----|----------|
| Mon | `/plan-week`, review week 1 |
| Tue | Build features |
| Wed | Build features |
| Thu | Add tests |
| Fri | `/evaluate`, `/retro` |

### Week 3: Polish

| Day | Activity |
|-----|----------|
| Mon | `/plan-week`, review progress |
| Tue | `/harden` - add tests, error handling |
| Wed | Documentation |
| Thu | Edge cases, cleanup |
| Fri | `/evaluate`, `/retro` |

### Week 4: Ship

| Day | Activity |
|-----|----------|
| Mon | `/plan-week`, final push |
| Tue | Finish deliverables |
| Wed | `/publish` prep |
| Thu | Demo, write-up |
| Fri | `/evaluate`, monthly review |

## Logging Progress & Reflections

### Automatic Logging

The hooks automatically log to `.claude/memory/progress_log.jsonl`:
- Week starts/ends
- Reflections from retros

### Manual Logging

You can also log manually by appending to the JSONL file:

```json
{"timestamp": "2026-01-07T14:00:00Z", "event": "task_completed", "task": "Built EDA notebook", "duration_hours": 2}
```

Or use Claude:
```
I just completed the EDA notebook. It took about 2 hours.
Please log this to my progress.
```

## Requesting Path Changes

### Automatic Adaptation

Run `/evaluate` followed by `/adapt-path` to get recommendations:

```
/evaluate
/adapt-path
```

The system will propose changes if needed:
- Remediation weeks for struggling areas
- Level upgrades if excelling
- Project swaps if better aligned with interests

### Manual Requests

You can also request changes directly:

```
I'd like to swap month 5's project for something more aligned with NLP.
Can we do a project swap?
```

The Coach Agent will help evaluate if the swap makes sense.

## Capturing Best Practices

### Using the Command

```
/add-best-practice

I learned that writing tests first helps me think through edge cases better.
```

### Manually Adding

Edit `.claude/memory/best_practices.md`:

```markdown
### Test-First Development
**Context**: Starting new features
**Practice**: Write a failing test before implementing
**Why**: Forces you to think about interface and edge cases
**Added**: 2026-01-15
```

## Troubleshooting

### "I don't know where I am"

Run `/status` to see:
- Current month and week
- Completion percentage
- Active tasks
- Blockers

### "I'm stuck"

Run `/debug-learning` with details:

```
/debug-learning

I've been stuck on pandas groupby for 2 hours. I've read the docs
and tried examples but my code still doesn't work.
```

### "My score is low"

1. Run `/evaluate` to see category breakdown
2. Check which category is lowest
3. Focus on improving that area
4. Run `/adapt-path` to see if remediation helps

### "The hooks don't work"

On Windows without WSL:
1. See [docs/hooks.md](hooks.md) for manual fallback steps
2. Run the equivalent Python/commands manually

## Quick Reference

| What You Want | What to Do |
|---------------|------------|
| Check status | `/status` |
| Plan the week | `/plan-week` |
| Start building | `/ship-mvp` |
| Add tests | `/harden` |
| Reflect | `/retro` |
| Check progress | `/evaluate` |
| Update tracker | `/report` |
| Get unstuck | `/debug-learning` |
| Capture learning | `/add-best-practice` |

## Next Steps

1. Go to your [Dashboard](../paths/Beginner/README.md)
2. Run `/status` to see where you are
3. Run `/plan-week` to plan your first week
4. Start learning!

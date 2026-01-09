# How to Use the Learning OS

A practical guide to running the AI Practitioner Booster system.

## Quick Start (5 Minutes)

### 1. Check Your Status
```
/status
```
This shows your current progress, active month, and next actions.

### 2. Plan Your Week
```
/plan-week
I have 10 hours available this week
```
Claude creates a day-by-day task breakdown.

### 3. Start Working
```
/start-week
```
Initializes your week structure and updates the tracker.

### 4. End of Week
```
/retro
```
Reflect on what worked, what didn't, and capture learnings.

---

## System Loop

The learning OS follows a continuous loop:

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   Evaluate → Recommend → YOU APPROVE → Execute          │
│       ↑                                      │          │
│       └──────────────────────────────────────┘          │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**You are always in control.** Claude provides recommendations; you decide what to act on.

---

## Weekly Cadence

### Week 1: Foundation
- Set up project structure
- Understand requirements
- Create initial plan
- Start building basics

### Week 2: Building
- Implement core features
- Write initial tests
- Document as you go
- Check progress mid-week

### Week 3: Refinement
- Complete MVP functionality
- Add error handling
- Improve test coverage
- Review and refactor

### Week 4: Ship & Reflect
- Finalize deliverables
- Run `/harden` for quality
- Run `/publish` for demo prep
- Run `/retro` for reflection
- Run `/evaluate` for scores

---

## Daily Workflow

### Morning Check-in (5 min)
```
/status
```
See where you are and what's next.

### Work Session
1. Pick a task from your plan
2. Work on it (timebox if needed)
3. Ask Claude for help when stuck
4. Mark task complete in your journal

### End of Session (5 min)
- Log what you did in your journal
- Note any blockers
- Capture any learnings

---

## Logging Progress

### Manual Journal Entry
Edit `paths/beginner/journal/month-XX-week-Y.md`:
```markdown
### Day 3 (Wednesday)
**Completed**:
- Implemented data validation function
- Wrote 3 unit tests

**Notes**:
Learned that pandas .apply() is slow for large datasets.
```

### Via Command
```
/add-best-practice
Always use vectorized operations in pandas instead of .apply()
```

---

## Requesting Path Changes

### When to Consider
- Consistently struggling (scores below 50)
- Significantly ahead (scores above 85)
- Life circumstances changed
- Interest shifted

### How to Request
```
/adapt-path
```
Review proposals and approve/reject each one.

### What Can Change
- Insert remediation weeks
- Reduce project scope
- Reorder upcoming months
- Change learner level (at month boundaries)

---

## Using Memory

### Viewing Your Profile
```
Read .claude/memory/learner_profile.json
```

### Viewing Progress History
```
Read .claude/memory/progress_log.jsonl
```

### Adding Best Practices
```
/add-best-practice
[Your learning here]
```

### Editing Memory
You can directly edit any file in `.claude/memory/`. These are your files.

---

## Running the Path Engine

### Get Evaluation Scores
```bash
cd .claude/path-engine
python evaluate.py
```

### See Adaptation Proposals
```bash
python adapt.py
```

### Update Tracker
```bash
python report.py
```

---

## Command Reference

| Command | When to Use |
|---------|-------------|
| `/status` | Start of session, feeling lost |
| `/plan-week` | Start of week |
| `/start-week` | After planning |
| `/ship-mvp` | Ready to finalize |
| `/harden` | After MVP, before publish |
| `/publish` | Ready to share |
| `/retro` | End of week |
| `/evaluate` | End of week/month |
| `/adapt-path` | Need changes |
| `/add-best-practice` | Learned something |
| `/debug-learning` | Stuck |

See [commands.md](commands.md) for full reference.

---

## Tips for Success

### 1. Start Small
Don't try to do everything. Focus on one task at a time.

### 2. Log As You Go
Quick notes while working are better than trying to remember later.

### 3. Use Commands
The slash commands are there to help. Use them liberally.

### 4. Reflect Weekly
The `/retro` command is your most valuable learning tool.

### 5. Ask for Help
When stuck, use `/debug-learning` or just ask Claude directly.

### 6. Trust the Process
Progress isn't always linear. Stick with the system through difficult weeks.

---

## Troubleshooting

### "I don't know where to start"
```
/status
```
Then
```
/plan-week
```

### "I'm stuck on something"
```
/debug-learning
[Describe what you're stuck on]
```

### "I'm falling behind"
```
/adapt-path
```
Consider scope reduction or remediation week.

### "Commands aren't working"
Make sure you're in Claude Code and the `.claude/commands/` folder exists.

---

## Next Steps

1. Run `/status` to see where you are
2. Check your month's README in `paths/beginner/month-XX/`
3. Start with the first task!

Remember: Progress beats perfection. Just start.

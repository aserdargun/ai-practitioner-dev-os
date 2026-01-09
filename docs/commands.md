# Commands Reference

Complete guide to slash commands in the learning OS.

## Quick Reference

| Command | Purpose | Agent |
|---------|---------|-------|
| `/status` | Show progress snapshot | Evaluator |
| `/plan-week` | Create weekly plan | Planner |
| `/start-week` | Initialize new week | Planner |
| `/ship-mvp` | Finalize MVP | Builder |
| `/harden` | Add tests, docs | Builder + Reviewer |
| `/publish` | Prepare for portfolio | Builder |
| `/retro` | Run retrospective | Coach + Reviewer |
| `/evaluate` | Get evaluation scores | Evaluator |
| `/adapt-path` | See adaptation proposals | Evaluator |
| `/add-best-practice` | Capture a learning | Coach |
| `/debug-learning` | Diagnose blockers | Coach |

See the full catalog: [.claude/commands/catalog.md](../.claude/commands/catalog.md)

---

## Progress & Planning

### /status

**What it does**: Displays your current progress snapshot.

**When to use**:
- Start of each work session
- When feeling lost
- Before planning a new week

**Example**:
```
/status
```

**What you get**:
- Tasks completed vs. planned
- Current focus and blockers
- Recommended next actions

---

### /plan-week

**What it does**: Creates a detailed weekly plan with day-by-day tasks.

**When to use**:
- Start of each week
- After completing a week
- When circumstances change

**Example**:
```
/plan-week
I have 12 hours this week, focus on the API project
```

**What you get**:
- Day-by-day task breakdown
- Time estimates
- Definition of done

---

### /start-week

**What it does**: Initializes structure for a new learning week.

**When to use**:
- After `/plan-week` is approved
- Beginning of each week

**Example**:
```
/start-week
```

**What you get**:
- Week journal file created
- Tracker updated
- Checklist ready

---

## Building & Shipping

### /ship-mvp

**What it does**: Finalizes your MVP to demo-ready state.

**When to use**:
- Core functionality is working
- Ready to polish for demo
- End of project phase

**Example**:
```
/ship-mvp
The MVP should process CSV files and output clean data
```

**What you get**:
- Working MVP verified
- Demo script created
- Known limitations documented

---

### /harden

**What it does**: Improves code quality with tests, docs, and error handling.

**When to use**:
- After MVP is working
- Before publishing
- When quality needs improvement

**Example**:
```
/harden the data_processor module
Focus on tests, target 80% coverage
```

**What you get**:
- Unit tests added
- Documentation improved
- Error handling enhanced

---

### /publish

**What it does**: Prepares your work for public sharing.

**When to use**:
- Project is complete and hardened
- Building your portfolio
- Sharing with community

**Example**:
```
/publish Month 3 project
For portfolio, targeting recruiters
```

**What you get**:
- Demo guide
- Write-up draft
- Publish checklist

---

## Reflection & Learning

### /retro

**What it does**: Runs a structured retrospective.

**When to use**:
- End of each week
- End of each month
- After completing a project

**Example**:
```
/retro for this week
```

**What you get**:
- What went well
- What was challenging
- Learnings captured
- Action items

---

### /add-best-practice

**What it does**: Captures a learning to best practices.

**When to use**:
- When you learn something worth remembering
- After solving a tricky problem
- During retrospectives

**Example**:
```
/add-best-practice
Always validate date formats before processing time series data
```

**What you get**:
- Entry in best_practices.md
- Event logged

---

### /debug-learning

**What it does**: Diagnoses why you're stuck and suggests solutions.

**When to use**:
- Stuck for more than 30 minutes
- Don't understand a concept
- Feeling frustrated or overwhelmed

**Example**:
```
/debug-learning
I can't understand how async/await works in Python
I've read docs but it's not clicking
```

**What you get**:
- Root cause diagnosis
- Multiple strategies to try
- Resource recommendations
- Action plan

---

## Evaluation & Adaptation

### /evaluate

**What it does**: Gets detailed evaluation scores against the rubric.

**When to use**:
- End of week or month
- Before adaptation decisions
- When uncertain about progress

**Example**:
```
/evaluate
```

**What you get**:
- Scores by dimension (Completion, Quality, Velocity, Learning)
- Gap analysis
- Trend indicators
- Recommendations

---

### /adapt-path

**What it does**: Shows proposed path adaptations.

**When to use**:
- After evaluation shows gaps
- When circumstances change
- At month boundaries

**Example**:
```
/adapt-path
```

**What you get**:
- Specific proposals
- Rationale for each
- Impact assessment
- Approval prompts

---

## Command Chaining

For common workflows, chain commands:

### Weekly Cycle
```
/start-week
[do the work during the week]
/retro
/evaluate
```

### Ship & Publish
```
/ship-mvp
/harden
/publish
```

### Course Correct
```
/status
/debug-learning
/adapt-path
/plan-week
```

---

## How Commands Work

Commands are defined in `.claude/commands/*.md`. Each file follows a standard format:

```markdown
# Command: /command-name

## Purpose
What this command does

## Inputs
What you need to provide

## Outputs
What you get back

## Agent Routing
Which agent handles it

## Example Usage
Copy-paste example
```

---

## Adding Custom Commands

1. Create a new `.md` file in `.claude/commands/`
2. Follow the format above
3. Add to the catalog

Example: Create `.claude/commands/daily-standup.md` for a custom standup command.

---

## Tips

1. **Use context**: Add relevant details to commands
   ```
   /plan-week focus on testing, I have limited time
   ```

2. **Chain when needed**: Multiple commands in sequence work well

3. **Check status first**: When in doubt, `/status` gives you bearings

4. **Log learnings**: Use `/add-best-practice` liberally

5. **Reflect regularly**: `/retro` is your most valuable tool

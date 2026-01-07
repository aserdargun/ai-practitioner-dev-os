# Commands Guide

This is a friendly guide to using commands in the AI Practitioner Learning OS. For the complete technical reference, see [.claude/commands/catalog.md](../.claude/commands/catalog.md).

## Quick Reference

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/status` | Check progress | Start of day |
| `/plan-week` | Plan the week | Monday |
| `/start-week` | Initialize week | Monday morning |
| `/ship-mvp` | Build something | Starting features |
| `/harden` | Add quality | After MVP works |
| `/publish` | Share your work | End of month |
| `/retro` | Reflect | Friday |
| `/evaluate` | Get scores | Weekly |
| `/adapt-path` | Adjust path | After evaluation |
| `/add-best-practice` | Capture learning | Anytime |
| `/debug-learning` | Get unstuck | When stuck |
| `/report` | Update tracker | Weekly |

## Planning Commands

### /status

**What it does**: Shows your current state - where you are, what you're working on, any blockers.

**Example**:
```
/status
```

**Output includes**:
- Current month and week
- Completion percentage
- Active tasks
- Blockers (if any)
- Suggested next actions

### /plan-week

**What it does**: Creates a detailed plan for the week based on your current month's goals.

**Example**:
```
/plan-week

I have 10 hours this week. Focus on the EDA module.
```

**Output includes**:
- Day-by-day breakdown
- Learning objectives
- Deliverables
- Time estimates

### /start-week

**What it does**: Initializes a new week - creates journal entry, updates tracker, runs pre-flight checks.

**Example**:
```
/start-week
```

## Building Commands

### /ship-mvp

**What it does**: Guides you through building a minimal viable product. Focuses on getting something working first.

**Example**:
```
/ship-mvp

Build a data cleaning pipeline that reads CSV, handles missing values, and outputs clean data.
```

**Output includes**:
- Scope definition
- Step-by-step implementation
- Working code
- Basic tests

### /harden

**What it does**: Improves existing code with tests, error handling, and documentation.

**Example**:
```
/harden

Add error handling for invalid inputs and write tests for the data pipeline.
```

**Output includes**:
- Test suggestions
- Error handling improvements
- Documentation updates
- Code quality report

### /publish

**What it does**: Prepares your work for demonstration and sharing.

**Example**:
```
/publish

Prepare a demo and write-up for my sentiment analysis project.
Target audience: potential employers.
```

**Output includes**:
- Demo script
- README updates
- Write-up outline
- Portfolio entry

## Coaching Commands

### /retro

**What it does**: Facilitates a retrospective on your week - what went well, what to improve.

**Example**:
```
/retro

Reflect on this week. I completed the EDA but struggled with visualization.
```

**Output includes**:
- What went well
- What could improve
- Action items
- Lessons learned

### /add-best-practice

**What it does**: Captures a new best practice you've discovered.

**Example**:
```
/add-best-practice

I found that writing a test before implementing helps me think through edge cases.
This works especially well for data validation functions.
```

### /debug-learning

**What it does**: Helps diagnose why you're stuck and suggests ways forward.

**Example**:
```
/debug-learning

I've been stuck on pandas groupby for 2 hours. I've read the docs and tried
examples but my aggregations aren't working as expected.
```

**Output includes**:
- Root cause analysis
- Specific recommendations
- Resources to review
- Alternative approaches

## Evaluation Commands

### /evaluate

**What it does**: Runs the evaluation engine to score your progress across categories.

**Example**:
```
/evaluate
```

**Output includes**:
- Overall score (0-100)
- Category scores (completion, quality, understanding, consistency)
- Strengths identified
- Gaps to address
- Recommendations

### /adapt-path

**What it does**: Analyzes your evaluation and proposes path modifications if needed.

**Example**:
```
/adapt-path

The evaluation shows I'm struggling with time series concepts.
What changes would help?
```

**Output includes**:
- Adaptation proposals (if any)
- Rationale for each
- Expected impact
- Request for your approval

### /report

**What it does**: Generates or updates your progress tracker.

**Example**:
```
/report
```

**Output**:
- Updates `paths/Beginner/tracker.md`
- Shows summary of progress
- Key metrics

## Command Patterns

### Daily Routine

```
/status                  # Start of day - see where you are
# ... do your work ...
# ... log progress ...   # End of day
```

### Weekly Routine

```
# Monday
/start-week
/plan-week

# Tuesday-Thursday
/status
# ... build ...

# Friday
/evaluate
/retro
/report
```

### Monthly Routine

```
# Week 4
/evaluate
/adapt-path              # Check if changes needed
/publish                 # If deliverable ready
/report
```

### When Stuck

```
/debug-learning          # First, get diagnosis
# ... try suggestions ...
/status                  # Check if unstuck
```

## Tips for Better Results

### Be Specific

```
# Less helpful
/plan-week

# More helpful
/plan-week
I have 8 hours this week, mostly on Tuesday and Thursday.
Focus on completing the baseline model for the churn prediction project.
```

### Provide Context

```
# Less helpful
/debug-learning
I'm stuck.

# More helpful
/debug-learning
I'm trying to build a Random Forest model but getting ValueError about
feature shapes. X_train has shape (1000, 10) but I'm passing 11 features.
I've checked my data loading code twice.
```

### Follow Up

After getting recommendations, take action and report back:

```
/evaluate
# ... see recommendations ...
# ... work on recommendations ...
/evaluate               # Check improvement
```

## Source of Truth

The canonical command reference is at:
[.claude/commands/catalog.md](../.claude/commands/catalog.md)

This includes:
- Full input/output specifications
- All options and parameters
- Agent routing information
- Examples for every command

# How to Use This Learning System

Complete guide to using the AI Practitioner Booster 2026 learning system.

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Daily Workflow](#daily-workflow)
3. [Weekly Workflow](#weekly-workflow)
4. [Monthly Workflow](#monthly-workflow)
5. [Using Commands](#using-commands)
6. [Working with Memory](#working-with-memory)
7. [Understanding Evaluation](#understanding-evaluation)
8. [Handling Adaptations](#handling-adaptations)
9. [Best Practices](#best-practices)

---

## Getting Started

### Prerequisites

- Python 3.11+ installed
- Git installed and configured
- VS Code (recommended) with Python extension
- Claude Code connected to your fork

### First-Time Setup

1. **Navigate to your dashboard**:
   ```
   paths/Advanced/README.md
   ```

2. **Check your profile**:
   ```
   .claude/memory/learner_profile.json
   ```

3. **Run your first status check**:
   ```
   /status
   ```

4. **Generate your first weekly plan**:
   ```
   /plan-week
   ```

---

## Daily Workflow

### Morning Routine (5 minutes)

1. **Open your dashboard**: `paths/Advanced/README.md`

2. **Check status**:
   ```
   /status
   ```
   This shows:
   - Current week and month
   - Tasks in progress
   - Blockers if any

3. **Review today's tasks** from your weekly plan in `paths/Advanced/journal/`

### During the Day

1. **Work on tasks** from your weekly plan

2. **When you complete something**:
   - Commit your work with a clear message
   - The system logs progress automatically

3. **When you learn something new**:
   ```
   /add-best-practice "What you learned"
   ```

4. **When you're stuck**:
   ```
   /debug-learning "Description of the blocker"
   ```

### End of Day (5 minutes)

1. **Commit any remaining work**:
   ```bash
   git add .
   git commit -m "Daily progress: [summary]"
   ```

2. **Quick reflection**: Note any insights or blockers for tomorrow

---

## Weekly Workflow

### Monday: Start the Week

```
/start-week
```

This:
- Runs pre-week checks
- Validates your environment
- Shows the week's focus

Then:
```
/plan-week
```

Review the generated plan in your journal.

### Tuesday–Thursday: Build

Focus on your weekly tasks. Use these commands as needed:

| Task | Command |
|------|---------|
| Ship working code | `/ship-mvp` |
| Add tests/docs | `/harden` |
| Get unstuck | `/debug-learning` |

### Friday: Polish

```
/harden
```

This reviews your code and:
- Adds missing tests
- Improves documentation
- Fixes linting issues

### Weekend: Reflect

```
/retro
```

The retrospective covers:
- What went well
- What could improve
- Key learnings
- Action items

Then evaluate:
```
/evaluate
```

Review your scores and recommendations.

---

## Monthly Workflow

Each month focuses on a specific topic. Your path is:

| Month | Topic | Tier |
|-------|-------|------|
| 01 | Foundations & Environment | Tier 1 |
| 02 | Data Engineering | Tier 1 |
| 03 | ML Fundamentals | Tier 1 |
| 04 | Deep Learning | Tier 1 |
| 05 | NLP & LLMs | Tier 2 |
| 06 | Computer Vision | Tier 2 |
| 07 | MLOps & Deployment | Tier 2 |
| 08 | System Design | Tier 2 |
| 09 | Evaluation & Testing | Tier 3 |
| 10 | Advanced Topics | Tier 3 |
| 11 | Capstone Project | Tier 3 |
| 12 | Portfolio & Career | Tier 3 |

### Month Start

1. Read the month's README: `paths/Advanced/month-XX/README.md`
2. Understand objectives and deliverables
3. Plan your weekly breakdown

### Month End

1. Complete the month's project
2. Run full evaluation:
   ```
   /evaluate
   ```

3. Check for path adaptations:
   ```
   /adapt-path
   ```

4. Prepare for demo:
   ```
   /publish
   ```

---

## Using Commands

### Command Reference

| Command | When to Use | What It Does |
|---------|------------|--------------|
| `/status` | Daily | Shows current progress |
| `/plan-week` | Monday | Generates weekly tasks |
| `/start-week` | Monday | Initializes the week |
| `/ship-mvp` | When feature is ready | Ships working code |
| `/harden` | Friday or before publish | Adds tests and docs |
| `/publish` | Month end | Prepares for demo |
| `/retro` | Weekend | Weekly reflection |
| `/evaluate` | Weekend or month end | Scores your progress |
| `/adapt-path` | After evaluation | Suggests path changes |
| `/add-best-practice` | After learning | Captures insights |
| `/debug-learning` | When stuck | Gets help |
| `/report` | Any time | Updates tracker |

### Command Tips

- Commands are case-insensitive
- You can ask Claude to explain what a command will do before running it
- Commands that modify files will show you what changed

---

## Working with Memory

### Memory Files

| File | Purpose | How to Use |
|------|---------|------------|
| `learner_profile.json` | Your configuration | Read-only (update carefully) |
| `progress_log.jsonl` | Activity history | Append-only |
| `decisions.jsonl` | Path change history | Append-only |
| `best_practices.md` | Your learnings | Append new entries |

### Updating Memory

**Progress is logged automatically** when you:
- Complete tasks
- Run evaluations
- Make commits

**Manually add best practices**:
```
/add-best-practice "Always validate inputs at API boundaries"
```

**Never delete** entries from `.jsonl` files—they're append-only logs.

---

## Understanding Evaluation

### Evaluation Dimensions

| Dimension | Weight | What It Measures |
|-----------|--------|------------------|
| Completion | 30% | Tasks completed |
| Quality | 25% | Test pass rate |
| Consistency | 20% | Regular commits and logging |
| Growth | 15% | Best practices captured |
| Engagement | 10% | Questions asked, blockers resolved |

### Score Interpretation

| Score | Status | Action |
|-------|--------|--------|
| 90%+ | Excellent | Consider acceleration |
| 70-89% | On Track | Continue current pace |
| 50-69% | Needs Attention | Focus on weak areas |
| <50% | At Risk | Consider remediation |

### Running Evaluation

```
/evaluate
```

Or manually:
```bash
python .claude/path-engine/evaluate.py
```

---

## Handling Adaptations

### Allowed Adaptations

The system can only propose these changes:

1. **Level Change**: Upgrade/downgrade your level
2. **Month Reorder**: Swap upcoming months
3. **Remediation Week**: Insert catch-up time
4. **Project Swap**: Change current project

### Reviewing Adaptations

```
/adapt-path
```

This shows proposed changes. Some are auto-approved (minor adjustments), others require your approval.

### Accepting or Rejecting

- **Auto-approved**: Applied automatically
- **Requires approval**: Review and decide
- You can always override or ignore suggestions

---

## Best Practices

### For Learning

1. **Ship early, iterate often**: Working code beats perfect plans
2. **Log everything**: Progress entries help evaluation
3. **Ask for help**: Use `/debug-learning` when stuck
4. **Capture learnings**: Add best practices as you discover them

### For Code

1. **Test as you build**: Don't save tests for the end
2. **Commit frequently**: Small commits are easier to review
3. **Document intent**: Explain why, not just what
4. **Use templates**: Start from `templates/` when possible

### For the System

1. **Trust the loop**: Evaluate → Adapt → Execute works
2. **Be honest**: Accurate progress logs help adaptation
3. **Review recommendations**: The system learns from your patterns
4. **Customize carefully**: The profile can be adjusted, but do so thoughtfully

---

## Troubleshooting

### Common Issues

**"Command not found"**
- Make sure you're using Claude Code, not a regular terminal

**"Evaluation shows 0%"**
- Run a few tasks and log progress first
- Check that memory files exist

**"Can't run hooks"**
- On Windows, use WSL or Git Bash
- Check that scripts have execute permission: `chmod +x .claude/hooks/*.sh`

**"Tests failing"**
- Run `pytest` in the specific template directory
- Check that dependencies are installed

### Getting Help

1. Use `/debug-learning` with a description of your issue
2. Check the documentation in `docs/`
3. Review examples in `examples/`

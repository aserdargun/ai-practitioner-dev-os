# Agents Guide

This guide explains the agents in the AI Practitioner Learning OS and how to work with them effectively.

For complete agent specifications, see [.claude/agents/](../.claude/agents/).

## Overview

Six specialized agents work together to support your learning:

| Agent | Role | You'll Use When |
|-------|------|-----------------|
| **Planner** | Plans and tracks progress | Starting weeks, checking status |
| **Builder** | Implements and ships code | Building features and projects |
| **Reviewer** | Reviews code quality | Getting feedback on code |
| **Evaluator** | Scores and adapts | Checking progress, adjusting path |
| **Coach** | Guides and supports | Reflecting, getting unstuck |
| **Researcher** | Finds resources | (Works behind the scenes) |

## How Agents Work Together

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   PLANNER    │────►│   BUILDER    │────►│   REVIEWER   │
│              │     │              │     │              │
│ Plans work   │     │ Implements   │     │ Reviews &    │
│ Sets goals   │     │ Ships code   │     │ Feedback     │
└──────────────┘     └──────────────┘     └──────────────┘
       │                    │                    │
       │                    │                    │
       ▼                    ▼                    ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  EVALUATOR   │◄────│    COACH     │◄────│  RESEARCHER  │
│              │     │              │     │              │
│ Scores &     │     │ Guidance &   │     │ Finds docs & │
│ Adapts       │     │ Retros       │     │ Examples     │
└──────────────┘     └──────────────┘     └──────────────┘
```

## Planner Agent

**Role**: Helps you plan and stay organized.

**Commands**:
- `/status` - Check where you are
- `/plan-week` - Create weekly plan
- `/start-week` - Initialize new week

**When to Use**:
- Start of each day (status check)
- Start of each week (planning)
- When you feel lost or overwhelmed

**Example Interaction**:
```
You: /plan-week
     I have about 10 hours this week. Main goal is finishing the EDA notebook.

Planner: Here's your week plan:

Monday (2h):
- Load and inspect the dataset
- Check data quality (missing values, duplicates)

Tuesday (2h):
- Univariate analysis of key variables
- Create distribution plots

Wednesday (2h):
- Bivariate analysis and correlations
- Feature relationships

Thursday (2h):
- Document insights
- Create EDA summary

Friday (2h):
- Review and polish notebook
- Run evaluation and retro
```

See [.claude/agents/planner.md](../.claude/agents/planner.md) for full details.

## Builder Agent

**Role**: Helps you implement and ship code.

**Commands**:
- `/ship-mvp` - Build minimal viable product
- `/harden` - Add tests, error handling, docs
- `/publish` - Prepare for demo and sharing

**When to Use**:
- Starting a new feature or project
- Need guidance on implementation
- Ready to polish and ship

**Example Interaction**:
```
You: /ship-mvp
     Build a simple data pipeline that cleans CSV data

Builder: Let's build your MVP data pipeline.

## Scope
- Input: Raw CSV file
- Output: Cleaned CSV file
- Key operations: Load, validate, clean, save

## Implementation

### Step 1: Create pipeline structure
[Creates basic file structure]

### Step 2: Implement cleaning functions
[Implements core logic]

### Step 3: Add basic tests
[Creates initial tests]

Ready to harden when you've verified it works!
```

See [.claude/agents/builder.md](../.claude/agents/builder.md) for full details.

## Reviewer Agent

**Role**: Reviews your code and provides feedback.

**When It's Used**:
- After Builder completes implementation
- When you request code review
- During `/harden` process

**What It Checks**:
- Correctness (does it work?)
- Clarity (is it readable?)
- Style (follows conventions?)
- Testing (adequate coverage?)
- Documentation (is it clear?)
- Security (any vulnerabilities?)

**Feedback Format**:
```markdown
## Summary
Good implementation with room for improvement in error handling.

## Must Fix (Blockers)
1. Missing input validation in load_data()

## Should Fix (Important)
1. Add docstrings to public functions
2. Consider edge case: empty CSV file

## Consider (Nice to Have)
1. Could add type hints for better IDE support

## Praise
- Clean separation of concerns
- Good use of pandas idioms
```

See [.claude/agents/reviewer.md](../.claude/agents/reviewer.md) for full details.

## Evaluator Agent

**Role**: Scores your progress and proposes adaptations.

**Commands**:
- `/evaluate` - Run evaluation
- `/adapt-path` - Propose path changes
- `/report` - Generate tracker report

**When to Use**:
- End of each week
- End of each month
- When wondering about progress

**Scoring Categories**:
| Category | Weight | What It Measures |
|----------|--------|------------------|
| Completion | 30% | Tasks done, deliverables shipped |
| Quality | 25% | Code quality, test coverage |
| Understanding | 25% | Reflections, documented decisions |
| Consistency | 20% | Regular progress, habits |

**Example Output**:
```
Overall Score: 75/100

Category Scores:
  completion      [████████░░] 80
  quality         [███████░░░] 70
  understanding   [███████░░░] 75
  consistency     [███████░░░] 75

Strengths:
  ✓ Regular commits
  ✓ Good test coverage

Gaps:
  ✗ Missing weekly reflections
  ✗ Documentation incomplete

Recommendations:
  → Complete your retros each week
  → Add README to your project
```

See [.claude/agents/evaluator.md](../.claude/agents/evaluator.md) for full details.

## Coach Agent

**Role**: Guides you, runs retros, captures learning.

**Commands**:
- `/retro` - Run retrospective
- `/add-best-practice` - Capture learning
- `/debug-learning` - Get unstuck

**When to Use**:
- Friday (weekly retro)
- When you discover something useful
- When stuck for more than an hour

**Example Interaction**:
```
You: /debug-learning
     I've been stuck on pandas merge for 2 hours.
     I've read the docs but my join is producing duplicates.

Coach: Let me help diagnose this.

## Clarifying Questions
1. Are you doing a left, right, inner, or outer merge?
2. Are your key columns unique in both dataframes?
3. Can you share the merge statement you're using?

## Likely Causes
Based on duplicates appearing, common causes are:
- Key columns have duplicate values in one or both dataframes
- Using wrong type of join for your use case

## Quick Checks
```python
# Check for duplicate keys
print(df1['key'].duplicated().sum())
print(df2['key'].duplicated().sum())
```

Let me know what you find!
```

See [.claude/agents/coach.md](../.claude/agents/coach.md) for full details.

## Researcher Agent

**Role**: Finds documentation and examples.

**When It's Used**:
- Other agents need resources
- Looking up documentation
- Finding code examples

This agent works behind the scenes - you typically don't invoke it directly.

See [.claude/agents/researcher.md](../.claude/agents/researcher.md) for details.

## Agent Routing

When you use a command, it's routed to the right agent:

| Command | Primary Agent | Supporting |
|---------|---------------|------------|
| `/status` | Planner | - |
| `/plan-week` | Planner | - |
| `/start-week` | Planner | - |
| `/ship-mvp` | Builder | Reviewer |
| `/harden` | Builder | Reviewer |
| `/publish` | Builder | Reviewer |
| `/retro` | Coach | Evaluator |
| `/evaluate` | Evaluator | - |
| `/adapt-path` | Evaluator | Coach |
| `/add-best-practice` | Coach | - |
| `/debug-learning` | Coach | Researcher |
| `/report` | Evaluator | - |

## Tips for Working with Agents

### Be Specific

The more context you provide, the better help you get:

```
# Less helpful
/ship-mvp
Build a model.

# More helpful
/ship-mvp
Build a logistic regression baseline for binary classification.
The target is 'churned' (0/1), data is in 'data/customers.csv'.
Focus on getting something working - we'll improve later.
```

### Follow the Flow

Work with agents in their natural sequence:
1. **Plan** with Planner
2. **Build** with Builder
3. **Review** with Reviewer
4. **Evaluate** with Evaluator
5. **Reflect** with Coach

### Ask for Help Early

Don't struggle alone:
- Stuck > 30 minutes? Use `/debug-learning`
- Unsure about approach? Ask before building
- Code feels messy? Request review

## Source Files

Each agent has a detailed specification:

- [Planner](../.claude/agents/planner.md)
- [Builder](../.claude/agents/builder.md)
- [Reviewer](../.claude/agents/reviewer.md)
- [Evaluator](../.claude/agents/evaluator.md)
- [Coach](../.claude/agents/coach.md)
- [Researcher](../.claude/agents/researcher.md)

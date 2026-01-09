# Agents Guide

How to work with AI agents in the learning OS.

## Overview

Agents are specialized advisory roles that Claude can assume. Each agent has specific expertise and responsibilities.

## Available Agents

| Agent | Expertise | Primary Commands |
|-------|-----------|------------------|
| Planner | Planning, scheduling | `/status`, `/plan-week` |
| Builder | Implementation, coding | `/start-week`, `/ship-mvp` |
| Reviewer | Quality, security | `/harden`, `/publish` |
| Evaluator | Assessment, scoring | `/evaluate`, `/adapt-path` |
| Coach | Guidance, unblocking | `/retro`, `/debug-learning` |
| Researcher | Information gathering | Research tasks |

## How Agents Work

### 1. You Invoke (via command or request)

```
/plan-week
```
or
```
"As the Planner, help me plan this week"
```

### 2. Agent Analyzes

The agent reads context:
- Memory files
- Current month goals
- Progress history
- Your request

### 3. Agent Recommends

The agent presents proposals:
- Week plan
- Code changes
- Evaluation results
- Adaptation suggestions

### 4. You Approve

**Critical**: No changes happen without your explicit approval.

```
**Approve this plan?** (yes/modify/no)
```

### 5. Agent Executes (Only If Approved)

After your approval, the agent applies changes.

## Agent Details

### Planner Agent

**Role**: Plans and schedules learning activities.

**Strengths**:
- Breaking down month goals into weekly tasks
- Time estimation
- Dependency identification
- Schedule optimization

**Invoked by**:
- `/status`
- `/plan-week`
- "Help me plan..."

**Hands off to**:
- Builder (after plan approved)
- Researcher (if research needed first)

See [.claude/agents/planner.md](../.claude/agents/planner.md)

### Builder Agent

**Role**: Implements projects and code.

**Strengths**:
- Code implementation
- Template usage
- Best practice application
- Incremental building

**Invoked by**:
- `/start-week`
- `/ship-mvp`
- "Implement..."

**Hands off to**:
- Reviewer (for code review)
- Coach (if stuck)

See [.claude/agents/builder.md](../.claude/agents/builder.md)

### Reviewer Agent

**Role**: Reviews quality, security, performance.

**Strengths**:
- Code review
- Security audit
- Performance analysis
- Documentation review

**Invoked by**:
- `/harden`
- `/publish`
- "Review this code..."

**Hands off to**:
- Builder (to fix issues)
- Coach (if learning opportunity)

See [.claude/agents/reviewer.md](../.claude/agents/reviewer.md)

### Evaluator Agent

**Role**: Assesses progress and proposes adaptations.

**Strengths**:
- Score computation
- Trend analysis
- Adaptation proposals
- Progress tracking

**Invoked by**:
- `/evaluate`
- `/adapt-path`
- "Evaluate my progress..."

**Hands off to**:
- Coach (if scores low)
- Planner (for replanning)

See [.claude/agents/evaluator.md](../.claude/agents/evaluator.md)

### Coach Agent

**Role**: Provides guidance when stuck.

**Strengths**:
- Unblocking
- Motivation
- Learning strategies
- Retrospectives

**Invoked by**:
- `/retro`
- `/debug-learning`
- `/add-best-practice`
- "I'm stuck on..."

**Hands off to**:
- Researcher (if research needed)
- Builder (ready to continue)

See [.claude/agents/coach.md](../.claude/agents/coach.md)

### Researcher Agent

**Role**: Gathers information and resources.

**Strengths**:
- Technology research
- Best practice discovery
- Resource curation
- Comparison analysis

**Invoked by**:
- "Research..."
- "Compare..."
- "What are the options for..."

**Hands off to**:
- Planner (research complete)
- Builder (implementation details)

See [.claude/agents/researcher.md](../.claude/agents/researcher.md)

## Invoking Agents

### Via Commands

Most common way:
```
/plan-week      → Planner
/harden         → Reviewer
/evaluate       → Evaluator
```

### Direct Request

Ask for a specific agent:
```
"As the Coach, help me understand why I'm stuck"
"Acting as the Researcher, compare Qdrant vs Pinecone"
```

### Implicit Routing

Claude routes based on context:
```
"Review my code" → Reviewer
"Plan next week" → Planner
"I'm confused" → Coach
```

## Agent Handoffs

Agents can suggest handoffs:

```
Planner: "Plan approved. I recommend handing off to
         the Builder to start implementation."

You: "Yes, proceed with Builder"

Builder: "Starting Week 2 implementation..."
```

**You control handoffs** - they don't happen automatically.

## Human-in-the-Loop

Every agent interaction requires your participation:

| Phase | Agent Does | You Do |
|-------|------------|--------|
| Analyze | Reads context | Provide input |
| Recommend | Presents options | Review options |
| Execute | Waits | Approve/Modify/Reject |
| Apply | Makes changes | Verify results |

## Tips for Working with Agents

1. **Be specific** - "Plan Week 2 focusing on tests" is better than "Plan"
2. **Provide context** - Share what you've tried, what's blocking you
3. **Review recommendations** - Don't just approve blindly
4. **Use handoffs** - Let agents collaborate via you
5. **Capture learnings** - Use Coach to reflect after completing work

## Agent Files

All agent definitions are in `.claude/agents/`:
- `README.md` - Overview
- `planner.md`, `builder.md`, etc. - Individual agents

Each file defines:
- Role and responsibilities
- Constraints
- Inputs and outputs
- Handoff recommendations

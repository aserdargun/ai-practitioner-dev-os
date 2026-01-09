# Agents

This folder contains the advisory agent definitions for the AI Practitioner Learning OS.

## Overview

Agents are specialized advisory roles that Claude Code can assume when helping you with your learning journey. Each agent has specific responsibilities, constraints, and recommended handoffs.

## Available Agents

| Agent | Role | Primary Commands |
|-------|------|------------------|
| [Planner](planner.md) | Plans and schedules learning activities | `/plan-week`, `/status` |
| [Builder](builder.md) | Implements projects and code | `/start-week`, `/ship-mvp` |
| [Reviewer](reviewer.md) | Reviews code, docs, and deliverables | `/harden`, `/publish` |
| [Evaluator](evaluator.md) | Assesses progress and computes scores | `/evaluate` |
| [Coach](coach.md) | Provides guidance when stuck | `/debug-learning`, `/retro` |
| [Researcher](researcher.md) | Gathers information and resources | `/status`, `/plan-week` |

## Human-in-the-Loop Requirement

**Critical**: Each agent must present recommendations to the user and wait for explicit approval before taking any action that modifies files, state, or learning path.

### Approval Workflow

1. Agent analyzes the situation
2. Agent presents recommendations with clear rationale
3. **User reviews and approves** (or modifies/rejects)
4. Only then does the agent execute approved actions

### Agent Handoffs

Agent handoffs must also be confirmed by the user:
- Agent A suggests: "I recommend handing off to the Builder agent to implement this"
- User confirms: "Yes, proceed with Builder"
- Handoff occurs

## Invoking Agents

You can invoke agents through their associated commands or by directly asking Claude to assume a role:

```
/plan-week           # Invokes Planner agent
/evaluate            # Invokes Evaluator agent
/debug-learning      # Invokes Coach agent
```

Or directly:
```
"As the Planner agent, help me plan this week's activities"
"As the Coach agent, I'm stuck on this concept..."
```

## Agent Definitions

Each agent definition file includes:
- **Role**: What the agent does
- **Responsibilities**: Specific duties
- **Constraints**: What the agent must NOT do
- **Inputs**: What information the agent needs
- **Outputs**: What the agent produces
- **Handoffs**: When to suggest another agent

See individual agent files for details.

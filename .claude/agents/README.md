# Agents

This folder contains the six AI advisor personas that power the learning OS.

## Available Agents

| Agent | File | Primary Role |
|-------|------|--------------|
| Planner | `planner.md` | Creates plans, timelines, and schedules |
| Builder | `builder.md` | Writes code and implements features |
| Reviewer | `reviewer.md` | Reviews code and provides feedback |
| Evaluator | `evaluator.md` | Assesses progress and generates scores |
| Coach | `coach.md` | Offers learning guidance and motivation |
| Researcher | `researcher.md` | Gathers information and explores topics |

## Human-in-the-Loop Requirement

**All agents operate in advisory mode.** They present recommendations and wait for your explicit approval before taking any action that modifies files, state, or your learning path.

### Agent Workflow

1. You invoke an agent (directly or via a command)
2. Agent analyzes context and generates recommendations
3. Agent presents recommendations to you
4. **You review and approve/reject/modify**
5. Only approved actions are executed

### Agent Handoffs

Agents can suggest handoffs to other agents when appropriate:
- Planner → Builder (after plan approval)
- Builder → Reviewer (after implementation)
- Reviewer → Builder (for revisions)
- Evaluator → Coach (for guidance)
- Researcher → any agent (with findings)

**All handoffs require your confirmation.**

## How to Invoke Agents

### Via Slash Commands
Most commands route to specific agents:
- `/plan-week` → Planner
- `/ship-mvp` → Builder
- `/retro` → Reviewer + Coach
- `/evaluate` → Evaluator

### Direct Invocation
You can invoke agents directly in Claude Code:
```
Ask the Planner agent to help me design next week's schedule
```

```
Ask the Builder agent to implement the data validation function
```

```
Ask the Reviewer agent to review my latest commit
```

## Agent Constraints

Each agent has defined constraints in their `.md` file:
- What they can and cannot do
- Required approvals before actions
- Memory access patterns
- Handoff protocols

See individual agent files for details.

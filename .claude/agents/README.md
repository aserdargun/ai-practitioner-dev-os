# Agents

This folder contains the agent definitions for the AI Practitioner Learning OS. Each agent has a specific role, responsibilities, constraints, and handoff protocols.

## Available Agents

| Agent | File | Primary Role |
|-------|------|--------------|
| Planner | [planner.md](planner.md) | Plans weeks, tracks milestones, manages goals |
| Builder | [builder.md](builder.md) | Implements features, ships code, creates MVPs |
| Reviewer | [reviewer.md](reviewer.md) | Reviews code, provides feedback, ensures quality |
| Evaluator | [evaluator.md](evaluator.md) | Scores progress, proposes path adaptations |
| Coach | [coach.md](coach.md) | Guides learner, runs retros, captures best practices |
| Researcher | [researcher.md](researcher.md) | Explores documentation, finds examples |

## Agent Interaction Model

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

## Command Routing

Each command is handled by a primary agent:

| Command | Primary Agent | Supporting Agents |
|---------|---------------|-------------------|
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

## Handoff Protocol

When an agent needs another agent's help:

1. **State the need**: Clearly describe what's needed
2. **Provide context**: Share relevant memory state
3. **Define success**: Specify what a successful handoff looks like
4. **Return control**: Hand back to the original agent with results

## Constraints (All Agents)

1. **Memory discipline**: Only append to memory files, never overwrite
2. **Allowed adaptations only**: When proposing changes, only use allowed mutations
3. **Learner agency**: Always explain options, let learner decide
4. **Scope awareness**: Stay within current tier (Beginner = Tier 1 only)

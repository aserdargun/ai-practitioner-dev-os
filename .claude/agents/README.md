# Agents

This folder contains AI advisor role definitions. Each agent has specific responsibilities and constraints.

## Available Agents

| Agent | File | Purpose |
|-------|------|---------|
| Planner | [planner.md](planner.md) | Suggests plans; you approve before execution |
| Builder | [builder.md](builder.md) | Proposes implementations; you review and approve |
| Reviewer | [reviewer.md](reviewer.md) | Provides feedback; you decide what to act on |
| Evaluator | [evaluator.md](evaluator.md) | Generates assessments; you validate results |
| Coach | [coach.md](coach.md) | Offers guidance; you choose which advice to follow |
| Researcher | [researcher.md](researcher.md) | Gathers information; you direct research focus |

## Human-in-the-Loop Principle

All agents follow the same core workflow:

1. **Agent analyzes** the current context
2. **Agent proposes** recommendations
3. **You review** the proposals
4. **You approve** (or reject/modify)
5. **Agent executes** only approved actions

No agent modifies files, state, or your learning path without explicit confirmation.

## Invoking Agents

You can invoke agents through:
- Slash commands (e.g., `/plan-week` routes to Planner)
- Direct request: "Ask the Builder agent to help me implement..."
- Context-aware routing: Claude will suggest the appropriate agent

## Agent Handoffs

Agents can suggest handing off to another agent:
- Planner → Builder (after plan is approved)
- Builder → Reviewer (after implementation)
- Reviewer → Evaluator (after code review)
- Evaluator → Coach (when guidance needed)

All handoffs require your confirmation.

## Related Documentation

- [docs/agents.md](../../docs/agents.md) — User guide for working with agents
- [commands/catalog.md](../commands/catalog.md) — Commands that invoke agents

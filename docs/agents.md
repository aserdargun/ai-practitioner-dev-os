# Agents Reference

Guide to the six AI advisor personas in the learning OS.

## Overview

Agents are specialized AI personas, each with defined responsibilities and constraints. They work in **advisory mode** — providing recommendations that require your approval before any action.

| Agent | Role | Commands |
|-------|------|----------|
| Planner | Plans and schedules | `/plan-week`, `/start-week` |
| Builder | Implements code | `/ship-mvp`, `/harden`, `/publish` |
| Reviewer | Reviews and feedback | `/harden`, `/retro` |
| Evaluator | Assesses progress | `/status`, `/evaluate`, `/adapt-path` |
| Coach | Guides and supports | `/retro`, `/add-best-practice`, `/debug-learning` |
| Researcher | Gathers information | Direct invocation |

See full specifications: [.claude/agents/](../.claude/agents/)

---

## Human-in-the-Loop Workflow

All agents follow this pattern:

```
1. You invoke agent (via command or directly)
2. Agent analyzes context
3. Agent generates recommendation
4. Agent presents to you for review
5. YOU APPROVE / MODIFY / REJECT
6. Only approved actions are executed
```

**No changes happen without your explicit approval.**

---

## Planner Agent

### Role
Senior project manager and learning scientist who creates structured plans.

### Responsibilities
- Create weekly learning plans
- Propose schedules based on your constraints
- Suggest timeline adjustments
- Balance learning goals with shipping

### When to Use
```
Ask the Planner to help me design next week's schedule
```
```
/plan-week I have 8 hours and want to focus on testing
```

### What It Reads
- `learner_profile.json` — Your goals and constraints
- `progress_log.jsonl` — Recent activity
- Month README — Current month's goals

### What It Proposes
- Weekly task breakdown
- Time estimates
- Dependencies
- Risk flags

See: [.claude/agents/planner.md](../.claude/agents/planner.md)

---

## Builder Agent

### Role
Senior software engineer who writes production-quality code.

### Responsibilities
- Write clean, tested code
- Implement features per approved plans
- Create data pipelines, models, APIs
- Debug and fix issues

### When to Use
```
Ask the Builder to implement the data validation function
```
```
/ship-mvp for the forecasting dashboard
```

### Templates Available
- `templates/template-fastapi-service/`
- `templates/template-data-pipeline/`
- `templates/template-rag-service/`
- `templates/template-eval-harness/`

### What It Proposes
- Code changes
- Test files
- Documentation updates

See: [.claude/agents/builder.md](../.claude/agents/builder.md)

---

## Reviewer Agent

### Role
Senior code reviewer who provides constructive feedback.

### Responsibilities
- Review code for correctness and clarity
- Check for security vulnerabilities
- Verify test adequacy
- Suggest improvements

### When to Use
```
Ask the Reviewer to review my DataProcessor class
```
```
/harden then review the changes
```

### Review Categories
- **Correctness**: Does it work?
- **Security**: Any vulnerabilities?
- **Maintainability**: Easy to understand?
- **Testing**: Adequate coverage?

### What It Outputs
- Structured comments
- Priority-ranked issues
- Suggested fixes

See: [.claude/agents/reviewer.md](../.claude/agents/reviewer.md)

---

## Evaluator Agent

### Role
Learning assessment specialist who measures progress objectively.

### Responsibilities
- Compute progress scores
- Identify skill gaps
- Generate reports
- Propose adaptations

### When to Use
```
/status
```
```
/evaluate Month 3
```
```
/adapt-path
```

### Evaluation Dimensions
| Dimension | Signals |
|-----------|---------|
| Completion | Tasks done, deliverables shipped |
| Quality | Tests, docs, reviews |
| Velocity | Progress rate, trends |
| Learning | Reflections, best practices |

### Scoring Scale
```
0-40:  At Risk
41-60: Needs Attention
61-80: On Track
81-100: Exceeding
```

See: [.claude/agents/evaluator.md](../.claude/agents/evaluator.md)

---

## Coach Agent

### Role
Learning coach who provides guidance and helps overcome blockers.

### Responsibilities
- Offer learning strategies
- Help diagnose blockers
- Provide motivation
- Guide retrospectives

### When to Use
```
/debug-learning I'm stuck on decorators
```
```
/retro for Week 2
```
```
Ask the Coach for perspective — I feel behind
```

### Coaching Modes
- **Debugging Blockers**: Why are you stuck?
- **Learning Strategies**: How to learn better?
- **Motivation**: Perspective and encouragement
- **Reflection**: What did you learn?

### What It Provides
- Personalized guidance
- Resource recommendations
- Reflection prompts

See: [.claude/agents/coach.md](../.claude/agents/coach.md)

---

## Researcher Agent

### Role
Technical researcher who gathers information and explores topics.

### Responsibilities
- Research technologies and tools
- Find documentation and tutorials
- Compare options
- Summarize complex topics

### When to Use
```
Ask the Researcher to explain FastAPI vs Flask
```
```
Ask the Researcher to find resources for learning pandas
```

### Research Modes
- **Technology Exploration**: Deep dive into tech
- **Comparison**: Compare options
- **How-To**: Find practical guidance
- **Context**: Provide background

### What It Provides
- Synthesized summaries
- Comparison tables
- Resource recommendations

See: [.claude/agents/researcher.md](../.claude/agents/researcher.md)

---

## Agent Handoffs

Agents can suggest handing off to other agents:

| From | To | When |
|------|----|------|
| Planner | Builder | After plan approval |
| Builder | Reviewer | After implementation |
| Reviewer | Builder | For revisions |
| Evaluator | Coach | For guidance |
| Researcher | Any | With findings |

**All handoffs require your confirmation.**

---

## Invoking Agents Directly

Besides commands, you can invoke agents directly:

```
Ask the [Agent] to [specific request]
```

Examples:
```
Ask the Planner to help me adjust my schedule for a busy week
```
```
Ask the Builder to add error handling to the API endpoint
```
```
Ask the Coach to help me understand why I'm procrastinating
```

---

## Tips

1. **Be specific**: Give agents context about what you need
2. **Review outputs**: Always review before approving
3. **Ask questions**: If something isn't clear, ask
4. **Use the right agent**: Match the agent to the task
5. **Combine agents**: Complex tasks may involve multiple agents

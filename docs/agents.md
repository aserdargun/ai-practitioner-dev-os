# Agents Guide

Understanding the AI agents that power the learning system.

---

## Overview

The learning system uses specialized AI agents, each with distinct responsibilities. When you invoke a command, Claude adopts the appropriate agent's role to provide focused assistance.

---

## Agent Roster

### 1. Planner Agent

**Role**: Creates structured plans and schedules

**Symbol**: 📋

**Primary Commands**: `/plan-week`, `/start-week`

**Responsibilities**:
- Generate weekly task lists
- Break down monthly objectives
- Sequence tasks by dependency
- Estimate effort
- Update journal entries

**When Planner Activates**:
- Beginning of each week
- When you need task breakdown
- When planning sprints

**Planner's Mindset**:
> "What needs to be done? In what order? How long will each task take?"

---

### 2. Builder Agent

**Role**: Writes code and ships features

**Symbol**: 🔨

**Primary Commands**: `/ship-mvp`, `/harden`, `/publish`

**Responsibilities**:
- Implement features
- Write tests
- Add documentation
- Fix bugs
- Ensure code quality

**When Builder Activates**:
- During implementation phases
- When shipping code
- When hardening existing code

**Builder's Mindset**:
> "Ship working code. Make it work first, then make it better."

---

### 3. Reviewer Agent

**Role**: Reviews code and ensures quality

**Symbol**: 🔍

**Supporting Commands**: `/ship-mvp`, `/harden`, `/publish`

**Responsibilities**:
- Code review
- Security checks
- Performance review
- Documentation review
- Style consistency

**When Reviewer Activates**:
- After Builder produces code
- Before shipping/publishing
- During hardening phase

**Reviewer's Mindset**:
> "Is this code correct, secure, and maintainable?"

---

### 4. Evaluator Agent

**Role**: Scores progress and identifies gaps

**Symbol**: 📊

**Primary Commands**: `/status`, `/evaluate`, `/adapt-path`, `/report`

**Responsibilities**:
- Calculate progress scores
- Read repo signals
- Analyze patterns
- Generate recommendations
- Trigger adaptations

**When Evaluator Activates**:
- Status checks
- Weekly/monthly evaluations
- Path adaptation decisions

**Evaluator's Mindset**:
> "How is the learner doing? What patterns indicate progress or struggle?"

---

### 5. Coach Agent

**Role**: Provides guidance and mentorship

**Symbol**: 🎯

**Primary Commands**: `/retro`, `/add-best-practice`, `/debug-learning`

**Responsibilities**:
- Facilitate retrospectives
- Capture learnings
- Provide encouragement
- Help overcome blockers
- Guide career development

**When Coach Activates**:
- Retrospectives
- When learner is stuck
- When capturing best practices

**Coach's Mindset**:
> "How can I help this learner grow? What have they learned?"

---

### 6. Researcher Agent

**Role**: Finds resources and investigates issues

**Symbol**: 🔬

**Supporting Commands**: `/debug-learning`, `/plan-week`

**Responsibilities**:
- Find learning resources
- Investigate technical issues
- Compile references
- Analyze alternatives
- Stay current with trends

**When Researcher Activates**:
- When learner needs resources
- When debugging complex issues
- When exploring new topics

**Researcher's Mindset**:
> "What resources would help? What does the documentation say?"

---

## Agent Collaboration

Agents often work together:

```
Command: /ship-mvp

┌──────────┐     ┌──────────┐     ┌──────────┐
│  Builder │────▶│ Reviewer │────▶│Evaluator │
│          │     │          │     │          │
│ Writes   │     │ Reviews  │     │ Logs     │
│ code     │     │ quality  │     │ progress │
└──────────┘     └──────────┘     └──────────┘
```

```
Command: /retro

┌──────────┐     ┌──────────┐
│  Coach   │────▶│Evaluator │
│          │     │          │
│ Guides   │     │ Provides │
│ reflection│    │ metrics  │
└──────────┘     └──────────┘
```

```
Command: /debug-learning

┌──────────┐     ┌──────────┐
│  Coach   │────▶│Researcher│
│          │     │          │
│ Identifies│    │ Finds    │
│ blocker  │     │ solutions│
└──────────┘     └──────────┘
```

---

## Command-Agent Routing

| Command | Primary | Supporting |
|---------|---------|------------|
| `/status` | Evaluator | — |
| `/plan-week` | Planner | Coach |
| `/start-week` | Planner | — |
| `/ship-mvp` | Builder | Reviewer |
| `/harden` | Builder | Reviewer |
| `/publish` | Builder | Coach |
| `/retro` | Coach | Evaluator |
| `/evaluate` | Evaluator | — |
| `/adapt-path` | Evaluator | Coach |
| `/add-best-practice` | Coach | — |
| `/debug-learning` | Coach | Researcher |
| `/report` | Evaluator | — |

---

## Agent Files

Agent definitions are in `.claude/agents/`:

```
.claude/agents/
├── planner.md
├── builder.md
├── reviewer.md
├── evaluator.md
├── coach.md
└── researcher.md
```

Each file contains:
- Role description
- Responsibilities
- Trigger commands
- Input/output specifications
- Process guidelines

---

## Customizing Agents

You can customize agent behavior by editing their definition files:

1. **Adjust priorities**: Change what the agent focuses on
2. **Add context**: Include domain-specific guidance
3. **Modify outputs**: Change output formats

Example customization in `builder.md`:
```markdown
## Additional Context

For this project, prioritize:
- Type hints on all functions
- Async patterns where appropriate
- Comprehensive error messages
```

---

## Best Practices

### Working with Agents

1. **Let agents do their job**: Trust the agent's focus area
2. **Provide context**: Give agents relevant information
3. **Follow up**: Agents can be asked clarifying questions

### Choosing Commands

1. **Match task to agent**: Use `/ship-mvp` for shipping, `/harden` for quality
2. **Follow the workflow**: Status → Plan → Build → Harden → Retro
3. **Combine when needed**: Run multiple commands in sequence

### Getting Better Results

1. **Be specific**: "Help me debug this error" vs "Something's wrong"
2. **Share context**: Include error messages, file names
3. **Iterate**: Ask follow-up questions if needed

---

## See Also

- [Commands Guide](commands.md) — Full command reference
- [System Overview](system-overview.md) — Architecture details
- [How to Use](how-to-use.md) — Workflow guide

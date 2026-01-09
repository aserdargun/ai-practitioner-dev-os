# Agents Guide

How to work with the AI advisor agents in the learning system.

## Overview

Six specialized agents help you through your learning journey:

| Agent | Role | Specialty |
|-------|------|-----------|
| **Planner** | Project Manager | Plans, tasks, schedules |
| **Builder** | Engineer | Code, implementation |
| **Reviewer** | QA Specialist | Feedback, quality |
| **Evaluator** | Assessor | Scoring, measurement |
| **Coach** | Mentor | Guidance, motivation |
| **Researcher** | Information Gatherer | Docs, examples, context |

For technical details, see [.claude/agents/](../.claude/agents/).

---

## Human-in-the-Loop Principle

**All agents follow this workflow:**

```
┌─────────────────────────────────────────┐
│                                         │
│   Agent analyzes context                │
│            ↓                            │
│   Agent proposes recommendations        │
│            ↓                            │
│   YOU REVIEW the proposals              │
│            ↓                            │
│   YOU APPROVE (or reject/modify)        │
│            ↓                            │
│   Agent executes ONLY approved actions  │
│                                         │
└─────────────────────────────────────────┘
```

No agent modifies files or changes your path without your explicit approval.

---

## Planner Agent

### What It Does
- Creates weekly plans
- Breaks down projects into tasks
- Estimates effort
- Identifies dependencies

### When to Invoke
- Start of each week
- When planning a new project
- When reprioritizing

### How to Invoke
```
/plan-week

Or directly:
"Planner, help me create a plan for this week."
```

### What You Approve
- The weekly plan before it's finalized
- Task prioritization
- Time allocations

---

## Builder Agent

### What It Does
- Implements features
- Writes code
- Creates project structure
- Applies skill playbooks

### When to Invoke
- During implementation phase
- When coding features
- When setting up projects

### How to Invoke
```
/ship-mvp

Or directly:
"Builder, help me implement the data pipeline."
```

### What You Approve
- Code changes before they're applied
- Architecture decisions
- Dependency choices

---

## Reviewer Agent

### What It Does
- Reviews code for issues
- Identifies potential bugs
- Suggests improvements
- Checks quality standards

### When to Invoke
- After implementing features
- Before publishing
- When hardening

### How to Invoke
```
/harden

Or directly:
"Reviewer, please review my API implementation."
```

### What You Approve
- Which feedback to act on
- Suggested changes
- Priority of fixes

---

## Evaluator Agent

### What It Does
- Assesses deliverables
- Computes scores
- Cites evidence
- Generates reports

### When to Invoke
- End of week
- End of month
- After completing deliverables

### How to Invoke
```
/evaluate

Or directly:
"Evaluator, assess my Month 3 project."
```

### What You Approve
- Validation of the assessment
- Score adjustments if evidence suggests
- Recording in progress log

---

## Coach Agent

### What It Does
- Provides guidance
- Offers motivation
- Helps with blockers
- Captures learnings

### When to Invoke
- When stuck or confused
- During retrospectives
- When feeling unmotivated
- To capture best practices

### How to Invoke
```
/retro
/debug-learning
/add-best-practice

Or directly:
"Coach, I'm feeling stuck on this concept."
```

### What You Approve
- Which advice to follow
- Learnings to save
- Path recommendations

---

## Researcher Agent

### What It Does
- Finds documentation
- Locates examples
- Compares technologies
- Summarizes information

### When to Invoke
- Learning new technologies
- Making technology decisions
- Need context or examples

### How to Invoke
```
"Researcher, help me understand the difference between
LangChain and LlamaIndex."

"Research the best practices for RAG evaluation."
```

### What You Approve
- Research focus direction
- Which sources to trust
- Conclusions and recommendations

---

## Agent Handoffs

Agents can suggest handing off to each other:

| From | To | When |
|------|----|------|
| Planner | Builder | Plan approved, ready to build |
| Builder | Reviewer | Implementation done |
| Reviewer | Evaluator | Code reviewed, ready for assessment |
| Evaluator | Coach | Evaluation reveals guidance needed |
| Coach | Planner | Ready to plan next steps |
| Any | Researcher | More information needed |

**All handoffs require your confirmation.**

---

## Tips for Working with Agents

### Be Specific
```
# Less effective
"Help me with my project."

# More effective
"Planner, help me create a week plan for the RAG project.
I have 10 hours this week and want to focus on evaluation."
```

### Provide Context
```
"Builder, help me implement the retrieval component.
I'm using LangChain and Chroma. The ingest step is done."
```

### Ask for Reasoning
```
"Evaluator, explain why my learning score is low.
What evidence are you using?"
```

### Challenge Recommendations
```
"I don't agree with that assessment. Here's additional
context: [your context]. Can you reconsider?"
```

---

## Related Documentation

- [.claude/agents/README.md](../.claude/agents/README.md) — Agent system overview
- [.claude/agents/*.md](../.claude/agents/) — Individual agent specs
- [commands.md](commands.md) — Commands that invoke agents
- [system-overview.md](system-overview.md) — How it all fits together

# Skills

This folder contains skill playbooks for the AI Practitioner Learning OS.

## Overview

Skills are step-by-step playbooks for common AI/ML tasks. Each skill provides a repeatable process with quality gates and artifact definitions.

## Available Skills

| Skill | Purpose | Level |
|-------|---------|-------|
| [EDA to Insight](eda-to-insight.md) | Exploratory data analysis workflow | All |
| [Baseline Model and Card](baseline-model-and-card.md) | Create baseline ML model with documentation | All |
| [Experiment Plan](experiment-plan.md) | Design and track ML experiments | All |
| [Forecasting Checklist](forecasting-checklist.md) | Time series forecasting workflow | Intermediate+ |
| [RAG with Evals](rag-with-evals.md) | Build RAG system with evaluation | Intermediate+ |
| [API Shipping Checklist](api-shipping-checklist.md) | Ship production-ready APIs | Intermediate+ |
| [Observability Starter](observability-starter.md) | Set up monitoring and observability | Intermediate+ |
| [K8s Deploy Checklist](k8s-deploy-checklist.md) | Deploy to Kubernetes | **Advanced only** |

## Skill Structure

Each skill playbook includes:

```markdown
# Skill: [Name]

## Trigger
When to use this skill

## Prerequisites
What you need before starting

## Steps
1. Step one...
2. Step two...

## Artifacts Produced
- artifact_one.py
- artifact_two.md

## Quality Bar
Minimum requirements to consider the skill complete

## Common Pitfalls
Things to watch out for

## Example
Concrete example of the skill in action
```

## Using Skills

Skills are referenced by agents when appropriate. You can also invoke them directly:

```
"Use the RAG with Evals skill to build my retrieval system"

"Follow the API Shipping Checklist skill for my FastAPI service"
```

The relevant agent (usually Builder or Reviewer) will apply the skill.

## Skill vs Command

| Aspect | Skill | Command |
|--------|-------|---------|
| Invocation | Referenced by name | Slash syntax (/command) |
| Scope | Multi-step process | Single action |
| Duration | Hours to days | Minutes |
| Output | Multiple artifacts | Single result |

## Extending Skills

To add a new skill:

1. Create `new-skill-name.md` in this folder
2. Follow the skill structure above
3. Update this README with the new skill
4. Reference from `docs/skills-playbook.md`

## Level Gates

Some skills are gated by level:
- **All levels**: EDA, Baseline Model, Experiment Plan
- **Intermediate+**: Forecasting, RAG, API, Observability
- **Advanced only**: K8s Deploy (requires cluster knowledge)

The skill files indicate their level requirements.

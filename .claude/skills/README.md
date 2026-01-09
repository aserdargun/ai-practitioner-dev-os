# Skills

This folder contains reusable playbooks for common AI/ML practitioner tasks.

## What Are Skills?

Skills are step-by-step guides for completing specific technical tasks. Each skill defines:
- **Trigger**: When to use this skill
- **Steps**: Detailed process to follow
- **Artifacts**: What gets produced
- **Quality Bar**: How to know you're done well

## Available Skills

| Skill | File | Description |
|-------|------|-------------|
| EDA to Insight | `eda-to-insight.md` | Exploratory data analysis workflow |
| Baseline Model and Card | `baseline-model-and-card.md` | Create first model with documentation |
| Experiment Plan | `experiment-plan.md` | Design and track experiments |
| Forecasting Checklist | `forecasting-checklist.md` | Time series forecasting workflow |
| RAG with Evals | `rag-with-evals.md` | Build RAG system with evaluation |
| API Shipping Checklist | `api-shipping-checklist.md` | Deploy production API |
| Observability Starter | `observability-starter.md` | Add logging and monitoring |
| K8s Deploy Checklist | `k8s-deploy-checklist.md` | Kubernetes deployment (Advanced) |

## How to Use Skills

### Direct Reference
Read the skill file and follow the steps:
```
Read .claude/skills/eda-to-insight.md and help me do EDA on my sales data
```

### Via Commands
Some commands automatically invoke skills:
- `/ship-mvp` may use `api-shipping-checklist.md`
- Building a RAG system invokes `rag-with-evals.md`

### Skill Chaining
Complex projects may use multiple skills:
1. EDA to Insight → understand data
2. Baseline Model → create first model
3. Experiment Plan → iterate on model
4. API Shipping → deploy model

## Skill Levels

| Tier | Skills |
|------|--------|
| Beginner (T1) | EDA, Baseline Model, Experiment Plan, Forecasting |
| Intermediate (T2) | RAG with Evals, API Shipping, Observability |
| Advanced (T3) | K8s Deploy Checklist |

Skills are unlocked based on your learner level, but you can read ahead.

## Creating Custom Skills

You can add your own skills by:
1. Creating a new `.md` file in this folder
2. Following the template structure
3. Documenting trigger, steps, artifacts, quality bar

## Skill Template

```markdown
# Skill: [Name]

## Trigger
When to use this skill

## Prerequisites
What you need before starting

## Steps
1. First step
2. Second step
3. ...

## Artifacts Produced
- Output 1
- Output 2

## Quality Bar
- [ ] Criteria 1
- [ ] Criteria 2

## Common Pitfalls
- Pitfall 1 and how to avoid
- Pitfall 2 and how to avoid

## Example
Real example of this skill in action
```

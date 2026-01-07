# Skills

This folder contains skill playbooks - step-by-step guides for common AI/ML tasks.

## Available Skills

| Skill | File | Tier | Description |
|-------|------|------|-------------|
| EDA to Insight | [eda-to-insight.md](eda-to-insight.md) | 1 | Exploratory data analysis workflow |
| Baseline Model | [baseline-model-and-card.md](baseline-model-and-card.md) | 1 | Building and documenting baseline models |
| Experiment Plan | [experiment-plan.md](experiment-plan.md) | 1 | Planning ML experiments |
| Forecasting | [forecasting-checklist.md](forecasting-checklist.md) | 1 | Time series forecasting checklist |
| RAG with Evals | [rag-with-evals.md](rag-with-evals.md) | 1-2 | Building RAG systems with evaluation |
| API Shipping | [api-shipping-checklist.md](api-shipping-checklist.md) | 1-2 | Deploying APIs |
| Observability | [observability-starter.md](observability-starter.md) | 2 | Adding monitoring and logging |
| K8s Deploy | [k8s-deploy-checklist.md](k8s-deploy-checklist.md) | 3 | Kubernetes deployment (Advanced only) |

## Skill Structure

Each skill playbook includes:

1. **Trigger**: When to use this skill
2. **Prerequisites**: What you need before starting
3. **Steps**: Numbered, actionable steps
4. **Artifacts**: What you'll produce
5. **Quality Bar**: How to know you're done

## How to Use Skills

### 1. Identify the Right Skill

Match your current task to a skill:
- Exploring data? → `eda-to-insight.md`
- Building first model? → `baseline-model-and-card.md`
- Deploying an API? → `api-shipping-checklist.md`

### 2. Check Prerequisites

Before starting, ensure you have:
- Required data/inputs
- Tools installed
- Dependencies available

### 3. Follow Steps

Work through each step:
- Don't skip steps
- Check off as you complete
- Ask for help if stuck

### 4. Verify Quality

Use the quality bar to confirm:
- All artifacts produced
- Quality criteria met
- Ready for review

## Tier Gating

Some skills are gated by tier:

| Tier | Available Skills |
|------|------------------|
| **Beginner (Tier 1)** | EDA, Baseline Model, Experiment Plan, Forecasting |
| **Intermediate (Tier 2)** | All Tier 1 + RAG, API Shipping, Observability |
| **Advanced (Tier 3)** | All Tier 2 + K8s Deploy |

**Current Level**: Beginner - Focus on Tier 1 skills.

## Documentation

For detailed usage guide, see [docs/skills-playbook.md](../../docs/skills-playbook.md).

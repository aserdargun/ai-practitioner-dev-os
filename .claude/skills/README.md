# Skills

Reusable playbooks for common AI/ML tasks. Each skill defines a structured approach to completing a specific type of work.

## Available Skills

| Skill | File | Description |
|-------|------|-------------|
| EDA to Insight | [eda-to-insight.md](eda-to-insight.md) | Exploratory data analysis workflow |
| Baseline Model | [baseline-model-and-card.md](baseline-model-and-card.md) | Creating baseline models with documentation |
| Experiment Plan | [experiment-plan.md](experiment-plan.md) | Designing ML experiments |
| Forecasting | [forecasting-checklist.md](forecasting-checklist.md) | Time series forecasting approach |
| RAG with Evals | [rag-with-evals.md](rag-with-evals.md) | Building RAG systems with evaluation |
| API Shipping | [api-shipping-checklist.md](api-shipping-checklist.md) | Deploying APIs to production |
| Observability | [observability-starter.md](observability-starter.md) | Setting up monitoring and logging |
| K8s Deploy | [k8s-deploy-checklist.md](k8s-deploy-checklist.md) | Kubernetes deployment (Advanced) |

## Skill Structure

Each skill includes:

1. **Trigger**: When to use this skill
2. **Prerequisites**: What you need before starting
3. **Steps**: Ordered actions to complete
4. **Artifacts**: What you produce
5. **Quality Bar**: Definition of "done well"

## How to Use Skills

### During Planning
Reference skills in your weekly plan:
```
Week 2 tasks:
- Apply "eda-to-insight" skill to dataset
- Use "baseline-model-and-card" for initial model
```

### During Building
Follow the steps in order, checking off as you go.

### During Review
Use the quality bar to assess your work.

## Skill Levels

| Level | Available Skills |
|-------|-----------------|
| Beginner | EDA, Baseline Model, Experiment Plan |
| Intermediate | All above + Forecasting, RAG, API Shipping, Observability |
| Advanced | All above + K8s Deploy |

## Related Documentation

- [docs/skills-playbook.md](../../docs/skills-playbook.md) — User guide
- [commands/catalog.md](../commands/catalog.md) — Commands that use skills

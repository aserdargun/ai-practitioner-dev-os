# Skills Playbook

Reusable playbooks for common AI/ML tasks.

## Overview

Skills are structured approaches to completing specific types of work. Each skill defines:
- **Trigger**: When to use it
- **Steps**: What to do
- **Artifacts**: What to produce
- **Quality Bar**: What "done well" looks like

For detailed skill definitions, see [.claude/skills/](../.claude/skills/).

---

## Available Skills

### Foundation Skills (All Levels)

| Skill | Purpose | Time |
|-------|---------|------|
| [EDA to Insight](../.claude/skills/eda-to-insight.md) | Exploratory data analysis | 2-4 hrs |
| [Baseline Model](../.claude/skills/baseline-model-and-card.md) | Create baseline with documentation | 1-3 hrs |
| [Experiment Plan](../.claude/skills/experiment-plan.md) | Design ML experiments | 1-2 hrs |

### Intermediate Skills

| Skill | Purpose | Time |
|-------|---------|------|
| [Forecasting](../.claude/skills/forecasting-checklist.md) | Time series forecasting | 3-6 hrs |
| [RAG with Evals](../.claude/skills/rag-with-evals.md) | Build RAG systems | 4-8 hrs |
| [API Shipping](../.claude/skills/api-shipping-checklist.md) | Deploy production APIs | 2-4 hrs |
| [Observability](../.claude/skills/observability-starter.md) | Set up monitoring | 2-4 hrs |

### Advanced Skills

| Skill | Purpose | Time |
|-------|---------|------|
| [K8s Deploy](../.claude/skills/k8s-deploy-checklist.md) | Kubernetes deployment | 3-6 hrs |

---

## How to Use Skills

### 1. Identify the Right Skill

Check the trigger conditions:

```markdown
**Trigger**: Use this skill when:
- Starting a new project with unfamiliar data
- Preparing data for modeling
- Investigating data quality issues
```

### 2. Check Prerequisites

Before starting:

```markdown
**Prerequisites**:
- [ ] Data loaded into pandas DataFrame
- [ ] Basic understanding of the domain
- [ ] Jupyter notebook ready
```

### 3. Follow the Steps

Work through each step in order:

```markdown
### Step 1: Initial Assessment (15 min)
[actions]

### Step 2: Missing Values (10 min)
[actions]

...
```

### 4. Produce Artifacts

Create the specified outputs:

```markdown
**Artifacts**:
- `eda_notebook.ipynb`
- `data_profile.md`
- `quality_report.md`
```

### 5. Check Quality Bar

Verify your work meets standards:

```markdown
**Quality Bar**:
- [ ] All columns explored
- [ ] Visualizations labeled
- [ ] Findings documented
- [ ] Quality issues cataloged
```

---

## Skill Summaries

### EDA to Insight

Transform raw data into actionable insights.

**Key Steps**:
1. Initial assessment (shape, types)
2. Missing value analysis
3. Univariate analysis (distributions)
4. Bivariate analysis (correlations)
5. Data quality checks
6. Synthesize insights

**Artifacts**: Notebook, data profile, quality report

### Baseline Model and Card

Create a simple baseline with proper documentation.

**Key Steps**:
1. Define baseline approach
2. Prepare data (train/test split)
3. Train simple model
4. Evaluate and document
5. Create model card
6. Save artifacts

**Artifacts**: Model file, metrics, model card

### Experiment Plan

Design structured ML experiments.

**Key Steps**:
1. Define hypotheses
2. Design experiments
3. Set up tracking
4. Run experiments
5. Analyze results
6. Document decisions

**Artifacts**: Plan doc, experiment logs, results summary

### Forecasting Checklist

Build reliable time series forecasting.

**Key Steps**:
1. Time series EDA
2. Create validation strategy
3. Establish baselines
4. Feature engineering
5. Model selection
6. Evaluation
7. Production considerations

**Artifacts**: Notebook, model, forecast card

### RAG with Evals

Build RAG systems with proper evaluation.

**Key Steps**:
1. Document preparation
2. Create embeddings
3. Build retrieval
4. Build generation
5. Create evaluation dataset
6. Evaluate retrieval
7. Evaluate generation
8. Document results

**Artifacts**: RAG components, golden set, eval results

### API Shipping Checklist

Deploy production-ready APIs.

**Key Steps**:
1. Structure API
2. Define contracts
3. Implement endpoints
4. Write tests
5. Containerize
6. Production checklist
7. Deploy
8. Verify

**Artifacts**: API code, tests, Dockerfile, docs

### Observability Starter

Set up monitoring and logging.

**Key Steps**:
1. Define key metrics
2. Add structured logging
3. Instrument with metrics
4. Set up tracing (optional)
5. Create dashboard
6. Configure alerts
7. Document runbook

**Artifacts**: Logging config, metrics, dashboard, runbook

### K8s Deploy Checklist

Deploy to Kubernetes (Advanced only).

**Key Steps**:
1. Create deployment
2. Create service
3. Create ConfigMap
4. Create secrets
5. Configure ingress
6. Set up HPA
7. Deploy
8. Production checklist

**Artifacts**: K8s manifests, docs

---

## Skills by Month

Suggested skill usage for intermediate curriculum:

| Month | Skills |
|-------|--------|
| 1-2 | EDA to Insight, Baseline Model |
| 3-4 | Experiment Plan, Forecasting |
| 5-6 | RAG with Evals |
| 7-8 | API Shipping |
| 9-10 | Observability |
| 11-12 | Integration projects |

---

## Related Documentation

- [.claude/skills/README.md](../.claude/skills/README.md) — Skills system overview
- [.claude/skills/*.md](../.claude/skills/) — Individual skill definitions
- [commands.md](commands.md) — Commands that use skills
- [how-to-use.md](how-to-use.md) — Overall workflow

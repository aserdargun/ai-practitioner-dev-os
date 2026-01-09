# Skills Playbook

Practical playbooks for common AI/ML tasks.

## Overview

Skills are step-by-step guides for completing specific tasks. Each skill provides a repeatable process with quality gates.

## Available Skills

| Skill | Purpose | Level |
|-------|---------|-------|
| [EDA to Insight](#eda-to-insight) | Explore data, extract insights | All |
| [Baseline Model](#baseline-model-and-card) | Create baseline with documentation | All |
| [Experiment Plan](#experiment-plan) | Design and track experiments | All |
| [Forecasting Checklist](#forecasting-checklist) | Time series forecasting | Intermediate+ |
| [RAG with Evals](#rag-with-evals) | Build RAG system with evaluation | Intermediate+ |
| [API Shipping Checklist](#api-shipping-checklist) | Ship production APIs | Intermediate+ |
| [Observability Starter](#observability-starter) | Set up monitoring | Intermediate+ |
| [K8s Deploy Checklist](#k8s-deploy-checklist) | Deploy to Kubernetes | **Advanced only** |

## How to Use Skills

### 1. Identify the Task

Match your current task to a skill:
- "Exploring new dataset" → EDA to Insight
- "Building RAG system" → RAG with Evals
- "Shipping an API" → API Shipping Checklist

### 2. Follow the Steps

Each skill has numbered steps. Work through them in order.

### 3. Meet the Quality Bar

Each skill defines minimum requirements. Don't skip these.

### 4. Produce Artifacts

Skills specify what outputs to create. Keep them organized.

## Skill Summaries

### EDA to Insight

**When**: Starting with a new dataset.

**Steps**:
1. Load and inspect
2. Check data quality
3. Univariate analysis
4. Bivariate analysis
5. Generate insights

**Artifacts**: `eda_notebook.ipynb`, `eda_insights.md`, visualizations

**Full guide**: [.claude/skills/eda-to-insight.md](../.claude/skills/eda-to-insight.md)

### Baseline Model and Card

**When**: Starting an ML project.

**Steps**:
1. Define the problem
2. Prepare data
3. Create naive baseline
4. Train simple model
5. Error analysis
6. Save model
7. Create model card

**Artifacts**: `baseline_model.joblib`, `model_card.md`

**Full guide**: [.claude/skills/baseline-model-and-card.md](../.claude/skills/baseline-model-and-card.md)

### Experiment Plan

**When**: Testing hypotheses or comparing approaches.

**Steps**:
1. Define hypothesis
2. Design experiment
3. Set up tracking
4. Run control
5. Run treatment
6. Analyze results
7. Document findings

**Artifacts**: `experiments.jsonl`, `experiment_results.md`

**Full guide**: [.claude/skills/experiment-plan.md](../.claude/skills/experiment-plan.md)

### Forecasting Checklist

**When**: Building time series models.

**Level**: Intermediate+

**Steps**:
1. Data preparation
2. Exploratory analysis
3. Stationarity check
4. Train/test split
5. Baseline models
6. ARIMA/SARIMA
7. Evaluate and visualize
8. Document results

**Artifacts**: `forecast_model.pkl`, `forecast_report.md`

**Full guide**: [.claude/skills/forecasting-checklist.md](../.claude/skills/forecasting-checklist.md)

### RAG with Evals

**When**: Building retrieval-augmented generation systems.

**Level**: Intermediate+

**Steps**:
1. Document preparation
2. Chunking strategy
3. Embedding generation
4. Vector store setup
5. Retrieval function
6. Answer generation
7. Create evaluation dataset
8. Evaluation metrics
9. Document results

**Artifacts**: `rag/`, `eval/golden_set.jsonl`, `rag_report.md`

**Full guide**: [.claude/skills/rag-with-evals.md](../.claude/skills/rag-with-evals.md)

### API Shipping Checklist

**When**: Shipping a production API.

**Level**: Intermediate+

**Checklist categories**:
1. Functionality
2. Security
3. Documentation
4. Testing
5. Observability
6. Performance
7. Deployment
8. Operations

**Artifacts**: Working API, OpenAPI docs, Dockerfile

**Full guide**: [.claude/skills/api-shipping-checklist.md](../.claude/skills/api-shipping-checklist.md)

### Observability Starter

**When**: Setting up monitoring for a service.

**Level**: Intermediate+

**Steps**:
1. Structured logging
2. Request ID tracking
3. Health endpoints
4. Basic metrics
5. Error tracking
6. Key metrics
7. Dashboard setup
8. Alerting rules

**Artifacts**: Logging config, `/health`, `/metrics`

**Full guide**: [.claude/skills/observability-starter.md](../.claude/skills/observability-starter.md)

### K8s Deploy Checklist

**When**: Deploying to Kubernetes.

**Level**: ⚠️ **Advanced only**

**Prerequisites**:
- Docker knowledge
- Basic K8s concepts
- kubectl configured

**Checklist**:
1. Container ready
2. K8s manifests
3. Resource configuration
4. Health probes
5. Scaling configuration
6. Ingress (if needed)

**Artifacts**: `k8s/*.yaml`, deployment runbook

**Full guide**: [.claude/skills/k8s-deploy-checklist.md](../.claude/skills/k8s-deploy-checklist.md)

## Using Skills with Agents

The Builder agent references skills automatically:

```
/start-week

Builder: "For the RAG task, I'll follow the RAG with Evals skill.
         Starting with Step 1: Document Preparation..."
```

You can also request explicitly:
```
"Use the API Shipping Checklist for this FastAPI service"
```

## Creating Your Own Skills

1. Create a new `.md` file in `.claude/skills/`
2. Follow the structure:
   - Trigger
   - Prerequisites
   - Steps
   - Artifacts
   - Quality bar
   - Common pitfalls

3. Update this playbook with a summary
4. Test the skill on a real project

## Quality Bars

Every skill defines minimum quality requirements. Examples:

| Skill | Quality Bar |
|-------|-------------|
| EDA | 3+ insights with data |
| Baseline | Beat naive baseline |
| RAG | Hits@5 > 70% |
| API | 0 critical security issues |

Don't skip quality bars - they ensure your work is production-worthy.

## Skill Files Location

All skills are in `.claude/skills/`:
```
.claude/skills/
├── README.md
├── eda-to-insight.md
├── baseline-model-and-card.md
├── experiment-plan.md
├── forecasting-checklist.md
├── rag-with-evals.md
├── api-shipping-checklist.md
├── observability-starter.md
└── k8s-deploy-checklist.md
```

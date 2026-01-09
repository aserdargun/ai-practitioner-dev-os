# Skills Playbook

Guide to using skill playbooks for common AI/ML tasks.

## What Are Skills?

Skills are step-by-step guides for completing specific technical tasks. Each skill includes:
- **Trigger**: When to use it
- **Steps**: Detailed process
- **Artifacts**: What gets produced
- **Quality Bar**: How to know you did it well

Skills live in: [.claude/skills/](../.claude/skills/)

---

## Available Skills

### Tier 1 (Beginner)

| Skill | File | Description |
|-------|------|-------------|
| EDA to Insight | [eda-to-insight.md](../.claude/skills/eda-to-insight.md) | Exploratory data analysis workflow |
| Baseline Model | [baseline-model-and-card.md](../.claude/skills/baseline-model-and-card.md) | Create first model with documentation |
| Experiment Plan | [experiment-plan.md](../.claude/skills/experiment-plan.md) | Design and track experiments |
| Forecasting | [forecasting-checklist.md](../.claude/skills/forecasting-checklist.md) | Time series forecasting workflow |

### Tier 2 (Intermediate)

| Skill | File | Description |
|-------|------|-------------|
| RAG with Evals | [rag-with-evals.md](../.claude/skills/rag-with-evals.md) | Build RAG system with evaluation |
| API Shipping | [api-shipping-checklist.md](../.claude/skills/api-shipping-checklist.md) | Deploy production API |
| Observability | [observability-starter.md](../.claude/skills/observability-starter.md) | Add logging and monitoring |

### Tier 3 (Advanced)

| Skill | File | Description |
|-------|------|-------------|
| K8s Deploy | [k8s-deploy-checklist.md](../.claude/skills/k8s-deploy-checklist.md) | Kubernetes deployment |

---

## How to Use Skills

### 1. Direct Reference
Read the skill file and follow the steps:
```
Read .claude/skills/eda-to-insight.md and help me do EDA on my sales data
```

### 2. Via Commands
Some commands invoke skills automatically:
- Building a model? Uses baseline-model-and-card
- Deploying an API? Uses api-shipping-checklist

### 3. With Claude Assistance
Ask Claude to guide you through a skill:
```
Guide me through the EDA to Insight skill for my customer dataset
```

---

## Skill Summaries

### EDA to Insight

**When**: Starting a new data project or receiving new data.

**Steps**:
1. First Look (shape, types, head)
2. Missing Data Analysis
3. Univariate Analysis (distributions)
4. Bivariate Analysis (correlations)
5. Time Patterns (if applicable)
6. Synthesize Insights

**Artifacts**:
- EDA notebook
- Summary document
- Key visualizations

---

### Baseline Model and Card

**When**: Starting an ML project, need a benchmark.

**Steps**:
1. Define the Problem
2. Prepare Data (split, preprocess)
3. Choose Baseline (simple model)
4. Train Baseline
5. Evaluate (multiple metrics)
6. Document in Model Card

**Artifacts**:
- Saved model
- Training notebook
- Model card

---

### Experiment Plan

**When**: Iterating beyond baseline, comparing approaches.

**Steps**:
1. Define Hypothesis
2. Create Tracking Table
3. Set Up Experiment Code
4. Run with Controls
5. Analyze Results
6. Document Learnings

**Artifacts**:
- Experiment plan
- Results log
- Comparison table

---

### Forecasting Checklist

**When**: Predicting future values (sales, demand, etc.).

**Steps**:
1. Time Series EDA
2. Stationarity Check
3. Decomposition
4. Train/Test Split (time-based!)
5. Baseline Forecast
6. Model Selection
7. Evaluation
8. Document

**Artifacts**:
- Forecasting notebook
- Model file
- Forecast summary

---

### RAG with Evals

**When**: Building Q&A over documents, knowledge base.

**Steps**:
1. Prepare Documents
2. Chunk Documents
3. Create Embeddings
4. Index in Vector Store
5. Build RAG Pipeline
6. Create Golden Set
7. Evaluate System
8. Iterate

**Artifacts**:
- RAG code (ingest, retrieve, answer)
- Golden set
- Evaluation results

---

### API Shipping Checklist

**When**: Deploying a REST API to production.

**Steps**:
1. Define API Contract
2. Implement Endpoints
3. Add Validation
4. Add Error Handling
5. Add Logging
6. Write Tests
7. Create Dockerfile
8. Pre-Deploy Checklist
9. Deploy

**Artifacts**:
- API source code
- Tests
- Dockerfile
- Documentation

---

### Observability Starter

**When**: Need visibility into production application.

**Steps**:
1. Structured Logging
2. Request Logging Middleware
3. Application Metrics
4. Health Checks
5. Error Tracking
6. (Optional) Distributed Tracing
7. Dashboard Setup

**Artifacts**:
- Logging configuration
- Metrics endpoint
- Health endpoints

---

### K8s Deploy Checklist (Advanced)

**When**: Deploying to Kubernetes.

**Steps**:
1. Verify Container Works
2. Create Deployment Manifest
3. Create Service
4. Create ConfigMap/Secrets
5. Create Ingress (optional)
6. Create HPA
7. Deploy
8. Verify
9. Pre-Production Checklist

**Artifacts**:
- Kubernetes manifests
- Deployment commands

---

## Skill Chaining

Complex projects often use multiple skills in sequence:

### Data Project
```
EDA to Insight → Baseline Model → Experiment Plan
```

### ML API
```
Baseline Model → API Shipping → Observability
```

### RAG Application
```
RAG with Evals → API Shipping → Observability
```

---

## Creating Custom Skills

1. Create new `.md` file in `.claude/skills/`
2. Follow the template structure:

```markdown
# Skill: [Name]

## Trigger
When to use this skill

## Prerequisites
What you need before starting

## Steps
1. First step
2. Second step
...

## Artifacts Produced
- Output 1
- Output 2

## Quality Bar
- [ ] Criteria 1
- [ ] Criteria 2

## Common Pitfalls
- Pitfall 1 and how to avoid

## Example
Real example of this skill
```

---

## Tips

1. **Follow the steps**: Skills are designed as sequences — don't skip steps
2. **Check the quality bar**: Use the checklist to verify you're done
3. **Avoid pitfalls**: Read the common pitfalls section before starting
4. **Adapt as needed**: Skills are guides, not rigid rules
5. **Document as you go**: Fill in artifacts during the process, not after

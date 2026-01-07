# Skills Playbook

Skills are step-by-step playbooks for common AI/ML tasks. This guide summarizes available skills and when to use them.

For complete skill details, see [.claude/skills/](../.claude/skills/).

## Available Skills

| Skill | Tier | Best For |
|-------|------|----------|
| [EDA to Insight](#eda-to-insight) | 1 | Starting any data project |
| [Baseline Model and Card](#baseline-model-and-card) | 1 | First model on a problem |
| [Experiment Plan](#experiment-plan) | 1 | Systematic improvement |
| [Forecasting Checklist](#forecasting-checklist) | 1 | Time series problems |
| [RAG with Evals](#rag-with-evals) | 1-2 | Q&A over documents |
| [API Shipping Checklist](#api-shipping-checklist) | 1-2 | Deploying services |
| [Observability Starter](#observability-starter) | 2 | Production monitoring |
| [K8s Deploy Checklist](#k8s-deploy-checklist) | 3 | Kubernetes deployment |

## Skill Structure

Every skill follows the same structure:

1. **Trigger**: When to use this skill
2. **Prerequisites**: What you need first
3. **Steps**: Numbered, actionable steps
4. **Artifacts**: What you'll produce
5. **Quality Bar**: How to know you're done

## Skills by Learning Phase

### Starting a Project

1. **EDA to Insight** - Understand your data
2. **Baseline Model and Card** - Get a working baseline
3. **Experiment Plan** - Plan improvements

### Building Features

4. **Forecasting Checklist** - For time series
5. **RAG with Evals** - For document Q&A

### Going to Production

6. **API Shipping Checklist** - Deploy your service
7. **Observability Starter** - Add monitoring
8. **K8s Deploy Checklist** - Scale on Kubernetes

---

## EDA to Insight

**Tier**: 1 (Beginner)

**Use When**: Starting any data project, received new dataset

**Steps Summary**:
1. Load and inspect data
2. Check data quality (missing, duplicates)
3. Univariate analysis (distributions)
4. Bivariate analysis (correlations)
5. Document insights

**Artifacts**:
- Jupyter notebook with analysis
- EDA summary document
- Key visualizations
- Data quality issues list

**Quality Bar**:
- All columns inspected
- Missing values quantified
- Summary document written
- Next steps defined

[Full skill: .claude/skills/eda-to-insight.md](../.claude/skills/eda-to-insight.md)

---

## Baseline Model and Card

**Tier**: 1 (Beginner)

**Use When**: EDA complete, ready for first model

**Steps Summary**:
1. Prepare data (train/test split)
2. Choose baseline model
3. Train and evaluate
4. Create model card
5. Save artifacts

**Artifacts**:
- Trained baseline model (.joblib)
- Metrics JSON file
- Model card (markdown)
- Training notebook

**Quality Bar**:
- Model trained on train set only
- Evaluated on held-out test set
- Model card complete
- Can reproduce results

[Full skill: .claude/skills/baseline-model-and-card.md](../.claude/skills/baseline-model-and-card.md)

---

## Experiment Plan

**Tier**: 1 (Beginner)

**Use When**: Baseline complete, want to improve

**Steps Summary**:
1. Define success criteria
2. Generate hypotheses
3. Prioritize experiments
4. Design protocol
5. Create experiment template
6. Document plan

**Artifacts**:
- Experiment plan document
- Prioritized hypothesis list
- Experiment template code
- Tracking spreadsheet

**Quality Bar**:
- Success criteria measurable
- Hypotheses testable
- Protocol prevents leakage
- Template ready to use

[Full skill: .claude/skills/experiment-plan.md](../.claude/skills/experiment-plan.md)

---

## Forecasting Checklist

**Tier**: 1 (Beginner)

**Use When**: Time series prediction problem

**Steps Summary**:
1. Prepare time series data
2. Visualize and decompose
3. Check stationarity
4. Train-test split (chronological!)
5. Build baseline forecasts
6. Build statistical model
7. Document results

**Artifacts**:
- Cleaned time series
- Decomposition visualization
- Trained forecasting model
- Model comparison table

**Quality Bar**:
- Data properly indexed
- Split is chronological
- Model beats naive baseline
- Forecast horizon defined

[Full skill: .claude/skills/forecasting-checklist.md](../.claude/skills/forecasting-checklist.md)

---

## RAG with Evals

**Tier**: 1-2 (Beginner to Intermediate)

**Use When**: Building Q&A over documents

**Steps Summary**:
1. Set up environment
2. Load and chunk documents
3. Create vector store
4. Build RAG chain
5. Create evaluation dataset
6. Run evaluation
7. Document results

**Artifacts**:
- Vector store
- RAG chain code
- Golden evaluation set
- Evaluation script
- Results documentation

**Quality Bar**:
- RAG answers correctly
- Retrieval returns relevant chunks
- Evaluation set has 10+ examples
- Failure cases analyzed

[Full skill: .claude/skills/rag-with-evals.md](../.claude/skills/rag-with-evals.md)

---

## API Shipping Checklist

**Tier**: 1-2 (Beginner to Intermediate)

**Use When**: Ready to deploy a service

**Steps Summary**:
1. Set up FastAPI project
2. Define request/response models
3. Add prediction endpoint
4. Add input validation
5. Add error handling
6. Write tests
7. Create Dockerfile
8. Document API

**Artifacts**:
- FastAPI application
- Pydantic models
- Tests (passing)
- Dockerfile
- README with usage

**Quality Bar**:
- Health check returns 200
- Prediction endpoint works
- Input validation catches bad requests
- Docker builds successfully

[Full skill: .claude/skills/api-shipping-checklist.md](../.claude/skills/api-shipping-checklist.md)

---

## Observability Starter

**Tier**: 2 (Intermediate)

**Use When**: Deploying to production

**Steps Summary**:
1. Set up structured logging
2. Add request logging middleware
3. Add application metrics
4. Add health checks
5. Add error tracking
6. Create dashboard config
7. Document observability

**Artifacts**:
- Logging configuration
- Request logging middleware
- Prometheus metrics
- Health check endpoints
- Dashboard configuration

**Quality Bar**:
- All requests logged
- Metrics exposed at /metrics
- Health check covers dependencies
- Errors logged with context

[Full skill: .claude/skills/observability-starter.md](../.claude/skills/observability-starter.md)

---

## K8s Deploy Checklist

**Tier**: 3 (Advanced)

> ⚠️ This skill is for Advanced learners only.

**Use When**: Need container orchestration at scale

**Steps Summary**:
1. Create Deployment manifest
2. Add health probes
3. Create Service
4. Configure Ingress
5. Add ConfigMap and Secrets
6. Set up HPA
7. Deploy and verify
8. Document deployment

**Artifacts**:
- Deployment manifest
- Service manifest
- Ingress manifest
- HPA configuration
- Deployment documentation

**Quality Bar**:
- Pods running and healthy
- Service accessible
- Auto-scaling working
- Rollback tested

[Full skill: .claude/skills/k8s-deploy-checklist.md](../.claude/skills/k8s-deploy-checklist.md)

---

## Using Skills Effectively

### 1. Check Prerequisites

Before starting a skill, verify you have:
- Required data/inputs
- Tools installed
- Previous skills completed (if dependent)

### 2. Follow Steps In Order

Skills are designed to build on each step:
- Don't skip steps
- Check off as you complete
- Ask for help if stuck

### 3. Verify Quality Bar

Use the quality bar to confirm:
- All artifacts produced
- Quality criteria met
- Ready for next skill

### 4. Combine with Commands

```
# Before starting a skill
/status           # Check where you are

# While working on a skill
/debug-learning   # If stuck

# After completing a skill
/evaluate         # Check progress
/add-best-practice  # Capture learnings
```

## Tier Gating

Skills are gated by tier for your current level:

**Beginner (Tier 1)**:
- EDA to Insight ✓
- Baseline Model and Card ✓
- Experiment Plan ✓
- Forecasting Checklist ✓

**Intermediate (adds Tier 2)**:
- RAG with Evals ✓
- API Shipping Checklist ✓
- Observability Starter ✓

**Advanced (adds Tier 3)**:
- K8s Deploy Checklist ✓

Focus on mastering Tier 1 skills before moving to Tier 2.

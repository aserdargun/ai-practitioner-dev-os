# Month 08: Cloud & MLOps

## Why It Matters

ML models need to run somewhere. This month teaches cloud deployment, MLOps practices, and production infrastructure—skills that turn experiments into business value.

**Job Relevance**: MLOps Engineer is one of the fastest-growing roles. Companies need people who can deploy and maintain ML systems at scale.

---

## Prerequisites

- Month 01-07 completed
- Docker proficiency
- API development experience

---

## Learning Goals

### Tier 1 Focus
- Cloud fundamentals
- DevOps basics
- CI/CD concepts

### Tier 2 Focus
- AWS/Azure/GCP services
- MLflow for model registry
- GitHub Actions pipelines
- Monitoring with Prometheus/Grafana
- S3/Blob storage
- Lambda/Azure Functions

### Tier 3 Focus
- Kubernetes introduction
- Infrastructure as Code concepts
- Advanced monitoring
- Cost optimization

---

## Main Project: Cloud ML Platform

Build an MLOps platform that:
1. Trains models in the cloud
2. Registers models in MLflow
3. Deploys automatically via CI/CD
4. Monitors predictions and drift
5. Scales based on demand

### Deliverables

1. **`training/`** - Cloud training scripts
2. **`deployment/`** - Deployment configurations
3. **`monitoring/`** - Observability setup
4. **`pipelines/`** - CI/CD workflows
5. **`infrastructure/`** - IaC templates
6. **`docs/`** - Architecture documentation

### Definition of Done

- [ ] Training runs in cloud (SageMaker/Vertex/Azure ML)
- [ ] Model registry with MLflow
- [ ] CI/CD deploys on merge
- [ ] Health monitoring in place
- [ ] Basic alerting configured
- [ ] Documentation complete

---

## Week-by-Week Plan

### Week 1: Cloud Fundamentals

**Focus**: Understand cloud services.

- Cloud provider comparison (AWS/Azure/GCP)
- Compute services (EC2, VMs)
- Storage services (S3, Blob)
- IAM and security basics
- Cost awareness

**Milestone**: Basic cloud resources provisioned.

### Week 2: ML Training in Cloud

**Focus**: Train at scale.

- SageMaker/Vertex AI/Azure ML
- Data in cloud storage
- Distributed training basics
- GPU instances
- Cost optimization

**Milestone**: Model training in cloud with MLflow tracking.

### Week 3: CI/CD for ML

**Focus**: Automate everything.

- GitHub Actions for ML
- Testing ML code
- Model validation in CI
- Automated deployment
- Environment management

**Milestone**: CI/CD pipeline for model deployment.

### Week 4: Monitoring & Operations

**Focus**: Keep it running.

- Prometheus metrics
- Grafana dashboards
- Log aggregation
- Alerting setup
- Incident response basics

**Milestone**: Complete observability stack.

---

## Stretch Goals

- Add A/B testing infrastructure
- Implement canary deployments
- Add data drift detection
- Build model performance dashboard
- Implement automated retraining

---

## Claude Prompts

### Planning
```
/plan-week
```

### Cloud Selection
```
As the Researcher, compare AWS SageMaker vs Azure ML vs Vertex AI for my use case.
```

### Observability Setup
```
Use the Observability Starter skill for my ML service.
```

### CI/CD Review
```
/harden

Review my GitHub Actions pipeline for best practices.
```

### Architecture Review
```
As the Reviewer, evaluate my MLOps architecture for production readiness.
```

---

## How to Publish

### Demo Script
```bash
# Show the end-to-end flow
git push origin main  # Triggers CI/CD
# Wait for deployment
curl https://your-api.com/predict -d '{"features": [...]}'
# Show monitoring dashboard
```

### Write-Up Topics
- Building an MLOps platform
- Cloud ML service comparison
- CI/CD for machine learning
- Monitoring ML systems in production

---

## Resources

- [AWS SageMaker Docs](https://docs.aws.amazon.com/sagemaker/)
- [Azure ML Documentation](https://docs.microsoft.com/azure/machine-learning/)
- [MLflow Documentation](https://mlflow.org/docs/latest/)
- [GitHub Actions for ML](https://docs.github.com/actions)
- Skill: `.claude/skills/observability-starter.md`

---

## Month Evaluation

At month end, run:
```bash
python .claude/path-engine/evaluate.py --month 8
```

# Month 08: MLOps Foundations

**Focus**: Build reproducible ML pipelines with proper tracking and orchestration.

---

## Why It Matters

MLOps transforms ML projects from one-off experiments to sustainable systems. Understanding pipelines, experiment tracking, and automation is essential for ML engineers working on production systems.

**Job Relevance**: Core ML engineering skill; differentiates senior from junior practitioners.

---

## Prerequisites

- Month 01-07 complete
- Docker experience
- CI/CD basics

---

## Learning Goals

**Tier 2 Technologies**:
- MLflow (experiment tracking, model registry)
- Airflow (workflow orchestration)
- dbt (data transformation)
- CI/CD for ML

**Skills**:
- Pipeline design
- Experiment tracking
- Model versioning
- Data versioning concepts

---

## Main Project: End-to-End ML Pipeline

Build a complete ML pipeline from data ingestion to model serving.

### Deliverables

1. **Data Pipeline** with validation
2. **Training Pipeline** with experiment tracking
3. **Model Registry** integration
4. **Orchestration** with Airflow
5. **GitHub Repository** with CI/CD

### Definition of Done

- [ ] Data ingestion pipeline working
- [ ] Data validation implemented
- [ ] Training script with MLflow tracking
- [ ] Experiments logged with metrics/params
- [ ] Model registered in MLflow
- [ ] Airflow DAG orchestrates pipeline
- [ ] Pipeline runs on schedule
- [ ] CI pipeline validates changes
- [ ] Documentation complete
- [ ] Can retrain and deploy new model version

---

## Stretch Goals

- [ ] Data versioning with DVC
- [ ] A/B model testing
- [ ] Automated retraining triggers
- [ ] Model monitoring setup

---

## Weekly Cadence

### Week 1: Data Pipeline
- Data ingestion script
- Data validation
- Feature engineering pipeline
- Store processed data

### Week 2: Training Pipeline
- MLflow setup
- Training with tracking
- Model registration
- Experiment comparison

### Week 3: Orchestration
- Airflow setup
- Create DAG
- Connect pipeline stages
- Add error handling

### Week 4: Polish & Ship
- CI integration
- Documentation
- Demo and write-up
- Retrospective

---

## Claude Prompts

### Planning
```
/plan-week

Starting Month 8 on MLOps. I want to build a retraining pipeline for my classifier.
Help me plan the MLflow and Airflow integration.
```

### Building
```
/ship-mvp

My pipeline has:
- Data ingestion DAG
- MLflow experiment tracking
- Model registration
What's missing for a complete MLOps setup?
```

### Review
```
/harden

Review my MLOps pipeline for:
- Pipeline reliability
- Error handling
- Monitoring gaps
- Documentation
```

### Research
```
Researcher, compare Airflow vs Prefect vs Dagster for ML pipelines.
Which is best for a small team getting started?
```

---

## How to Publish

### Demo
- Show pipeline execution
- Demonstrate MLflow UI
- Show Airflow DAG

### Write-up
- "From Notebooks to Pipelines: My MLOps Journey"
- Include architecture diagram
- Share pipeline design decisions

---

## Resources

### Templates
- [Data Pipeline Template](../../../templates/template-data-pipeline/)

### Documentation
- [MLflow Documentation](https://mlflow.org/docs/latest/)
- [Airflow Documentation](https://airflow.apache.org/docs/)
- [dbt Documentation](https://docs.getdbt.com/)

---

## Next Month Preview

**Month 09**: Cloud Deployment — Deploy ML systems to AWS, Azure, or GCP.

# Month 02: ML Fundamentals

**Focus**: Build and evaluate machine learning models with scikit-learn.

---

## Why It Matters

Machine learning fundamentals are essential for any AI practitioner. Understanding how to train, evaluate, and compare models is the core skill for data scientists and ML engineers. This month bridges data analysis with predictive modeling.

**Job Relevance**: Core requirement for data science and ML engineering roles.

---

## Prerequisites

- Month 01 complete (Python, Pandas, visualization)
- Basic statistics understanding
- Familiarity with train/test concepts

---

## Learning Goals

**Tier 1 Technologies**:
- scikit-learn (ML algorithms)
- KNN, Naive Bayes, SVM
- Decision Forests, Boosting
- Statistics, Probability
- Experimental Design

**Tier 2 Technologies**:
- XGBoost, LightGBM, CatBoost
- MLflow (experiment tracking)

**Skills**:
- Model training and evaluation
- Feature engineering basics
- Cross-validation
- Hyperparameter tuning

---

## Main Project: Classification Pipeline

Build an end-to-end classification pipeline with proper evaluation.

### Deliverables

1. **Classification Notebook** with multiple models
2. **Model Card** documenting the best model
3. **Evaluation Report** with metrics and analysis
4. **GitHub Repository** with reproducible code

### Definition of Done

- [ ] Dataset prepared with proper train/test split
- [ ] At least 5 different models trained
- [ ] Baseline model established
- [ ] Cross-validation performed
- [ ] Hyperparameter tuning attempted
- [ ] Model comparison table created
- [ ] Best model selected with justification
- [ ] Model card written
- [ ] Experiment tracking set up (MLflow)
- [ ] Code is clean and reproducible

---

## Stretch Goals

- [ ] Feature importance analysis
- [ ] Learning curves plotted
- [ ] Ensemble model created
- [ ] Model saved and loadable

---

## Weekly Cadence

### Week 1: Data Prep & Baseline
- Select classification dataset
- Prepare features and target
- Train baseline model
- Set up MLflow tracking

### Week 2: Model Exploration
- Train multiple model types
- Compare performance
- Apply cross-validation

### Week 3: Optimization
- Hyperparameter tuning
- Feature engineering
- Model selection

### Week 4: Document & Ship
- Write model card
- Create evaluation report
- Demo and write-up
- Retrospective

---

## Claude Prompts

### Planning
```
/plan-week

Starting Month 2 on ML fundamentals. I want to focus on classification.
Help me plan with dataset selection and baseline setup.
```

### Building
```
/ship-mvp

I've trained 5 models on my dataset. Here are the results:
- Logistic Regression: 0.82 accuracy
- Random Forest: 0.87 accuracy
- XGBoost: 0.89 accuracy
...
Am I ready for MVP? What should I focus on next?
```

### Review
```
/harden

Review my ML pipeline for:
- Data leakage risks
- Proper evaluation methodology
- Code quality
```

### Evaluation
```
/evaluate

Evaluate my Month 2 deliverables:
- Classification pipeline complete
- Model card written
- MLflow experiments logged
```

---

## How to Publish

### Demo
- Show model training pipeline
- Demonstrate MLflow UI
- Walk through model comparison

### Write-up
- "Comparing ML Algorithms: What I Learned"
- Focus on methodology and decision-making
- Include confusion matrices and metrics

---

## Resources

### Datasets
- [Kaggle Classification Datasets](https://www.kaggle.com/datasets?tags=classification)
- Iris, Titanic, Heart Disease (classics)

### Skill Playbooks
- [Baseline Model and Card](../../../.claude/skills/baseline-model-and-card.md)
- [Experiment Plan](../../../.claude/skills/experiment-plan.md)

### Documentation
- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)

---

## Next Month Preview

**Month 03**: Production APIs — Deploy your model as a FastAPI service.

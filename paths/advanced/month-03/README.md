# Month 03: Classical Machine Learning

## Why It Matters

Classical ML algorithms remain highly effective for many real-world problems. Understanding these foundations makes you a better deep learning practitioner and gives you tools that often outperform neural networks on tabular data.

**Job Relevance**: Many production ML systems use classical algorithms. Companies value practitioners who can choose the right tool for the job.

---

## Prerequisites

- Month 01-02 completed
- Statistics and probability understanding
- Pandas proficiency

---

## Learning Goals

### Tier 1 Focus
- Supervised learning (classification, regression)
- Unsupervised learning (clustering, dimensionality reduction)
- Algorithms: KNN, SVM, Decision Trees, Random Forests
- Boosting: Gradient Boosting fundamentals
- Feature engineering
- Model evaluation metrics

### Tier 2 Focus
- scikit-learn mastery
- XGBoost, LightGBM, CatBoost
- Cross-validation strategies
- Hyperparameter tuning
- MLflow for experiment tracking

### Tier 3 Preview
- When to use classical vs deep learning
- Interpretability and explainability

---

## Main Project: ML Model Pipeline

Build an end-to-end ML pipeline that:
1. Loads and preprocesses data
2. Engineers features
3. Trains multiple models
4. Evaluates and compares performance
5. Tracks experiments with MLflow
6. Serves the best model

### Deliverables

1. **`ml_pipeline/`** - Training and inference code
2. **`features/`** - Feature engineering functions
3. **`models/`** - Saved model artifacts
4. **`experiments/`** - MLflow tracking
5. **`model_card.md`** - Model documentation
6. **`tests/`** - Unit and integration tests

### Definition of Done

- [ ] Data preprocessing pipeline
- [ ] At least 5 different models trained
- [ ] Cross-validation implemented
- [ ] MLflow experiment tracking
- [ ] Model card with evaluation metrics
- [ ] Best model beats baseline by >10%

---

## Week-by-Week Plan

### Week 1: Foundations & Baseline

**Focus**: Establish the baseline.

- Problem framing and success metrics
- Train/test split strategies
- Naive baseline models
- First simple model (logistic regression or linear regression)
- Basic evaluation metrics

**Milestone**: Baseline model established with documented metrics.

### Week 2: Algorithm Zoo

**Focus**: Explore multiple algorithms.

- Decision Trees and Random Forests
- SVMs for classification
- K-Nearest Neighbors
- Gradient Boosting (XGBoost, LightGBM)
- Algorithm selection criteria

**Milestone**: 5 models trained and compared.

### Week 3: Feature Engineering & Tuning

**Focus**: Improve model performance.

- Feature engineering techniques
- Handling categorical variables
- Feature selection methods
- Hyperparameter tuning (GridSearch, RandomSearch)
- Cross-validation strategies

**Milestone**: Best model significantly improved through feature engineering.

### Week 4: MLOps & Documentation

**Focus**: Production readiness.

- MLflow experiment tracking
- Model serialization
- Model card creation
- Testing the ML pipeline
- Documentation

**Milestone**: Complete pipeline with MLflow tracking and model card.

---

## Stretch Goals

- Add SHAP for model interpretability
- Implement AutoML comparison
- Build prediction API endpoint
- Add model monitoring setup
- Create automated retraining pipeline

---

## Claude Prompts

### Planning
```
/plan-week
```

### Baseline Model
```
Use the Baseline Model and Card skill for my classification problem.
```

### Experiment Design
```
Use the Experiment Plan skill to design experiments for model comparison.
```

### Feature Engineering
```
As the Builder, help me engineer features for [problem type].
```

### Model Review
```
/harden

Review my ML pipeline for best practices and potential issues.
```

---

## How to Publish

### Demo Script
```python
# demo.py
from ml_pipeline import load_model, predict

model = load_model("best_model.joblib")
sample = load_sample_input()
prediction = predict(model, sample)
print(f"Prediction: {prediction}")
print(f"Model: {model.name}, Accuracy: {model.accuracy}")
```

### Write-Up Topics
- When to use classical ML vs deep learning
- Feature engineering lessons
- Model comparison insights
- MLflow for experiment tracking

---

## Resources

- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [MLflow Quickstart](https://mlflow.org/docs/latest/quickstart.html)
- Skill: `.claude/skills/baseline-model-and-card.md`
- Skill: `.claude/skills/experiment-plan.md`

---

## Month Evaluation

At month end, run:
```bash
python .claude/path-engine/evaluate.py --month 3
```

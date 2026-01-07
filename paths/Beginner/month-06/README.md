# Month 6: Machine Learning Intermediate

**Focus**: Master ensemble methods and advanced ML techniques

---

## Why It Matters

Ensemble methods often win ML competitions and perform best in production. This month you'll learn:
- Random Forests and boosting
- Hyperparameter tuning
- Feature importance
- Handling imbalanced data

These skills differentiate junior from mid-level practitioners.

---

## Prerequisites

- Month 5 completed
- Comfortable with basic ML workflow
- Understand evaluation metrics

---

## Learning Goals

By the end of this month, you will:

1. **Ensemble Methods**
   - [ ] Random Forest
   - [ ] Gradient Boosting
   - [ ] XGBoost/LightGBM basics
   - [ ] Voting and stacking concepts

2. **Advanced Techniques**
   - [ ] Hyperparameter tuning (Grid/Random search)
   - [ ] Feature selection methods
   - [ ] Handling imbalanced classes
   - [ ] Pipeline construction

3. **Model Interpretation**
   - [ ] Feature importance
   - [ ] Partial dependence plots
   - [ ] SHAP values (intro)

4. **Production Considerations**
   - [ ] Model persistence
   - [ ] Inference optimization
   - [ ] Monitoring considerations

---

## Main Project: Regression Challenge

Build an optimized regression model with proper experimentation.

### Deliverables

1. **Experiment notebook** (`regression_experiments.ipynb`)
   - Baseline model
   - At least 5 experiments
   - Hyperparameter tuning
   - Final model selection

2. **Experiment log** (`experiments.csv`)
   - Track all experiments
   - Hyperparameters used
   - Results achieved

3. **Model artifacts**
   - Saved model file
   - Preprocessing pipeline
   - Config file

4. **Analysis report** (`report.md`)
   - Methodology
   - Results comparison
   - Feature importance analysis
   - Recommendations

### Definition of Done

- [ ] At least 5 documented experiments
- [ ] Hyperparameter tuning performed
- [ ] Best model beats baseline by >10%
- [ ] Feature importance analyzed
- [ ] Model saved and loadable
- [ ] Report complete

### Dataset Suggestions

- [House Prices](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
- [California Housing](https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset)
- [Energy Efficiency](https://archive.ics.uci.edu/ml/datasets/Energy+efficiency)
- Sales forecasting dataset

---

## Stretch Goals

- [ ] Implement stacking ensemble
- [ ] Add SHAP analysis
- [ ] Create feature selection pipeline
- [ ] Optimize for inference speed

---

## Weekly Breakdown

### Week 1: Ensemble Methods
- Random Forest deep dive
- Gradient Boosting concepts
- XGBoost introduction
- Comparing ensemble methods

### Week 2: Tuning & Features
- Grid and random search
- Cross-validation strategies
- Feature selection techniques
- Handling imbalanced data

### Week 3: Interpretation
- Feature importance methods
- Partial dependence plots
- SHAP basics
- Model explainability

### Week 4: Project & Production
- Complete experiments
- Optimize final model
- Save and document
- Production considerations

---

## Claude Prompts

### Start of Month
```
/status

I'm starting Month 6: ML Intermediate.
Help me understand ensemble methods and plan experiments.
```

### Experiment Planning
```
I want to apply the Experiment Plan skill.
Walk me through .claude/skills/experiment-plan.md
for improving my regression model.
```

### Algorithm Deep Dive
```
Explain how [Random Forest / XGBoost / etc] works:
- The algorithm intuition
- Key hyperparameters
- When it works well
- Code example with tuning
```

### Hyperparameter Tuning
```
I'm tuning a [model type] for [problem].
Current best score: [metric]

What hyperparameters should I focus on?
Show me how to set up grid search.
```

### Feature Importance
```
My model's top features are:
1. [feature]: importance [value]
2. [feature]: importance [value]
...

Help me interpret this and decide if I should:
- Remove low-importance features
- Engineer new features
- Investigate interactions
```

### Imbalanced Data
```
My classification problem has:
- Class 0: 9000 samples
- Class 1: 1000 samples

What techniques should I use to handle this?
Show me the code.
```

### Project Review
```
/evaluate

I've completed my regression experiments.
Best model: [model]
RMSE improved from [baseline] to [final].

Review my approach and suggest improvements.
```

---

## How to Publish

### Demo

Showcase your experiments:
1. Problem and baseline
2. Experiment progression
3. Final model performance
4. Feature importance insights

### Write-up

Create a post about:
- Systematic experimentation
- What worked and what didn't
- Hyperparameter tuning insights
- Model interpretation

### Portfolio

- Experiment notebook with clear progression
- Results visualization
- Reproducible experiments

---

## Resources

### Ensemble Methods
- [Random Forests Explained](https://www.stat.berkeley.edu/~breiman/RandomForests/cc_home.htm)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [LightGBM Documentation](https://lightgbm.readthedocs.io/)

### Tuning
- [Hyperparameter Tuning Guide](https://scikit-learn.org/stable/modules/grid_search.html)
- [Optuna](https://optuna.org/) (advanced)

### Interpretation
- [SHAP Documentation](https://shap.readthedocs.io/)
- [Interpretable ML Book](https://christophm.github.io/interpretable-ml-book/)

---

## Next Month

[Month 7: Time Series](../month-07/README.md) - Forecasting and temporal data

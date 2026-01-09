# Month 5: Introduction to Machine Learning

**Theme**: Enter the world of ML with regression and your first predictive models.

## Why It Matters

Machine learning is the core of AI. This month you'll build your first real ML models—the same techniques used in industry. Understanding regression gives you the foundation for all predictive modeling.

## Prerequisites

- Month 3 completed (statistics, especially correlation)
- Month 4 completed (visualization for model analysis)
- Strong pandas skills

## Learning Goals

### ML Fundamentals (Week 1)
- [ ] What is machine learning?
- [ ] Supervised vs unsupervised learning
- [ ] Training vs testing data
- [ ] Overfitting and underfitting
- [ ] Cross-validation basics

### Regression (Week 2-3)
- [ ] Linear regression theory
- [ ] Multiple regression
- [ ] Polynomial regression
- [ ] Regularization (Ridge, Lasso)
- [ ] Evaluation metrics (MSE, RMSE, R²)
- [ ] Feature importance

### Practical ML Workflow (Week 4)
- [ ] Data preparation for ML
- [ ] Feature engineering basics
- [ ] Model selection
- [ ] Hyperparameter tuning
- [ ] Making predictions

## Main Project: House Price Predictor

Build a regression model to predict house prices.

### Dataset
Use the classic Boston Housing or California Housing dataset from sklearn.

### Deliverables
1. ML Pipeline notebook:
   - Data exploration
   - Feature analysis
   - Train/test split
   - Model training
   - Model evaluation

2. Model comparison:
   - Linear Regression
   - Ridge Regression
   - Lasso Regression
   - Compare performance

3. Model Card:
   - What the model predicts
   - Features used
   - Performance metrics
   - Limitations

### Definition of Done
- [ ] Complete ML pipeline
- [ ] 3+ models compared
- [ ] Evaluation metrics calculated
- [ ] Model card written
- [ ] Can explain predictions
- [ ] Code documented

## Stretch Goals

- [ ] Add polynomial features
- [ ] Implement cross-validation
- [ ] Create feature importance plot
- [ ] Try Gradient Boosting preview
- [ ] Deploy as simple API

## Weekly Breakdown

### Week 1: ML Fundamentals
- ML concepts and terminology
- Train/test splits
- Introduction to scikit-learn
- Explore housing dataset

### Week 2: Linear Regression
- Simple linear regression
- Multiple regression
- Evaluation metrics
- Build first model

### Week 3: Advanced Regression
- Regularization
- Feature engineering
- Model comparison
- Improve predictions

### Week 4: Complete Project
- Final model selection
- Model card
- Documentation
- Demo prep

## Claude Prompts

### Planning
```
/plan-week
Month 5 Week 2 - Focus on linear regression
I want to understand regression deeply
```

### Concept Help
```
Ask the Researcher to explain regularization
(Ridge vs Lasso) with practical examples.
When should I use each?
```

### Building
```
Ask the Builder to help me create a scikit-learn
pipeline that includes preprocessing and regression.
Show best practices.
```

### Model Review
```
Ask the Reviewer to review my regression model.
Is there overfitting? Am I evaluating correctly?
```

### Baseline Skill
```
Guide me through the Baseline Model and Card skill
for my house price predictor.
```

## How to Publish

### Demo
1. Show the dataset
2. Explain key features
3. Show model training
4. Compare model performance
5. Make a prediction and explain it

### Write-up Topics
- What affects house prices?
- How regression works
- Model comparison insights
- Lessons learned about ML

### Portfolio Entry
- Jupyter notebook with clear explanations
- Model card
- Visualizations of results

## Resources

### Machine Learning
- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [ML Course by Andrew Ng](https://www.coursera.org/learn/machine-learning)
- [Hands-On ML Book](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/)

### Regression
- [StatQuest: Linear Regression](https://www.youtube.com/watch?v=nk2CQITm_eo)
- [Regularization Explained](https://www.youtube.com/watch?v=Q81RR3yKn30)

### Practice
- [Kaggle Learn ML](https://www.kaggle.com/learn/intro-to-machine-learning)

## Tips

1. **Start simple** — Linear regression before complex models
2. **Understand the data** — EDA before modeling
3. **Check assumptions** — Linear regression has requirements
4. **Cross-validate** — One split isn't enough
5. **Think about features** — Feature engineering often beats complex models

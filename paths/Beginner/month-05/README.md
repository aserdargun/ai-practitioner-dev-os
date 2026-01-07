# Month 5: Machine Learning Basics

**Focus**: Build your first ML models with scikit-learn

---

## Why It Matters

Machine learning is the core skill for AI practitioners. This month you'll learn to:
- Frame problems as ML tasks
- Build and evaluate models
- Avoid common pitfalls
- Understand the ML workflow

Employers expect familiarity with standard ML algorithms and proper evaluation practices.

---

## Prerequisites

- Months 1-4 completed
- Strong pandas skills
- Statistics fundamentals
- Visualization ability

---

## Learning Goals

By the end of this month, you will:

1. **ML Fundamentals**
   - [ ] Supervised vs unsupervised learning
   - [ ] Classification vs regression
   - [ ] Training, validation, test sets
   - [ ] Bias-variance tradeoff

2. **Algorithms**
   - [ ] Linear regression
   - [ ] Logistic regression
   - [ ] K-Nearest Neighbors
   - [ ] Decision trees

3. **Model Evaluation**
   - [ ] Train/test split
   - [ ] Cross-validation
   - [ ] Classification metrics (accuracy, precision, recall, F1)
   - [ ] Regression metrics (MSE, RMSE, R²)

4. **Best Practices**
   - [ ] Feature scaling
   - [ ] Handling categorical variables
   - [ ] Avoiding data leakage
   - [ ] Model selection

---

## Main Project: Classification Model

Build a classification model to predict a binary outcome.

### Deliverables

1. **Analysis notebook** (`classification_project.ipynb`)
   - EDA of the dataset
   - Feature engineering
   - Model training and selection
   - Evaluation and interpretation

2. **Model card** (`model_card.md`)
   - Model description
   - Intended use
   - Training data
   - Performance metrics
   - Limitations

3. **Prediction script** (`predict.py`)
   - Load trained model
   - Make predictions on new data
   - Output results

4. **Tests**
   - Test prediction function
   - Test data preprocessing

### Definition of Done

- [ ] EDA completed and documented
- [ ] At least 3 models compared
- [ ] Best model selected with justification
- [ ] Model card complete
- [ ] Prediction script works
- [ ] Tests pass

### Dataset Suggestions

- [Titanic Survival](https://www.kaggle.com/c/titanic)
- [Heart Disease](https://archive.ics.uci.edu/ml/datasets/heart+disease)
- [Bank Marketing](https://archive.ics.uci.edu/ml/datasets/bank+marketing)
- Customer churn dataset

---

## Stretch Goals

- [ ] Add ensemble methods
- [ ] Implement feature importance analysis
- [ ] Create confusion matrix visualizations
- [ ] Build a simple web interface

---

## Weekly Breakdown

### Week 1: ML Foundations
- Supervised learning concepts
- Train/test splitting
- Linear regression
- Model evaluation basics

### Week 2: Classification Algorithms
- Logistic regression
- K-Nearest Neighbors
- Decision trees
- Cross-validation

### Week 3: Model Evaluation
- Classification metrics deep dive
- Confusion matrices
- ROC curves and AUC
- Model comparison

### Week 4: Project Completion
- Build end-to-end pipeline
- Model selection
- Documentation
- Prediction script

---

## Claude Prompts

### Start of Month
```
/status

I'm starting Month 5: ML Basics.
Help me understand the key concepts and plan the month.
```

### Skill Application
```
I want to apply the Baseline Model skill.
Walk me through .claude/skills/baseline-model-and-card.md
for my [dataset name] dataset.
```

### Algorithm Explanation
```
Explain [algorithm name] in simple terms:
- How does it work?
- When should I use it?
- What are the hyperparameters?
- Show me a scikit-learn example.
```

### Debugging Models
```
/debug-learning

My model has:
- Training accuracy: 95%
- Test accuracy: 65%

What's happening and how do I fix it?
```

### Feature Engineering
```
My dataset has these features: [list features]
The target is: [target]

What feature engineering should I consider?
```

### Model Comparison
```
I've trained these models:
- Logistic Regression: accuracy=0.78, F1=0.72
- KNN: accuracy=0.75, F1=0.70
- Decision Tree: accuracy=0.82, F1=0.79

Help me decide which to choose and why.
```

### Project Planning
```
/plan-week

I'm building a classification model for [problem].
The dataset has [n] rows and [m] features.
Help me plan this week.
```

---

## How to Publish

### Demo

Show your classification model:
1. The problem and why it matters
2. Key EDA findings
3. Model comparison results
4. Making a prediction

### Write-up

Cover:
- Problem framing
- Data exploration highlights
- Model selection process
- Results and limitations

### Portfolio

- Notebook on GitHub
- Model card included
- Prediction script ready to use

---

## Resources

### scikit-learn
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [scikit-learn Tutorials](https://scikit-learn.org/stable/tutorial/index.html)

### Concepts
- [ML Crash Course (Google)](https://developers.google.com/machine-learning/crash-course)
- [StatQuest ML Playlist](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF)

### Practice
- [Kaggle Learn ML](https://www.kaggle.com/learn/intro-to-machine-learning)

---

## Next Month

[Month 6: ML Intermediate](../month-06/README.md) - Ensemble methods and advanced techniques

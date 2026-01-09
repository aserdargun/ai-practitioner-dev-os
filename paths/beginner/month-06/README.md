# Month 6: Classification Algorithms

**Theme**: Master classification techniques for categorical predictions.

## Why It Matters

Classification is everywhere—spam detection, disease diagnosis, customer churn, fraud detection. This month adds essential algorithms to your toolkit that you'll use throughout your career.

## Prerequisites

- Month 5 completed (ML fundamentals, regression)
- Understanding of train/test splits and evaluation

## Learning Goals

### Classification Fundamentals (Week 1)
- [ ] Binary vs multi-class classification
- [ ] Evaluation metrics (accuracy, precision, recall, F1)
- [ ] Confusion matrix
- [ ] ROC curves and AUC
- [ ] Class imbalance handling

### Core Algorithms (Week 2-3)
- [ ] K-Nearest Neighbors (KNN)
- [ ] Naive Bayes
- [ ] Decision Trees
- [ ] Random Forests
- [ ] Support Vector Machines (SVM)

### Ensemble Methods (Week 4)
- [ ] Boosting concepts
- [ ] Gradient Boosting introduction
- [ ] Model selection and comparison
- [ ] Hyperparameter tuning

## Main Project: Customer Churn Predictor

Build a classification model to predict customer churn.

### Dataset
Use a telecom or subscription churn dataset from Kaggle.

### Deliverables
1. Classification pipeline:
   - Data preprocessing
   - Handle class imbalance
   - Train multiple models
   - Evaluate and compare

2. Model comparison report:
   - At least 4 algorithms compared
   - Confusion matrices for each
   - ROC curves comparison
   - Business interpretation

3. Production-ready model:
   - Best model saved
   - Prediction function
   - Model card

### Definition of Done
- [ ] 4+ models implemented
- [ ] Proper evaluation (not just accuracy)
- [ ] Class imbalance addressed
- [ ] Best model selected with justification
- [ ] Can predict new customers
- [ ] Model card complete

## Stretch Goals

- [ ] Implement cross-validation
- [ ] Add feature importance analysis
- [ ] Create prediction explanation
- [ ] Handle missing data elegantly
- [ ] Build simple Streamlit app

## Weekly Breakdown

### Week 1: Classification Basics
- Classification concepts
- Evaluation metrics deep dive
- ROC curves and AUC
- Explore churn dataset

### Week 2: KNN and Naive Bayes
- KNN algorithm and tuning
- Naive Bayes varieties
- Apply to churn data
- Compare results

### Week 3: Trees and Forests
- Decision Trees
- Random Forests
- Feature importance
- Model comparison

### Week 4: Complete Project
- SVM exploration
- Final model selection
- Model card
- Demo prep

## Claude Prompts

### Planning
```
/plan-week
Month 6 Week 2 - Focus on KNN and Naive Bayes
I want to understand when to use each algorithm
```

### Concept Help
```
Ask the Researcher to explain precision vs recall
trade-offs with practical business examples.
```

### Building
```
Ask the Builder to help me implement a Random Forest
with proper cross-validation and hyperparameter tuning
using GridSearchCV.
```

### Evaluation
```
Ask the Reviewer to review my classification metrics.
Am I handling class imbalance correctly?
Is my evaluation sound?
```

## How to Publish

### Demo
1. Present the business problem
2. Show class distribution
3. Compare model performances
4. Explain best model selection
5. Predict churn for sample customers

### Write-up Topics
- Business impact of churn prediction
- Algorithm comparison insights
- Handling imbalanced data
- What precision/recall means for business

### Portfolio Entry
- Clear business framing
- Comparison visualizations
- Code with explanations

## Resources

### Classification
- [scikit-learn Classification](https://scikit-learn.org/stable/supervised_learning.html)
- [StatQuest: Classification](https://www.youtube.com/playlist?list=PLblh5JKOoLUKxzEP5HA2d-Li7IJkHfXSe)

### Specific Algorithms
- [KNN Explained](https://www.youtube.com/watch?v=HVXime0nQeI)
- [Decision Trees](https://www.youtube.com/watch?v=_L39rN6gz7Y)
- [Random Forests](https://www.youtube.com/watch?v=J4Wdy0Wc_xQ)

### Practice
- [Kaggle Learn Classification](https://www.kaggle.com/learn/intermediate-machine-learning)

## Tips

1. **Don't rely on accuracy** — Especially with imbalanced classes
2. **Understand the algorithms** — Not just how to use them
3. **Business context matters** — Is false positive or negative worse?
4. **Start with baselines** — Simple models first
5. **Feature engineering helps** — Often more than algorithm choice

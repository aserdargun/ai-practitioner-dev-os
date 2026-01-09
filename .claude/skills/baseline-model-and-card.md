# Skill: Baseline Model and Card

Create a simple baseline model with proper documentation (model card).

## Trigger

Use this skill when:
- Starting a new ML project
- Need a benchmark to beat
- Establishing evaluation metrics
- Creating documentation for your model

## Prerequisites

- EDA completed (know your data)
- Clear problem definition (classification, regression, etc.)
- Target variable identified
- Train/test split strategy decided
- Evaluation metrics chosen

## Steps

### 1. Define the Problem (10 min)

Document in model card:
```markdown
## Model Overview
- **Task**: [Classification / Regression / Ranking / ...]
- **Target**: [What we're predicting]
- **Business Goal**: [Why this matters]
- **Success Metric**: [Primary metric to optimize]
```

### 2. Prepare Data (20 min)

```python
from sklearn.model_selection import train_test_split

# Features and target
X = df.drop(columns=[target_col])
y = df[target_col]

# Split (stratify for classification)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y  # if classification
)

print(f"Train: {len(X_train)}, Test: {len(X_test)}")
```

Basic preprocessing:
```python
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Numeric: scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train[numeric_cols])

# Categorical: encode
encoder = LabelEncoder()
for col in categorical_cols:
    X_train[col] = encoder.fit_transform(X_train[col])
```

### 3. Choose Baseline Model (5 min)

| Task | Simple Baseline | Reasonable Baseline |
|------|-----------------|---------------------|
| Classification | Majority class | Logistic Regression |
| Regression | Mean/median | Linear Regression |
| Time Series | Last value / Average | Simple moving average |
| Ranking | Random | Popularity-based |

### 4. Train Baseline (15 min)

```python
# Example: Classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Simple baseline: always predict majority class
majority_class = y_train.mode()[0]
baseline_preds = [majority_class] * len(y_test)
baseline_acc = accuracy_score(y_test, baseline_preds)
print(f"Majority baseline accuracy: {baseline_acc:.3f}")

# Reasonable baseline: Logistic Regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train_processed, y_train)
y_pred = model.predict(X_test_processed)

print(classification_report(y_test, y_pred))
```

### 5. Evaluate (15 min)

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_auc_score
)

# Calculate metrics
metrics = {
    'accuracy': accuracy_score(y_test, y_pred),
    'precision': precision_score(y_test, y_pred, average='weighted'),
    'recall': recall_score(y_test, y_pred, average='weighted'),
    'f1': f1_score(y_test, y_pred, average='weighted'),
}

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d')
```

### 6. Document in Model Card (20 min)

```markdown
## Model Card: [Model Name] Baseline

### Model Overview
- **Task**: Binary classification
- **Target**: Customer churn (yes/no)
- **Model Type**: Logistic Regression
- **Version**: 0.1 (Baseline)

### Intended Use
- Predict which customers are likely to churn
- Use for retention campaign targeting
- NOT for individual customer decisions

### Training Data
- Source: Customer database export
- Size: 40,000 records (train), 10,000 records (test)
- Date Range: Jan 2024 - Dec 2025
- Known Issues: 5% missing tenure data (imputed with median)

### Evaluation Metrics
| Metric | Baseline (Majority) | This Model |
|--------|---------------------|------------|
| Accuracy | 0.73 | 0.81 |
| Precision | 0.00 | 0.78 |
| Recall | 0.00 | 0.65 |
| F1 Score | 0.00 | 0.71 |
| ROC AUC | 0.50 | 0.84 |

### Feature Importance
1. tenure (0.35)
2. monthly_charges (0.22)
3. contract_type (0.18)

### Limitations
- Trained on historical data; may not reflect recent changes
- Performance lower on new customer segment
- Does not account for seasonal effects

### Ethical Considerations
- Model should not be used alone for decisions affecting customers
- Potential bias: performance varies by customer segment
- Regular monitoring needed

### Next Steps
- Try ensemble methods (Random Forest, XGBoost)
- Feature engineering from EDA insights
- Hyperparameter tuning
```

## Artifacts Produced

- [ ] `baseline_model.pkl` — Saved model
- [ ] `baseline_notebook.ipynb` — Training notebook
- [ ] `model_card.md` — Model documentation
- [ ] `metrics.json` — Evaluation metrics
- [ ] Preprocessor artifacts (scaler, encoder)

## Quality Bar

- [ ] Baseline beats naive predictor
- [ ] Multiple metrics reported (not just accuracy)
- [ ] Train/test split is proper (no leakage)
- [ ] Model card is complete
- [ ] Code is reproducible (random seeds set)
- [ ] Preprocessing is documented

## Common Pitfalls

1. **Data leakage**
   - Fit preprocessors on train only, transform test

2. **Only reporting accuracy**
   - For imbalanced data, accuracy is misleading

3. **Skipping the naive baseline**
   - You need something to compare against

4. **No model card**
   - Documentation is part of the deliverable

5. **Overly complex baseline**
   - Keep it simple; complexity comes in iteration

## Example

See `templates/template-eval-harness/` for a complete baseline example with proper evaluation.

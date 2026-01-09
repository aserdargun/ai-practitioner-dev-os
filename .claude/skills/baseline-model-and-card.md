# Skill: Baseline Model and Card

## Trigger

Use this skill when starting an ML project to establish a baseline model with proper documentation.

## Prerequisites

- Completed EDA (use `eda-to-insight.md` skill first)
- Clear target variable and success metric
- Train/test split strategy decided
- Python environment with scikit-learn

## Steps

### 1. Define the Problem (15 min)

```markdown
## Problem Definition

**Task Type**: [Classification / Regression / Ranking / etc.]
**Target Variable**: [column_name]
**Success Metric**: [Accuracy / RMSE / F1 / etc.]
**Baseline Target**: [What score would be "good enough"?]
**Business Context**: [Why does this matter?]
```

### 2. Prepare Data (30 min)

```python
import pandas as pd
from sklearn.model_selection import train_test_split

# Load and prepare
df = pd.read_csv("cleaned_data.csv")

# Define features and target
feature_cols = ['col1', 'col2', 'col3']  # Your features
target_col = 'target'

X = df[feature_cols]
y = df[target_col]

# Split data (stratify for classification)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y  # Remove stratify for regression
)

print(f"Train: {len(X_train)}, Test: {len(X_test)}")
```

### 3. Create Naive Baseline (15 min)

```python
from sklearn.dummy import DummyClassifier, DummyRegressor
from sklearn.metrics import accuracy_score, mean_squared_error

# For classification
dummy = DummyClassifier(strategy='most_frequent')
dummy.fit(X_train, y_train)
naive_score = accuracy_score(y_test, dummy.predict(X_test))
print(f"Naive baseline (majority class): {naive_score:.3f}")

# For regression
# dummy = DummyRegressor(strategy='mean')
# dummy.fit(X_train, y_train)
# naive_rmse = mean_squared_error(y_test, dummy.predict(X_test), squared=False)
# print(f"Naive baseline (mean): {naive_rmse:.3f}")
```

### 4. Train Simple Model (30 min)

```python
from sklearn.ensemble import RandomForestClassifier  # or RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Create pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train
pipeline.fit(X_train, y_train)

# Evaluate
y_pred = pipeline.predict(X_test)
baseline_score = accuracy_score(y_test, y_pred)
print(f"Baseline model: {baseline_score:.3f}")
print(f"Improvement over naive: {baseline_score - naive_score:.3f}")
```

### 5. Error Analysis (20 min)

```python
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Classification report
print(classification_report(y_test, y_pred))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.savefig('confusion_matrix.png')

# Feature importance
importances = pd.DataFrame({
    'feature': feature_cols,
    'importance': pipeline.named_steps['model'].feature_importances_
}).sort_values('importance', ascending=False)
print(importances)
```

### 6. Save Model and Artifacts (15 min)

```python
import joblib
import json

# Save model
joblib.dump(pipeline, 'baseline_model.joblib')

# Save metadata
metadata = {
    'model_type': 'RandomForestClassifier',
    'features': feature_cols,
    'target': target_col,
    'naive_baseline': float(naive_score),
    'baseline_score': float(baseline_score),
    'test_size': len(X_test),
    'train_date': '2026-01-09'
}
with open('model_metadata.json', 'w') as f:
    json.dump(metadata, f, indent=2)
```

### 7. Create Model Card (30 min)

```markdown
# Model Card: [Project Name] Baseline

## Model Details
- **Model Type**: Random Forest Classifier
- **Version**: 1.0.0 (Baseline)
- **Created**: 2026-01-09
- **Author**: [Your Name]

## Intended Use
- **Primary Use**: [What is this model for?]
- **Out-of-Scope Uses**: [What should it NOT be used for?]

## Training Data
- **Source**: [Where did the data come from?]
- **Size**: X rows, Y features
- **Date Range**: [If applicable]
- **Preprocessing**: [Key transformations applied]

## Evaluation
| Metric | Naive Baseline | This Model |
|--------|----------------|------------|
| Accuracy | 0.XXX | 0.XXX |
| F1 Score | N/A | 0.XXX |

## Limitations
- [Limitation 1]
- [Limitation 2]

## Ethical Considerations
- [Any bias concerns?]
- [Fairness across groups?]

## Next Steps
- [ ] [Improvement 1]
- [ ] [Improvement 2]
```

## Artifacts Produced

- `baseline_model.joblib` - Serialized model
- `model_metadata.json` - Model metadata
- `model_card.md` - Documentation
- `confusion_matrix.png` - Visualization
- `baseline_training.py` - Training script

## Quality Bar

- [ ] Naive baseline established
- [ ] Model beats naive baseline
- [ ] Error analysis completed
- [ ] Model card written
- [ ] Model serialized and loadable

## Common Pitfalls

1. **No naive baseline** - Always compare to simple approach
2. **Data leakage** - Ensure test set is truly held out
3. **Wrong metric** - Use business-relevant metrics
4. **Missing documentation** - Model card is required

## Example

See `templates/template-eval-harness/` for baseline model patterns.

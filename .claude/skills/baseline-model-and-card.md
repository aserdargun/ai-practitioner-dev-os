# Skill: Baseline Model and Card

**Tier**: 1 (Beginner)

Build a simple baseline model and document it with a model card for reproducibility and communication.

---

## Trigger

Use this skill when:
- EDA is complete
- Ready to build first model
- Need a benchmark to improve upon

## Prerequisites

- [ ] EDA completed (see [eda-to-insight.md](eda-to-insight.md))
- [ ] Clean dataset ready
- [ ] Target variable defined
- [ ] Python with scikit-learn installed

## Steps

### Step 1: Prepare Data (15 min)

```python
import pandas as pd
from sklearn.model_selection import train_test_split

# Load cleaned data
df = pd.read_csv('cleaned_data.csv')

# Define features and target
X = df.drop('target', axis=1)
y = df['target']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Train size: {len(X_train)}")
print(f"Test size: {len(X_test)}")
print(f"Target distribution:\n{y.value_counts(normalize=True)}")
```

**Checkpoint**: Data split into train/test with documented sizes.

### Step 2: Choose Baseline Model (5 min)

Select appropriate baseline:

| Task | Baseline Model |
|------|----------------|
| Binary Classification | LogisticRegression or DummyClassifier |
| Multi-class Classification | LogisticRegression |
| Regression | LinearRegression or DummyRegressor |
| Time Series | Naive (last value) or Mean |

```python
from sklearn.linear_model import LogisticRegression  # or appropriate model

# Initialize baseline
baseline = LogisticRegression(random_state=42)
```

**Checkpoint**: Baseline model selected and justified.

### Step 3: Train and Evaluate (15 min)

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report
)

# Train
baseline.fit(X_train, y_train)

# Predict
y_pred = baseline.predict(X_test)

# Evaluate
print("Classification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Store metrics
metrics = {
    'accuracy': accuracy_score(y_test, y_pred),
    'precision': precision_score(y_test, y_pred, average='weighted'),
    'recall': recall_score(y_test, y_pred, average='weighted'),
    'f1': f1_score(y_test, y_pred, average='weighted')
}
print(f"\nMetrics: {metrics}")
```

**Checkpoint**: Model trained with documented metrics.

### Step 4: Create Model Card (20 min)

Create `model_card.md`:

```markdown
# Model Card: [Model Name] Baseline

## Model Details

- **Model type**: [e.g., Logistic Regression]
- **Version**: 1.0 (baseline)
- **Date**: [Date]
- **Author**: [Your name]

## Intended Use

- **Primary use**: [What this model predicts]
- **Users**: [Who will use it]
- **Out of scope**: [What it shouldn't be used for]

## Training Data

- **Source**: [Where data came from]
- **Size**: [N records, M features]
- **Date range**: [If applicable]
- **Preprocessing**: [Steps applied]

## Evaluation Data

- **Test set size**: [N records]
- **Split method**: [Random 80/20, stratified, etc.]

## Metrics

| Metric | Value |
|--------|-------|
| Accuracy | X.XX |
| Precision | X.XX |
| Recall | X.XX |
| F1 Score | X.XX |

## Limitations

- [Limitation 1]
- [Limitation 2]

## Ethical Considerations

- [Any bias concerns]
- [Fairness considerations]

## Recommendations

- [How to improve]
- [What to try next]
```

**Checkpoint**: Model card completed with all sections.

### Step 5: Save Artifacts (10 min)

```python
import joblib
import json

# Save model
joblib.dump(baseline, 'models/baseline_v1.joblib')

# Save metrics
with open('models/baseline_metrics.json', 'w') as f:
    json.dump(metrics, f, indent=2)

print("Model and metrics saved!")
```

**Checkpoint**: Model and metrics saved to disk.

## Artifacts Produced

- [ ] Trained baseline model (`.joblib`)
- [ ] Metrics JSON file
- [ ] Model card (markdown)
- [ ] Training notebook

## Quality Bar

✅ **Done when**:
- Model trained on train set only
- Evaluated on held-out test set
- Metrics documented
- Model card complete
- Artifacts saved
- Can reproduce results

## Common Pitfalls

- **Data leakage**: Never use test data for training or feature selection
- **Wrong metric**: Choose metrics appropriate for the problem (e.g., F1 for imbalanced data)
- **No documentation**: Model card is not optional
- **Over-engineering**: Keep baseline simple - that's the point

## Baseline Benchmarks

Know if your baseline is reasonable:

| Task | Metric | Reasonable Baseline |
|------|--------|---------------------|
| Binary (balanced) | Accuracy | > 50% |
| Binary (imbalanced) | F1 | > majority class % |
| Regression | R² | > 0 |
| Time Series | MAE | < naive forecast |

## Example Prompt

```
I've finished EDA on customer churn data. Help me:

1. Build a logistic regression baseline
2. Evaluate with appropriate metrics
3. Create a model card

The target is 'churned' (0/1) and it's 20% positive class.
```

## Related Skills

- [EDA to Insight](eda-to-insight.md) - Do this first
- [Experiment Plan](experiment-plan.md) - Plan improvements

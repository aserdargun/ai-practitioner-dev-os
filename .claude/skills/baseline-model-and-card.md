# Skill: Baseline Model and Card

Create a simple baseline model with proper documentation using a model card.

## Trigger

Use this skill when:
- Starting a new ML project
- Need a benchmark to compare against
- Validating that the problem is learnable
- Creating the first iteration before optimization

## Prerequisites

- [ ] EDA completed (use `eda-to-insight` skill)
- [ ] Target variable defined
- [ ] Train/test split strategy decided
- [ ] Success metrics identified

## Steps

### 1. Define the Baseline (10 min)

Choose the simplest reasonable approach:

| Problem Type | Baseline Options |
|--------------|------------------|
| Classification | Majority class, Logistic Regression |
| Regression | Mean/median prediction, Linear Regression |
| Time Series | Naive (last value), Seasonal naive |
| NLP | TF-IDF + Logistic Regression |
| Ranking | Random, Popularity-based |

**Document**: Why this baseline is appropriate.

### 2. Prepare Data (20 min)

```python
from sklearn.model_selection import train_test_split

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Basic preprocessing
# - Handle missing values (simple: drop or fill with median/mode)
# - Encode categoricals (one-hot or label encoding)
# - Scale numerics if needed
```

**Document**: Preprocessing choices and rationale.

### 3. Train Baseline (15 min)

```python
from sklearn.linear_model import LogisticRegression  # or appropriate model

# Train
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]  # if classification
```

### 4. Evaluate (20 min)

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report
)

# Calculate metrics
metrics = {
    'accuracy': accuracy_score(y_test, y_pred),
    'precision': precision_score(y_test, y_pred),
    'recall': recall_score(y_test, y_pred),
    'f1': f1_score(y_test, y_pred)
}

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
```

**Document**: All metric values with interpretation.

### 5. Create Model Card (30 min)

Create `model_card.md`:

```markdown
# Model Card: [Project Name] Baseline

## Model Details
- **Model type**: [e.g., Logistic Regression]
- **Version**: 0.1.0 (baseline)
- **Created**: [date]
- **Framework**: scikit-learn [version]

## Intended Use
- **Primary use**: [what this model is for]
- **Users**: [who will use it]
- **Out of scope**: [what it shouldn't be used for]

## Training Data
- **Source**: [where data came from]
- **Size**: [train/test sizes]
- **Features**: [number and types]
- **Target**: [what we're predicting]

## Evaluation Results

| Metric | Value |
|--------|-------|
| Accuracy | X.XX |
| Precision | X.XX |
| Recall | X.XX |
| F1 | X.XX |

## Limitations
- [Limitation 1]
- [Limitation 2]

## Ethical Considerations
- [Any bias concerns]
- [Fairness considerations]

## Next Steps
- [Planned improvements]
```

### 6. Save Artifacts (10 min)

```python
import joblib

# Save model
joblib.dump(model, 'models/baseline_model.joblib')

# Save metrics
import json
with open('models/baseline_metrics.json', 'w') as f:
    json.dump(metrics, f, indent=2)
```

## Artifacts

| Artifact | Description |
|----------|-------------|
| `baseline_model.joblib` | Trained model file |
| `baseline_metrics.json` | Evaluation metrics |
| `model_card.md` | Model documentation |
| `baseline_notebook.ipynb` | Training notebook |

## Quality Bar

- [ ] Baseline is genuinely simple (not over-engineered)
- [ ] Train/test split prevents data leakage
- [ ] Multiple metrics reported (not just accuracy)
- [ ] Model card is complete and honest
- [ ] Artifacts are versioned and reproducible
- [ ] Clear next steps identified

## Time Estimate

| Experience | Time |
|------------|------|
| First time | 2-3 hours |
| Practiced | 1-1.5 hours |
| Expert | 30-45 min |

## Common Pitfalls

- Making the baseline too complex
- Not documenting preprocessing
- Ignoring class imbalance
- Using test data during training
- Skipping the model card

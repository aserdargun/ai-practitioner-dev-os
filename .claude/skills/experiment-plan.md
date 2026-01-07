# Skill: Experiment Plan

**Tier**: 1 (Beginner)

Design a structured experiment plan to systematically improve model performance.

---

## Trigger

Use this skill when:
- Baseline model is complete
- Want to improve performance
- Need to compare approaches systematically

## Prerequisites

- [ ] Baseline model trained (see [baseline-model-and-card.md](baseline-model-and-card.md))
- [ ] Baseline metrics documented
- [ ] Clear understanding of the problem

## Steps

### Step 1: Define Success Criteria (10 min)

```markdown
## Success Criteria

**Primary metric**: [e.g., F1 Score]
**Target**: [e.g., Improve from 0.72 to 0.80]
**Constraints**:
- Inference time < X ms
- Model size < Y MB
- Must be interpretable (if required)
```

**Checkpoint**: Clear, measurable success criteria defined.

### Step 2: Generate Hypotheses (15 min)

Brainstorm what might improve performance:

```markdown
## Hypotheses

### H1: Feature Engineering
- **Hypothesis**: Creating interaction features will capture non-linear relationships
- **Test**: Add polynomial features for top 5 correlated variables
- **Expected impact**: +5% accuracy

### H2: Better Model
- **Hypothesis**: Tree-based models will handle feature interactions better
- **Test**: Train Random Forest with default hyperparameters
- **Expected impact**: +3-5% accuracy

### H3: Handling Imbalance
- **Hypothesis**: Class imbalance is hurting minority class recall
- **Test**: Apply SMOTE or class weights
- **Expected impact**: +10% recall for minority class

### H4: Hyperparameter Tuning
- **Hypothesis**: Default hyperparameters are suboptimal
- **Test**: Grid search on regularization strength
- **Expected impact**: +2-3% accuracy
```

**Checkpoint**: 3-5 testable hypotheses documented.

### Step 3: Prioritize Experiments (10 min)

Rank by expected impact vs. effort:

| Experiment | Expected Impact | Effort | Priority |
|------------|-----------------|--------|----------|
| H2: Random Forest | High | Low | 1 |
| H3: Handle Imbalance | High | Medium | 2 |
| H1: Feature Engineering | Medium | High | 3 |
| H4: Hyperparameter Tuning | Low | Medium | 4 |

**Checkpoint**: Experiments prioritized.

### Step 4: Design Experiment Protocol (15 min)

```markdown
## Experiment Protocol

### Data Split Strategy
- Train: 60%
- Validation: 20%
- Test: 20% (held out until final evaluation)

### Cross-Validation
- Method: 5-fold stratified CV
- Metric: Mean ± Std of primary metric

### Tracking
- Log all experiments in experiment_log.csv
- Track: model, hyperparameters, metrics, notes

### Code Structure
experiments/
├── exp_01_random_forest.py
├── exp_02_handle_imbalance.py
├── exp_03_feature_engineering.py
└── experiment_log.csv
```

**Checkpoint**: Protocol documented.

### Step 5: Create Experiment Template (10 min)

```python
"""
Experiment: [NAME]
Hypothesis: [HYPOTHESIS]
Date: [DATE]
"""
import pandas as pd
from sklearn.model_selection import cross_val_score
import json

# Load data (same split as baseline)
X_train = pd.read_csv('data/X_train.csv')
y_train = pd.read_csv('data/y_train.csv')

# Experiment setup
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=42)

# Cross-validation
scores = cross_val_score(model, X_train, y_train.values.ravel(),
                         cv=5, scoring='f1_weighted')

# Results
results = {
    'experiment': 'random_forest_default',
    'hypothesis': 'Tree models better capture interactions',
    'cv_mean': scores.mean(),
    'cv_std': scores.std(),
    'notes': 'Default hyperparameters'
}

print(f"CV F1: {scores.mean():.4f} ± {scores.std():.4f}")

# Log results
with open('experiment_log.jsonl', 'a') as f:
    f.write(json.dumps(results) + '\n')
```

**Checkpoint**: Reusable experiment template ready.

### Step 6: Document Experiment Plan (10 min)

Create `experiment_plan.md`:

```markdown
# Experiment Plan: [Project Name]

## Objective
Improve [model] performance from [baseline] to [target].

## Baseline
- Model: [Baseline model]
- Metric: [Baseline metric value]

## Success Criteria
- Primary: [Metric] > [Value]
- Secondary: [Other constraints]

## Hypotheses (Prioritized)
1. [H1 summary]
2. [H2 summary]
3. [H3 summary]

## Protocol
- CV: [Strategy]
- Tracking: [Method]
- Timeline: [Estimated]

## Schedule
| Week | Experiment | Expected Outcome |
|------|------------|------------------|
| 1 | Exp 1 | Results + decision |
| 2 | Exp 2 | Results + decision |

## Decision Points
- If Exp 1 succeeds → proceed to Exp 2
- If Exp 1 fails → investigate why before proceeding
```

**Checkpoint**: Complete experiment plan document.

## Artifacts Produced

- [ ] Experiment plan document
- [ ] Prioritized hypothesis list
- [ ] Experiment template code
- [ ] Tracking spreadsheet/file

## Quality Bar

✅ **Done when**:
- Success criteria are measurable
- Hypotheses are testable
- Protocol prevents data leakage
- Experiments are prioritized
- Template is ready to use

## Common Pitfalls

- **Testing on test set**: Only use test set for final evaluation
- **No baseline comparison**: Always compare to baseline
- **Changing metrics mid-experiment**: Stick to your primary metric
- **Not tracking experiments**: Log everything for reproducibility

## Example Prompt

```
My baseline logistic regression has F1 = 0.72 on customer churn prediction.
Help me create an experiment plan to improve performance.

The data is imbalanced (20% churn) and I have 2 weeks to iterate.
```

## Related Skills

- [Baseline Model and Card](baseline-model-and-card.md) - Create baseline first
- [EDA to Insight](eda-to-insight.md) - Inform hypotheses with EDA

# Skill: Experiment Plan

Design and track ML experiments systematically.

## Trigger

Use this skill when:
- Iterating beyond baseline model
- Comparing multiple approaches
- Tuning hyperparameters
- Trying different features or architectures

## Prerequisites

- Baseline model established
- Evaluation metrics defined
- Reproducible training pipeline
- Version control in place

## Steps

### 1. Define Experiment Hypothesis (10 min)

For each experiment, write:
```markdown
## Experiment: [Name]

**Hypothesis**: [What you expect to happen]
**Change**: [What you're changing from baseline]
**Success Criteria**: [How you'll know it worked]
**Estimated Time**: [How long to run]
```

Example:
```markdown
## Experiment: Add Polynomial Features

**Hypothesis**: Adding polynomial interactions between top 3 features
will improve F1 by at least 5% due to non-linear relationships seen in EDA.

**Change**: Add degree-2 polynomial features for tenure, charges, contract.
**Success Criteria**: F1 > 0.75 (baseline: 0.71)
**Estimated Time**: 2 hours
```

### 2. Create Experiment Tracking Table (5 min)

```markdown
| ID | Name | Change | Metric (F1) | Result | Date |
|----|------|--------|-------------|--------|------|
| B0 | Baseline | LogReg | 0.71 | Baseline | 2026-03-01 |
| E1 | Poly Features | + poly(2) | 0.73 | +2.8% | 2026-03-02 |
| E2 | Random Forest | RF n=100 | 0.78 | +9.9% | 2026-03-02 |
| E3 | XGBoost | XGB default | 0.82 | +15.5% | 2026-03-03 |
```

### 3. Set Up Experiment Code (20 min)

```python
import mlflow
from datetime import datetime

def run_experiment(name, model, params, X_train, y_train, X_test, y_test):
    """Run a tracked experiment."""

    with mlflow.start_run(run_name=name):
        # Log parameters
        mlflow.log_params(params)

        # Train
        model.fit(X_train, y_train)

        # Evaluate
        y_pred = model.predict(X_test)
        metrics = calculate_metrics(y_test, y_pred)

        # Log metrics
        mlflow.log_metrics(metrics)

        # Log model
        mlflow.sklearn.log_model(model, "model")

        return metrics

# Example usage
from sklearn.ensemble import RandomForestClassifier

params = {'n_estimators': 100, 'max_depth': 10, 'random_state': 42}
model = RandomForestClassifier(**params)

results = run_experiment(
    name="E2_RandomForest",
    model=model,
    params=params,
    X_train=X_train, y_train=y_train,
    X_test=X_test, y_test=y_test
)
```

### 4. Run Experiment with Controls (30 min)

Ensure reproducibility:
```python
import random
import numpy as np

def set_seeds(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    # For torch: torch.manual_seed(seed)

set_seeds(42)
```

Run and record:
```python
# Before running
print(f"Experiment: {experiment_name}")
print(f"Started: {datetime.now()}")
print(f"Git commit: {get_git_commit()}")

# Run experiment
results = run_experiment(...)

# After running
print(f"Finished: {datetime.now()}")
print(f"Results: {results}")
```

### 5. Analyze Results (15 min)

```python
# Compare to baseline
baseline_f1 = 0.71
experiment_f1 = results['f1']
improvement = (experiment_f1 - baseline_f1) / baseline_f1 * 100

print(f"F1: {experiment_f1:.3f} ({improvement:+.1f}% vs baseline)")

# Statistical significance (for classification)
from scipy import stats
# ... run statistical tests if needed

# Document findings
findings = f"""
## Experiment {experiment_name} Results

- F1: {experiment_f1:.3f} ({improvement:+.1f}% vs baseline)
- Hypothesis: {'Confirmed' if experiment_f1 > 0.75 else 'Not confirmed'}
- Notable observations: [what you learned]
- Next steps: [what to try next]
"""
```

### 6. Document Learnings (10 min)

After each experiment:
```markdown
## Experiment Log: E2_RandomForest

**Date**: 2026-03-02
**Duration**: 45 minutes

**What Worked**:
- Random Forest significantly outperformed LogReg
- Feature importance aligns with EDA insights

**What Didn't**:
- Training is 10x slower
- Default params might be overfitting

**Surprises**:
- tenure is even more important than expected

**Next Experiment**:
- Try XGBoost for better speed
- Add regularization to prevent overfitting
```

## Artifacts Produced

- [ ] `experiment_plan.md` — Planned experiments
- [ ] `experiment_log.md` — Results and learnings
- [ ] `experiments/` folder with notebooks
- [ ] Tracking table (markdown or MLflow)
- [ ] Best model saved

## Quality Bar

- [ ] Hypothesis stated before running
- [ ] Single change per experiment (isolate variables)
- [ ] Results are reproducible (seeds, versions logged)
- [ ] Comparison to baseline documented
- [ ] Learnings captured, not just metrics
- [ ] Failed experiments documented too

## Common Pitfalls

1. **Changing too many things at once**
   - One change per experiment for clarity

2. **Not logging parameters**
   - You'll forget what you tried

3. **Ignoring failed experiments**
   - Document what didn't work and why

4. **No baseline comparison**
   - Always report improvement over baseline

5. **P-hacking / over-testing**
   - Pre-register your success criteria

## Example

See `templates/template-eval-harness/` for a structured experiment setup.

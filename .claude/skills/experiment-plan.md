# Skill: Experiment Plan

## Trigger

Use this skill when you need to systematically test hypotheses, compare approaches, or optimize ML models.

## Prerequisites

- Baseline model established (use `baseline-model-and-card.md` first)
- Clear hypothesis to test
- Evaluation infrastructure ready
- Experiment tracking tool (MLflow, W&B, or simple logging)

## Steps

### 1. Define Hypothesis (15 min)

```markdown
## Experiment: [Descriptive Name]

**Hypothesis**: If we [change X], then [metric Y] will [improve/change] because [reasoning].

**Example**:
- If we add TF-IDF text features, then accuracy will improve by 5%+ because the text field contains predictive signal we're not using.

**Null Hypothesis**: The change will have no significant effect.
```

### 2. Design Experiment (20 min)

```markdown
## Experiment Design

**Independent Variable**: [What we're changing]
- Variant A (Control): [Current approach]
- Variant B (Treatment): [New approach]
- [Optional] Variant C: [Another approach]

**Dependent Variable**: [What we're measuring]
- Primary: [Main metric, e.g., Accuracy]
- Secondary: [Supporting metrics, e.g., F1, Latency]

**Control Variables**: [What stays the same]
- Same train/test split
- Same random seed
- Same hyperparameters (unless that's the experiment)

**Sample Size**:
- Test set: X samples
- Statistical power: [If relevant]
```

### 3. Set Up Tracking (20 min)

```python
# Simple tracking with JSON
import json
from datetime import datetime

def log_experiment(name, config, metrics, notes=""):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "name": name,
        "config": config,
        "metrics": metrics,
        "notes": notes
    }
    with open("experiments.jsonl", "a") as f:
        f.write(json.dumps(entry) + "\n")

# Or use MLflow
import mlflow

mlflow.set_experiment("my-experiment")
with mlflow.start_run(run_name="variant_a"):
    mlflow.log_params(config)
    # ... train model ...
    mlflow.log_metrics(metrics)
    mlflow.log_artifact("model.joblib")
```

### 4. Run Control (Variant A) (30 min)

```python
# Establish control baseline
control_config = {
    "model": "RandomForest",
    "features": ["num_col1", "num_col2", "cat_col1"],
    "n_estimators": 100
}

# Train and evaluate
control_metrics = train_and_evaluate(control_config)

log_experiment(
    name="text_features_experiment_control",
    config=control_config,
    metrics=control_metrics,
    notes="Control: baseline features only"
)

print(f"Control accuracy: {control_metrics['accuracy']:.3f}")
```

### 5. Run Treatment (Variant B) (30 min)

```python
# Add the experimental change
treatment_config = {
    "model": "RandomForest",
    "features": ["num_col1", "num_col2", "cat_col1", "tfidf_text"],  # Added
    "n_estimators": 100
}

# Train and evaluate
treatment_metrics = train_and_evaluate(treatment_config)

log_experiment(
    name="text_features_experiment_treatment",
    config=treatment_config,
    metrics=treatment_metrics,
    notes="Treatment: added TF-IDF text features"
)

print(f"Treatment accuracy: {treatment_metrics['accuracy']:.3f}")
```

### 6. Analyze Results (20 min)

```python
# Compare results
improvement = treatment_metrics['accuracy'] - control_metrics['accuracy']
relative_improvement = improvement / control_metrics['accuracy'] * 100

print(f"Absolute improvement: {improvement:.3f}")
print(f"Relative improvement: {relative_improvement:.1f}%")

# Statistical significance (if applicable)
from scipy import stats

# For classification, use McNemar's test
# For regression, use paired t-test
# ... statistical test code ...

# Practical significance
threshold = 0.05  # 5% improvement target
if improvement >= threshold:
    print("✅ Hypothesis SUPPORTED: Improvement meets threshold")
else:
    print("❌ Hypothesis NOT SUPPORTED: Improvement below threshold")
```

### 7. Document Findings (20 min)

```markdown
## Experiment Results: [Name]

**Date**: 2026-01-09
**Status**: [Completed / In Progress / Blocked]

### Results Summary

| Variant | Accuracy | F1 | Latency (ms) |
|---------|----------|-----|--------------|
| Control | 0.823 | 0.801 | 45 |
| Treatment | 0.856 | 0.839 | 52 |
| Δ | +0.033 | +0.038 | +7 |

### Conclusion

[Hypothesis supported/not supported]. Adding TF-IDF features improved accuracy by 3.3% (above 5% threshold: NO, but meaningful).

### Trade-offs

- ✅ Accuracy improved
- ⚠️ Latency increased 15%
- ⚠️ Feature pipeline more complex

### Decision

[Accept / Reject / Iterate]

Recommend: **Accept** with caveat about latency monitoring.

### Next Experiments

1. Try different TF-IDF parameters (max_features)
2. Experiment with embedding-based features
3. Optimize latency with feature caching
```

## Artifacts Produced

- `experiments.jsonl` - Experiment log
- `experiment_[name].py` - Experiment code
- `experiment_results.md` - Findings document
- `plots/` - Comparison visualizations

## Quality Bar

- [ ] Hypothesis clearly stated
- [ ] Control and treatment defined
- [ ] Same evaluation conditions
- [ ] Results documented with metrics
- [ ] Decision made and justified

## Common Pitfalls

1. **No control** - Always compare to baseline
2. **Multiple changes** - One variable at a time
3. **Cherry-picking** - Report all experiments, not just wins
4. **No reproducibility** - Log configs and random seeds

## Example

```python
# Minimal experiment template
experiments = [
    {"name": "control", "config": {...}, "metrics": None},
    {"name": "treatment_a", "config": {...}, "metrics": None},
    {"name": "treatment_b", "config": {...}, "metrics": None},
]

for exp in experiments:
    exp["metrics"] = train_and_evaluate(exp["config"])
    log_experiment(**exp)

# Compare
best = max(experiments, key=lambda x: x["metrics"]["accuracy"])
print(f"Best: {best['name']} with {best['metrics']['accuracy']:.3f}")
```

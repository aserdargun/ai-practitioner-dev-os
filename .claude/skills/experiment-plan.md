# Skill: Experiment Plan

Design structured ML experiments to systematically improve model performance.

## Trigger

Use this skill when:
- Baseline model is established
- Ready to iterate and improve
- Comparing multiple approaches
- Need to justify model choices

## Prerequisites

- [ ] Baseline model complete (use `baseline-model-and-card` skill)
- [ ] Evaluation metrics defined
- [ ] Compute resources available
- [ ] Version control set up

## Steps

### 1. Define Hypotheses (15 min)

List specific, testable hypotheses:

```markdown
## Hypotheses

1. **H1**: Adding feature X will improve F1 by at least 5%
   - Rationale: [why you think this]
   - Risk: [what could go wrong]

2. **H2**: Using model Y instead of baseline will improve AUC
   - Rationale: [why you think this]
   - Risk: [what could go wrong]

3. **H3**: Hyperparameter tuning will improve performance
   - Rationale: [why you think this]
   - Risk: [what could go wrong]
```

### 2. Design Experiments (20 min)

For each hypothesis, define:

```markdown
## Experiment: [Name]

### Hypothesis
[What you're testing]

### Variables
- **Independent**: [What you're changing]
- **Dependent**: [What you're measuring]
- **Controlled**: [What stays constant]

### Method
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Success Criteria
- Primary: [metric] improves by [amount]
- Secondary: [other considerations]

### Resources
- Estimated time: [hours]
- Compute: [requirements]
```

### 3. Set Up Tracking (15 min)

```python
# Using MLflow (or similar)
import mlflow

mlflow.set_experiment("project-name")

with mlflow.start_run(run_name="experiment-1"):
    # Log parameters
    mlflow.log_params({
        "model_type": "random_forest",
        "n_estimators": 100,
        "max_depth": 10
    })

    # Train model
    model.fit(X_train, y_train)

    # Log metrics
    mlflow.log_metrics({
        "accuracy": accuracy,
        "f1": f1_score,
        "auc": auc
    })

    # Log model
    mlflow.sklearn.log_model(model, "model")
```

### 4. Run Experiments (varies)

Execute experiments in order of:
1. Expected impact (highest first)
2. Resource cost (cheapest first if similar impact)
3. Dependencies (prerequisites first)

**Document each run**:
- Configuration used
- Results obtained
- Observations and surprises

### 5. Analyze Results (30 min)

```markdown
## Results Summary

| Experiment | Hypothesis | Result | Metric Change |
|------------|------------|--------|---------------|
| Exp 1 | H1 | ✅ Confirmed | +7% F1 |
| Exp 2 | H2 | ❌ Rejected | -2% AUC |
| Exp 3 | H3 | ⚠️ Partial | +3% (not 5%) |

## Key Findings
1. [Finding 1]
2. [Finding 2]

## Recommendations
- [What to do next]
```

### 6. Document Decisions (15 min)

Record final choices:

```markdown
## Experiment Conclusions

### Selected Approach
[What you're going with and why]

### Rejected Alternatives
1. [Alternative 1]: Rejected because [reason]
2. [Alternative 2]: Rejected because [reason]

### Future Work
- [Ideas to explore later]
```

## Artifacts

| Artifact | Description |
|----------|-------------|
| `experiment_plan.md` | Hypothesis and design document |
| `experiment_log/` | Individual experiment records |
| `results_summary.md` | Analysis and conclusions |
| MLflow runs | Tracked experiments |

## Quality Bar

- [ ] Hypotheses are specific and testable
- [ ] Experiments are reproducible
- [ ] All runs are tracked with parameters and metrics
- [ ] Results are analyzed, not just collected
- [ ] Decisions are documented with rationale
- [ ] Failed experiments are documented too

## Time Estimate

Varies by experiment complexity. Planning phase:

| Experience | Time |
|------------|------|
| First time | 2-3 hours |
| Practiced | 1-1.5 hours |
| Expert | 30-45 min |

## Common Pitfalls

- Running experiments without clear hypotheses
- Not tracking all parameters
- Changing multiple things at once
- Ignoring negative results
- Over-fitting to validation set
- Not documenting failed attempts

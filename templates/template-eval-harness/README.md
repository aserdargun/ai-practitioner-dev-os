# Evaluation Harness Template

A minimal template for evaluating ML models with multiple metrics and datasets.

## Features

- Pluggable evaluation metrics
- Multiple dataset support
- Comparison across model versions
- HTML and JSON reports
- Tests included

## Quick Start

```bash
# Install dependencies
pip install -e ".[dev]"

# Run evaluation
python -m eval_harness.main --model model.pkl --data test.csv

# Run tests
pytest
```

## Project Structure

```
template-eval-harness/
├── eval_harness/
│   ├── __init__.py
│   ├── main.py           # CLI entry point
│   ├── config.py         # Configuration
│   ├── loader.py         # Model and data loading
│   ├── metrics/
│   │   ├── __init__.py
│   │   ├── base.py       # Base metric class
│   │   ├── classification.py
│   │   └── regression.py
│   ├── runner.py         # Evaluation runner
│   └── reporter.py       # Report generation
├── tests/
│   ├── __init__.py
│   └── test_eval.py      # Evaluation tests
├── pyproject.toml
└── README.md
```

## Usage

### Command Line

```bash
# Basic evaluation
python -m eval_harness.main --model model.pkl --data test.csv

# With specific metrics
python -m eval_harness.main --model model.pkl --data test.csv \
  --metrics accuracy f1_score precision recall

# Generate HTML report
python -m eval_harness.main --model model.pkl --data test.csv \
  --output report.html --format html

# Compare multiple models
python -m eval_harness.main \
  --models model_v1.pkl model_v2.pkl \
  --data test.csv \
  --compare
```

### Programmatic Usage

```python
from eval_harness.runner import EvaluationRunner
from eval_harness.metrics import Accuracy, F1Score

runner = EvaluationRunner()
runner.add_metric(Accuracy())
runner.add_metric(F1Score())

results = runner.evaluate(
    model=my_model,
    X=X_test,
    y=y_test,
)

print(results.summary())
```

## Configuration

Create an `eval_config.yaml`:

```yaml
evaluation:
  name: "Model Evaluation"

datasets:
  - name: "test_set"
    path: "data/test.csv"
    target_column: "label"

metrics:
  - accuracy
  - f1_score
  - precision
  - recall
  - confusion_matrix

output:
  format: "html"
  path: "reports/"
```

## Built-in Metrics

### Classification
- `accuracy` - Accuracy score
- `precision` - Precision (macro/micro/weighted)
- `recall` - Recall (macro/micro/weighted)
- `f1_score` - F1 score (macro/micro/weighted)
- `confusion_matrix` - Confusion matrix
- `roc_auc` - ROC AUC score
- `classification_report` - Full classification report

### Regression
- `mse` - Mean Squared Error
- `rmse` - Root Mean Squared Error
- `mae` - Mean Absolute Error
- `r2` - R-squared score
- `mape` - Mean Absolute Percentage Error

## Adding Custom Metrics

```python
from eval_harness.metrics.base import BaseMetric

class MyCustomMetric(BaseMetric):
    name = "my_metric"

    def compute(self, y_true, y_pred):
        # Your metric logic
        return {"my_metric": value}
```

## License

MIT

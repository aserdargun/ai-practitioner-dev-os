# Evaluation Harness Template

A template for building ML/AI evaluation frameworks.

## Features

- Modular evaluation metrics
- Batch evaluation support
- Results reporting
- CI integration ready

## Quick Start

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -e ".[dev]"

# Run evaluation
python -m src.evaluate --config config/eval_config.yaml

# Run tests
pytest
```

## Project Structure

```
template-eval-harness/
├── src/
│   ├── __init__.py
│   ├── evaluate.py       # Main evaluation logic
│   ├── metrics.py        # Metric implementations
│   ├── loaders.py        # Data loading
│   ├── reporters.py      # Result reporting
│   └── models.py         # Pydantic models
├── tests/
│   ├── __init__.py
│   └── test_metrics.py
├── config/
│   └── eval_config.yaml  # Evaluation configuration
├── data/
│   └── eval_data.json    # Sample evaluation data
├── pyproject.toml
└── README.md
```

## Usage

### Run Evaluation

```python
from src.evaluate import EvaluationHarness

harness = EvaluationHarness()
results = harness.run(
    predictions=predictions,
    ground_truth=ground_truth,
    metrics=["accuracy", "f1", "precision", "recall"],
)
print(results.summary())
```

### Add Custom Metrics

```python
from src.metrics import register_metric

@register_metric("custom_metric")
def custom_metric(predictions, ground_truth):
    # Your metric logic
    return score
```

## Configuration

YAML configuration example:

```yaml
evaluation:
  metrics:
    - accuracy
    - f1
    - precision
  threshold: 0.8
  output_format: json
```

## License

MIT

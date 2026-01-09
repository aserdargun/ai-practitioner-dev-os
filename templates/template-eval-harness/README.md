# Evaluation Harness Template

A minimal evaluation framework for testing ML models and AI systems.

## What This Template Provides

- Evaluation runner framework
- Multiple grader implementations
- Golden dataset support
- Metrics aggregation
- Test setup with pytest

## Quick Start

### 1. Install Dependencies

```bash
cd template-eval-harness
pip install -e ".[dev]"
```

### 2. Run Tests

```bash
pytest
```

### 3. Run Evaluations

```bash
python -m evals.run_evals --dataset datasets/sample_golden.jsonl --output results.json
```

## Project Structure

```
template-eval-harness/
├── evals/
│   ├── run_evals.py      # Main evaluation runner
│   └── graders.py        # Grading functions
├── datasets/
│   └── sample_golden.jsonl  # Sample golden dataset
├── pyproject.toml        # Dependencies and tooling
└── README.md
```

## Evaluation Flow

```
Golden Dataset → Run Model → Grade Outputs → Aggregate Metrics → Report
```

### 1. Golden Dataset
Define expected inputs and outputs.

### 2. Run Model
Execute your model/system on each input.

### 3. Grade
Score outputs against expectations.

### 4. Report
Aggregate and analyze results.

## Golden Dataset Format

`datasets/sample_golden.jsonl`:
```json
{"id": "test_001", "input": "What is 2+2?", "expected": "4", "category": "math"}
{"id": "test_002", "input": "Capital of France?", "expected": "Paris", "category": "geography"}
```

### Required Fields
- `id`: Unique identifier
- `input`: Input to the system
- `expected`: Expected output

### Optional Fields
- `category`: For grouping results
- `metadata`: Additional context
- `tags`: For filtering

## Graders

### Built-in Graders

#### ExactMatch
```python
from evals.graders import exact_match

score = exact_match(output="Paris", expected="Paris")
# Returns: 1.0 (exact match)
```

#### ContainsMatch
```python
from evals.graders import contains_match

score = contains_match(output="The capital is Paris", expected="Paris")
# Returns: 1.0 (contains expected)
```

#### SemanticSimilarity
```python
from evals.graders import semantic_similarity

score = semantic_similarity(
    output="The answer is 4",
    expected="Four",
    threshold=0.8
)
# Returns: similarity score (0-1)
```

### Custom Graders

```python
from evals.graders import Grader

class MyCustomGrader(Grader):
    def grade(self, output: str, expected: str, **kwargs) -> float:
        # Your grading logic
        return score
```

## Running Evaluations

### Basic Usage

```python
from evals.run_evals import EvalRunner

runner = EvalRunner(
    model_fn=my_model.predict,
    grader="exact_match"
)

results = runner.run("datasets/sample_golden.jsonl")
print(results.summary())
```

### CLI Usage

```bash
# Run with default grader
python -m evals.run_evals --dataset datasets/sample_golden.jsonl

# Specify grader
python -m evals.run_evals --dataset datasets/sample_golden.jsonl --grader contains

# Filter by category
python -m evals.run_evals --dataset datasets/sample_golden.jsonl --category math

# Output to file
python -m evals.run_evals --dataset datasets/sample_golden.jsonl --output results.json
```

## Results Format

```json
{
  "summary": {
    "total": 100,
    "passed": 85,
    "failed": 15,
    "accuracy": 0.85,
    "avg_score": 0.87
  },
  "by_category": {
    "math": {"total": 50, "accuracy": 0.90},
    "geography": {"total": 50, "accuracy": 0.80}
  },
  "results": [
    {"id": "test_001", "input": "...", "output": "...", "expected": "...", "score": 1.0, "passed": true}
  ]
}
```

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `EVAL_BATCH_SIZE` | `10` | Batch size for evaluation |
| `EVAL_TIMEOUT` | `30` | Timeout per evaluation (seconds) |
| `EVAL_PARALLEL` | `1` | Number of parallel workers |

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=evals

# Run specific test
pytest tests/ -v
```

## Best Practices

### Golden Dataset Design
1. Cover edge cases
2. Include diverse examples
3. Use clear, unambiguous expectations
4. Document any special formatting

### Grader Selection
1. Use exact_match for deterministic outputs
2. Use contains_match for flexible responses
3. Use semantic_similarity for natural language

### Evaluation Process
1. Start with a small golden set
2. Expand based on failure patterns
3. Version your golden datasets
4. Track metrics over time

## Extending

### Adding a New Grader

```python
# evals/graders.py

def my_grader(output: str, expected: str, **kwargs) -> float:
    """
    Custom grading logic.

    Args:
        output: Model output
        expected: Expected output
        **kwargs: Additional parameters

    Returns:
        Score between 0 and 1
    """
    # Your logic here
    return score

# Register in GRADERS dict
GRADERS["my_grader"] = my_grader
```

### Adding a New Metric

```python
# evals/run_evals.py

def calculate_custom_metric(results: list[dict]) -> float:
    """Calculate custom aggregate metric."""
    # Your logic here
    return metric_value
```

## Resources

- [LMSYS Eval Guide](https://lmsys.org/)
- [OpenAI Evals](https://github.com/openai/evals)
- [EleutherAI LM Eval Harness](https://github.com/EleutherAI/lm-evaluation-harness)

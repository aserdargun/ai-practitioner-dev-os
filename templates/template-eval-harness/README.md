# Evaluation Harness Template

A minimal evaluation harness for ML models with custom graders.

## Features

- Configurable evaluation pipelines
- Multiple grader types (exact match, semantic, LLM-based)
- Golden set management
- Detailed reporting
- Easy to extend

## Quick Start

```bash
# Install dependencies
pip install -e .

# Run evaluations
python evals/run_evals.py --dataset datasets/sample_golden.jsonl

# Run with specific grader
python evals/run_evals.py --dataset datasets/sample_golden.jsonl --grader exact

# Generate report
python evals/run_evals.py --dataset datasets/sample_golden.jsonl --report
```

## Project Structure

```
template-eval-harness/
├── evals/
│   ├── run_evals.py     # Main evaluation runner
│   └── graders.py       # Grading implementations
├── datasets/
│   └── sample_golden.jsonl  # Sample test data
├── pyproject.toml       # Project configuration
└── README.md            # This file
```

## Running Tests

```bash
pytest -v
```

## Golden Set Format

Each line in the JSONL file should contain:

```json
{
  "id": "unique_test_id",
  "input": "The input to your model",
  "expected": "The expected output",
  "metadata": {"category": "classification", "difficulty": "easy"}
}
```

## Graders

### Exact Match
```python
from evals.graders import ExactMatchGrader

grader = ExactMatchGrader()
result = grader.grade("hello", "hello")  # Returns GradeResult(score=1.0, passed=True)
```

### Contains Match
```python
from evals.graders import ContainsGrader

grader = ContainsGrader()
result = grader.grade("hello world", "hello")  # Returns GradeResult(score=1.0, passed=True)
```

### Semantic Similarity
```python
from evals.graders import SemanticGrader

grader = SemanticGrader(threshold=0.8)
result = grader.grade("The cat sat", "A cat was sitting")
```

## Custom Graders

Implement the `Grader` interface:

```python
from evals.graders import Grader, GradeResult

class MyCustomGrader(Grader):
    def grade(self, actual: str, expected: str) -> GradeResult:
        # Your grading logic
        score = compute_score(actual, expected)
        return GradeResult(
            score=score,
            passed=score >= self.threshold,
            reason="Explanation of the grade"
        )
```

## Evaluation Results

Results include:
- **Pass rate**: Percentage of test cases passed
- **Average score**: Mean score across all cases
- **Per-category breakdown**: Results grouped by metadata
- **Failure analysis**: Details on failed cases

## CLI Options

| Argument | Description | Default |
|----------|-------------|---------|
| `--dataset` | Path to golden set | Required |
| `--grader` | Grader type | `exact` |
| `--threshold` | Pass threshold | `0.8` |
| `--report` | Generate detailed report | `False` |
| `--output` | Output file for results | `stdout` |

## Customization

1. Add new graders in `graders.py`
2. Create domain-specific golden sets in `datasets/`
3. Extend `run_evals.py` for custom reporting
4. Add metadata fields for better analysis

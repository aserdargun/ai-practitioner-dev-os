# Evaluation Harness Template

A framework for evaluating LLM and ML system outputs with customizable graders.

## Features

- Multiple grading strategies (exact match, fuzzy, LLM-based)
- Golden set evaluation
- Detailed metrics and reports
- Extensible grader system
- JSON/JSONL dataset support

## Quick Start

```bash
# Install dependencies
pip install -e ".[all]"

# Run evaluations
python evals/run_evals.py --dataset datasets/sample_golden.jsonl

# Run with specific grader
python evals/run_evals.py --dataset datasets/sample_golden.jsonl --grader fuzzy

# Generate report
python evals/run_evals.py --dataset datasets/sample_golden.jsonl --output report.json

# Run tests
pytest
```

## Project Structure

```
template-eval-harness/
├── evals/
│   ├── run_evals.py   # Main evaluation runner
│   └── graders.py     # Grading strategies
├── datasets/
│   └── sample_golden.jsonl
├── pyproject.toml
└── README.md
```

## Dataset Format

Golden sets are JSONL files with one test case per line:

```jsonl
{"input": "What is 2+2?", "expected": "4", "category": "math"}
{"input": "Capital of France?", "expected": "Paris", "category": "geography"}
```

### Fields

| Field | Required | Description |
|-------|----------|-------------|
| `input` | Yes | The input/prompt to evaluate |
| `expected` | Yes | Expected output/answer |
| `category` | No | Test category for grouping |
| `metadata` | No | Additional context |

## Graders

### Built-in Graders

1. **ExactMatchGrader**: Binary exact string match
2. **FuzzyMatchGrader**: Similarity-based matching with threshold
3. **ContainsGrader**: Checks if expected is substring of output
4. **LLMGrader**: Uses LLM to judge correctness (placeholder)

### Custom Graders

```python
from graders import BaseGrader, GradeResult

class MyGrader(BaseGrader):
    def grade(self, output: str, expected: str, **kwargs) -> GradeResult:
        # Your grading logic
        is_correct = my_logic(output, expected)
        return GradeResult(
            passed=is_correct,
            score=1.0 if is_correct else 0.0,
            reason="Explanation"
        )
```

## Metrics

The evaluation produces:
- **Pass Rate**: Percentage of passing tests
- **Average Score**: Mean score across all tests
- **Category Breakdown**: Metrics by category
- **Failure Analysis**: Details on failed cases

## Configuration

Environment variables:
- `OPENAI_API_KEY`: For LLM-based grading
- `DEFAULT_GRADER`: Default grading strategy
- `SIMILARITY_THRESHOLD`: Fuzzy match threshold (0-1)

## Usage in Curriculum

This template is used in:
- Month 05: Model evaluation basics
- Month 06: RAG evaluation
- Month 07: LLM evaluation patterns
- Month 11: Agent evaluation

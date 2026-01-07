# Data Pipeline Template

A template for building robust data pipelines with validation.

## Features

- Pydantic data validation
- Multiple input/output formats
- Data quality checks
- CLI interface
- Comprehensive tests

## Quick Start

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -e ".[dev]"

# Run the pipeline
python -m src.pipeline --input data/sample.csv --output data/output.parquet

# Run tests
pytest

# Run linting
ruff check src/ tests/
```

## Project Structure

```
template-data-pipeline/
├── src/
│   ├── __init__.py
│   ├── pipeline.py       # Main pipeline logic
│   ├── models.py         # Pydantic data models
│   ├── loaders.py        # Data loading utilities
│   ├── transformers.py   # Data transformations
│   └── validators.py     # Validation logic
├── tests/
│   ├── __init__.py
│   ├── test_pipeline.py
│   └── test_validators.py
├── data/
│   └── sample.csv        # Sample data
├── pyproject.toml
└── README.md
```

## Usage

### As a module

```python
from src.pipeline import DataPipeline

pipeline = DataPipeline()
result = pipeline.run(
    input_path="data/input.csv",
    output_path="data/output.parquet",
)
print(f"Processed {result.rows_processed} rows")
```

### As CLI

```bash
python -m src.pipeline \
    --input data/input.csv \
    --output data/output.parquet \
    --validate
```

## Configuration

Environment variables:
- `LOG_LEVEL`: Logging level (default: INFO)
- `STRICT_VALIDATION`: Fail on validation errors (default: false)

## Development

1. Add new transformers in `transformers.py`
2. Add new validators in `validators.py`
3. Update models in `models.py`
4. Add tests for new functionality

## License

MIT

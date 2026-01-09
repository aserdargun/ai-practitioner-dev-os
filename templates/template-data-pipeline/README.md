# Data Pipeline Template

A minimal, production-ready data pipeline template with validation.

## Features

- Configurable data pipeline stages
- Data validation with detailed error reporting
- Schema enforcement
- Logging and metrics
- Easy testing

## Quick Start

```bash
# Install dependencies
pip install -e .

# Run the pipeline
python pipeline/run.py --input data/raw.csv --output data/processed.csv

# Run with validation only
python pipeline/validate.py --input data/raw.csv
```

## Project Structure

```
template-data-pipeline/
├── pipeline/
│   ├── run.py           # Main pipeline runner
│   └── validate.py      # Data validation
├── tests/
│   └── test_validate.py # Validation tests
├── pyproject.toml       # Project configuration
└── README.md            # This file
```

## Running Tests

```bash
pytest tests/ -v
```

## Pipeline Stages

1. **Load**: Read data from source
2. **Validate**: Check schema and data quality
3. **Transform**: Apply transformations
4. **Output**: Write to destination

## Customization

1. Add your data loading logic in `pipeline/run.py`
2. Define your schema in `validate.py`
3. Implement custom transformations
4. Add additional validation rules

## Configuration

The pipeline accepts these command-line arguments:

| Argument | Description | Required |
|----------|-------------|----------|
| `--input` | Input file path | Yes |
| `--output` | Output file path | Yes |
| `--config` | Config file path | No |
| `--validate-only` | Only validate, don't transform | No |

## Data Validation

The validator checks:
- Schema compliance (required columns, data types)
- Null values in required fields
- Value ranges and constraints
- Custom business rules

## Example Usage

```python
from pipeline.validate import DataValidator, Schema

# Define schema
schema = Schema(
    columns={
        "id": {"type": "int", "required": True},
        "value": {"type": "float", "required": True, "min": 0},
        "category": {"type": "str", "required": False},
    }
)

# Validate data
validator = DataValidator(schema)
result = validator.validate(df)

if result.is_valid:
    print("Data is valid!")
else:
    for error in result.errors:
        print(f"Error: {error}")
```

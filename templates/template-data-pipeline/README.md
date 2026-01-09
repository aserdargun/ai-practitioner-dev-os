# Data Pipeline Template

A reproducible data pipeline template with validation and testing.

## Features

- Data ingestion with validation
- Schema enforcement
- Data quality checks
- Pytest integration
- Configurable via environment

## Quick Start

```bash
# Install dependencies
pip install -e .

# Run the pipeline
python pipeline/run.py --input data/raw/input.csv --output data/processed/output.parquet

# Run with validation only
python pipeline/validate.py --input data/raw/input.csv

# Run tests
pytest
```

## Project Structure

```
template-data-pipeline/
├── pipeline/
│   ├── run.py         # Main pipeline script
│   └── validate.py    # Data validation
├── tests/
│   └── test_validate.py
├── pyproject.toml
└── README.md
```

## Pipeline Stages

1. **Load**: Read raw data from source
2. **Validate**: Check schema and data quality
3. **Transform**: Apply transformations
4. **Save**: Write to output format

## Validation Rules

The validator checks:
- Required columns present
- Data types match schema
- No null values in required fields
- Value ranges within bounds
- Custom business rules

## Configuration

Environment variables:
- `INPUT_PATH`: Input data path
- `OUTPUT_PATH`: Output data path
- `VALIDATION_MODE`: strict or lenient

## Customization

1. Define your schema in `pipeline/validate.py`
2. Add transformation logic in `pipeline/run.py`
3. Add custom validators as needed
4. Write tests for your transformations

## Integration with MLOps

This template integrates with:
- **MLflow**: Log pipeline runs as experiments
- **Airflow**: Wrap as DAG tasks
- **DVC**: Version control data artifacts

## Usage in Curriculum

This template is used in:
- Month 02: Data analysis pipelines
- Month 08: MLOps and pipeline orchestration

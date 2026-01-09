# Data Pipeline Template

A minimal, tested data pipeline template for processing and validating data.

## What This Template Provides

- Data loading and processing structure
- Data validation framework
- Test setup with pytest
- Code quality with ruff

## Quick Start

### 1. Install Dependencies

```bash
cd template-data-pipeline
pip install -e ".[dev]"
```

### 2. Run Tests

```bash
pytest
```

### 3. Run the Pipeline

```bash
python -m pipeline.run --input data/input.csv --output data/output.csv
```

## Project Structure

```
template-data-pipeline/
├── pipeline/
│   ├── run.py            # Main pipeline runner
│   └── validate.py       # Data validation functions
├── tests/
│   └── test_validate.py  # Test suite
├── data/                 # Data directory (gitignored)
├── pyproject.toml        # Dependencies and tooling
└── README.md
```

## Pipeline Stages

```
Input Data → Load → Validate → Transform → Validate → Output
```

### 1. Load
Read data from various sources (CSV, JSON, databases).

### 2. Validate
Check data quality (nulls, types, ranges, uniqueness).

### 3. Transform
Apply business logic transformations.

### 4. Output
Write processed data to destination.

## Customization

### Adding New Validations

Edit `pipeline/validate.py`:

```python
def validate_custom_rule(df: pd.DataFrame) -> ValidationResult:
    """Check custom business rule."""
    issues = []

    # Your validation logic
    if df["value"].max() > 1000:
        issues.append("Value exceeds maximum allowed")

    return ValidationResult(
        passed=len(issues) == 0,
        issues=issues
    )
```

### Adding New Transformations

Edit `pipeline/run.py`:

```python
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Apply transformations."""
    df = df.copy()

    # Your transformations
    df["processed_at"] = datetime.now()
    df["normalized_value"] = df["value"] / df["value"].max()

    return df
```

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `INPUT_PATH` | `data/input.csv` | Input file path |
| `OUTPUT_PATH` | `data/output.csv` | Output file path |
| `LOG_LEVEL` | `INFO` | Logging level |
| `FAIL_ON_WARNINGS` | `false` | Fail pipeline on warnings |

### Pipeline Options

```bash
# Dry run (validate only)
python -m pipeline.run --dry-run

# Skip validation
python -m pipeline.run --skip-validation

# Verbose output
python -m pipeline.run --verbose
```

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=pipeline

# Run specific test
pytest tests/test_validate.py -v
```

## Code Quality

```bash
# Check code style
ruff check .

# Format code
ruff format .
```

## Common Patterns

### Error Handling

```python
try:
    df = load_data(input_path)
except FileNotFoundError:
    logger.error(f"Input file not found: {input_path}")
    sys.exit(1)
except pd.errors.EmptyDataError:
    logger.error("Input file is empty")
    sys.exit(1)
```

### Logging

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

logger.info(f"Processing {len(df)} rows")
logger.warning(f"Found {null_count} null values")
```

### Checkpointing

```python
# Save intermediate results for debugging
df.to_csv("data/checkpoint_after_transform.csv", index=False)
```

## Production Checklist

- [ ] Configure input/output paths
- [ ] Set up logging
- [ ] Add all required validations
- [ ] Test with production-like data
- [ ] Set up monitoring/alerting
- [ ] Document data requirements
- [ ] Handle edge cases

## Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Great Expectations](https://greatexpectations.io/) - Advanced data validation
- [Prefect](https://www.prefect.io/) - Workflow orchestration

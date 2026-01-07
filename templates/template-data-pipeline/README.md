# Data Pipeline Template

A minimal template for building data processing pipelines with Python.

## Features

- Configurable pipeline stages
- Data validation with Pydantic
- Logging and error handling
- CSV and JSON data sources
- Tests included

## Quick Start

```bash
# Install dependencies
pip install -e ".[dev]"

# Run the pipeline
python -m pipeline.main --config config.yaml

# Run tests
pytest
```

## Project Structure

```
template-data-pipeline/
├── pipeline/
│   ├── __init__.py
│   ├── main.py           # Pipeline entry point
│   ├── config.py         # Configuration handling
│   ├── stages/
│   │   ├── __init__.py
│   │   ├── extract.py    # Data extraction
│   │   ├── transform.py  # Data transformation
│   │   └── load.py       # Data loading
│   └── utils.py          # Utility functions
├── tests/
│   ├── __init__.py
│   └── test_pipeline.py  # Pipeline tests
├── config.yaml           # Example configuration
├── pyproject.toml
└── README.md
```

## Configuration

```yaml
# config.yaml
pipeline:
  name: "example-pipeline"

extract:
  source: "data/input.csv"
  format: "csv"

transform:
  steps:
    - drop_nulls: true
    - normalize: ["column1", "column2"]

load:
  destination: "data/output.csv"
  format: "csv"
```

## Usage

### Running the Pipeline

```bash
# With default config
python -m pipeline.main

# With custom config
python -m pipeline.main --config my_config.yaml

# Dry run (validate only)
python -m pipeline.main --dry-run
```

### Programmatic Usage

```python
from pipeline.main import Pipeline
from pipeline.config import PipelineConfig

config = PipelineConfig.from_yaml("config.yaml")
pipeline = Pipeline(config)
result = pipeline.run()
print(f"Processed {result.rows_processed} rows")
```

## Customization

### Adding a Transform Stage

1. Create a new function in `pipeline/stages/transform.py`
2. Register it in the transform registry
3. Reference it in your config

```python
# In transform.py
@register_transform("my_transform")
def my_transform(df, params):
    # Your transformation logic
    return df
```

### Adding a New Data Source

1. Implement an extractor in `pipeline/stages/extract.py`
2. Register it for your format type

## License

MIT

# Tests

This directory contains tests for the sentiment classifier.

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_model.py

# Run with verbose output
pytest -v
```

## Test Structure

| File | Tests |
|------|-------|
| `test_model.py` | Model training and prediction |

## Test Categories

### Unit Tests
- Data loading
- Pipeline creation
- Single predictions

### Integration Tests
- Full training pipeline
- Model save/load
- Batch predictions

## Test Data

Tests use the sample data in `data/sample_reviews.json`.

For faster tests, a subset of data is used where appropriate.

## Coverage Goals

- Aim for >80% coverage on core functions
- All public functions should have at least one test
- Edge cases should be covered (empty input, etc.)

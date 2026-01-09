# Tests

This directory contains tests for the sentiment analysis service.

## Files

| File | Purpose |
|------|---------|
| `test_model.py` | Unit tests for the model class |
| `test_api.py` | Integration tests for the API |

## Running Tests

```bash
# Run all tests
pytest -v

# Run with coverage
pytest --cov=src -v

# Run specific test file
pytest tests/test_model.py -v
```

## Test Categories

### Unit Tests (test_model.py)
- Model initialization
- Training functionality
- Prediction logic
- Save/load operations

### Integration Tests (test_api.py)
- Health endpoint
- Prediction endpoint
- Error handling
- Input validation

## Writing Good Tests

1. **Arrange-Act-Assert**: Structure tests clearly
2. **One assertion per test**: Test one thing at a time
3. **Descriptive names**: `test_predict_returns_positive_for_happy_text`
4. **Independent tests**: Tests shouldn't depend on each other

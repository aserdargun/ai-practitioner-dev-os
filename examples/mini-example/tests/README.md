# Tests

This directory contains tests for the Iris classifier.

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_train.py -v

# Run specific test
pytest tests/test_predict.py::TestPredict::test_predict_setosa -v
```

## Test Structure

### `test_train.py`

Tests for model training and evaluation:
- `test_train_model`: Model trains without errors
- `test_model_accuracy`: Model achieves expected accuracy
- `test_evaluate_model`: Evaluation returns correct metrics
- `test_save_and_load_model`: Model serialization works

### `test_predict.py`

Tests for prediction functions:
- `test_predict_setosa`: Correctly predicts setosa class
- `test_predict_versicolor`: Correctly predicts versicolor class
- `test_predict_virginica`: Correctly predicts virginica class
- `test_predict_proba`: Probabilities sum to 1
- `test_invalid_input`: Handles invalid input gracefully

## Writing New Tests

Follow this pattern:

```python
import pytest

class TestMyFeature:
    """Tests for my feature."""

    def test_happy_path(self):
        """Test normal operation."""
        result = my_function(valid_input)
        assert result == expected_output

    def test_edge_case(self):
        """Test edge case."""
        result = my_function(edge_input)
        assert result == edge_output

    def test_error_handling(self):
        """Test error handling."""
        with pytest.raises(ValueError):
            my_function(invalid_input)
```

## Test Coverage Goals

- Aim for >80% code coverage
- Every public function should have at least one test
- Edge cases should be tested
- Error paths should be tested

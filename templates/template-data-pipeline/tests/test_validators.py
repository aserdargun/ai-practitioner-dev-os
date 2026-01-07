"""Tests for data validators."""

import pandas as pd
import pytest

from src.validators import validate_not_null, validate_range, validate_unique


class TestValidateNotNull:
    """Tests for validate_not_null function."""

    def test_no_nulls_returns_empty(self):
        """Test that no nulls returns empty error list."""
        df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
        errors = validate_not_null(df, ["col1", "col2"])
        assert errors == []

    def test_with_nulls_returns_errors(self):
        """Test that nulls are detected."""
        df = pd.DataFrame({"col1": [1, None, 3], "col2": ["a", "b", None]})
        errors = validate_not_null(df, ["col1", "col2"])
        assert len(errors) == 2
        assert "col1" in errors[0]
        assert "col2" in errors[1]

    def test_missing_column_ignored(self):
        """Test that missing columns are ignored."""
        df = pd.DataFrame({"col1": [1, 2, 3]})
        errors = validate_not_null(df, ["col1", "missing_col"])
        assert errors == []


class TestValidateUnique:
    """Tests for validate_unique function."""

    def test_unique_values_returns_empty(self):
        """Test that unique values return empty error list."""
        df = pd.DataFrame({"id": [1, 2, 3]})
        errors = validate_unique(df, ["id"])
        assert errors == []

    def test_duplicates_returns_errors(self):
        """Test that duplicates are detected."""
        df = pd.DataFrame({"id": [1, 1, 3]})
        errors = validate_unique(df, ["id"])
        assert len(errors) == 1
        assert "duplicate" in errors[0].lower()


class TestValidateRange:
    """Tests for validate_range function."""

    def test_within_range_returns_empty(self):
        """Test that values within range return empty error list."""
        df = pd.DataFrame({"value": [5, 10, 15]})
        errors = validate_range(df, "value", min_value=0, max_value=20)
        assert errors == []

    def test_below_min_returns_error(self):
        """Test that values below minimum are detected."""
        df = pd.DataFrame({"value": [-5, 10, 15]})
        errors = validate_range(df, "value", min_value=0)
        assert len(errors) == 1
        assert "below" in errors[0].lower()

    def test_above_max_returns_error(self):
        """Test that values above maximum are detected."""
        df = pd.DataFrame({"value": [5, 10, 25]})
        errors = validate_range(df, "value", max_value=20)
        assert len(errors) == 1
        assert "above" in errors[0].lower()

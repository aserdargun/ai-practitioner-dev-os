"""
Tests for Data Validation Module

Run with: pytest tests/test_validate.py -v
"""

import pandas as pd
import pytest

from pipeline.validate import (
    run_all_validations,
    validate_column_types,
    validate_no_nulls,
    validate_not_empty,
    validate_required_columns,
    validate_unique,
    validate_value_range,
)


@pytest.fixture
def sample_df():
    """Create a sample DataFrame for testing."""
    return pd.DataFrame(
        {
            "id": [1, 2, 3, 4, 5],
            "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
            "age": [25, 30, 35, 40, 45],
            "score": [85.5, 90.0, 78.5, 92.0, 88.0],
        }
    )


@pytest.fixture
def df_with_nulls():
    """Create a DataFrame with null values."""
    return pd.DataFrame(
        {
            "id": [1, 2, 3],
            "name": ["Alice", None, "Charlie"],
            "age": [25, 30, None],
        }
    )


@pytest.fixture
def df_with_duplicates():
    """Create a DataFrame with duplicate values."""
    return pd.DataFrame(
        {
            "id": [1, 2, 2, 3],
            "name": ["Alice", "Bob", "Bob", "Charlie"],
        }
    )


class TestValidateNotEmpty:
    """Tests for validate_not_empty."""

    def test_non_empty_df_passes(self, sample_df):
        """Non-empty DataFrame should pass."""
        result = validate_not_empty(sample_df)
        assert result["passed"] is True
        assert len(result["issues"]) == 0

    def test_empty_df_fails(self):
        """Empty DataFrame should fail."""
        empty_df = pd.DataFrame()
        result = validate_not_empty(empty_df)
        assert result["passed"] is False
        assert "DataFrame is empty" in result["issues"]

    def test_no_columns_fails(self):
        """DataFrame with no columns should fail."""
        no_cols_df = pd.DataFrame(index=[0, 1, 2])
        result = validate_not_empty(no_cols_df)
        assert result["passed"] is False


class TestValidateNoNulls:
    """Tests for validate_no_nulls."""

    def test_no_nulls_passes(self, sample_df):
        """DataFrame without nulls should pass."""
        result = validate_no_nulls(sample_df)
        assert result["passed"] is True

    def test_with_nulls_fails(self, df_with_nulls):
        """DataFrame with nulls should fail."""
        result = validate_no_nulls(df_with_nulls)
        assert result["passed"] is False
        assert any("null values" in issue for issue in result["issues"])

    def test_specific_columns(self, df_with_nulls):
        """Should only check specified columns."""
        result = validate_no_nulls(df_with_nulls, columns=["id"])
        assert result["passed"] is True

    def test_missing_column(self, sample_df):
        """Should report missing columns."""
        result = validate_no_nulls(sample_df, columns=["nonexistent"])
        assert result["passed"] is False
        assert "not found" in result["issues"][0]


class TestValidateUnique:
    """Tests for validate_unique."""

    def test_unique_values_passes(self, sample_df):
        """Unique values should pass."""
        result = validate_unique(sample_df, columns=["id"])
        assert result["passed"] is True

    def test_duplicates_fails(self, df_with_duplicates):
        """Duplicate values should fail."""
        result = validate_unique(df_with_duplicates, columns=["id"])
        assert result["passed"] is False
        assert any("duplicate" in issue for issue in result["issues"])

    def test_no_columns_passes(self, sample_df):
        """No columns specified should pass."""
        result = validate_unique(sample_df, columns=None)
        assert result["passed"] is True


class TestValidateColumnTypes:
    """Tests for validate_column_types."""

    def test_correct_types_passes(self, sample_df):
        """Correct types should pass."""
        expected = {"id": "int64", "name": "object"}
        result = validate_column_types(sample_df, expected)
        assert result["passed"] is True

    def test_wrong_type_fails(self, sample_df):
        """Wrong type should fail."""
        expected = {"id": "object"}  # id is actually int64
        result = validate_column_types(sample_df, expected)
        assert result["passed"] is False


class TestValidateValueRange:
    """Tests for validate_value_range."""

    def test_within_range_passes(self, sample_df):
        """Values within range should pass."""
        result = validate_value_range(sample_df, "age", min_value=0, max_value=100)
        assert result["passed"] is True

    def test_below_min_fails(self, sample_df):
        """Values below minimum should fail."""
        result = validate_value_range(sample_df, "age", min_value=30)
        assert result["passed"] is False
        assert any("below" in issue for issue in result["issues"])

    def test_above_max_fails(self, sample_df):
        """Values above maximum should fail."""
        result = validate_value_range(sample_df, "age", max_value=35)
        assert result["passed"] is False
        assert any("above" in issue for issue in result["issues"])


class TestValidateRequiredColumns:
    """Tests for validate_required_columns."""

    def test_all_present_passes(self, sample_df):
        """All required columns present should pass."""
        result = validate_required_columns(sample_df, ["id", "name"])
        assert result["passed"] is True

    def test_missing_columns_fails(self, sample_df):
        """Missing required columns should fail."""
        result = validate_required_columns(sample_df, ["id", "nonexistent"])
        assert result["passed"] is False
        assert "Missing required columns" in result["issues"][0]


class TestRunAllValidations:
    """Tests for run_all_validations."""

    def test_valid_df_passes(self, sample_df):
        """Valid DataFrame should pass all validations."""
        result = run_all_validations(sample_df)
        assert result["passed"] is True

    def test_empty_df_fails(self):
        """Empty DataFrame should fail."""
        result = run_all_validations(pd.DataFrame())
        assert result["passed"] is False

    def test_with_options(self, sample_df):
        """Should apply specified validations."""
        result = run_all_validations(
            sample_df,
            required_columns=["id", "name"],
            unique_columns=["id"],
            no_null_columns=["name"],
        )
        assert result["passed"] is True

    def test_collects_all_issues(self, df_with_nulls):
        """Should collect all validation issues."""
        result = run_all_validations(
            df_with_nulls,
            no_null_columns=["name", "age"],
        )
        assert result["passed"] is False
        assert len(result["issues"]) >= 2  # At least 2 null issues

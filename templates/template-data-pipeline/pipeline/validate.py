"""
Data Validation Module

Functions for validating data quality.
"""

from typing import TypedDict

import pandas as pd


class ValidationResult(TypedDict):
    """Result of a validation check."""

    passed: bool
    issues: list[str]


def validate_not_empty(df: pd.DataFrame) -> ValidationResult:
    """
    Check that DataFrame is not empty.

    Args:
        df: DataFrame to validate

    Returns:
        ValidationResult with pass/fail and issues
    """
    issues = []

    if len(df) == 0:
        issues.append("DataFrame is empty")

    if len(df.columns) == 0:
        issues.append("DataFrame has no columns")

    return ValidationResult(passed=len(issues) == 0, issues=issues)


def validate_no_nulls(
    df: pd.DataFrame, columns: list[str] | None = None
) -> ValidationResult:
    """
    Check for null values in specified columns.

    Args:
        df: DataFrame to validate
        columns: Columns to check (default: all columns)

    Returns:
        ValidationResult with pass/fail and issues
    """
    issues = []

    if columns is None:
        columns = df.columns.tolist()

    for col in columns:
        if col not in df.columns:
            issues.append(f"Column '{col}' not found")
            continue

        null_count = df[col].isna().sum()
        if null_count > 0:
            issues.append(f"Column '{col}' has {null_count} null values")

    return ValidationResult(passed=len(issues) == 0, issues=issues)


def validate_unique(
    df: pd.DataFrame, columns: list[str] | None = None
) -> ValidationResult:
    """
    Check that specified columns have unique values.

    Args:
        df: DataFrame to validate
        columns: Columns to check for uniqueness

    Returns:
        ValidationResult with pass/fail and issues
    """
    issues = []

    if columns is None:
        return ValidationResult(passed=True, issues=[])

    for col in columns:
        if col not in df.columns:
            issues.append(f"Column '{col}' not found")
            continue

        duplicate_count = df[col].duplicated().sum()
        if duplicate_count > 0:
            issues.append(f"Column '{col}' has {duplicate_count} duplicate values")

    return ValidationResult(passed=len(issues) == 0, issues=issues)


def validate_column_types(
    df: pd.DataFrame, expected_types: dict[str, str]
) -> ValidationResult:
    """
    Check that columns have expected data types.

    Args:
        df: DataFrame to validate
        expected_types: Dict mapping column names to expected types
                       (e.g., {"age": "int64", "name": "object"})

    Returns:
        ValidationResult with pass/fail and issues
    """
    issues = []

    for col, expected_type in expected_types.items():
        if col not in df.columns:
            issues.append(f"Column '{col}' not found")
            continue

        actual_type = str(df[col].dtype)
        if actual_type != expected_type:
            issues.append(
                f"Column '{col}' has type '{actual_type}', expected '{expected_type}'"
            )

    return ValidationResult(passed=len(issues) == 0, issues=issues)


def validate_value_range(
    df: pd.DataFrame,
    column: str,
    min_value: float | None = None,
    max_value: float | None = None,
) -> ValidationResult:
    """
    Check that column values are within expected range.

    Args:
        df: DataFrame to validate
        column: Column to check
        min_value: Minimum allowed value (inclusive)
        max_value: Maximum allowed value (inclusive)

    Returns:
        ValidationResult with pass/fail and issues
    """
    issues = []

    if column not in df.columns:
        return ValidationResult(passed=False, issues=[f"Column '{column}' not found"])

    if min_value is not None:
        below_min = (df[column] < min_value).sum()
        if below_min > 0:
            issues.append(f"Column '{column}' has {below_min} values below {min_value}")

    if max_value is not None:
        above_max = (df[column] > max_value).sum()
        if above_max > 0:
            issues.append(f"Column '{column}' has {above_max} values above {max_value}")

    return ValidationResult(passed=len(issues) == 0, issues=issues)


def validate_required_columns(
    df: pd.DataFrame, required: list[str]
) -> ValidationResult:
    """
    Check that all required columns are present.

    Args:
        df: DataFrame to validate
        required: List of required column names

    Returns:
        ValidationResult with pass/fail and issues
    """
    issues = []

    missing = set(required) - set(df.columns)
    if missing:
        issues.append(f"Missing required columns: {sorted(missing)}")

    return ValidationResult(passed=len(issues) == 0, issues=issues)


def run_all_validations(
    df: pd.DataFrame,
    required_columns: list[str] | None = None,
    unique_columns: list[str] | None = None,
    no_null_columns: list[str] | None = None,
) -> ValidationResult:
    """
    Run all configured validations.

    Customize this function to include the validations you need.

    Args:
        df: DataFrame to validate
        required_columns: Columns that must be present
        unique_columns: Columns that must have unique values
        no_null_columns: Columns that must not have nulls

    Returns:
        Combined ValidationResult
    """
    all_issues: list[str] = []

    # Always check: not empty
    result = validate_not_empty(df)
    all_issues.extend(result["issues"])

    # Required columns
    if required_columns:
        result = validate_required_columns(df, required_columns)
        all_issues.extend(result["issues"])

    # Unique columns
    if unique_columns:
        result = validate_unique(df, unique_columns)
        all_issues.extend(result["issues"])

    # No nulls
    if no_null_columns:
        result = validate_no_nulls(df, no_null_columns)
        all_issues.extend(result["issues"])

    return ValidationResult(passed=len(all_issues) == 0, issues=all_issues)

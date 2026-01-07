"""Data validation utilities."""

import logging
from typing import Type

import pandas as pd
from pydantic import BaseModel, ValidationError

logger = logging.getLogger(__name__)


def validate_dataframe(
    df: pd.DataFrame,
    model: Type[BaseModel],
) -> tuple[pd.DataFrame, list[str]]:
    """Validate DataFrame rows against a Pydantic model.

    Args:
        df: DataFrame to validate
        model: Pydantic model class for validation

    Returns:
        Tuple of (valid_df, errors)
    """
    valid_rows = []
    errors = []

    for idx, row in df.iterrows():
        try:
            # Convert row to dict and validate
            record = model(**row.to_dict())
            valid_rows.append(record.model_dump())
        except ValidationError as e:
            error_msg = f"Row {idx}: {e.error_count()} validation error(s)"
            errors.append(error_msg)
            logger.warning(error_msg)

    if valid_rows:
        valid_df = pd.DataFrame(valid_rows)
    else:
        valid_df = pd.DataFrame()

    logger.info(f"Validation complete: {len(valid_rows)} valid, {len(errors)} invalid")

    return valid_df, errors


def validate_not_null(df: pd.DataFrame, columns: list[str]) -> list[str]:
    """Check that specified columns have no null values.

    Args:
        df: DataFrame to check
        columns: Columns to validate

    Returns:
        List of errors found
    """
    errors = []
    for col in columns:
        if col in df.columns:
            null_count = df[col].isnull().sum()
            if null_count > 0:
                errors.append(f"Column '{col}' has {null_count} null values")
    return errors


def validate_unique(df: pd.DataFrame, columns: list[str]) -> list[str]:
    """Check that specified columns have unique values.

    Args:
        df: DataFrame to check
        columns: Columns to validate

    Returns:
        List of errors found
    """
    errors = []
    for col in columns:
        if col in df.columns:
            duplicate_count = df[col].duplicated().sum()
            if duplicate_count > 0:
                errors.append(f"Column '{col}' has {duplicate_count} duplicate values")
    return errors


def validate_range(
    df: pd.DataFrame,
    column: str,
    min_value: float | None = None,
    max_value: float | None = None,
) -> list[str]:
    """Check that values in a column are within a specified range.

    Args:
        df: DataFrame to check
        column: Column to validate
        min_value: Minimum allowed value
        max_value: Maximum allowed value

    Returns:
        List of errors found
    """
    errors = []
    if column not in df.columns:
        return errors

    if min_value is not None:
        below_min = (df[column] < min_value).sum()
        if below_min > 0:
            errors.append(f"Column '{column}' has {below_min} values below {min_value}")

    if max_value is not None:
        above_max = (df[column] > max_value).sum()
        if above_max > 0:
            errors.append(f"Column '{column}' has {above_max} values above {max_value}")

    return errors

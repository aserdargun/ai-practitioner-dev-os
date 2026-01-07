"""Data transformation stage."""

import pandas as pd

from pipeline.config import TransformConfig

# Registry of transform functions
TRANSFORMS = {}


def register_transform(name: str):
    """Decorator to register a transform function."""

    def decorator(func):
        TRANSFORMS[name] = func
        return func

    return decorator


@register_transform("drop_nulls")
def drop_nulls(df: pd.DataFrame, columns: list[str] | None = None) -> pd.DataFrame:
    """Drop rows with null values.

    Args:
        df: Input DataFrame.
        columns: Specific columns to check, or None for all.

    Returns:
        DataFrame with nulls dropped.
    """
    if columns:
        return df.dropna(subset=columns)
    return df.dropna()


@register_transform("normalize")
def normalize(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Normalize numeric columns to 0-1 range.

    Args:
        df: Input DataFrame.
        columns: Columns to normalize.

    Returns:
        DataFrame with normalized columns.
    """
    result = df.copy()
    for col in columns:
        if col in result.columns:
            min_val = result[col].min()
            max_val = result[col].max()
            if max_val > min_val:
                result[col] = (result[col] - min_val) / (max_val - min_val)
    return result


@register_transform("filter")
def filter_rows(
    df: pd.DataFrame, column: str, operator: str, value: float
) -> pd.DataFrame:
    """Filter rows based on condition.

    Args:
        df: Input DataFrame.
        column: Column to filter on.
        operator: Comparison operator (>, <, ==, >=, <=, !=).
        value: Value to compare against.

    Returns:
        Filtered DataFrame.
    """
    ops = {
        ">": lambda x, v: x > v,
        "<": lambda x, v: x < v,
        "==": lambda x, v: x == v,
        ">=": lambda x, v: x >= v,
        "<=": lambda x, v: x <= v,
        "!=": lambda x, v: x != v,
    }
    if operator not in ops:
        raise ValueError(f"Unsupported operator: {operator}")
    return df[ops[operator](df[column], value)]


def transform_data(df: pd.DataFrame, config: TransformConfig) -> pd.DataFrame:
    """Apply all transform steps.

    Args:
        df: Input DataFrame.
        config: Transform configuration.

    Returns:
        Transformed DataFrame.
    """
    result = df.copy()

    for step in config.steps:
        if not step.enabled:
            continue

        if step.name not in TRANSFORMS:
            raise ValueError(f"Unknown transform: {step.name}")

        transform_func = TRANSFORMS[step.name]

        # Pass columns if specified
        if step.columns:
            result = transform_func(result, step.columns)
        else:
            result = transform_func(result)

    return result

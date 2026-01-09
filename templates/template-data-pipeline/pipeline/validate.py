"""Data Validation Module.

Provides schema validation and data quality checks.
"""

import argparse
import json
import logging
import os
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

# Configure logging
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@dataclass
class ValidationSchema:
    """Schema definition for data validation."""

    required_columns: list[str] = field(default_factory=list)
    column_types: dict[str, type | tuple[type, ...]] = field(default_factory=dict)
    nullable_columns: list[str] = field(default_factory=list)
    value_ranges: dict[str, tuple[float, float]] = field(default_factory=dict)
    allowed_values: dict[str, list[Any]] = field(default_factory=dict)


class DataValidator:
    """Validates data against a schema."""

    def __init__(self, schema: ValidationSchema):
        self.schema = schema
        self.errors: list[str] = []

    def validate(self, data: list[dict]) -> tuple[bool, list[str]]:
        """Validate data against schema.

        Returns (is_valid, list of error messages).
        """
        self.errors = []

        if not data:
            self.errors.append("Data is empty")
            return False, self.errors

        # Check required columns on first row
        first_row = data[0]
        self._check_required_columns(first_row)

        # Validate each row
        for i, row in enumerate(data):
            self._validate_row(row, row_index=i)

        is_valid = len(self.errors) == 0
        return is_valid, self.errors

    def _check_required_columns(self, row: dict) -> None:
        """Check that all required columns are present."""
        for col in self.schema.required_columns:
            if col not in row:
                self.errors.append(f"Missing required column: {col}")

    def _validate_row(self, row: dict, row_index: int) -> None:
        """Validate a single row."""
        # Check column types
        for col, expected_type in self.schema.column_types.items():
            if col in row:
                value = row[col]
                if value is not None and not isinstance(value, expected_type):
                    self.errors.append(
                        f"Row {row_index}: Column '{col}' has type {type(value).__name__}, "
                        f"expected {expected_type}"
                    )

        # Check null values
        for col in self.schema.required_columns:
            if col not in self.schema.nullable_columns:
                if col in row and row[col] is None:
                    self.errors.append(
                        f"Row {row_index}: Column '{col}' cannot be null"
                    )

        # Check value ranges
        for col, (min_val, max_val) in self.schema.value_ranges.items():
            if col in row and row[col] is not None:
                value = row[col]
                if not (min_val <= value <= max_val):
                    self.errors.append(
                        f"Row {row_index}: Column '{col}' value {value} "
                        f"outside range [{min_val}, {max_val}]"
                    )

        # Check allowed values
        for col, allowed in self.schema.allowed_values.items():
            if col in row and row[col] is not None:
                value = row[col]
                if value not in allowed:
                    self.errors.append(
                        f"Row {row_index}: Column '{col}' value '{value}' "
                        f"not in allowed values: {allowed}"
                    )


def validate_file(file_path: str, schema: ValidationSchema) -> tuple[bool, list[str]]:
    """Validate a data file against a schema.

    Args:
        file_path: Path to the data file (CSV or JSON)
        schema: Validation schema

    Returns:
        (is_valid, list of error messages)
    """
    path = Path(file_path)

    if not path.exists():
        return False, [f"File not found: {file_path}"]

    # Load data based on file type
    suffix = path.suffix.lower()

    if suffix == ".json":
        with open(path) as f:
            data = json.load(f)
    elif suffix == ".csv":
        # Placeholder: Use pandas or csv module
        # import pandas as pd
        # data = pd.read_csv(path).to_dict(orient='records')
        return False, ["CSV loading not implemented in template"]
    else:
        return False, [f"Unsupported file type: {suffix}"]

    validator = DataValidator(schema)
    return validator.validate(data)


def main():
    """CLI entry point for validation."""
    parser = argparse.ArgumentParser(description="Validate data file")
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Input data path",
    )
    parser.add_argument(
        "--schema",
        type=str,
        help="Schema JSON file (optional)",
    )
    args = parser.parse_args()

    # Default schema for template
    schema = ValidationSchema(
        required_columns=["id", "value", "category"],
        column_types={"id": int, "value": (int, float), "category": str},
        value_ranges={"value": (0, 1000)},
        allowed_values={"category": ["A", "B", "C"]},
    )

    # Override with custom schema if provided
    if args.schema:
        with open(args.schema) as f:
            schema_dict = json.load(f)
            schema = ValidationSchema(**schema_dict)

    is_valid, errors = validate_file(args.input, schema)

    if is_valid:
        print("Validation passed!")
        return 0
    else:
        print("Validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())

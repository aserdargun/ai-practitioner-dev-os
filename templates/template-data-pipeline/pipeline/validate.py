"""Data validation utilities."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class Schema:
    """Schema definition for data validation."""

    columns: Dict[str, Dict[str, Any]]

    def get_required_columns(self) -> List[str]:
        """Return list of required column names."""
        return [
            name
            for name, config in self.columns.items()
            if config.get("required", False)
        ]

    def get_column_type(self, column: str) -> Optional[str]:
        """Return expected type for a column."""
        if column in self.columns:
            return self.columns[column].get("type")
        return None


@dataclass
class ValidationResult:
    """Result of data validation."""

    is_valid: bool
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    stats: Dict[str, Any] = field(default_factory=dict)

    def add_error(self, message: str) -> None:
        """Add an error message."""
        self.errors.append(message)
        self.is_valid = False

    def add_warning(self, message: str) -> None:
        """Add a warning message."""
        self.warnings.append(message)


class DataValidator:
    """Validates data against a schema."""

    TYPE_MAP = {
        "int": (int,),
        "float": (int, float),
        "str": (str,),
        "bool": (bool,),
    }

    def __init__(self, schema: Schema):
        """Initialize validator with schema."""
        self.schema = schema

    def validate(self, data: List[Dict[str, Any]]) -> ValidationResult:
        """Validate data against schema."""
        result = ValidationResult(is_valid=True)
        result.stats["total_rows"] = len(data)
        result.stats["validated_at"] = self._current_timestamp()

        if not data:
            result.add_warning("Empty dataset")
            return result

        # Check required columns exist
        self._validate_required_columns(data[0], result)

        # Validate each row
        for i, row in enumerate(data):
            self._validate_row(row, i, result)

        result.stats["error_count"] = len(result.errors)
        result.stats["warning_count"] = len(result.warnings)

        return result

    def _validate_required_columns(
        self, sample_row: Dict[str, Any], result: ValidationResult
    ) -> None:
        """Check that all required columns are present."""
        required = self.schema.get_required_columns()
        present = set(sample_row.keys())

        for col in required:
            if col not in present:
                result.add_error(f"Missing required column: {col}")

    def _validate_row(
        self, row: Dict[str, Any], row_index: int, result: ValidationResult
    ) -> None:
        """Validate a single row."""
        for col_name, col_config in self.schema.columns.items():
            if col_name not in row:
                continue

            value = row[col_name]

            # Check required fields for null
            if col_config.get("required") and value is None:
                result.add_error(f"Row {row_index}: Required field '{col_name}' is null")
                continue

            if value is None:
                continue

            # Type validation
            expected_type = col_config.get("type")
            if expected_type and not self._check_type(value, expected_type):
                result.add_error(
                    f"Row {row_index}: Field '{col_name}' expected {expected_type}, "
                    f"got {type(value).__name__}"
                )

            # Range validation
            if "min" in col_config and value < col_config["min"]:
                result.add_error(
                    f"Row {row_index}: Field '{col_name}' value {value} "
                    f"below minimum {col_config['min']}"
                )

            if "max" in col_config and value > col_config["max"]:
                result.add_error(
                    f"Row {row_index}: Field '{col_name}' value {value} "
                    f"above maximum {col_config['max']}"
                )

            # Allowed values validation
            if "allowed" in col_config and value not in col_config["allowed"]:
                result.add_error(
                    f"Row {row_index}: Field '{col_name}' value '{value}' "
                    f"not in allowed values: {col_config['allowed']}"
                )

    def _check_type(self, value: Any, expected_type: str) -> bool:
        """Check if value matches expected type."""
        allowed_types = self.TYPE_MAP.get(expected_type)
        if allowed_types is None:
            return True  # Unknown type, skip check
        return isinstance(value, allowed_types)

    def _current_timestamp(self) -> str:
        """Return current timestamp as ISO string."""
        from datetime import datetime

        return datetime.utcnow().isoformat() + "Z"


def validate_file(file_path: str, schema: Schema) -> ValidationResult:
    """Convenience function to validate a file."""
    from pathlib import Path

    path = Path(file_path)
    if not path.exists():
        result = ValidationResult(is_valid=False)
        result.add_error(f"File not found: {file_path}")
        return result

    # Simple CSV parsing
    data = []
    with open(path, "r") as f:
        lines = f.readlines()
        if lines:
            headers = [h.strip() for h in lines[0].split(",")]
            for line in lines[1:]:
                values = [v.strip() for v in line.split(",")]
                if len(values) == len(headers):
                    row = dict(zip(headers, values))
                    # Type conversion
                    for key, value in row.items():
                        if value == "":
                            row[key] = None
                        elif value.isdigit():
                            row[key] = int(value)
                        else:
                            try:
                                row[key] = float(value)
                            except ValueError:
                                pass
                    data.append(row)

    validator = DataValidator(schema)
    return validator.validate(data)

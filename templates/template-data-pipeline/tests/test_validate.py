"""Tests for data validation."""

import pytest

# Add pipeline directory to path
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "pipeline"))

from validate import DataValidator, ValidationSchema


class TestValidationSchema:
    """Tests for ValidationSchema."""

    def test_schema_defaults(self):
        """Schema should have sensible defaults."""
        schema = ValidationSchema()
        assert schema.required_columns == []
        assert schema.column_types == {}
        assert schema.nullable_columns == []

    def test_schema_with_columns(self):
        """Schema should accept column definitions."""
        schema = ValidationSchema(
            required_columns=["id", "name"],
            column_types={"id": int, "name": str},
        )
        assert "id" in schema.required_columns
        assert schema.column_types["id"] == int


class TestDataValidator:
    """Tests for DataValidator."""

    @pytest.fixture
    def simple_schema(self):
        """Create a simple validation schema."""
        return ValidationSchema(
            required_columns=["id", "value"],
            column_types={"id": int, "value": (int, float)},
        )

    @pytest.fixture
    def strict_schema(self):
        """Create a strict validation schema with ranges and allowed values."""
        return ValidationSchema(
            required_columns=["id", "value", "category"],
            column_types={"id": int, "value": (int, float), "category": str},
            value_ranges={"value": (0, 100)},
            allowed_values={"category": ["A", "B", "C"]},
        )

    def test_valid_data(self, simple_schema):
        """Valid data should pass validation."""
        data = [
            {"id": 1, "value": 100},
            {"id": 2, "value": 200},
        ]
        validator = DataValidator(simple_schema)
        is_valid, errors = validator.validate(data)
        assert is_valid is True
        assert errors == []

    def test_empty_data(self, simple_schema):
        """Empty data should fail validation."""
        validator = DataValidator(simple_schema)
        is_valid, errors = validator.validate([])
        assert is_valid is False
        assert "Data is empty" in errors

    def test_missing_required_column(self, simple_schema):
        """Missing required column should fail validation."""
        data = [{"id": 1}]  # Missing 'value'
        validator = DataValidator(simple_schema)
        is_valid, errors = validator.validate(data)
        assert is_valid is False
        assert any("Missing required column: value" in e for e in errors)

    def test_wrong_type(self, simple_schema):
        """Wrong column type should fail validation."""
        data = [{"id": "not_an_int", "value": 100}]
        validator = DataValidator(simple_schema)
        is_valid, errors = validator.validate(data)
        assert is_valid is False
        assert any("type" in e.lower() for e in errors)

    def test_value_out_of_range(self, strict_schema):
        """Value outside range should fail validation."""
        data = [{"id": 1, "value": 999, "category": "A"}]  # value > 100
        validator = DataValidator(strict_schema)
        is_valid, errors = validator.validate(data)
        assert is_valid is False
        assert any("outside range" in e for e in errors)

    def test_invalid_category(self, strict_schema):
        """Invalid category should fail validation."""
        data = [{"id": 1, "value": 50, "category": "X"}]  # X not in [A, B, C]
        validator = DataValidator(strict_schema)
        is_valid, errors = validator.validate(data)
        assert is_valid is False
        assert any("not in allowed values" in e for e in errors)

    def test_null_in_required_column(self):
        """Null in required non-nullable column should fail."""
        schema = ValidationSchema(
            required_columns=["id", "value"],
            nullable_columns=[],  # value is not nullable
        )
        data = [{"id": 1, "value": None}]
        validator = DataValidator(schema)
        is_valid, errors = validator.validate(data)
        assert is_valid is False
        assert any("cannot be null" in e for e in errors)

    def test_null_in_nullable_column(self):
        """Null in nullable column should pass."""
        schema = ValidationSchema(
            required_columns=["id", "value"],
            nullable_columns=["value"],  # value is nullable
        )
        data = [{"id": 1, "value": None}]
        validator = DataValidator(schema)
        is_valid, errors = validator.validate(data)
        assert is_valid is True

    def test_multiple_rows_validation(self, strict_schema):
        """Multiple rows should all be validated."""
        data = [
            {"id": 1, "value": 50, "category": "A"},  # Valid
            {"id": 2, "value": 150, "category": "B"},  # Invalid: value > 100
            {"id": 3, "value": 30, "category": "X"},  # Invalid: category not allowed
        ]
        validator = DataValidator(strict_schema)
        is_valid, errors = validator.validate(data)
        assert is_valid is False
        assert len(errors) == 2  # Two invalid rows

    def test_accepts_multiple_types(self):
        """Column accepting multiple types should validate both."""
        schema = ValidationSchema(
            required_columns=["value"],
            column_types={"value": (int, float)},
        )
        data = [
            {"value": 100},  # int
            {"value": 100.5},  # float
        ]
        validator = DataValidator(schema)
        is_valid, errors = validator.validate(data)
        assert is_valid is True

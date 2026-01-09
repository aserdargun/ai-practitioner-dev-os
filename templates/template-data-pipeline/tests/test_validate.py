"""Tests for data validation."""

import pytest

from pipeline.validate import DataValidator, Schema, ValidationResult


class TestSchema:
    """Tests for Schema class."""

    def test_get_required_columns(self):
        """Should return only required columns."""
        schema = Schema(
            columns={
                "id": {"type": "int", "required": True},
                "name": {"type": "str", "required": True},
                "optional": {"type": "str", "required": False},
            }
        )
        required = schema.get_required_columns()
        assert "id" in required
        assert "name" in required
        assert "optional" not in required

    def test_get_column_type(self):
        """Should return column type."""
        schema = Schema(columns={"id": {"type": "int", "required": True}})
        assert schema.get_column_type("id") == "int"
        assert schema.get_column_type("nonexistent") is None


class TestValidationResult:
    """Tests for ValidationResult class."""

    def test_starts_valid(self):
        """New result should be valid."""
        result = ValidationResult(is_valid=True)
        assert result.is_valid is True

    def test_add_error_marks_invalid(self):
        """Adding error should mark result as invalid."""
        result = ValidationResult(is_valid=True)
        result.add_error("Test error")
        assert result.is_valid is False
        assert "Test error" in result.errors

    def test_add_warning_stays_valid(self):
        """Adding warning should not affect validity."""
        result = ValidationResult(is_valid=True)
        result.add_warning("Test warning")
        assert result.is_valid is True
        assert "Test warning" in result.warnings


class TestDataValidator:
    """Tests for DataValidator class."""

    @pytest.fixture
    def simple_schema(self):
        """Create a simple test schema."""
        return Schema(
            columns={
                "id": {"type": "int", "required": True},
                "value": {"type": "float", "required": True},
                "category": {"type": "str", "required": False},
            }
        )

    def test_valid_data_passes(self, simple_schema):
        """Valid data should pass validation."""
        validator = DataValidator(simple_schema)
        data = [
            {"id": 1, "value": 1.5, "category": "A"},
            {"id": 2, "value": 2.5, "category": "B"},
        ]
        result = validator.validate(data)
        assert result.is_valid is True
        assert len(result.errors) == 0

    def test_missing_required_column_fails(self, simple_schema):
        """Missing required column should fail."""
        validator = DataValidator(simple_schema)
        data = [{"id": 1, "category": "A"}]  # Missing 'value'
        result = validator.validate(data)
        assert result.is_valid is False
        assert any("Missing required column" in e for e in result.errors)

    def test_null_required_field_fails(self, simple_schema):
        """Null in required field should fail."""
        validator = DataValidator(simple_schema)
        data = [{"id": 1, "value": None, "category": "A"}]
        result = validator.validate(data)
        assert result.is_valid is False
        assert any("is null" in e for e in result.errors)

    def test_wrong_type_fails(self, simple_schema):
        """Wrong type should fail."""
        validator = DataValidator(simple_schema)
        data = [{"id": "not_an_int", "value": 1.5, "category": "A"}]
        result = validator.validate(data)
        assert result.is_valid is False
        assert any("expected int" in e for e in result.errors)

    def test_empty_data_warns(self, simple_schema):
        """Empty data should produce warning."""
        validator = DataValidator(simple_schema)
        result = validator.validate([])
        assert result.is_valid is True
        assert any("Empty dataset" in w for w in result.warnings)

    def test_range_validation_min(self):
        """Value below minimum should fail."""
        schema = Schema(
            columns={"value": {"type": "float", "required": True, "min": 0}}
        )
        validator = DataValidator(schema)
        data = [{"value": -1.0}]
        result = validator.validate(data)
        assert result.is_valid is False
        assert any("below minimum" in e for e in result.errors)

    def test_range_validation_max(self):
        """Value above maximum should fail."""
        schema = Schema(
            columns={"value": {"type": "float", "required": True, "max": 100}}
        )
        validator = DataValidator(schema)
        data = [{"value": 150.0}]
        result = validator.validate(data)
        assert result.is_valid is False
        assert any("above maximum" in e for e in result.errors)

    def test_allowed_values_validation(self):
        """Value not in allowed list should fail."""
        schema = Schema(
            columns={
                "status": {
                    "type": "str",
                    "required": True,
                    "allowed": ["active", "inactive"],
                }
            }
        )
        validator = DataValidator(schema)
        data = [{"status": "unknown"}]
        result = validator.validate(data)
        assert result.is_valid is False
        assert any("not in allowed values" in e for e in result.errors)

    def test_optional_null_passes(self, simple_schema):
        """Null in optional field should pass."""
        validator = DataValidator(simple_schema)
        data = [{"id": 1, "value": 1.5, "category": None}]
        result = validator.validate(data)
        assert result.is_valid is True

    def test_stats_populated(self, simple_schema):
        """Validation stats should be populated."""
        validator = DataValidator(simple_schema)
        data = [
            {"id": 1, "value": 1.5, "category": "A"},
            {"id": 2, "value": 2.5, "category": "B"},
        ]
        result = validator.validate(data)
        assert result.stats["total_rows"] == 2
        assert "validated_at" in result.stats

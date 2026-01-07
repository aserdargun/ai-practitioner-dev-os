"""Pydantic models for data validation."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class DataRecord(BaseModel):
    """Model for a single data record."""

    id: int = Field(..., ge=1, description="Unique identifier")
    name: str = Field(..., min_length=1, max_length=100, description="Record name")
    value: float = Field(..., description="Numeric value")
    category: str = Field(..., description="Category classification")
    created_at: Optional[datetime] = Field(default=None, description="Creation timestamp")

    @field_validator("category")
    @classmethod
    def validate_category(cls, v: str) -> str:
        """Validate category is one of allowed values."""
        allowed = {"A", "B", "C", "D"}
        if v.upper() not in allowed:
            raise ValueError(f"Category must be one of {allowed}")
        return v.upper()


class PipelineConfig(BaseModel):
    """Configuration for the data pipeline."""

    input_path: str = Field(..., description="Path to input file")
    output_path: str = Field(..., description="Path to output file")
    validate: bool = Field(default=True, description="Enable validation")
    strict: bool = Field(default=False, description="Fail on validation errors")
    batch_size: int = Field(default=1000, ge=1, description="Processing batch size")


class PipelineResult(BaseModel):
    """Result of pipeline execution."""

    success: bool = Field(..., description="Whether pipeline succeeded")
    rows_processed: int = Field(default=0, description="Number of rows processed")
    rows_failed: int = Field(default=0, description="Number of rows that failed validation")
    output_path: Optional[str] = Field(default=None, description="Path to output file")
    errors: list[str] = Field(default_factory=list, description="List of errors encountered")

"""Pipeline tests."""

import tempfile
from pathlib import Path

import pandas as pd
import pytest

from pipeline.config import (
    ExtractConfig,
    LoadConfig,
    PipelineConfig,
    TransformConfig,
    TransformStep,
)
from pipeline.main import Pipeline
from pipeline.stages.extract import extract_data
from pipeline.stages.load import load_data
from pipeline.stages.transform import drop_nulls, normalize, transform_data


@pytest.fixture
def sample_csv(tmp_path):
    """Create a sample CSV file."""
    csv_path = tmp_path / "test.csv"
    df = pd.DataFrame(
        {
            "id": [1, 2, 3, 4, 5],
            "value": [10.0, 20.0, None, 40.0, 50.0],
            "category": ["A", "B", "A", "B", "A"],
        }
    )
    df.to_csv(csv_path, index=False)
    return csv_path


def test_extract_csv(sample_csv):
    """Test CSV extraction."""
    config = ExtractConfig(source=str(sample_csv), format="csv")
    df = extract_data(config)
    assert len(df) == 5
    assert "id" in df.columns
    assert "value" in df.columns


def test_extract_file_not_found():
    """Test extraction with missing file raises error."""
    config = ExtractConfig(source="nonexistent.csv", format="csv")
    with pytest.raises(FileNotFoundError):
        extract_data(config)


def test_drop_nulls():
    """Test null dropping transform."""
    df = pd.DataFrame({"a": [1, 2, None], "b": [4, None, 6]})
    result = drop_nulls(df)
    assert len(result) == 1
    assert result["a"].iloc[0] == 1


def test_normalize():
    """Test normalization transform."""
    df = pd.DataFrame({"value": [0, 50, 100]})
    result = normalize(df, ["value"])
    assert result["value"].min() == 0.0
    assert result["value"].max() == 1.0
    assert result["value"].iloc[1] == 0.5


def test_transform_data():
    """Test transform pipeline."""
    df = pd.DataFrame({"value": [0, None, 100]})
    config = TransformConfig(
        steps=[
            TransformStep(name="drop_nulls"),
            TransformStep(name="normalize", columns=["value"]),
        ]
    )
    result = transform_data(df, config)
    assert len(result) == 2
    assert result["value"].min() == 0.0
    assert result["value"].max() == 1.0


def test_load_csv(tmp_path):
    """Test CSV loading."""
    df = pd.DataFrame({"a": [1, 2, 3]})
    output_path = tmp_path / "output.csv"
    config = LoadConfig(destination=str(output_path), format="csv")
    load_data(df, config)
    assert output_path.exists()
    loaded = pd.read_csv(output_path)
    assert len(loaded) == 3


def test_full_pipeline(sample_csv, tmp_path):
    """Test full pipeline execution."""
    output_path = tmp_path / "output.csv"
    config = PipelineConfig(
        name="test",
        extract=ExtractConfig(source=str(sample_csv), format="csv"),
        transform=TransformConfig(
            steps=[TransformStep(name="drop_nulls")]
        ),
        load=LoadConfig(destination=str(output_path), format="csv"),
    )
    pipeline = Pipeline(config)
    result = pipeline.run()
    assert result.success
    assert result.rows_processed == 4  # One row dropped (null)
    assert output_path.exists()


def test_pipeline_dry_run(sample_csv, tmp_path):
    """Test pipeline dry run doesn't write output."""
    output_path = tmp_path / "output.csv"
    config = PipelineConfig(
        name="test",
        extract=ExtractConfig(source=str(sample_csv), format="csv"),
        load=LoadConfig(destination=str(output_path), format="csv"),
    )
    pipeline = Pipeline(config)
    result = pipeline.run(dry_run=True)
    assert result.success
    assert not output_path.exists()

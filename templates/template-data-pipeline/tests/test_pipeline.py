"""Tests for the data pipeline."""

import tempfile
from pathlib import Path

import pandas as pd
import pytest

from src.pipeline import DataPipeline


@pytest.fixture
def sample_data():
    """Create sample data for testing."""
    return pd.DataFrame({
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", "Charlie"],
        "value": [10.0, 20.0, 30.0],
        "category": ["A", "B", "C"],
    })


@pytest.fixture
def pipeline():
    """Create pipeline instance."""
    return DataPipeline()


class TestDataPipeline:
    """Tests for DataPipeline class."""

    def test_load_csv(self, pipeline, sample_data):
        """Test loading CSV files."""
        with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as f:
            sample_data.to_csv(f.name, index=False)
            loaded = pipeline.load(f.name)

        assert len(loaded) == 3
        assert list(loaded.columns) == ["id", "name", "value", "category"]

    def test_transform_normalizes_columns(self, pipeline, sample_data):
        """Test that transform normalizes column names."""
        df = sample_data.copy()
        df.columns = ["ID ", "Name", " VALUE", "Category"]

        transformed = pipeline.transform(df)

        assert list(transformed.columns) == ["id", "name", "value", "category"]

    def test_transform_standardizes_categories(self, pipeline, sample_data):
        """Test that transform standardizes categories to uppercase."""
        df = sample_data.copy()
        df["category"] = ["a", "b", "c"]

        transformed = pipeline.transform(df)

        assert list(transformed["category"]) == ["A", "B", "C"]

    def test_save_csv(self, pipeline, sample_data):
        """Test saving to CSV."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "output.csv"
            pipeline.save(sample_data, str(output_path))

            assert output_path.exists()
            loaded = pd.read_csv(output_path)
            assert len(loaded) == 3

    def test_save_parquet(self, pipeline, sample_data):
        """Test saving to Parquet."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "output.parquet"
            pipeline.save(sample_data, str(output_path))

            assert output_path.exists()
            loaded = pd.read_parquet(output_path)
            assert len(loaded) == 3

    def test_run_pipeline_success(self, pipeline, sample_data):
        """Test full pipeline run."""
        with tempfile.TemporaryDirectory() as tmpdir:
            input_path = Path(tmpdir) / "input.csv"
            output_path = Path(tmpdir) / "output.parquet"

            sample_data.to_csv(input_path, index=False)

            result = pipeline.run(
                input_path=str(input_path),
                output_path=str(output_path),
                validate=False,
            )

            assert result.success
            assert result.rows_processed == 3
            assert output_path.exists()

    def test_run_pipeline_with_validation(self, pipeline, sample_data):
        """Test pipeline with validation enabled."""
        with tempfile.TemporaryDirectory() as tmpdir:
            input_path = Path(tmpdir) / "input.csv"
            output_path = Path(tmpdir) / "output.csv"

            sample_data.to_csv(input_path, index=False)

            result = pipeline.run(
                input_path=str(input_path),
                output_path=str(output_path),
                validate=True,
            )

            assert result.success
            assert result.rows_processed == 3

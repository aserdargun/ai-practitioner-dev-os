"""Main data pipeline logic."""

import argparse
import logging
from pathlib import Path

import pandas as pd

from src.models import DataRecord, PipelineConfig, PipelineResult
from src.validators import validate_dataframe

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataPipeline:
    """Data pipeline for processing and validating data."""

    def __init__(self, config: PipelineConfig | None = None):
        """Initialize the pipeline.

        Args:
            config: Pipeline configuration
        """
        self.config = config

    def load(self, path: str) -> pd.DataFrame:
        """Load data from file.

        Args:
            path: Path to input file

        Returns:
            Loaded DataFrame
        """
        path = Path(path)
        logger.info(f"Loading data from {path}")

        if path.suffix == ".csv":
            return pd.read_csv(path)
        elif path.suffix == ".parquet":
            return pd.read_parquet(path)
        elif path.suffix == ".json":
            return pd.read_json(path)
        else:
            raise ValueError(f"Unsupported file format: {path.suffix}")

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Apply transformations to the data.

        Args:
            df: Input DataFrame

        Returns:
            Transformed DataFrame
        """
        logger.info("Applying transformations")

        # Example transformations
        df = df.copy()

        # Normalize column names
        df.columns = [col.lower().strip().replace(" ", "_") for col in df.columns]

        # Handle missing values
        if "value" in df.columns:
            df["value"] = df["value"].fillna(0)

        # Standardize categories
        if "category" in df.columns:
            df["category"] = df["category"].str.upper()

        return df

    def validate(self, df: pd.DataFrame) -> tuple[pd.DataFrame, list[str]]:
        """Validate the data.

        Args:
            df: DataFrame to validate

        Returns:
            Tuple of (valid_df, errors)
        """
        logger.info("Validating data")
        return validate_dataframe(df, DataRecord)

    def save(self, df: pd.DataFrame, path: str) -> None:
        """Save data to file.

        Args:
            df: DataFrame to save
            path: Output path
        """
        path = Path(path)
        logger.info(f"Saving data to {path}")

        path.parent.mkdir(parents=True, exist_ok=True)

        if path.suffix == ".csv":
            df.to_csv(path, index=False)
        elif path.suffix == ".parquet":
            df.to_parquet(path, index=False)
        elif path.suffix == ".json":
            df.to_json(path, orient="records", indent=2)
        else:
            raise ValueError(f"Unsupported file format: {path.suffix}")

    def run(
        self,
        input_path: str,
        output_path: str,
        validate: bool = True,
    ) -> PipelineResult:
        """Run the complete pipeline.

        Args:
            input_path: Path to input file
            output_path: Path to output file
            validate: Whether to validate data

        Returns:
            Pipeline execution result
        """
        errors: list[str] = []
        rows_failed = 0

        try:
            # Load
            df = self.load(input_path)
            total_rows = len(df)
            logger.info(f"Loaded {total_rows} rows")

            # Transform
            df = self.transform(df)

            # Validate
            if validate:
                df, validation_errors = self.validate(df)
                rows_failed = total_rows - len(df)
                errors.extend(validation_errors)

            # Save
            self.save(df, output_path)

            return PipelineResult(
                success=True,
                rows_processed=len(df),
                rows_failed=rows_failed,
                output_path=output_path,
                errors=errors,
            )

        except Exception as e:
            logger.error(f"Pipeline failed: {e}")
            return PipelineResult(
                success=False,
                errors=[str(e)],
            )


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Data Pipeline")
    parser.add_argument("--input", required=True, help="Input file path")
    parser.add_argument("--output", required=True, help="Output file path")
    parser.add_argument("--validate", action="store_true", help="Enable validation")

    args = parser.parse_args()

    pipeline = DataPipeline()
    result = pipeline.run(
        input_path=args.input,
        output_path=args.output,
        validate=args.validate,
    )

    if result.success:
        print(f"Pipeline completed: {result.rows_processed} rows processed")
        if result.rows_failed > 0:
            print(f"  {result.rows_failed} rows failed validation")
    else:
        print(f"Pipeline failed: {result.errors}")
        exit(1)


if __name__ == "__main__":
    main()

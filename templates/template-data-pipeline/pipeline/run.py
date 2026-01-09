"""Data Pipeline Runner.

A reproducible data pipeline with validation and transformation.
"""

import argparse
import json
import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

# Configure logging
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


class PipelineConfig:
    """Pipeline configuration."""

    def __init__(
        self,
        input_path: str,
        output_path: str,
        validation_mode: str = "strict",
    ):
        self.input_path = Path(input_path)
        self.output_path = Path(output_path)
        self.validation_mode = validation_mode
        self.run_id = datetime.now().strftime("%Y%m%d_%H%M%S")


class DataPipeline:
    """Main data pipeline class."""

    def __init__(self, config: PipelineConfig):
        self.config = config
        self.metrics: dict[str, Any] = {}

    def load(self) -> list[dict]:
        """Load data from input source.

        Replace with your actual data loading logic.
        Supports CSV, JSON, Parquet, etc.
        """
        logger.info(f"Loading data from {self.config.input_path}")

        if not self.config.input_path.exists():
            raise FileNotFoundError(f"Input file not found: {self.config.input_path}")

        # Placeholder: Replace with actual loading logic
        # Example with pandas:
        #   import pandas as pd
        #   df = pd.read_csv(self.config.input_path)
        #   return df.to_dict(orient='records')

        # Demo data for template
        data = [
            {"id": 1, "value": 100, "category": "A"},
            {"id": 2, "value": 200, "category": "B"},
            {"id": 3, "value": 150, "category": "A"},
        ]

        self.metrics["rows_loaded"] = len(data)
        logger.info(f"Loaded {len(data)} rows")
        return data

    def validate(self, data: list[dict]) -> tuple[bool, list[str]]:
        """Validate loaded data.

        Returns (is_valid, list of error messages).
        """
        from validate import DataValidator, ValidationSchema

        logger.info("Validating data...")

        # Define your schema
        schema = ValidationSchema(
            required_columns=["id", "value", "category"],
            column_types={"id": int, "value": (int, float), "category": str},
        )

        validator = DataValidator(schema)
        is_valid, errors = validator.validate(data)

        self.metrics["validation_errors"] = len(errors)

        if errors:
            for error in errors:
                logger.warning(f"Validation error: {error}")

        return is_valid, errors

    def transform(self, data: list[dict]) -> list[dict]:
        """Apply transformations to data.

        Replace with your actual transformation logic.
        """
        logger.info("Transforming data...")

        transformed = []
        for row in data:
            # Example transformations
            new_row = row.copy()

            # Add derived columns
            new_row["value_normalized"] = row["value"] / 100.0

            # Add metadata
            new_row["processed_at"] = datetime.now().isoformat()
            new_row["run_id"] = self.config.run_id

            transformed.append(new_row)

        self.metrics["rows_transformed"] = len(transformed)
        logger.info(f"Transformed {len(transformed)} rows")
        return transformed

    def save(self, data: list[dict]) -> None:
        """Save transformed data to output.

        Replace with your actual saving logic.
        """
        logger.info(f"Saving data to {self.config.output_path}")

        # Ensure output directory exists
        self.config.output_path.parent.mkdir(parents=True, exist_ok=True)

        # Placeholder: Replace with actual saving logic
        # Example with pandas:
        #   import pandas as pd
        #   df = pd.DataFrame(data)
        #   df.to_parquet(self.config.output_path)

        # Demo: Save as JSON
        with open(self.config.output_path, "w") as f:
            json.dump(data, f, indent=2, default=str)

        self.metrics["rows_saved"] = len(data)
        logger.info(f"Saved {len(data)} rows")

    def run(self) -> dict[str, Any]:
        """Execute the full pipeline."""
        logger.info(f"Starting pipeline run: {self.config.run_id}")
        start_time = datetime.now()

        try:
            # Load
            data = self.load()

            # Validate
            is_valid, errors = self.validate(data)
            if not is_valid and self.config.validation_mode == "strict":
                raise ValueError(f"Validation failed: {errors}")

            # Transform
            transformed = self.transform(data)

            # Save
            self.save(transformed)

            self.metrics["status"] = "success"
            self.metrics["duration_seconds"] = (
                datetime.now() - start_time
            ).total_seconds()

            logger.info(f"Pipeline completed successfully in {self.metrics['duration_seconds']:.2f}s")

        except Exception as e:
            self.metrics["status"] = "failed"
            self.metrics["error"] = str(e)
            logger.error(f"Pipeline failed: {e}")
            raise

        return self.metrics


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Run data pipeline")
    parser.add_argument(
        "--input",
        type=str,
        default=os.getenv("INPUT_PATH", "data/raw/input.csv"),
        help="Input data path",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=os.getenv("OUTPUT_PATH", "data/processed/output.json"),
        help="Output data path",
    )
    parser.add_argument(
        "--validation-mode",
        type=str,
        choices=["strict", "lenient"],
        default=os.getenv("VALIDATION_MODE", "strict"),
        help="Validation mode",
    )
    args = parser.parse_args()

    config = PipelineConfig(
        input_path=args.input,
        output_path=args.output,
        validation_mode=args.validation_mode,
    )

    pipeline = DataPipeline(config)

    try:
        metrics = pipeline.run()
        print(json.dumps(metrics, indent=2))
        return 0
    except Exception:
        return 1


if __name__ == "__main__":
    sys.exit(main())

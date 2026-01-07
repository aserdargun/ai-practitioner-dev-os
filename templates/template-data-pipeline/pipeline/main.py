"""Pipeline main entry point."""

import argparse
import logging
from dataclasses import dataclass
from pathlib import Path

from pipeline.config import PipelineConfig
from pipeline.stages.extract import extract_data
from pipeline.stages.load import load_data
from pipeline.stages.transform import transform_data

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@dataclass
class PipelineResult:
    """Result of pipeline execution."""

    success: bool
    rows_processed: int
    errors: list[str]


class Pipeline:
    """Data processing pipeline."""

    def __init__(self, config: PipelineConfig):
        """Initialize pipeline with configuration."""
        self.config = config
        self.logger = logging.getLogger(f"pipeline.{config.name}")

    def run(self, dry_run: bool = False) -> PipelineResult:
        """Execute the pipeline.

        Args:
            dry_run: If True, validate only without writing output.

        Returns:
            PipelineResult with execution details.
        """
        errors = []

        try:
            # Extract
            self.logger.info(f"Extracting from {self.config.extract.source}")
            df = extract_data(self.config.extract)
            self.logger.info(f"Extracted {len(df)} rows")

            # Transform
            self.logger.info("Applying transformations")
            df = transform_data(df, self.config.transform)
            self.logger.info(f"Transformed to {len(df)} rows")

            # Load
            if not dry_run:
                self.logger.info(f"Loading to {self.config.load.destination}")
                load_data(df, self.config.load)
                self.logger.info("Load complete")
            else:
                self.logger.info("Dry run - skipping load")

            return PipelineResult(
                success=True,
                rows_processed=len(df),
                errors=errors,
            )

        except Exception as e:
            self.logger.error(f"Pipeline failed: {e}")
            errors.append(str(e))
            return PipelineResult(
                success=False,
                rows_processed=0,
                errors=errors,
            )


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Run data pipeline")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("config.yaml"),
        help="Path to configuration file",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate without writing output",
    )
    args = parser.parse_args()

    config = PipelineConfig.from_yaml(args.config)
    pipeline = Pipeline(config)
    result = pipeline.run(dry_run=args.dry_run)

    if result.success:
        logger.info(f"Pipeline completed: {result.rows_processed} rows processed")
    else:
        logger.error(f"Pipeline failed: {result.errors}")
        exit(1)


if __name__ == "__main__":
    main()

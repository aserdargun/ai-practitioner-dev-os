"""Main data pipeline runner."""

import argparse
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from pipeline.validate import DataValidator, Schema, ValidationResult

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


class PipelineError(Exception):
    """Custom exception for pipeline errors."""

    pass


class DataPipeline:
    """A configurable data processing pipeline."""

    def __init__(self, schema: Optional[Schema] = None):
        """Initialize the pipeline with optional schema."""
        self.schema = schema or self._default_schema()
        self.validator = DataValidator(self.schema)
        self.transformations: List[callable] = []

    def _default_schema(self) -> Schema:
        """Return default schema for demonstration."""
        return Schema(
            columns={
                "id": {"type": "int", "required": True},
                "value": {"type": "float", "required": True},
                "category": {"type": "str", "required": False},
            }
        )

    def add_transformation(self, func: callable) -> "DataPipeline":
        """Add a transformation function to the pipeline."""
        self.transformations.append(func)
        return self

    def load(self, input_path: Path) -> List[Dict[str, Any]]:
        """Load data from CSV file."""
        logger.info(f"Loading data from {input_path}")

        if not input_path.exists():
            raise PipelineError(f"Input file not found: {input_path}")

        # Simple CSV parsing without pandas dependency
        data = []
        with open(input_path, "r") as f:
            lines = f.readlines()
            if not lines:
                return data

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
                                pass  # Keep as string
                    data.append(row)

        logger.info(f"Loaded {len(data)} records")
        return data

    def validate(self, data: List[Dict[str, Any]]) -> ValidationResult:
        """Validate data against schema."""
        logger.info("Validating data...")
        result = self.validator.validate(data)

        if result.is_valid:
            logger.info("Validation passed")
        else:
            logger.warning(f"Validation failed with {len(result.errors)} errors")
            for error in result.errors[:5]:  # Show first 5 errors
                logger.warning(f"  - {error}")

        return result

    def transform(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Apply all transformations to data."""
        logger.info(f"Applying {len(self.transformations)} transformations...")

        result = data
        for i, transform in enumerate(self.transformations):
            logger.debug(f"Applying transformation {i + 1}")
            result = transform(result)

        logger.info("Transformations complete")
        return result

    def save(self, data: List[Dict[str, Any]], output_path: Path) -> None:
        """Save data to CSV file."""
        logger.info(f"Saving data to {output_path}")

        if not data:
            logger.warning("No data to save")
            return

        output_path.parent.mkdir(parents=True, exist_ok=True)

        headers = list(data[0].keys())
        with open(output_path, "w") as f:
            f.write(",".join(headers) + "\n")
            for row in data:
                values = [str(row.get(h, "")) for h in headers]
                f.write(",".join(values) + "\n")

        logger.info(f"Saved {len(data)} records")

    def run(
        self,
        input_path: Path,
        output_path: Path,
        validate_only: bool = False,
    ) -> bool:
        """Run the complete pipeline."""
        logger.info("Starting pipeline run")

        try:
            # Load
            data = self.load(input_path)

            # Validate
            validation_result = self.validate(data)
            if not validation_result.is_valid:
                logger.error("Pipeline aborted due to validation errors")
                return False

            if validate_only:
                logger.info("Validation-only mode, skipping transform and save")
                return True

            # Transform
            transformed = self.transform(data)

            # Save
            self.save(transformed, output_path)

            logger.info("Pipeline completed successfully")
            return True

        except PipelineError as e:
            logger.error(f"Pipeline error: {e}")
            return False
        except Exception as e:
            logger.exception(f"Unexpected error: {e}")
            return False


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Run data pipeline")
    parser.add_argument("--input", "-i", required=True, help="Input file path")
    parser.add_argument("--output", "-o", required=True, help="Output file path")
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Only validate, don't transform",
    )

    args = parser.parse_args()

    pipeline = DataPipeline()

    # Add example transformations
    pipeline.add_transformation(
        lambda data: [
            {**row, "processed": True} for row in data
        ]
    )

    success = pipeline.run(
        input_path=Path(args.input),
        output_path=Path(args.output),
        validate_only=args.validate_only,
    )

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

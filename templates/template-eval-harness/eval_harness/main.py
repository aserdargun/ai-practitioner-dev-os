"""CLI entry point for evaluation harness."""

import argparse
import json
import logging
from pathlib import Path

from eval_harness.config import EvalConfig
from eval_harness.loader import load_data, load_model
from eval_harness.metrics import METRIC_REGISTRY
from eval_harness.reporter import generate_report
from eval_harness.runner import EvaluationRunner

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Evaluate ML models")
    parser.add_argument(
        "--model",
        type=Path,
        required=True,
        help="Path to model file",
    )
    parser.add_argument(
        "--data",
        type=Path,
        required=True,
        help="Path to test data",
    )
    parser.add_argument(
        "--target",
        type=str,
        default="target",
        help="Target column name",
    )
    parser.add_argument(
        "--metrics",
        nargs="+",
        default=["accuracy", "f1_score"],
        help="Metrics to compute",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output file path",
    )
    parser.add_argument(
        "--format",
        choices=["json", "html"],
        default="json",
        help="Output format",
    )
    parser.add_argument(
        "--config",
        type=Path,
        help="Path to config file",
    )
    args = parser.parse_args()

    # Load config if provided
    if args.config and args.config.exists():
        config = EvalConfig.from_yaml(args.config)
    else:
        config = EvalConfig(
            metrics=args.metrics,
            output_format=args.format,
        )

    # Load model and data
    logger.info(f"Loading model from {args.model}")
    model = load_model(args.model)

    logger.info(f"Loading data from {args.data}")
    X, y = load_data(args.data, target_column=args.target)

    # Set up runner with metrics
    runner = EvaluationRunner()
    for metric_name in config.metrics:
        if metric_name in METRIC_REGISTRY:
            runner.add_metric(METRIC_REGISTRY[metric_name]())
        else:
            logger.warning(f"Unknown metric: {metric_name}")

    # Run evaluation
    logger.info("Running evaluation...")
    results = runner.evaluate(model, X, y)

    # Generate report
    if args.output:
        logger.info(f"Generating {args.format} report...")
        generate_report(results, args.output, format=args.format)
        logger.info(f"Report saved to {args.output}")
    else:
        # Print to stdout
        print("\n" + "=" * 50)
        print("EVALUATION RESULTS")
        print("=" * 50)
        print(json.dumps(results.to_dict(), indent=2))

    return 0


if __name__ == "__main__":
    exit(main())

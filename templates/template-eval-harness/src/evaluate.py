"""Main evaluation harness."""

import argparse
import json
import logging
from pathlib import Path
from typing import Any

import yaml

from src.metrics import get_metric, list_metrics
from src.models import EvaluationConfig, EvaluationResult, MetricResult

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class EvaluationHarness:
    """Harness for running evaluations."""

    def __init__(self, config: EvaluationConfig | None = None):
        """Initialize evaluation harness.

        Args:
            config: Evaluation configuration
        """
        self.config = config or EvaluationConfig()

    def run(
        self,
        predictions: list[Any],
        ground_truth: list[Any],
        metrics: list[str] | None = None,
    ) -> EvaluationResult:
        """Run evaluation.

        Args:
            predictions: Model predictions
            ground_truth: Ground truth values
            metrics: Metrics to compute (uses config if not provided)

        Returns:
            Evaluation result
        """
        metrics = metrics or self.config.metrics
        if not metrics:
            metrics = ["accuracy"]  # Default metric

        logger.info(f"Running evaluation with metrics: {metrics}")

        if len(predictions) != len(ground_truth):
            return EvaluationResult(
                success=False,
                errors=["Predictions and ground truth have different lengths"],
            )

        results = []
        errors = []

        for metric_name in metrics:
            try:
                metric_fn = get_metric(metric_name)
                value = metric_fn(predictions, ground_truth)

                # Check threshold
                threshold = self.config.thresholds.get(metric_name)
                passed = True
                if threshold is not None:
                    passed = value >= threshold

                results.append(
                    MetricResult(
                        name=metric_name,
                        value=value,
                        passed=passed,
                        threshold=threshold,
                    )
                )
                logger.info(f"  {metric_name}: {value:.4f}")

            except Exception as e:
                errors.append(f"Error computing {metric_name}: {e}")
                logger.error(f"  {metric_name}: ERROR - {e}")

        overall_passed = all(r.passed for r in results)

        return EvaluationResult(
            success=len(errors) == 0,
            metrics=results,
            overall_passed=overall_passed,
            samples_evaluated=len(predictions),
            errors=errors,
        )

    def run_from_file(self, data_file: str) -> EvaluationResult:
        """Run evaluation from data file.

        Args:
            data_file: Path to evaluation data JSON

        Returns:
            Evaluation result
        """
        with open(data_file) as f:
            data = json.load(f)

        predictions = data.get("predictions", [])
        ground_truth = data.get("ground_truth", [])

        return self.run(predictions, ground_truth)


def load_config(config_file: str) -> EvaluationConfig:
    """Load evaluation config from YAML file.

    Args:
        config_file: Path to config file

    Returns:
        Evaluation configuration
    """
    with open(config_file) as f:
        data = yaml.safe_load(f)

    eval_config = data.get("evaluation", {})
    return EvaluationConfig(**eval_config)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Run evaluation")
    parser.add_argument("--config", help="Path to config file")
    parser.add_argument("--data", help="Path to evaluation data JSON")
    parser.add_argument("--metrics", nargs="+", help="Metrics to compute")
    parser.add_argument("--list-metrics", action="store_true", help="List available metrics")

    args = parser.parse_args()

    if args.list_metrics:
        print("Available metrics:")
        for metric in list_metrics():
            print(f"  - {metric}")
        return

    # Load config
    if args.config:
        config = load_config(args.config)
    else:
        config = EvaluationConfig()

    if args.metrics:
        config.metrics = args.metrics

    harness = EvaluationHarness(config)

    # Run evaluation
    if args.data:
        result = harness.run_from_file(args.data)
    else:
        # Demo with sample data
        predictions = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]
        ground_truth = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1]
        result = harness.run(predictions, ground_truth, config.metrics or ["accuracy", "f1"])

    print(result.summary())

    if not result.overall_passed and config.fail_on_threshold:
        exit(1)


if __name__ == "__main__":
    main()

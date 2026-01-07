#!/usr/bin/env python3
"""Example: Running evaluations programmatically.

This script demonstrates how to use the evaluation system.
"""

import json
import subprocess
import sys
from pathlib import Path

# Paths
REPO_ROOT = Path(__file__).parent.parent
PATH_ENGINE = REPO_ROOT / ".claude" / "path-engine"


def run_evaluation(scope: str = "week") -> dict:
    """Run the evaluation script.

    Args:
        scope: Evaluation scope (week, month, overall)

    Returns:
        Evaluation results
    """
    result = subprocess.run(
        [sys.executable, str(PATH_ENGINE / "evaluate.py"), "--scope", scope, "--output", "json"],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )

    if result.returncode != 0:
        print(f"Evaluation failed: {result.stderr}")
        return {}

    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        print(f"Could not parse output: {result.stdout}")
        return {}


def run_adaptation() -> dict:
    """Run the adaptation script.

    Returns:
        Adaptation proposals
    """
    result = subprocess.run(
        [sys.executable, str(PATH_ENGINE / "adapt.py"), "--output", "json"],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )

    if result.returncode != 0:
        print(f"Adaptation failed: {result.stderr}")
        return {}

    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return {}


def print_evaluation_report(evaluation: dict) -> None:
    """Print a formatted evaluation report.

    Args:
        evaluation: Evaluation results
    """
    if not evaluation:
        print("No evaluation results available")
        return

    print("=" * 50)
    print("EVALUATION REPORT")
    print("=" * 50)
    print()
    print(f"Learner: {evaluation.get('learner_id', 'unknown')}")
    print(f"Level: {evaluation.get('level', 'unknown')}")
    print(f"Status: {evaluation.get('status', 'unknown').upper()}")
    print()

    scores = evaluation.get("scores", {})
    print("SCORES")
    print("-" * 30)
    for dimension, score in scores.items():
        bar = "█" * int(score * 10) + "░" * (10 - int(score * 10))
        print(f"  {dimension:12} [{bar}] {score:.0%}")
    print()
    print(f"  {'OVERALL':12} [{evaluation.get('overall', 0):.0%}]")
    print()

    recommendations = evaluation.get("recommendations", [])
    if recommendations:
        print("RECOMMENDATIONS")
        print("-" * 30)
        for rec in recommendations:
            print(f"  • {rec}")
    print()


def check_and_adapt(evaluation: dict) -> None:
    """Check evaluation and suggest adaptations if needed.

    Args:
        evaluation: Evaluation results
    """
    overall = evaluation.get("overall", 0.7)
    status = evaluation.get("status", "on_track")

    print("ADAPTATION CHECK")
    print("-" * 30)

    if overall < 0.6:
        print("⚠️  Score below threshold. Running adaptation analysis...")
        adaptations = run_adaptation()

        mutations = adaptations.get("mutations", [])
        if mutations:
            print(f"\nProposed changes ({len(mutations)}):")
            for m in mutations:
                approval = "⚠️" if m.get("requires_approval") else "✓"
                print(f"  {approval} [{m['type']}] {m['description']}")
        else:
            print("\n  No adaptations proposed")
    else:
        print(f"✓ Score is {overall:.0%} ({status}) - no adaptation needed")


# Example usage
if __name__ == "__main__":
    print("\n=== Running Weekly Evaluation ===\n")

    # Run evaluation
    evaluation = run_evaluation("week")

    # Print report
    print_evaluation_report(evaluation)

    # Check for adaptations
    check_and_adapt(evaluation)

    print("\n" + "=" * 50)
    print("Demo complete!")

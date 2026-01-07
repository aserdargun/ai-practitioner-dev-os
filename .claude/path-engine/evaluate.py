#!/usr/bin/env python3
"""
Evaluate learner progress based on memory files and repo signals.

This script reads the learner's progress log, profile, and best practices
to compute scores across multiple dimensions.

Usage:
    python evaluate.py
    python evaluate.py --output json
    python evaluate.py --scope month

Output:
    Writes evaluation results to stdout and optionally to a JSON file.
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


# Configuration
REPO_ROOT = Path(__file__).parent.parent.parent
MEMORY_DIR = REPO_ROOT / ".claude" / "memory"
OUTPUT_DIR = REPO_ROOT / ".claude" / "path-engine" / "output"


def read_jsonl(filepath: Path) -> list[dict]:
    """Read a JSON Lines file."""
    if not filepath.exists():
        return []
    entries = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    entries.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return entries


def read_json(filepath: Path) -> dict:
    """Read a JSON file."""
    if not filepath.exists():
        return {}
    with open(filepath, "r") as f:
        return json.load(f)


def count_commits(days: int = 7) -> int:
    """Count git commits in the last N days."""
    try:
        result = subprocess.run(
            ["git", "log", f"--since={days} days ago", "--oneline"],
            capture_output=True,
            text=True,
            cwd=REPO_ROOT,
        )
        if result.returncode == 0:
            return len(result.stdout.strip().split("\n")) if result.stdout.strip() else 0
    except Exception:
        pass
    return 0


def check_tests() -> tuple[int, int]:
    """Run pytest and return (passed, failed) counts."""
    try:
        result = subprocess.run(
            ["pytest", "--tb=no", "-q"],
            capture_output=True,
            text=True,
            cwd=REPO_ROOT,
        )
        # Parse pytest output for pass/fail counts
        output = result.stdout
        # Look for pattern like "X passed" or "X failed"
        passed = 0
        failed = 0
        for line in output.split("\n"):
            if "passed" in line:
                parts = line.split()
                for i, p in enumerate(parts):
                    if p == "passed" and i > 0:
                        try:
                            passed = int(parts[i - 1])
                        except ValueError:
                            pass
            if "failed" in line:
                parts = line.split()
                for i, p in enumerate(parts):
                    if p == "failed" and i > 0:
                        try:
                            failed = int(parts[i - 1])
                        except ValueError:
                            pass
        return passed, failed
    except Exception:
        return 0, 0


def count_best_practices() -> int:
    """Count best practice entries."""
    bp_file = MEMORY_DIR / "best_practices.md"
    if not bp_file.exists():
        return 0
    with open(bp_file, "r") as f:
        content = f.read()
    # Count entries by counting "### " headers after the template section
    return content.count("\n### ")


def score_completion(progress_log: list[dict]) -> float:
    """Score based on task completion rate."""
    if not progress_log:
        return 0.0

    completed = sum(1 for e in progress_log if "completed" in e.get("event", "").lower())
    started = sum(1 for e in progress_log if "started" in e.get("event", "").lower())

    if started == 0:
        return 0.5  # Neutral if no tasks started

    return min(1.0, completed / max(1, started))


def score_quality(test_passed: int, test_failed: int) -> float:
    """Score based on test results."""
    total = test_passed + test_failed
    if total == 0:
        return 0.5  # Neutral if no tests

    return test_passed / total


def score_consistency(progress_log: list[dict], commits: int) -> float:
    """Score based on regular activity."""
    # Combine progress log entries and commits
    log_score = min(1.0, len(progress_log) / 10)  # Target: 10 entries
    commit_score = min(1.0, commits / 5)  # Target: 5 commits per week

    return (log_score + commit_score) / 2


def score_growth(best_practices_count: int) -> float:
    """Score based on captured learnings."""
    # Target: 5 best practices
    return min(1.0, best_practices_count / 5)


def score_engagement(progress_log: list[dict]) -> float:
    """Score based on interaction patterns."""
    if not progress_log:
        return 0.0

    # Look for engagement signals
    engagement_events = ["question", "blocker", "retro", "feedback"]
    engaged = sum(
        1 for e in progress_log
        if any(ev in e.get("event", "").lower() for ev in engagement_events)
    )

    return min(1.0, engaged / 3)  # Target: 3 engagement events


def evaluate(scope: str = "week") -> dict:
    """Run full evaluation and return results."""
    # Read data
    progress_log = read_jsonl(MEMORY_DIR / "progress_log.jsonl")
    profile = read_json(MEMORY_DIR / "learner_profile.json")

    # Collect signals
    commits = count_commits(7 if scope == "week" else 30)
    test_passed, test_failed = check_tests()
    best_practices = count_best_practices()

    # Calculate scores
    scores = {
        "completion": round(score_completion(progress_log), 2),
        "quality": round(score_quality(test_passed, test_failed), 2),
        "consistency": round(score_consistency(progress_log, commits), 2),
        "growth": round(score_growth(best_practices), 2),
        "engagement": round(score_engagement(progress_log), 2),
    }

    # Weighted average
    weights = {
        "completion": 0.30,
        "quality": 0.25,
        "consistency": 0.20,
        "growth": 0.15,
        "engagement": 0.10,
    }
    overall = sum(scores[k] * weights[k] for k in scores)

    # Generate recommendations
    recommendations = []
    if scores["completion"] < 0.6:
        recommendations.append("Focus on completing more tasks before starting new ones")
    if scores["quality"] < 0.7:
        recommendations.append("Add tests to improve code quality score")
    if scores["consistency"] < 0.7:
        recommendations.append("Commit more frequently and log progress regularly")
    if scores["growth"] < 0.5:
        recommendations.append("Capture learnings as best practices after each task")
    if scores["engagement"] < 0.5:
        recommendations.append("Ask questions and request feedback more often")

    # Determine status
    if overall >= 0.8:
        status = "excellent"
    elif overall >= 0.6:
        status = "on_track"
    elif overall >= 0.4:
        status = "needs_attention"
    else:
        status = "at_risk"

    return {
        "learner_id": profile.get("learner_id", "unknown"),
        "level": profile.get("level", "unknown"),
        "scope": scope,
        "scores": scores,
        "overall": round(overall, 2),
        "status": status,
        "recommendations": recommendations,
        "signals": {
            "commits": commits,
            "tests_passed": test_passed,
            "tests_failed": test_failed,
            "best_practices": best_practices,
            "log_entries": len(progress_log),
        },
        "evaluated_at": datetime.now(timezone.utc).isoformat(),
    }


def print_report(result: dict) -> None:
    """Print human-readable evaluation report."""
    print("=" * 50)
    print("  EVALUATION REPORT")
    print("=" * 50)
    print()
    print(f"Learner: {result['learner_id']} ({result['level']})")
    print(f"Scope: {result['scope']}")
    print(f"Status: {result['status'].upper()}")
    print()

    print("SCORES")
    print("-" * 30)
    for dimension, score in result["scores"].items():
        bar = "█" * int(score * 10) + "░" * (10 - int(score * 10))
        print(f"  {dimension:12} [{bar}] {score:.0%}")
    print()
    print(f"  {'OVERALL':12} [{result['overall']:.0%}]")
    print()

    print("SIGNALS")
    print("-" * 30)
    signals = result["signals"]
    print(f"  Commits: {signals['commits']}")
    print(f"  Tests: {signals['tests_passed']} passed, {signals['tests_failed']} failed")
    print(f"  Best Practices: {signals['best_practices']}")
    print(f"  Log Entries: {signals['log_entries']}")
    print()

    if result["recommendations"]:
        print("RECOMMENDATIONS")
        print("-" * 30)
        for rec in result["recommendations"]:
            print(f"  • {rec}")
        print()

    print(f"Evaluated at: {result['evaluated_at']}")
    print("=" * 50)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Evaluate learner progress")
    parser.add_argument(
        "--scope",
        choices=["week", "month", "overall"],
        default="week",
        help="Evaluation scope",
    )
    parser.add_argument(
        "--output",
        choices=["text", "json"],
        default="text",
        help="Output format",
    )
    parser.add_argument(
        "--save",
        action="store_true",
        help="Save results to output directory",
    )

    args = parser.parse_args()

    result = evaluate(args.scope)

    if args.output == "json":
        print(json.dumps(result, indent=2))
    else:
        print_report(result)

    if args.save:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        output_file = OUTPUT_DIR / f"evaluation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(output_file, "w") as f:
            json.dump(result, f, indent=2)
        print(f"\nResults saved to: {output_file}")

    # Exit with appropriate code
    sys.exit(0 if result["status"] in ["excellent", "on_track"] else 1)


if __name__ == "__main__":
    main()

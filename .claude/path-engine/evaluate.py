#!/usr/bin/env python3
"""
Evaluate learner progress and output scores.

Reads from .claude/memory/* and computes scores for:
- Completion: Tasks done vs planned
- Quality: Observable quality signals
- Velocity: Progress rate and trends
- Learning: Reflection and practice capture

Usage:
    python evaluate.py [--json] [--month N]

Output:
    Scores by dimension with explanations.
    Use --json for machine-readable output.

Note: This script uses Python stdlib only.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any


# Find repo root
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent.parent
MEMORY_DIR = REPO_ROOT / ".claude" / "memory"
PATHS_DIR = REPO_ROOT / "paths" / "beginner"


def load_jsonl(filepath: Path) -> list[dict]:
    """Load JSON Lines file."""
    entries = []
    if filepath.exists():
        with open(filepath, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        entries.append(json.loads(line))
                    except json.JSONDecodeError:
                        continue
    return entries


def load_json(filepath: Path) -> dict:
    """Load JSON file."""
    if filepath.exists():
        with open(filepath, "r") as f:
            return json.load(f)
    return {}


def count_file_lines(filepath: Path) -> int:
    """Count non-empty lines in a file."""
    if not filepath.exists():
        return 0
    with open(filepath, "r") as f:
        return sum(1 for line in f if line.strip())


def parse_timestamp(ts: str) -> datetime:
    """Parse ISO timestamp."""
    # Handle various formats
    ts = ts.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(ts)
    except:
        return datetime.now()


def get_recent_events(events: list[dict], days: int = 30) -> list[dict]:
    """Filter events from last N days."""
    cutoff = datetime.now() - timedelta(days=days)
    recent = []
    for event in events:
        ts = event.get("timestamp", "")
        if ts:
            event_time = parse_timestamp(ts)
            if event_time.replace(tzinfo=None) > cutoff:
                recent.append(event)
    return recent


def evaluate_completion(progress: list[dict], profile: dict) -> dict:
    """Evaluate task completion."""
    # Count completion events
    completed = [e for e in progress if e.get("event") == "task_completed"]
    week_completions = [e for e in progress if e.get("event") == "week_completed"]

    # Recent activity
    recent = get_recent_events(progress, days=30)
    recent_completed = [e for e in recent if e.get("event") == "task_completed"]

    # Calculate score (simplified)
    # In real implementation, would compare against expected tasks
    base_score = min(len(completed) * 5, 50)  # Up to 50 points for tasks
    week_score = min(len(week_completions) * 10, 30)  # Up to 30 for weeks
    activity_score = min(len(recent_completed) * 2, 20)  # Up to 20 for recency

    score = base_score + week_score + activity_score

    return {
        "score": min(score, 100),
        "tasks_completed": len(completed),
        "weeks_completed": len(week_completions),
        "recent_tasks": len(recent_completed),
        "explanation": f"{len(completed)} tasks, {len(week_completions)} weeks completed"
    }


def evaluate_quality(progress: list[dict], profile: dict) -> dict:
    """Evaluate quality signals."""
    # Look for quality-related events
    hardening_events = [e for e in progress if "harden" in e.get("event", "").lower()]
    review_events = [e for e in progress if "review" in e.get("event", "").lower()]
    test_events = [e for e in progress if "test" in e.get("event", "").lower()]

    # Check for publish events (indicate quality bar met)
    publish_events = [e for e in progress if "publish" in e.get("event", "").lower()]

    # Calculate score
    base_score = 50  # Start at midpoint
    hardening_bonus = min(len(hardening_events) * 10, 20)
    review_bonus = min(len(review_events) * 5, 15)
    publish_bonus = min(len(publish_events) * 15, 30)

    score = base_score + hardening_bonus + review_bonus + publish_bonus

    return {
        "score": min(score, 100),
        "hardening_events": len(hardening_events),
        "review_events": len(review_events),
        "publish_events": len(publish_events),
        "explanation": f"Quality signals: {len(hardening_events)} hardens, {len(review_events)} reviews, {len(publish_events)} publishes"
    }


def evaluate_velocity(progress: list[dict], profile: dict) -> dict:
    """Evaluate progress velocity."""
    recent = get_recent_events(progress, days=14)
    older = get_recent_events(progress, days=28)

    recent_count = len(recent)
    older_count = len(older) - recent_count  # Events from 14-28 days ago

    # Calculate trend
    if older_count > 0:
        trend = (recent_count - older_count) / older_count
    else:
        trend = 0 if recent_count == 0 else 1

    # Calculate score based on activity and trend
    activity_score = min(recent_count * 5, 60)
    trend_score = 20 + int(trend * 20)  # -20 to +20 based on trend
    trend_score = max(0, min(40, trend_score))

    score = activity_score + trend_score

    # Determine trend direction
    if trend > 0.1:
        trend_direction = "improving"
    elif trend < -0.1:
        trend_direction = "declining"
    else:
        trend_direction = "stable"

    return {
        "score": min(score, 100),
        "recent_events": recent_count,
        "trend": round(trend, 2),
        "trend_direction": trend_direction,
        "explanation": f"Velocity {trend_direction}: {recent_count} events in last 2 weeks"
    }


def evaluate_learning(progress: list[dict], best_practices: int, profile: dict) -> dict:
    """Evaluate learning and reflection."""
    # Count learning events
    retro_events = [e for e in progress if "retro" in e.get("event", "").lower()]
    journal_events = [e for e in progress if "journal" in e.get("event", "").lower() or "reflection" in e.get("event", "").lower()]

    # Calculate score
    retro_score = min(len(retro_events) * 15, 30)
    journal_score = min(len(journal_events) * 10, 30)
    practice_score = min(best_practices * 5, 40)

    score = retro_score + journal_score + practice_score

    return {
        "score": min(score, 100),
        "retros_completed": len(retro_events),
        "journal_entries": len(journal_events),
        "best_practices": best_practices,
        "explanation": f"{len(retro_events)} retros, {best_practices} best practices captured"
    }


def run_evaluation(month: int = None) -> dict:
    """Run full evaluation."""
    # Load data
    progress = load_jsonl(MEMORY_DIR / "progress_log.jsonl")
    profile = load_json(MEMORY_DIR / "learner_profile.json")
    decisions = load_jsonl(MEMORY_DIR / "decisions.jsonl")

    # Count best practices (approximate by counting headers)
    bp_file = MEMORY_DIR / "best_practices.md"
    best_practices_count = 0
    if bp_file.exists():
        with open(bp_file, "r") as f:
            content = f.read()
            best_practices_count = content.count("### ")

    # Run evaluations
    completion = evaluate_completion(progress, profile)
    quality = evaluate_quality(progress, profile)
    velocity = evaluate_velocity(progress, profile)
    learning = evaluate_learning(progress, best_practices_count, profile)

    # Calculate overall score
    weights = {"completion": 0.30, "quality": 0.25, "velocity": 0.25, "learning": 0.20}
    overall = (
        completion["score"] * weights["completion"] +
        quality["score"] * weights["quality"] +
        velocity["score"] * weights["velocity"] +
        learning["score"] * weights["learning"]
    )

    return {
        "timestamp": datetime.now().isoformat(),
        "overall_score": round(overall),
        "dimensions": {
            "completion": completion,
            "quality": quality,
            "velocity": velocity,
            "learning": learning
        },
        "profile": {
            "level": profile.get("level", "beginner"),
            "hours_per_week": profile.get("constraints", {}).get("hours_per_week", 10)
        },
        "data_summary": {
            "progress_events": len(progress),
            "decisions": len(decisions),
            "best_practices": best_practices_count
        }
    }


def print_report(evaluation: dict):
    """Print human-readable evaluation report."""
    print("=" * 50)
    print("EVALUATION REPORT")
    print(f"Generated: {evaluation['timestamp']}")
    print("=" * 50)
    print()

    overall = evaluation["overall_score"]
    print(f"OVERALL SCORE: {overall}/100", end=" ")
    if overall >= 70:
        print("(On Track)")
    elif overall >= 50:
        print("(Needs Attention)")
    else:
        print("(At Risk)")
    print()

    print("DIMENSION SCORES")
    print("-" * 50)

    dims = evaluation["dimensions"]
    for name, data in dims.items():
        score = data["score"]
        bar = "█" * (score // 5) + "░" * (20 - score // 5)
        status = "✓" if score >= 60 else "⚠" if score >= 40 else "✗"
        print(f"{name.capitalize():12} {bar} {score:3}/100 {status}")
        print(f"             {data['explanation']}")
        print()

    print("DATA SUMMARY")
    print("-" * 50)
    summary = evaluation["data_summary"]
    print(f"Progress events: {summary['progress_events']}")
    print(f"Decisions logged: {summary['decisions']}")
    print(f"Best practices: {summary['best_practices']}")
    print()

    print("RECOMMENDATIONS")
    print("-" * 50)
    # Generate recommendations based on scores
    for name, data in dims.items():
        if data["score"] < 60:
            if name == "completion":
                print("• Focus on completing planned tasks before adding new ones")
            elif name == "quality":
                print("• Run /harden on recent work to improve quality signals")
            elif name == "velocity":
                print("• Check for blockers with /debug-learning")
            elif name == "learning":
                print("• Run /retro to capture reflections and learnings")

    print()
    print("Run 'python adapt.py' to see adaptation proposals.")


def main():
    parser = argparse.ArgumentParser(description="Evaluate learner progress")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--month", type=int, help="Evaluate specific month")
    args = parser.parse_args()

    evaluation = run_evaluation(args.month)

    if args.json:
        print(json.dumps(evaluation, indent=2))
    else:
        print_report(evaluation)


if __name__ == "__main__":
    main()

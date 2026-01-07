#!/usr/bin/env python3
"""
evaluate.py - Score learner progress

Reads memory files and computes evaluation scores.
Uses Python stdlib only - no external dependencies.

Usage:
    python .claude/path-engine/evaluate.py

Output:
    Prints evaluation results to stdout
    Appends evaluation event to progress_log.jsonl
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any


# Configuration
REPO_ROOT = Path(__file__).parent.parent.parent
MEMORY_DIR = REPO_ROOT / ".claude" / "memory"
LEARNER_LEVEL = "Beginner"

# Scoring weights
WEIGHTS = {
    "completion": 0.30,
    "quality": 0.25,
    "understanding": 0.25,
    "consistency": 0.20,
}


def load_json(path: Path) -> dict:
    """Load a JSON file."""
    if not path.exists():
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_jsonl(path: Path) -> list:
    """Load a JSONL file."""
    if not path.exists():
        return []
    entries = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                entries.append(json.loads(line))
    return entries


def append_jsonl(path: Path, entry: dict) -> None:
    """Append an entry to a JSONL file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")


def get_recent_events(progress: list, days: int = 7) -> list:
    """Get events from the last N days."""
    cutoff = datetime.utcnow() - timedelta(days=days)
    recent = []
    for event in progress:
        ts = event.get("timestamp", "")
        if ts:
            try:
                event_time = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                if event_time.replace(tzinfo=None) >= cutoff:
                    recent.append(event)
            except ValueError:
                pass
    return recent


def score_completion(progress: list, profile: dict) -> tuple[int, list, list]:
    """Score task completion."""
    recent = get_recent_events(progress, days=7)

    # Count completed tasks
    tasks_completed = len([e for e in recent if e.get("event") == "task_completed"])
    mvps_shipped = len([e for e in recent if e.get("event") == "mvp_shipped"])

    # Calculate score (target: 3-5 tasks per week)
    if tasks_completed >= 5:
        score = 100
    elif tasks_completed >= 3:
        score = 80
    elif tasks_completed >= 1:
        score = 60
    else:
        score = 30

    # Bonus for MVPs
    score = min(100, score + mvps_shipped * 10)

    strengths = []
    gaps = []

    if tasks_completed >= 3:
        strengths.append(f"Completed {tasks_completed} tasks this week")
    else:
        gaps.append(f"Only {tasks_completed} tasks completed (target: 3-5)")

    if mvps_shipped > 0:
        strengths.append(f"Shipped {mvps_shipped} MVP(s)")

    return score, strengths, gaps


def score_quality(progress: list, profile: dict) -> tuple[int, list, list]:
    """Score work quality."""
    recent = get_recent_events(progress, days=14)

    # Look for quality signals
    has_tests = any("test" in str(e).lower() for e in recent)
    has_review = any(e.get("event") == "code_reviewed" for e in recent)
    has_docs = any("doc" in str(e).lower() or "readme" in str(e).lower() for e in recent)

    score = 50  # Base score
    strengths = []
    gaps = []

    if has_tests:
        score += 20
        strengths.append("Writing tests")
    else:
        gaps.append("No tests mentioned in recent work")

    if has_review:
        score += 15
        strengths.append("Getting code reviews")

    if has_docs:
        score += 15
        strengths.append("Documenting work")
    else:
        gaps.append("Documentation could be improved")

    return min(100, score), strengths, gaps


def score_understanding(progress: list, decisions: list) -> tuple[int, list, list]:
    """Score learning understanding."""
    recent_progress = get_recent_events(progress, days=14)
    recent_decisions = get_recent_events(decisions, days=14)

    # Look for understanding signals
    has_reflections = any(e.get("reflection") for e in recent_progress)
    has_decisions = len(recent_decisions) > 0
    has_learning = any("learn" in str(e).lower() for e in recent_progress)

    score = 50
    strengths = []
    gaps = []

    if has_reflections:
        score += 25
        strengths.append("Regular reflections")
    else:
        gaps.append("Missing weekly reflections")

    if has_decisions:
        score += 15
        strengths.append("Documenting decisions")

    if has_learning:
        score += 10
        strengths.append("Explicit learning noted")

    return min(100, score), strengths, gaps


def score_consistency(progress: list, profile: dict) -> tuple[int, list, list]:
    """Score consistency and habit formation."""
    # Look at week starts/ends
    week_starts = [e for e in progress if e.get("event") == "week_start"]
    week_ends = [e for e in progress if e.get("event") == "week_end"]

    # Check for regular patterns
    recent = get_recent_events(progress, days=14)
    days_with_activity = set()
    for event in recent:
        ts = event.get("timestamp", "")
        if ts:
            try:
                dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                days_with_activity.add(dt.date())
            except ValueError:
                pass

    score = 50
    strengths = []
    gaps = []

    # Score based on active days (target: 4-5 days per week)
    active_days = len(days_with_activity)
    if active_days >= 8:
        score += 30
        strengths.append(f"Active {active_days} days in past 2 weeks")
    elif active_days >= 4:
        score += 15
        strengths.append(f"Active {active_days} days in past 2 weeks")
    else:
        gaps.append(f"Only {active_days} active days (target: 4-5/week)")

    # Bonus for week structure
    if len(week_starts) > 0 and len(week_ends) > 0:
        score += 20
        strengths.append("Following weekly structure")
    else:
        gaps.append("Missing week start/end hooks")

    return min(100, score), strengths, gaps


def run_evaluation() -> dict:
    """Run full evaluation."""
    # Load data
    profile = load_json(MEMORY_DIR / "learner_profile.json")
    progress = load_jsonl(MEMORY_DIR / "progress_log.jsonl")
    decisions = load_jsonl(MEMORY_DIR / "decisions.jsonl")

    # Score each category
    completion_score, completion_strengths, completion_gaps = score_completion(progress, profile)
    quality_score, quality_strengths, quality_gaps = score_quality(progress, profile)
    understanding_score, understanding_strengths, understanding_gaps = score_understanding(progress, decisions)
    consistency_score, consistency_strengths, consistency_gaps = score_consistency(progress, profile)

    # Calculate overall score
    overall_score = int(
        completion_score * WEIGHTS["completion"]
        + quality_score * WEIGHTS["quality"]
        + understanding_score * WEIGHTS["understanding"]
        + consistency_score * WEIGHTS["consistency"]
    )

    # Aggregate strengths and gaps
    all_strengths = completion_strengths + quality_strengths + understanding_strengths + consistency_strengths
    all_gaps = completion_gaps + quality_gaps + understanding_gaps + consistency_gaps

    # Generate recommendations
    recommendations = []
    if completion_score < 70:
        recommendations.append("Focus on completing more tasks this week")
    if quality_score < 70:
        recommendations.append("Add tests to your recent code")
    if understanding_score < 70:
        recommendations.append("Complete your weekly reflections")
    if consistency_score < 70:
        recommendations.append("Try to work on learning at least 4 days per week")

    # Build result
    result = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "level": profile.get("level", LEARNER_LEVEL),
        "overall_score": overall_score,
        "categories": {
            "completion": completion_score,
            "quality": quality_score,
            "understanding": understanding_score,
            "consistency": consistency_score,
        },
        "strengths": all_strengths[:5],  # Top 5
        "gaps": all_gaps[:5],  # Top 5
        "recommendations": recommendations,
    }

    return result


def main():
    """Run evaluation and output results."""
    print("=" * 50)
    print("  AI Practitioner Learning OS - Evaluation")
    print("=" * 50)
    print()

    result = run_evaluation()

    # Print results
    print(f"Level: {result['level']}")
    print(f"Overall Score: {result['overall_score']}/100")
    print()

    print("Category Scores:")
    for category, score in result["categories"].items():
        bar = "█" * (score // 10) + "░" * (10 - score // 10)
        print(f"  {category:15} [{bar}] {score}")
    print()

    if result["strengths"]:
        print("Strengths:")
        for s in result["strengths"]:
            print(f"  ✓ {s}")
        print()

    if result["gaps"]:
        print("Gaps:")
        for g in result["gaps"]:
            print(f"  ✗ {g}")
        print()

    if result["recommendations"]:
        print("Recommendations:")
        for r in result["recommendations"]:
            print(f"  → {r}")
        print()

    # Score interpretation
    score = result["overall_score"]
    if score >= 90:
        print("Status: Excellent! Consider acceleration.")
    elif score >= 70:
        print("Status: On track. Keep going!")
    elif score >= 50:
        print("Status: Struggling. Consider remediation.")
    else:
        print("Status: At risk. Remediation recommended.")

    print()
    print("=" * 50)

    # Append to progress log
    progress_entry = {
        "timestamp": result["timestamp"],
        "event": "evaluation",
        "overall_score": result["overall_score"],
        "categories": result["categories"],
        "recommendations": result["recommendations"],
    }
    append_jsonl(MEMORY_DIR / "progress_log.jsonl", progress_entry)
    print("Evaluation logged to progress_log.jsonl")

    # Output JSON for programmatic use
    print()
    print("JSON output:")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

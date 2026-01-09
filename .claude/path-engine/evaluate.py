#!/usr/bin/env python3
"""
evaluate.py — Compute evaluation scores from progress data.

Reads memory files and repository signals to produce scores for user review.
Uses Python standard library only.

Usage:
    python .claude/path-engine/evaluate.py [--month MONTH] [--week WEEK]
"""

import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional


# Configuration
REPO_ROOT = Path(__file__).parent.parent.parent.parent
MEMORY_DIR = REPO_ROOT / ".claude" / "memory"
PATHS_DIR = REPO_ROOT / "paths" / "intermediate"

# Scoring weights
WEIGHTS = {
    "completeness": 0.25,
    "quality": 0.25,
    "learning": 0.25,
    "reflection": 0.25,
}


def load_jsonl(filepath: Path) -> list:
    """Load entries from a JSONL file."""
    entries = []
    if filepath.exists():
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        entries.append(json.loads(line))
                    except json.JSONDecodeError:
                        pass
    return entries


def load_json(filepath: Path) -> dict:
    """Load a JSON file."""
    if filepath.exists():
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def get_recent_entries(entries: list, days: int = 7) -> list:
    """Filter entries to recent ones."""
    cutoff = datetime.utcnow() - timedelta(days=days)
    recent = []
    for entry in entries:
        if "timestamp" in entry:
            try:
                ts = datetime.fromisoformat(entry["timestamp"].replace("Z", "+00:00"))
                if ts.replace(tzinfo=None) > cutoff:
                    recent.append(entry)
            except (ValueError, TypeError):
                pass
    return recent


def count_events(entries: list, event_type: str) -> int:
    """Count events of a specific type."""
    return sum(1 for e in entries if e.get("event") == event_type)


def score_completeness(progress: list, current_month: int) -> tuple:
    """Score based on deliverables completed."""
    # Count milestones in recent progress
    milestones = count_events(progress, "milestone")
    week_completions = count_events(progress, "week_end")

    # Score based on activity
    if milestones >= 4 and week_completions >= 4:
        score = 95
        evidence = f"{milestones} milestones, {week_completions} weeks completed"
    elif milestones >= 2 and week_completions >= 2:
        score = 80
        evidence = f"{milestones} milestones, {week_completions} weeks completed"
    elif milestones >= 1 or week_completions >= 1:
        score = 65
        evidence = f"{milestones} milestones, {week_completions} weeks completed"
    else:
        score = 40
        evidence = "Limited activity recorded"

    return score, evidence


def score_quality(progress: list) -> tuple:
    """Score based on quality signals."""
    # Look for quality-related events
    reviews = count_events(progress, "review")
    tests = count_events(progress, "tests_passed")
    deployments = count_events(progress, "deployment")

    # Score based on quality activities
    quality_score = min(100, 50 + (reviews * 10) + (tests * 15) + (deployments * 20))
    evidence = f"{reviews} reviews, {tests} test runs, {deployments} deployments"

    return quality_score, evidence


def score_learning(progress: list, decisions: list) -> tuple:
    """Score based on learning evidence."""
    # Count learning-related events
    learnings = count_events(progress, "learning")
    experiments = count_events(progress, "experiment")
    best_practices = count_events(progress, "best_practice_added")

    # Count significant decisions
    tech_decisions = sum(1 for d in decisions if d.get("type") in [
        "technology_choice", "architecture_decision", "approach_selection"
    ])

    learning_score = min(100, 50 + (learnings * 10) + (experiments * 8) +
                        (best_practices * 12) + (tech_decisions * 5))
    evidence = f"{learnings} learnings, {experiments} experiments, {best_practices} best practices"

    return learning_score, evidence


def score_reflection(progress: list) -> tuple:
    """Score based on reflection activities."""
    # Count reflection events
    retros = count_events(progress, "retrospective")
    journal_entries = count_events(progress, "journal_entry")
    reflections = count_events(progress, "reflection")

    reflection_score = min(100, 40 + (retros * 15) + (journal_entries * 10) + (reflections * 8))
    evidence = f"{retros} retros, {journal_entries} journal entries, {reflections} reflections"

    return reflection_score, evidence


def compute_overall(scores: dict) -> float:
    """Compute weighted overall score."""
    total = 0.0
    for criterion, score in scores.items():
        weight = WEIGHTS.get(criterion, 0)
        total += score * weight
    return round(total, 1)


def evaluate(month: Optional[int] = None, week: Optional[int] = None) -> dict:
    """Run evaluation and return results."""
    # Load data
    progress = load_jsonl(MEMORY_DIR / "progress_log.jsonl")
    decisions = load_jsonl(MEMORY_DIR / "decisions.jsonl")
    profile = load_json(MEMORY_DIR / "learner_profile.json")

    # Determine current position
    if month is None:
        # Estimate from progress
        month = 1
        for entry in progress:
            if entry.get("month"):
                month = max(month, entry.get("month", 1))

    # Get recent entries (last 30 days for monthly, 7 days for weekly)
    days = 7 if week else 30
    recent_progress = get_recent_entries(progress, days=days)
    recent_decisions = get_recent_entries(decisions, days=days)

    # Compute scores
    completeness_score, completeness_evidence = score_completeness(recent_progress, month)
    quality_score, quality_evidence = score_quality(recent_progress)
    learning_score, learning_evidence = score_learning(recent_progress, recent_decisions)
    reflection_score, reflection_evidence = score_reflection(recent_progress)

    scores = {
        "completeness": completeness_score,
        "quality": quality_score,
        "learning": learning_score,
        "reflection": reflection_score,
    }

    evidence = {
        "completeness": completeness_evidence,
        "quality": quality_evidence,
        "learning": learning_evidence,
        "reflection": reflection_evidence,
    }

    overall = compute_overall(scores)

    # Determine assessment
    if overall >= 90:
        assessment = "Exceptional"
    elif overall >= 80:
        assessment = "Strong"
    elif overall >= 70:
        assessment = "Satisfactory"
    elif overall >= 60:
        assessment = "Needs Improvement"
    else:
        assessment = "At Risk"

    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "month": month,
        "week": week,
        "level": profile.get("level", "intermediate"),
        "scores": scores,
        "evidence": evidence,
        "overall": overall,
        "assessment": assessment,
        "total_entries": len(progress),
        "recent_entries": len(recent_progress),
    }


def print_report(result: dict):
    """Print evaluation report to stdout."""
    print("=" * 60)
    print("EVALUATION REPORT")
    print("=" * 60)
    print(f"Timestamp: {result['timestamp']}")
    print(f"Level: {result['level'].title()}")
    print(f"Month: {result['month']}")
    if result.get('week'):
        print(f"Week: {result['week']}")
    print()

    print("-" * 60)
    print("SCORES")
    print("-" * 60)
    print(f"{'Criterion':<15} {'Score':>8} {'Weight':>8} {'Weighted':>10}")
    print("-" * 60)

    for criterion in WEIGHTS:
        score = result['scores'].get(criterion, 0)
        weight = WEIGHTS[criterion]
        weighted = score * weight
        print(f"{criterion.title():<15} {score:>8.0f} {weight*100:>7.0f}% {weighted:>10.1f}")

    print("-" * 60)
    print(f"{'OVERALL':<15} {result['overall']:>8.1f}")
    print(f"{'Assessment':<15} {result['assessment']:>8}")
    print()

    print("-" * 60)
    print("EVIDENCE")
    print("-" * 60)
    for criterion, evidence in result['evidence'].items():
        print(f"{criterion.title()}: {evidence}")
    print()

    print("-" * 60)
    print("DATA SUMMARY")
    print("-" * 60)
    print(f"Total progress entries: {result['total_entries']}")
    print(f"Recent entries (evaluation window): {result['recent_entries']}")
    print()

    print("=" * 60)
    print("This evaluation is for your review.")
    print("Run `python .claude/path-engine/adapt.py` to see adaptation proposals.")
    print("=" * 60)


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Evaluate learning progress")
    parser.add_argument("--month", type=int, help="Current month (1-12)")
    parser.add_argument("--week", type=int, help="Current week (1-4)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    result = evaluate(month=args.month, week=args.week)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print_report(result)

    return 0


if __name__ == "__main__":
    sys.exit(main())

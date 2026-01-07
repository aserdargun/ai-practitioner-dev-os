#!/usr/bin/env python3
"""
adapt.py - Propose path modifications

Reads evaluation results and proposes allowed adaptations.
Uses Python stdlib only - no external dependencies.

Usage:
    python .claude/path-engine/adapt.py

Output:
    Prints adaptation proposals to stdout
    Appends decision to decisions.jsonl if adaptation proposed
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Optional


# Configuration
REPO_ROOT = Path(__file__).parent.parent.parent
MEMORY_DIR = REPO_ROOT / ".claude" / "memory"

# Allowed adaptation types
ALLOWED_ADAPTATIONS = [
    "level_change",
    "month_reorder",
    "remediation_week",
    "project_swap",
]

# Thresholds
THRESHOLD_ACCELERATE = 90  # Score to consider acceleration
THRESHOLD_REMEDIATE = 60  # Score to consider remediation
THRESHOLD_AT_RISK = 50  # Score for urgent remediation


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


def get_latest_evaluation(progress: list) -> Optional[dict]:
    """Get the most recent evaluation event."""
    evaluations = [e for e in progress if e.get("event") == "evaluation"]
    if not evaluations:
        return None
    return evaluations[-1]


def check_level_change(
    evaluation: dict, profile: dict, decisions: list
) -> Optional[dict]:
    """Check if level change is appropriate."""
    current_level = profile.get("level", "Beginner")
    score = evaluation.get("overall_score", 0)

    # Check for recent level changes (avoid flip-flopping)
    recent_level_changes = [
        d for d in decisions[-5:] if d.get("decision") == "level_change"
    ]
    if recent_level_changes:
        return None  # Don't propose another change too soon

    # Upgrade conditions
    if score >= THRESHOLD_ACCELERATE and current_level == "Beginner":
        return {
            "type": "level_change",
            "from": "Beginner",
            "to": "Intermediate",
            "effective": "next_month_boundary",
            "rationale": f"Consistently scoring {score}+ with strong understanding",
        }

    # Downgrade conditions (only if struggling severely)
    if score < THRESHOLD_AT_RISK and current_level == "Intermediate":
        return {
            "type": "level_change",
            "from": "Intermediate",
            "to": "Beginner",
            "effective": "next_month_boundary",
            "rationale": f"Score {score} indicates need for stronger foundation",
        }

    return None


def check_remediation(
    evaluation: dict, profile: dict, decisions: list
) -> Optional[dict]:
    """Check if remediation week is needed."""
    score = evaluation.get("overall_score", 0)
    categories = evaluation.get("categories", {})
    current_month = profile.get("current_month", 1)
    current_week = profile.get("current_week", 1)

    # Check for recent remediation (avoid too many)
    recent_remediation = [
        d for d in decisions[-3:] if d.get("decision") == "remediation_week"
    ]
    if recent_remediation:
        return None

    if score < THRESHOLD_REMEDIATE:
        # Find weakest category
        weakest = min(categories.items(), key=lambda x: x[1]) if categories else ("general", 50)
        focus_area = weakest[0]

        # Map category to focus topic
        focus_topics = {
            "completion": "task management and delivery",
            "quality": "code quality and testing",
            "understanding": "concepts and fundamentals",
            "consistency": "learning habits and routine",
        }
        focus = focus_topics.get(focus_area, focus_area)

        return {
            "type": "remediation_week",
            "month": current_month,
            "week": current_week + 1,
            "focus": focus,
            "rationale": f"Score {score} with weak {focus_area} ({weakest[1]})",
        }

    return None


def check_month_reorder(
    evaluation: dict, profile: dict, decisions: list
) -> Optional[dict]:
    """Check if month reordering would help."""
    # This is a placeholder - real implementation would analyze
    # learning patterns and suggest better month ordering
    return None


def check_project_swap(
    evaluation: dict, profile: dict, decisions: list
) -> Optional[dict]:
    """Check if project swap would help."""
    # This is a placeholder - real implementation would analyze
    # project fit and suggest alternatives
    return None


def run_adaptation() -> dict:
    """Run adaptation analysis."""
    # Load data
    profile = load_json(MEMORY_DIR / "learner_profile.json")
    progress = load_jsonl(MEMORY_DIR / "progress_log.jsonl")
    decisions = load_jsonl(MEMORY_DIR / "decisions.jsonl")

    # Get latest evaluation
    evaluation = get_latest_evaluation(progress)
    if not evaluation:
        return {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "needs_adaptation": False,
            "message": "No evaluation found. Run /evaluate first.",
            "proposals": [],
        }

    # Check each adaptation type
    proposals = []

    level_change = check_level_change(evaluation, profile, decisions)
    if level_change:
        proposals.append(level_change)

    remediation = check_remediation(evaluation, profile, decisions)
    if remediation:
        proposals.append(remediation)

    month_reorder = check_month_reorder(evaluation, profile, decisions)
    if month_reorder:
        proposals.append(month_reorder)

    project_swap = check_project_swap(evaluation, profile, decisions)
    if project_swap:
        proposals.append(project_swap)

    result = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "evaluation_score": evaluation.get("overall_score", 0),
        "needs_adaptation": len(proposals) > 0,
        "proposals": proposals,
    }

    return result


def main():
    """Run adaptation and output results."""
    print("=" * 50)
    print("  AI Practitioner Learning OS - Adaptation")
    print("=" * 50)
    print()

    result = run_adaptation()

    print(f"Evaluation Score: {result.get('evaluation_score', 'N/A')}")
    print(f"Needs Adaptation: {result['needs_adaptation']}")
    print()

    if result.get("message"):
        print(f"Message: {result['message']}")
        print()

    if result["proposals"]:
        print("Proposed Adaptations:")
        print()
        for i, proposal in enumerate(result["proposals"], 1):
            print(f"  [{i}] {proposal['type'].upper()}")
            for key, value in proposal.items():
                if key != "type":
                    print(f"      {key}: {value}")
            print()

        print("To accept an adaptation, update your learner_profile.json")
        print("and run /report to regenerate your tracker.")
        print()

        # Log proposals to decisions
        for proposal in result["proposals"]:
            decision_entry = {
                "timestamp": result["timestamp"],
                "decision": proposal["type"],
                "status": "proposed",
                **{k: v for k, v in proposal.items() if k != "type"},
            }
            append_jsonl(MEMORY_DIR / "decisions.jsonl", decision_entry)
        print("Proposals logged to decisions.jsonl")
    else:
        print("No adaptations needed at this time.")
        print("Keep up the good work!")

    print()
    print("=" * 50)

    # Output JSON
    print()
    print("JSON output:")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

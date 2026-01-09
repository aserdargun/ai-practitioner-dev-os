#!/usr/bin/env python3
"""
adapt.py — Propose learning path adaptations based on evaluation.

CRITICAL: This script outputs PROPOSALS ONLY. It does NOT automatically
apply changes. All adaptations require explicit user approval.

Usage:
    python .claude/path-engine/adapt.py [--eval-file FILE]
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional


# Configuration
REPO_ROOT = Path(__file__).parent.parent.parent.parent
MEMORY_DIR = REPO_ROOT / ".claude" / "memory"

# Adaptation thresholds
THRESHOLDS = {
    "upgrade": 90,          # Score to consider level upgrade
    "downgrade": 50,        # Score to consider level downgrade
    "remediation": 60,      # Score to suggest remediation
    "acceleration": 95,     # Score to suggest acceleration
}

# Allowed adaptation types
ADAPTATION_TYPES = [
    "level_change",
    "month_reorder",
    "remediation_week",
    "project_swap",
]


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


def get_recent_evaluations(progress: list, count: int = 4) -> list:
    """Get recent evaluation events."""
    evals = [e for e in progress if e.get("event") == "evaluation"]
    return sorted(evals, key=lambda x: x.get("timestamp", ""), reverse=True)[:count]


def analyze_trend(evaluations: list) -> str:
    """Analyze score trend from recent evaluations."""
    if len(evaluations) < 2:
        return "insufficient_data"

    scores = [e.get("overall", 0) for e in evaluations if "overall" in e]
    if len(scores) < 2:
        return "insufficient_data"

    # Compare recent to older
    recent_avg = sum(scores[:2]) / 2 if len(scores) >= 2 else scores[0]
    older_avg = sum(scores[2:]) / len(scores[2:]) if len(scores) > 2 else recent_avg

    diff = recent_avg - older_avg
    if diff > 10:
        return "improving"
    elif diff < -10:
        return "declining"
    else:
        return "stable"


def propose_level_change(profile: dict, overall: float, trend: str) -> Optional[dict]:
    """Propose level change if warranted."""
    current_level = profile.get("level", "intermediate")

    # Check for upgrade
    if overall >= THRESHOLDS["upgrade"] and trend in ["improving", "stable"]:
        if current_level == "beginner":
            return {
                "type": "level_change",
                "from_level": "beginner",
                "to_level": "intermediate",
                "rationale": f"Consistently high scores ({overall:.0f}) with {trend} trend",
                "impact": "Tier 2 technologies will be added to curriculum",
                "risk": "Increased pace may be challenging initially",
            }
        elif current_level == "intermediate":
            return {
                "type": "level_change",
                "from_level": "intermediate",
                "to_level": "advanced",
                "rationale": f"Consistently high scores ({overall:.0f}) with {trend} trend",
                "impact": "Tier 3 technologies will be added to curriculum",
                "risk": "Significant increase in complexity and depth",
            }

    # Check for downgrade
    if overall <= THRESHOLDS["downgrade"] and trend == "declining":
        if current_level == "advanced":
            return {
                "type": "level_change",
                "from_level": "advanced",
                "to_level": "intermediate",
                "rationale": f"Declining scores ({overall:.0f}) suggest pace adjustment needed",
                "impact": "Tier 3 technologies will be removed, focus on Tier 1+2",
                "risk": "None - this is a supportive adjustment",
            }
        elif current_level == "intermediate":
            return {
                "type": "level_change",
                "from_level": "intermediate",
                "to_level": "beginner",
                "rationale": f"Declining scores ({overall:.0f}) suggest foundation focus needed",
                "impact": "Tier 2 technologies will be deferred, focus on Tier 1",
                "risk": "None - this is a supportive adjustment",
            }

    return None


def propose_remediation(scores: dict, overall: float) -> Optional[dict]:
    """Propose remediation if specific areas are weak."""
    if overall > THRESHOLDS["remediation"]:
        return None

    weak_areas = [k for k, v in scores.items() if v < 60]

    if weak_areas:
        return {
            "type": "remediation_week",
            "focus_areas": weak_areas,
            "rationale": f"Below threshold in: {', '.join(weak_areas)}",
            "impact": "Insert 1-week review block before next month",
            "risk": "Extends timeline by 1 week",
        }

    return None


def propose_project_swap(profile: dict, scores: dict) -> Optional[dict]:
    """Propose project swap if engagement is low."""
    # This would typically check for specific patterns
    # For now, just check if learning score is low but others are ok
    if scores.get("learning", 100) < 50 and scores.get("completeness", 0) > 70:
        return {
            "type": "project_swap",
            "rationale": "Low learning engagement despite completion",
            "impact": "Replace current project with alternative of same scope",
            "risk": "May require some rework",
            "note": "Discuss with Coach agent for project alternatives",
        }
    return None


def generate_proposals(
    profile: dict,
    progress: list,
    decisions: list,
    evaluation: Optional[dict] = None
) -> list:
    """Generate adaptation proposals."""
    proposals = []

    # Get evaluation data
    if evaluation:
        overall = evaluation.get("overall", 70)
        scores = evaluation.get("scores", {})
    else:
        # Use most recent evaluation from progress
        recent_evals = get_recent_evaluations(progress)
        if recent_evals:
            overall = recent_evals[0].get("overall", 70)
            scores = recent_evals[0].get("scores", {})
        else:
            overall = 70
            scores = {}

    # Analyze trend
    trend = analyze_trend(get_recent_evaluations(progress))

    # Check for level change
    level_proposal = propose_level_change(profile, overall, trend)
    if level_proposal:
        proposals.append(level_proposal)

    # Check for remediation
    remediation_proposal = propose_remediation(scores, overall)
    if remediation_proposal:
        proposals.append(remediation_proposal)

    # Check for project swap
    swap_proposal = propose_project_swap(profile, scores)
    if swap_proposal:
        proposals.append(swap_proposal)

    return proposals


def print_proposals(proposals: list, profile: dict):
    """Print proposals to stdout."""
    print("=" * 60)
    print("ADAPTATION PROPOSALS")
    print("=" * 60)
    print()
    print("IMPORTANT: These are PROPOSALS only. No changes will be made")
    print("until you explicitly approve them.")
    print()

    if not proposals:
        print("No adaptations proposed at this time.")
        print()
        print("Your current path appears appropriate. Continue with:")
        print(f"  - Level: {profile.get('level', 'intermediate').title()}")
        print("  - Current curriculum unchanged")
        print()
    else:
        print(f"Found {len(proposals)} proposal(s):")
        print()

        for i, proposal in enumerate(proposals, 1):
            print("-" * 60)
            print(f"PROPOSAL {i}: {proposal['type'].replace('_', ' ').title()}")
            print("-" * 60)

            for key, value in proposal.items():
                if key != "type":
                    label = key.replace("_", " ").title()
                    print(f"  {label}: {value}")

            print()

    print("=" * 60)
    print("TO APPROVE PROPOSALS:")
    print("=" * 60)
    print("1. Review each proposal above")
    print("2. For each proposal you approve:")
    print("   - Tell Claude: 'I approve proposal N'")
    print("   - Or manually update the relevant files")
    print("3. Run `python .claude/path-engine/report.py` to update tracker")
    print()
    print("TO REJECT PROPOSALS:")
    print("  Simply do not approve them. No action needed.")
    print("=" * 60)


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Propose path adaptations")
    parser.add_argument("--eval-file", type=str, help="JSON file with evaluation results")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    # Load data
    profile = load_json(MEMORY_DIR / "learner_profile.json")
    progress = load_jsonl(MEMORY_DIR / "progress_log.jsonl")
    decisions = load_jsonl(MEMORY_DIR / "decisions.jsonl")

    # Load evaluation if provided
    evaluation = None
    if args.eval_file:
        eval_path = Path(args.eval_file)
        if eval_path.exists():
            with open(eval_path) as f:
                evaluation = json.load(f)

    # Generate proposals
    proposals = generate_proposals(profile, progress, decisions, evaluation)

    # Output
    if args.json:
        output = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "current_level": profile.get("level", "intermediate"),
            "proposals": proposals,
            "requires_approval": True,
        }
        print(json.dumps(output, indent=2))
    else:
        print_proposals(proposals, profile)

    return 0


if __name__ == "__main__":
    sys.exit(main())

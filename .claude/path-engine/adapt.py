#!/usr/bin/env python3
"""
Generate adaptation proposals based on evaluation.

Proposes changes such as:
- Remediation weeks
- Scope adjustments
- Project swaps
- Level changes (at month boundaries)

Usage:
    python adapt.py [--json]

Output:
    Adaptation proposals for user review and approval.
    NO changes are made automatically.

Note: This script uses Python stdlib only.
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

# Import evaluate for scores
from evaluate import run_evaluation, load_jsonl, load_json


# Constants
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent.parent
MEMORY_DIR = REPO_ROOT / ".claude" / "memory"


# Thresholds for triggering adaptations
THRESHOLDS = {
    "remediation_quality": 55,      # Quality below this suggests remediation
    "remediation_completion": 50,   # Completion below this suggests remediation
    "scope_reduction": 45,          # Overall below this suggests scope reduction
    "level_down": 40,               # Consistent scores below this suggest level down
    "acceleration": 85,             # Consistent scores above this suggest acceleration
}


def generate_proposals(evaluation: dict) -> list[dict]:
    """Generate adaptation proposals based on evaluation."""
    proposals = []
    dims = evaluation["dimensions"]
    overall = evaluation["overall_score"]

    # Check for quality gap -> remediation week
    if dims["quality"]["score"] < THRESHOLDS["remediation_quality"]:
        proposals.append({
            "id": "remediation_quality",
            "type": "remediation_week",
            "title": "Insert Quality Remediation Week",
            "description": "Add a focused week on testing and code quality",
            "rationale": f"Quality score ({dims['quality']['score']}) is below target ({THRESHOLDS['remediation_quality']}). "
                        f"A focused week can help build quality habits.",
            "impact": [
                "Current week's remaining tasks shift by 1 week",
                "Focus on: writing tests, code review, documentation",
                "No change to month-end date (uses buffer time)"
            ],
            "priority": "high" if dims["quality"]["score"] < 40 else "medium"
        })

    # Check for completion gap -> scope reduction
    if dims["completion"]["score"] < THRESHOLDS["remediation_completion"]:
        proposals.append({
            "id": "scope_reduction",
            "type": "scope_adjustment",
            "title": "Reduce Project Scope",
            "description": "Focus on core MVP features, move extras to stretch goals",
            "rationale": f"Completion score ({dims['completion']['score']}) indicates falling behind. "
                        f"Reducing scope helps maintain momentum.",
            "impact": [
                "Move non-essential features to 'stretch goals'",
                "Focus on definition of done for core features",
                "Maintain quality on smaller scope"
            ],
            "priority": "high" if dims["completion"]["score"] < 30 else "medium"
        })

    # Check for velocity decline -> blocker investigation
    if dims["velocity"]["trend_direction"] == "declining":
        proposals.append({
            "id": "velocity_investigation",
            "type": "process_change",
            "title": "Investigate Velocity Decline",
            "description": "Diagnose why progress has slowed",
            "rationale": f"Velocity is {dims['velocity']['trend_direction']} "
                        f"(trend: {dims['velocity']['trend']}). Early intervention helps.",
            "impact": [
                "Run /debug-learning to identify blockers",
                "Review time allocation and constraints",
                "Consider schedule adjustments"
            ],
            "priority": "medium"
        })

    # Check for learning gap -> reflection focus
    if dims["learning"]["score"] < 50:
        proposals.append({
            "id": "learning_focus",
            "type": "process_change",
            "title": "Increase Reflection Practice",
            "description": "Add regular retrospectives and best practice capture",
            "rationale": f"Learning score ({dims['learning']['score']}) is low. "
                        f"Reflection helps consolidate learning and avoid repeated mistakes.",
            "impact": [
                "Schedule weekly /retro sessions",
                "Capture at least one best practice per week",
                "Update journal more regularly"
            ],
            "priority": "low"
        })

    # Check for consistent struggle -> level change consideration
    if overall < THRESHOLDS["level_down"]:
        proposals.append({
            "id": "level_down_consideration",
            "type": "level_change",
            "title": "Consider Level Adjustment",
            "description": "Review if current level matches your situation",
            "rationale": f"Overall score ({overall}) suggests significant challenges. "
                        f"This is informational - only consider at month boundaries.",
            "impact": [
                "Could reduce pace/scope pressure",
                "Focus on fundamentals before advancing",
                "Only applies at month boundaries"
            ],
            "priority": "low",
            "requires_month_boundary": True
        })

    # Check for consistent excellence -> acceleration
    if overall >= THRESHOLDS["acceleration"] and dims["velocity"]["trend_direction"] != "declining":
        proposals.append({
            "id": "acceleration",
            "type": "level_change",
            "title": "Consider Acceleration",
            "description": "You're exceeding expectations - consider advancing faster",
            "rationale": f"Overall score ({overall}) is excellent. "
                        f"You might benefit from more challenge.",
            "impact": [
                "Could add stretch goals to current work",
                "Consider looking ahead to next month topics",
                "Only formal level change at month boundaries"
            ],
            "priority": "low",
            "requires_month_boundary": True
        })

    return proposals


def format_proposal(proposal: dict, index: int) -> str:
    """Format a single proposal for display."""
    lines = [
        "─" * 60,
        f"PROPOSAL {index + 1}: {proposal['title']}",
        "─" * 60,
        "",
        f"Type: {proposal['type']}",
        f"Priority: {proposal['priority'].upper()}",
        "",
        "Description:",
        f"  {proposal['description']}",
        "",
        "Rationale:",
        f"  {proposal['rationale']}",
        "",
        "Impact if approved:",
    ]

    for impact in proposal["impact"]:
        lines.append(f"  • {impact}")

    if proposal.get("requires_month_boundary"):
        lines.append("")
        lines.append("  ⚠ This change only applies at month boundaries")

    lines.append("")
    lines.append(f"Approve this proposal? [Y/N]")
    lines.append("")

    return "\n".join(lines)


def print_proposals(proposals: list[dict], evaluation: dict):
    """Print all proposals in human-readable format."""
    print("=" * 60)
    print("ADAPTATION PROPOSALS")
    print(f"Based on evaluation from: {evaluation['timestamp']}")
    print(f"Overall score: {evaluation['overall_score']}/100")
    print("=" * 60)
    print()

    if not proposals:
        print("No adaptations recommended at this time.")
        print()
        print("Your scores are within acceptable ranges.")
        print("Continue with your current plan!")
        return

    print(f"Found {len(proposals)} proposal(s) for your review:")
    print()

    for i, proposal in enumerate(proposals):
        print(format_proposal(proposal, i))

    print("─" * 60)
    print("IMPORTANT: No changes are made automatically.")
    print("Review each proposal and decide what to approve.")
    print()
    print("To apply approved changes, work with Claude to update:")
    print("  • paths/beginner/tracker.md")
    print("  • .claude/memory/decisions.jsonl")
    print("─" * 60)


def save_proposals(proposals: list[dict], evaluation: dict):
    """Save proposals to a JSON file for later reference."""
    output = {
        "generated": datetime.now().isoformat(),
        "evaluation_score": evaluation["overall_score"],
        "proposals": proposals,
        "status": "pending_review"
    }

    output_path = MEMORY_DIR / "pending_adaptations.json"
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)

    return output_path


def main():
    parser = argparse.ArgumentParser(description="Generate adaptation proposals")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--save", action="store_true", help="Save proposals to file")
    args = parser.parse_args()

    # Run evaluation first
    evaluation = run_evaluation()

    # Generate proposals
    proposals = generate_proposals(evaluation)

    if args.json:
        output = {
            "timestamp": datetime.now().isoformat(),
            "evaluation": evaluation,
            "proposals": proposals
        }
        print(json.dumps(output, indent=2))
    else:
        print_proposals(proposals, evaluation)

    if args.save:
        saved_path = save_proposals(proposals, evaluation)
        print(f"\nProposals saved to: {saved_path}")


if __name__ == "__main__":
    main()

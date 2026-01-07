#!/usr/bin/env python3
"""
Propose learning path adaptations based on evaluation results.

This script analyzes evaluation scores and proposes mutations to the
learning path using only the allowed adaptation types.

Allowed Mutations:
1. level_change - Upgrade or downgrade learner level
2. month_reorder - Swap upcoming month modules
3. remediation_week - Insert a remediation week
4. project_swap - Replace project with equivalent alternative

Usage:
    python adapt.py
    python adapt.py --evaluation-file output/evaluation_xxx.json
    python adapt.py --dry-run

Output:
    Writes adaptation proposals to stdout and optionally applies them.
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


# Configuration
REPO_ROOT = Path(__file__).parent.parent.parent
MEMORY_DIR = REPO_ROOT / ".claude" / "memory"
OUTPUT_DIR = REPO_ROOT / ".claude" / "path-engine" / "output"
PATHS_DIR = REPO_ROOT / "paths"


# Adaptation thresholds
THRESHOLDS = {
    "level_downgrade": 0.4,      # Consider downgrade if overall < 0.4
    "remediation": 0.6,          # Insert remediation if overall < 0.6
    "on_track": 0.8,             # No changes needed if >= 0.6 and < 0.8
    "acceleration": 0.9,         # Consider acceleration if >= 0.9
}


def read_json(filepath: Path) -> dict:
    """Read a JSON file."""
    if not filepath.exists():
        return {}
    with open(filepath, "r") as f:
        return json.load(f)


def append_jsonl(filepath: Path, entry: dict) -> None:
    """Append an entry to a JSON Lines file."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "a") as f:
        f.write(json.dumps(entry) + "\n")


def get_latest_evaluation() -> dict:
    """Get the most recent evaluation result."""
    if not OUTPUT_DIR.exists():
        return {}

    eval_files = sorted(OUTPUT_DIR.glob("evaluation_*.json"), reverse=True)
    if eval_files:
        return read_json(eval_files[0])
    return {}


def propose_level_change(evaluation: dict, current_level: str) -> dict | None:
    """Propose a level change if warranted."""
    overall = evaluation.get("overall", 0.7)
    profile = read_json(MEMORY_DIR / "learner_profile.json")
    current_month = profile.get("current_month", 1)

    # Only consider level changes at month boundaries
    # (simplified: we'll just check if it's been requested)

    if overall < THRESHOLDS["level_downgrade"]:
        levels = ["Beginner", "Intermediate", "Advanced"]
        current_idx = levels.index(current_level) if current_level in levels else 2

        if current_idx > 0:
            return {
                "type": "level_change",
                "description": f"Consider moving from {current_level} to {levels[current_idx - 1]}",
                "details": {
                    "current_level": current_level,
                    "proposed_level": levels[current_idx - 1],
                    "reason": "Overall score is below threshold",
                    "score": overall,
                    "threshold": THRESHOLDS["level_downgrade"],
                },
                "requires_approval": True,
            }

    if overall >= THRESHOLDS["acceleration"]:
        levels = ["Beginner", "Intermediate", "Advanced"]
        current_idx = levels.index(current_level) if current_level in levels else 2

        # For Advanced, suggest acceleration challenges instead
        if current_idx == 2:
            return {
                "type": "level_change",
                "description": "Consider adding stretch goals or acceleration challenges",
                "details": {
                    "current_level": current_level,
                    "proposed_level": "Advanced+",
                    "reason": "Exceeding expectations",
                    "score": overall,
                },
                "requires_approval": True,
            }

    return None


def propose_remediation_week(evaluation: dict) -> dict | None:
    """Propose a remediation week if needed."""
    overall = evaluation.get("overall", 0.7)
    scores = evaluation.get("scores", {})
    recommendations = evaluation.get("recommendations", [])

    if THRESHOLDS["level_downgrade"] <= overall < THRESHOLDS["remediation"]:
        # Identify weak areas
        weak_areas = [k for k, v in scores.items() if v < 0.5]

        return {
            "type": "remediation_week",
            "description": "Insert a remediation week to strengthen weak areas",
            "details": {
                "weak_areas": weak_areas,
                "focus_recommendations": recommendations[:3],
                "reason": "Overall score below on-track threshold",
                "score": overall,
            },
            "requires_approval": False,  # Can auto-apply
        }

    return None


def propose_month_reorder(evaluation: dict, profile: dict) -> dict | None:
    """Propose reordering upcoming months if beneficial."""
    scores = evaluation.get("scores", {})
    current_month = profile.get("current_month", 1)

    # Only suggest reorder if there are clear skill gaps
    # that could be addressed by a different month order
    if scores.get("quality", 1.0) < 0.5 and current_month < 6:
        return {
            "type": "month_reorder",
            "description": "Consider moving a testing/quality-focused month earlier",
            "details": {
                "reason": "Quality scores are low, earlier exposure to testing may help",
                "current_month": current_month,
            },
            "requires_approval": True,
        }

    return None


def propose_project_swap(evaluation: dict, profile: dict) -> dict | None:
    """Propose swapping the current project for an alternative."""
    scores = evaluation.get("scores", {})
    status = evaluation.get("status", "on_track")

    # Suggest swap if engagement is very low
    if scores.get("engagement", 1.0) < 0.3 and scores.get("completion", 1.0) < 0.4:
        return {
            "type": "project_swap",
            "description": "Consider swapping current project for a more engaging alternative",
            "details": {
                "reason": "Low engagement and completion suggest project mismatch",
                "engagement_score": scores.get("engagement"),
                "completion_score": scores.get("completion"),
            },
            "requires_approval": True,
        }

    return None


def generate_adaptations(evaluation: dict) -> dict:
    """Generate all applicable adaptations."""
    profile = read_json(MEMORY_DIR / "learner_profile.json")
    current_level = profile.get("level", "Advanced")

    mutations = []

    # Check each adaptation type
    level_change = propose_level_change(evaluation, current_level)
    if level_change:
        mutations.append(level_change)

    remediation = propose_remediation_week(evaluation)
    if remediation:
        mutations.append(remediation)

    reorder = propose_month_reorder(evaluation, profile)
    if reorder:
        mutations.append(reorder)

    swap = propose_project_swap(evaluation, profile)
    if swap:
        mutations.append(swap)

    # Determine if auto-approved (no changes or only auto-approvable changes)
    requires_manual = any(m.get("requires_approval", True) for m in mutations)

    return {
        "learner_id": profile.get("learner_id", "unknown"),
        "evaluation_overall": evaluation.get("overall", 0),
        "evaluation_status": evaluation.get("status", "unknown"),
        "mutations": mutations,
        "requires_approval": requires_manual and len(mutations) > 0,
        "auto_approved": not requires_manual or len(mutations) == 0,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }


def apply_adaptations(adaptations: dict, dry_run: bool = True) -> None:
    """Apply approved adaptations (if not dry run)."""
    if dry_run:
        print("\n[DRY RUN] Would apply the following changes:")
        for mutation in adaptations.get("mutations", []):
            if not mutation.get("requires_approval", True):
                print(f"  - {mutation['type']}: {mutation['description']}")
        return

    # Log decision
    decision_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "decision_type": "adaptation_proposal",
        "mutations": adaptations["mutations"],
        "auto_approved": adaptations["auto_approved"],
        "applied": not adaptations["requires_approval"],
    }
    append_jsonl(MEMORY_DIR / "decisions.jsonl", decision_entry)

    print("\nAdaptation decision logged.")
    if adaptations["requires_approval"]:
        print("Manual approval required for some mutations.")
        print("Review the proposals and apply manually if appropriate.")


def print_report(adaptations: dict) -> None:
    """Print human-readable adaptation report."""
    print("=" * 50)
    print("  ADAPTATION PROPOSAL")
    print("=" * 50)
    print()
    print(f"Learner: {adaptations['learner_id']}")
    print(f"Evaluation Score: {adaptations['evaluation_overall']:.0%}")
    print(f"Status: {adaptations['evaluation_status'].upper()}")
    print()

    mutations = adaptations.get("mutations", [])

    if not mutations:
        print("No adaptations needed.")
        print("Continue with current learning path.")
    else:
        print(f"PROPOSED MUTATIONS ({len(mutations)})")
        print("-" * 30)
        for i, mutation in enumerate(mutations, 1):
            approval = "⚠️  Requires Approval" if mutation.get("requires_approval") else "✓ Auto-approved"
            print(f"\n{i}. [{mutation['type'].upper()}] {approval}")
            print(f"   {mutation['description']}")
            if mutation.get("details"):
                for key, value in mutation["details"].items():
                    print(f"   • {key}: {value}")

    print()
    print(f"Generated at: {adaptations['generated_at']}")
    print("=" * 50)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Propose learning path adaptations")
    parser.add_argument(
        "--evaluation-file",
        type=Path,
        help="Path to evaluation JSON file (uses latest if not specified)",
    )
    parser.add_argument(
        "--output",
        choices=["text", "json"],
        default="text",
        help="Output format",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=True,
        help="Don't apply changes, just show what would happen",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply auto-approved adaptations",
    )

    args = parser.parse_args()

    # Load evaluation
    if args.evaluation_file:
        evaluation = read_json(args.evaluation_file)
    else:
        evaluation = get_latest_evaluation()

    if not evaluation:
        print("No evaluation found. Run evaluate.py first.")
        sys.exit(1)

    # Generate adaptations
    adaptations = generate_adaptations(evaluation)

    # Output
    if args.output == "json":
        print(json.dumps(adaptations, indent=2))
    else:
        print_report(adaptations)

    # Apply if requested
    if args.apply:
        apply_adaptations(adaptations, dry_run=False)
    elif not args.dry_run:
        apply_adaptations(adaptations, dry_run=False)

    # Save proposal
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_file = OUTPUT_DIR / f"adaptation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, "w") as f:
        json.dump(adaptations, f, indent=2)


if __name__ == "__main__":
    main()

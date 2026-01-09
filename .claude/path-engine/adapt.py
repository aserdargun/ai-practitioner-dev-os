#!/usr/bin/env python3
"""
Adaptation Engine for AI Practitioner Learning OS.

Proposes path adaptations based on evaluation results.
All proposals require explicit user approval.

Usage:
    python adapt.py [--month N] [--json]

Output:
    Adaptation proposals for user review.
"""

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Optional


# Paths
REPO_ROOT = Path(__file__).parent.parent.parent
MEMORY_DIR = REPO_ROOT / ".claude" / "memory"
PATHS_DIR = REPO_ROOT / "paths" / "advanced"

# Import evaluation functions
from evaluate import compute_scores, load_json, load_jsonl, PASSING_THRESHOLD


# Allowed adaptation types (the ONLY mutations this script can propose)
ALLOWED_ADAPTATIONS = [
    "level_change",      # Change learner level
    "month_reorder",     # Swap upcoming months
    "remediation_week",  # Insert remediation week
    "project_swap",      # Replace project with equivalent
]


def analyze_for_adaptations(scores: dict, month: int) -> list[dict]:
    """Analyze scores and generate adaptation proposals."""
    proposals = []

    overall = scores.get("overall", 0)
    completion = scores.get("completion", 0)
    velocity = scores.get("velocity", 0)
    quality = scores.get("quality", 0)

    # Check for level change needs
    if overall < 50:
        # Significantly struggling - consider level downgrade
        proposals.append({
            "type": "level_change",
            "from": "advanced",
            "to": "intermediate",
            "rationale": f"Overall score ({overall:.1f}%) is significantly below threshold. Reducing scope may help build momentum.",
            "reversible": True,
            "review_at_month": month + 3,
        })

    # Check for remediation needs
    if completion < 60 and overall < PASSING_THRESHOLD:
        proposals.append({
            "type": "remediation_week",
            "month": month,
            "insert_after_week": 4,
            "focus": "Complete remaining deliverables from current month",
            "rationale": f"Completion score ({completion:.1f}%) is low. Extra week to finish DoD items.",
            "impact": f"Month {month + 1:02d} starts 1 week later",
        })

    if velocity < 50 and overall < PASSING_THRESHOLD:
        proposals.append({
            "type": "remediation_week",
            "month": month,
            "insert_after_week": 4,
            "focus": "Address velocity issues and blockers",
            "rationale": f"Velocity score ({velocity:.1f}%) indicates pacing issues.",
            "impact": f"Month {month + 1:02d} starts 1 week later",
        })

    # Check for month reorder opportunities
    if quality > 85 and velocity > 85 and overall >= 90:
        # High performer - consider acceleration
        proposals.append({
            "type": "month_reorder",
            "swap": [month + 1, month + 2],
            "rationale": "Strong performance. Consider tackling more challenging content sooner.",
            "impact": "Different order, same content coverage within tier scope.",
            "optional": True,
        })

    # Check for project swap opportunities
    progress_log = load_jsonl(MEMORY_DIR / "progress_log.jsonl")
    recent_blockers = [e for e in progress_log[-20:] if e.get("type") == "blocker"]

    if len(recent_blockers) >= 3:
        # Multiple blockers - might need project adjustment
        blocker_desc = recent_blockers[-1].get("description", "")
        proposals.append({
            "type": "project_swap",
            "month": month,
            "rationale": f"Multiple blockers detected. Consider alternative project with similar learning goals.",
            "original": f"Current Month {month:02d} project",
            "alternatives": [
                "Simplified version with reduced scope",
                "Alternative project focusing on same skills",
            ],
            "requires_discussion": True,
        })

    return proposals


def format_proposal(proposal: dict, index: int) -> str:
    """Format a single proposal for display."""
    ptype = proposal.get("type", "unknown")

    output = f"""
### Proposal {index}: {ptype.replace('_', ' ').title()}

**Type**: `{ptype}`

**Details**:
```json
{json.dumps(proposal, indent=2)}
```

**Rationale**: {proposal.get('rationale', 'N/A')}

**Impact**: {proposal.get('impact', 'See details above')}

"""

    if proposal.get("optional"):
        output += "**Note**: This is an optional suggestion, not required.\n"

    if proposal.get("requires_discussion"):
        output += "**Note**: This requires further discussion to determine specifics.\n"

    return output


def generate_adaptation_report(month: int, as_json: bool = False) -> str:
    """Generate adaptation proposals report."""
    scores = compute_scores(month)
    proposals = analyze_for_adaptations(scores, month)

    if as_json:
        return json.dumps({
            "month": month,
            "evaluation": scores,
            "proposals": proposals,
            "approval_required": True,
            "timestamp": datetime.now().isoformat(),
        }, indent=2)

    # Generate markdown report
    report = f"""# Adaptation Proposals: Month {month:02d}

**Generated**: {datetime.now().isoformat()}
**Based on**: Evaluation scores (overall: {scores['overall']:.1f}%)
**Threshold**: {PASSING_THRESHOLD}%

## Current Scores Summary

| Category | Score |
|----------|-------|
| Completion | {scores['completion']:.1f}% |
| Quality | {scores['quality']:.1f}% |
| Velocity | {scores['velocity']:.1f}% |
| Reflection | {scores['reflection']:.1f}% |
| **Overall** | **{scores['overall']:.1f}%** |

## Proposals

"""

    if not proposals:
        report += """**No adaptations recommended.**

Your scores are within acceptable range. Continue with the current plan.

If you feel stuck despite these scores, consider:
- Running `/debug-learning` to explore specific issues
- Reviewing your week plan with `/plan-week`
- Discussing with the Coach agent

"""
    else:
        report += f"**{len(proposals)} proposal(s) generated** for your review.\n\n"
        report += "⚠️ **IMPORTANT**: These are proposals only. No changes will be applied without your explicit approval.\n"

        for i, proposal in enumerate(proposals, 1):
            report += format_proposal(proposal, i)

        report += """
## How to Apply

1. Review each proposal above
2. Decide which (if any) to apply
3. For approved proposals:
   - Level changes: Update `learner_profile.json`
   - Month reorder: Update month README files
   - Remediation week: Add to current month schedule
   - Project swap: Update month project description

4. Log your decision:
   ```bash
   echo '{"timestamp": "...", "type": "adaptation_applied", "proposal": "..."}' >> .claude/memory/decisions.jsonl
   ```

Or use the `/adapt-path` command in Claude Code for guided application.

"""

    report += """---
*This report contains proposals only. No changes have been made to your learning path.*
"""

    return report


def main():
    parser = argparse.ArgumentParser(description="Propose path adaptations")
    parser.add_argument("--month", type=int, help="Month number")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    # Determine current month from profile
    profile = load_json(MEMORY_DIR / "learner_profile.json")
    month = args.month or profile.get("current_month", 1)

    report = generate_adaptation_report(month, as_json=args.json)
    print(report)


if __name__ == "__main__":
    main()

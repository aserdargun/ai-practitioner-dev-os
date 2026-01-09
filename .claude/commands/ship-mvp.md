# Command: /ship-mvp

## Purpose
Finalize the Minimum Viable Product to a demo-ready state, ensuring core functionality works end-to-end and can be demonstrated.

## Inputs
- **MVP scope**: What the MVP should do
- **Demo scenario**: How it will be demonstrated
- **Must-haves vs nice-to-haves**: Priority guidance

## Outputs
- **Working MVP**: Functional code that can be run
- **Demo Script**: Step-by-step demo instructions
- **Known Limitations**: What's not included
- **Ship Checklist**: Verification that MVP is ready

## When to Use
- End of a project phase when core functionality is complete
- When you have working code but need to polish for demo
- Before moving to hardening or publishing
- When you need to "call it done" for the MVP scope

## Agent Routing
**Builder** — focuses on getting core functionality complete and demo-ready

## Example Usage

### Basic Ship
```
/ship-mvp
The MVP should ingest data, validate it, and output a clean CSV
```

### With Demo Focus
```
/ship-mvp for the forecasting dashboard
Demo scenario: show prediction for next 7 days
Must-have: chart visualization
Nice-to-have: date range selector
```

### Minimal Ship
```
/ship-mvp
Just get the API endpoint returning real predictions
Minimal demo: curl command that returns JSON
```

## Sample Output

```
🚢 MVP SHIP CHECKLIST — Data Pipeline

Core Functionality:
✓ Data ingestion from CSV
✓ Validation with error reporting
✓ Clean output generation
✓ Basic error handling

Demo Ready:
✓ Sample data file included
✓ Run command documented
✓ Expected output shown

Ship Checklist:
✓ Code runs without errors
✓ Happy path works end-to-end
✓ README has usage instructions
✓ Dependencies documented
☐ Demo script written (doing now)

Demo Script:
1. Install: pip install -r requirements.txt
2. Run: python pipeline/run.py data/sample.csv
3. Check output: output/clean_data.csv
4. Verify: 100 rows processed, 3 rows flagged

Known Limitations:
- Only handles CSV (not JSON yet)
- Max 10k rows (memory constraint)
- No retry on network errors

What's NOT in MVP:
- Web interface
- Scheduling
- Multiple file formats

Ready to demo! 🎉

Next steps:
- /harden — Add tests and error handling
- /publish — Prepare write-up and portfolio entry
```

## Ship Criteria

An MVP is ready to ship when:
- [ ] Core use case works end-to-end
- [ ] Can be run by someone else with instructions
- [ ] Fails gracefully (no cryptic errors)
- [ ] Scope is clear (what's in, what's out)
- [ ] Can be demonstrated in < 5 minutes

## Related Commands
- `/harden` — Add quality after MVP
- `/publish` — Prepare for portfolio
- `/retro` — Reflect on the build process

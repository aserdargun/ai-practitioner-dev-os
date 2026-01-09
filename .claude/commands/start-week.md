# Command: /start-week

## Purpose

Begin executing the approved week plan. This transitions from planning to building, scaffolding initial code and starting the first task.

## Inputs

- An approved week plan (from `/plan-week`)
- Current project context

## Outputs

- Initial project scaffolding (if needed)
- First task implementation started
- Progress log entry
- **All changes require user approval**

## When to Use

- After approving a week plan
- Monday morning (or your week start)
- After a break to resume work

## Agent Routing

**Primary**: Builder Agent

The Builder takes the approved plan and begins implementation, showing you proposed changes before applying them.

## Example Usage

**User Input**:
```
/start-week
```

**Expected Output**:
```
## Starting Week 2

### Approved Plan Summary
1. [ ] Set up vector store connection (today)
2. [ ] Implement chunking logic
3. [ ] Build retrieval function
4. [ ] Write unit tests
5. [ ] Documentation

### First Task: Set up vector store connection

I'll create the following structure:

**New Files**:
```
rag/
├── __init__.py
├── store.py      # VectorStore class
└── config.py     # Configuration
tests/
└── test_store.py # Store tests skeleton
```

**Proposed: rag/store.py**
```python
"""Vector store connection and operations."""
from dataclasses import dataclass
from typing import Optional
import os

@dataclass
class StoreConfig:
    url: str = os.getenv("QDRANT_URL", "localhost")
    port: int = int(os.getenv("QDRANT_PORT", "6333"))
    collection: str = "documents"

class VectorStore:
    def __init__(self, config: Optional[StoreConfig] = None):
        self.config = config or StoreConfig()
        self._client = None

    def connect(self):
        """Establish connection to vector store."""
        # Implementation will go here
        pass

    def health_check(self) -> bool:
        """Check if store is reachable."""
        # Implementation will go here
        return True
```

**Do you approve creating these files?** (yes / modify / no)
```

## Continuation

After the first task is approved and created:
```
/start-week continue
```

Or simply continue working and use `/status` to track progress.

## Related Commands

- `/plan-week` - Create the plan first
- `/status` - Check progress during the week
- `/ship-mvp` - When core functionality is done
- `/harden` - Before shipping for quality review

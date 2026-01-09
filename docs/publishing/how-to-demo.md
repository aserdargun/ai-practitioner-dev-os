# How to Demo

Guide to demonstrating your month projects.

## Overview

Each month, you build a project. A good demo showcases your work and reinforces learning.

## Demo Structure

### 5-Minute Demo Template

| Segment | Duration | Content |
|---------|----------|---------|
| Intro | 30s | What you built, why it matters |
| Problem | 30s | What problem does this solve? |
| Solution | 2m | Live demo of the working system |
| Technical | 1m | Key design decisions, architecture |
| Wrap-up | 30s | What you learned, next steps |
| Q&A | 30s | Answer questions (if live) |

## Preparation Checklist

### Before Recording/Presenting

- [ ] System works end-to-end
- [ ] Sample data ready
- [ ] No secrets visible
- [ ] Clean terminal/browser
- [ ] Script/outline prepared
- [ ] Backup plan if live demo fails

### Technical Setup

```bash
# Run pre-publish checks
bash .claude/hooks/pre_publish_check.sh

# Verify system works
python demo.py  # or equivalent

# Clear terminal
clear
```

### Content Preparation

1. **Write a script** (even if not reading it)
2. **Prepare sample data** that shows off features
3. **Anticipate questions** and prepare answers
4. **Time yourself** - aim for under 5 minutes

## Demo Script Template

```markdown
# Demo: [Project Name]

## Intro (30s)
"I'm [Name], and today I'll show you [Project Name],
a [type of system] that [main value proposition].

This is my Month [X] project for [learning goal]."

## Problem (30s)
"The problem we're solving is [problem description].

Without this, you'd have to [painful alternative].
With this system, you can [benefit]."

## Solution Demo (2m)
"Let me show you how it works.

First, I'll [action 1]...
[Run command, show result]

Now I'll [action 2]...
[Run command, show result]

As you can see, [highlight key feature]..."

## Technical Highlights (1m)
"A few design decisions worth noting:

1. I chose [technology] because [reason]
2. The architecture uses [pattern] to [benefit]
3. For [challenge], I solved it by [solution]"

## Wrap-up (30s)
"Key learnings from this project:
- [Learning 1]
- [Learning 2]

Next, I plan to [next steps].

Thanks for watching!"
```

## Recording Tips

### Screen Recording

**Tools**:
- OBS Studio (free, cross-platform)
- QuickTime (macOS)
- Windows Game Bar (Windows)

**Settings**:
- Resolution: 1920x1080
- Frame rate: 30fps
- Audio: Include microphone

### Best Practices

1. **Clean desktop** - Remove clutter
2. **Large fonts** - Increase terminal/editor font size
3. **Hide notifications** - Turn on Do Not Disturb
4. **Practice** - Do a test recording first
5. **Edit** - Cut mistakes, speed up waiting

### Video Length

| Platform | Ideal Length |
|----------|--------------|
| Portfolio | 3-5 min |
| LinkedIn | 1-2 min |
| Technical | 5-10 min |
| Full tutorial | 15-30 min |

## Live Demo Tips

### If Presenting Live

1. **Have a backup** - Screenshots/video if demo fails
2. **Pre-run commands** - Ensure everything is cached/ready
3. **Explain while waiting** - Fill loading time with context
4. **Embrace errors** - Debug live to show problem-solving

### Common Issues

| Issue | Solution |
|-------|----------|
| API timeout | Use cached responses |
| Database connection | Check connection before demo |
| Missing dependency | Run `pip install -r requirements.txt` first |
| Typo in live coding | Practice the exact commands |

## Demo Artifacts

### Create These Files

```
demo/
├── demo.py           # Main demo script
├── sample_data/      # Demo-ready data
├── demo_script.md    # Your spoken script
└── screenshots/      # Backup visuals
```

### Sample demo.py

```python
#!/usr/bin/env python3
"""
Demo script for [Project Name].

Usage:
    python demo.py
"""

import time

def main():
    print("=== [Project Name] Demo ===\n")

    # Step 1
    print("1. Loading data...")
    # ... your code ...
    print("   Done!\n")

    # Step 2
    print("2. Processing...")
    # ... your code ...
    print("   Done!\n")

    # Step 3
    print("3. Showing results...")
    # ... your code ...

    print("\n=== Demo Complete ===")

if __name__ == "__main__":
    main()
```

## Sharing Your Demo

### Platforms

| Platform | Format | Audience |
|----------|--------|----------|
| YouTube (unlisted) | Video | Portfolio link |
| GitHub README | GIF/Video | Repo visitors |
| LinkedIn | Short video | Professional network |
| Portfolio site | Embedded video | Employers |

### GitHub README Demo

Add to your project README:
```markdown
## Demo

![Demo GIF](demo/demo.gif)

Or watch the full demo: [YouTube link]
```

### Creating GIFs

Tools:
- [gifski](https://gif.ski/) - High quality
- [Peek](https://github.com/phw/peek) - Linux
- [LICEcap](https://www.cockos.com/licecap/) - Windows/Mac

## Monthly Demo Cadence

| Week | Demo Activity |
|------|---------------|
| Week 1 | Plan demo approach |
| Week 2 | Build demo-able features first |
| Week 3 | Create demo script |
| Week 4 | Record/present demo |

## Demo Quality Bar

Before sharing:
- [ ] Works without errors
- [ ] Clear narrative flow
- [ ] Under 5 minutes (or specified length)
- [ ] No secrets visible
- [ ] Good audio quality (if narrated)
- [ ] Key features demonstrated
- [ ] Learning outcomes mentioned

## Related Docs

- [How to Write Medium Post](how-to-write-medium-post.md)
- [Portfolio Checklist](portfolio-checklist.md)
- [/publish Command](../../.claude/commands/publish.md)

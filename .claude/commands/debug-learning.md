# Command: /debug-learning

## Purpose
Diagnose why you're stuck on a learning blocker and get actionable strategies to move forward.

## Inputs
- **Blocker description**: What you're stuck on
- **Context**: What you've already tried
- **Duration**: How long you've been stuck

## Outputs
- **Diagnosis**: Root cause analysis of the blocker
- **Strategies**: Multiple approaches to try
- **Resources**: Helpful learning materials
- **Action Plan**: Specific next steps
- **Escalation Path**: When to ask for more help

## When to Use
- When you've been stuck for more than 30 minutes
- When you don't understand a concept
- When something isn't working and you don't know why
- When you feel frustrated or overwhelmed

## Agent Routing
**Coach** — diagnoses blockers and provides strategies

## Example Usage

### Concept Blocker
```
/debug-learning
I don't understand how decorators work in Python.
I've read the docs but it's not clicking.
```

### Technical Blocker
```
/debug-learning
My API keeps returning 500 errors on the /predict endpoint.
I've checked the logs but can't find the issue.
Stuck for 2 hours.
```

### Overwhelm
```
/debug-learning
The ML pipeline feels too complex.
I don't know where to start.
```

## Sample Output

```
🔍 LEARNING DEBUG — Decorators in Python

Blocker Type: Concept Understanding
Duration: ~1 hour (normal for this topic)

Diagnosis:
Decorators often feel confusing because they combine several
Python concepts at once:
1. Functions as first-class objects
2. Closures and scope
3. Higher-order functions
4. The @ syntax (syntactic sugar)

You're likely missing the mental model of "functions that
take functions and return functions."

Strategies to Try:

1. Build Up Incrementally
   Start with simpler concepts first:
   - First: Understand functions as values
   - Then: Functions that return functions
   - Then: Functions that take functions as args
   - Finally: Combine into decorators

2. Trace by Hand
   Write out what happens step-by-step:
   ```python
   def my_decorator(func):
       def wrapper():
           print("Before")
           func()
           print("After")
       return wrapper

   @my_decorator
   def say_hello():
       print("Hello!")

   # say_hello is now wrapper
   # Calling say_hello() calls wrapper()
   ```

3. Use Print Statements
   Add prints to see the execution order.

4. Try Without @ Syntax
   Write the equivalent without @:
   ```python
   say_hello = my_decorator(say_hello)
   ```

Resources:
- Real Python: Primer on Decorators (article)
- Corey Schafer: Decorators (YouTube, 30 min)
- Python docs: functools.wraps

Action Plan:
1. [Now] Watch the Corey Schafer video
2. [After] Write 3 simple decorators by hand
3. [After] Trace the execution with print statements
4. [Tomorrow] Apply a decorator in your project

If Still Stuck After 30 More Minutes:
- Ask Claude to explain with a different analogy
- Find a peer to rubber-duck with
- Take a break and return fresh

Remember: Decorators are genuinely tricky. Most Python
developers struggled with them at first.
```

## Blocker Types

| Type | Signs | Approach |
|------|-------|----------|
| Concept | "I don't understand" | Break down, analogies, examples |
| Technical | "It doesn't work" | Debug systematically, isolate |
| Overwhelm | "Too much" | Scope down, prioritize |
| Motivation | "I can't focus" | Breaks, smaller wins |
| Environment | "Setup issues" | Simplify, use containers |

## Related Commands
- `/status` — Context before debugging
- `/add-best-practice` — Capture solution as practice
- `/retro` — Reflect on blockers

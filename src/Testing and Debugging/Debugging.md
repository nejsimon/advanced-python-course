# Debugging

Debugging is an essential skill for any developer, allowing you to identify, trace, and resolve issues in your code. Python provides a wide range of tools and techniques for debugging, from built-in functions to advanced interactive debuggers.

---

## 1. Mindset and Strategy

* **Reproduce the Bug**: Ensure the issue is consistent.
* **Minimize the Code**: Isolate the failing behavior in a minimal example.
* **Ask the Right Questions**: What did I expect? What actually happened?
* **Use Assertions**: Catch problems early with self-checks.

---

## 2. Built-in Tools

### `print()` Debugging

* Fast, simple, and effective for small-scale issues
* Add contextual print statements to inspect variables
* Works even when debuggers are not an option

### `assert` Statements

* Used for invariants and assumptions
* Raises `AssertionError` if the condition is false

```python
assert isinstance(user, User), "Expected a User instance"
```

---

## 3. The `pdb` Module (Python Debugger)

### Basic Usage

```python
import pdb
pdb.set_trace()
```

### Common Commands

* `n` – next line
* `s` – step into function
* `c` – continue
* `l` – list source code
* `p var` – print variable
* `q` – quit debugger

### Run a Script with `pdb`

```bash
python -m pdb script.py
```

### Breakpoints (Python 3.7+)

```python
breakpoint()  # drops into the default debugger
```

---

## 4. Interactive Debugging Tools

### `ipdb`

* IPython-enhanced `pdb`
* Better history and tab-completion

```bash
pip install ipdb
```

```python
import ipdb; ipdb.set_trace()
```

### `pudb`

* Full-screen TUI debugger

```bash
pip install pudb
python -m pudb your_script.py
```

### `debugpy`

* Debug adapter for VS Code and remote debugging
* Use with `ptvsd` or `debugpy.listen()` for remote sessions

---

## 5. IDE and Editor Support

### Visual Studio Code

* Built-in debugger with breakpoints, variable inspection, watch expressions
* Supports remote debugging via `debugpy`

### PyCharm

* Robust debugger with visual stack traces
* Supports inline evaluation, watches, conditional breakpoints

---

## 6. Logging

Use the `logging` module instead of `print()` in production code:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("Starting execution")
```

Advantages:

* Configurable levels (`DEBUG`, `INFO`, `WARNING`, etc.)
* Redirect to files or streams
* Supports formatting and structured logs

---

## 7. Post-Mortem Debugging

Automatically enter debugger on exception:

```python
import pdb
import sys

try:
    some_function()
except:
    pdb.post_mortem()
```

---

## 8. Tracebacks and Stack Frames

### Reading Tracebacks

* Tracebacks show the call stack at the time of the exception
* Start reading from the bottom: the most recent call is last

### Extracting Stack Traces Programmatically

```python
import traceback

try:
    1 / 0
except Exception as e:
    print(traceback.format_exc())
```

---

## 9. Tracing Execution

### `trace` Module

Run scripts with execution tracing:

```bash
python -m trace --trace your_script.py
```

### `sys.settrace()`

Custom function call tracing for profiling/debugging

---

## 10. Static Analysis and Linters

### Tools

* `flake8`, `pylint`, `pyflakes` – code style and potential bug detection
* `mypy` – type-checking to catch mismatches
* `bandit` – security linter

Use linters to catch:

* Unused variables
* Dangerous patterns
* Shadowing and redefinitions

---

## 11. Debugging in Production

* Use structured logs (e.g., JSON) and log aggregation (e.g., ELK stack)
* Add tracing identifiers (e.g., request IDs)
* Implement health checks and monitoring
* Use feature flags to isolate problematic paths
* Avoid interactive debuggers in deployed services

---

## 12. Advanced Techniques

* **Binary search your codebase** to isolate change that introduced the bug (e.g., `git bisect`)
* **Record/replay tools** like `rr` (with Python C extensions)
* **Test coverage tools** (`coverage.py`) to verify paths exercised by tests

---

## Final Tips

* Write tests for fixed bugs to prevent regressions
* Use assertions liberally in internal code
* Combine logging + breakpoints for flexible triage
* Don’t ignore warnings — enable them via `-Wd`

```bash
python -Wd my_script.py
```


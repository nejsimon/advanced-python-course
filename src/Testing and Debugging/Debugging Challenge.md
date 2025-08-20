# Debugging in Python: Coding Challenges

These hands-on challenges are designed to reinforce debugging strategies and tools discussed in the documentation. They simulate common real-world issues and guide you through resolving them using print statements, `pdb`, logging, and more.

---

## Challenge 1: Find the Off-by-One Error

**Code:**

```python
def average(numbers):
    return sum(numbers) / (len(numbers) - 1)  # bug here

print(average([10, 20, 30]))
```

**Task:** Identify and fix the off-by-one bug.

* Use a print debugger or `pdb.set_trace()` to inspect intermediate values.
* Fix the logic error.

---

## Challenge 2: Log the Flow

**Code Skeleton:**

```python
import logging

def process(data):
    # simulate logic
    return data[::-1]

def main():
    items = ["foo", "bar", "baz"]
    for item in items:
        result = process(item)
        print(result)

main()
```

**Task:** Replace `print()` with structured logging:

* Use `logging.basicConfig()`.
* Log before and after `process()` with levels like `INFO` and `DEBUG`.

---

## Challenge 3: Post-Mortem Debugging

**Code:**

```python
def fail():
    x = 5
    y = 0
    return x / y

try:
    fail()
except:
    pass  # placeholder
```

**Task:** Replace the `pass` with a call to `pdb.post_mortem()`.

* Use the debugger to inspect the stack and variable values.

---

## Challenge 4: Fix the Function Signature Bug

**Code:**

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Hi"))
```

**Task:** Identify and fix the argument mismatch.

* Run it with `pdb.set_trace()` and inspect the arguments.

---

## Challenge 5: Trace Execution Flow

**Code:**

```python
def step1(): return "one"
def step2(): return "two"
def step3(): return "three"

def pipeline():
    a = step1()
    b = step2()
    c = step3()
    return a + b + c

print(pipeline())
```

**Task:** Use the `trace` module to show the exact execution path:

```bash
python -m trace --trace pipeline.py
```

---

## Challenge 6: Logging Exceptions with Tracebacks

**Code Skeleton:**

```python
import logging
import traceback

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

def risky():
    return 1 / 0

try:
    risky()
except Exception as e:
    # log the exception with traceback
    pass
```

**Task:** Complete the `except` block to log the full traceback.

---

## Challenge 7: Debug with an IDE

**Task:** Use an IDE (e.g., VS Code, PyCharm) to:

* Set a breakpoint in a function.
* Inspect variables in scope.
* Use step-into and step-over.
* Modify a variable live and resume execution.

You can reuse one of the earlier challenge snippets as the target.

---

## Challenge 8: Analyze Traceback

**Code:**

```python
def foo():
    return bar()

def bar():
    return baz()

def baz():
    return 1 / 0

foo()
```

**Task:** Read the traceback, identify where the error originates, and how the call stack leads to it. Bonus: Use `traceback.format_exc()` to print the traceback programmatically.

---

## Challenge 9: Lint and Static Analysis

**Task:**

* Create a Python file with common mistakes:

  * Unused import
  * Variable shadowing
  * Function missing a return
* Run `flake8` or `pylint` on it.
* Fix all issues reported by the linter.

---

## Challenge 10: Debug a Real Bug with ipdb

**Task:**

* Install `ipdb`.
* Add `import ipdb; ipdb.set_trace()` to a function with a known issue.
* Use tab-completion and introspection (`locals()`, `globals()`, `dir()`) to inspect state.
* Resume and verify the fix.


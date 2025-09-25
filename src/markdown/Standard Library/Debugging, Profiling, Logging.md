# Standard Library – Debugging, Profiling & Logging

## Python’s standard library provides a variety of tools for **debugging, performance profiling, and logging**. These modules are essential for diagnosing issues, improving performance, and keeping track of application behavior in production environments.

---

## 1. `pdb` – Python Debugger
- **Purpose**: Interactive debugger for Python code.
- Features:
  - Set breakpoints.
  - Step through code.
  - Inspect and modify variables at runtime.
- Example:
  ```python
  import pdb

  def buggy_function(x):
      y = x + 1
      pdb.set_trace()  # start debugger
      z = y * 2
      return z

  buggy_function(5)
  ```

- Commands in the debugger:
  - n (next), s (step into), c (continue), p var (print variable), q (quit).

## 2. traceback – Traceback Handling
- **Purpose:** Extract, format, and print stack traces.
- Example:
  ```python
  import traceback

  try:
      1 / 0
  except Exception as e:
      print("Error:", e)
      print(traceback.format_exc())
  ```

## 3. warnings – Warning Messages
- **Purpose:** Issue non-fatal warnings to developers/users.
- Example:
  ```python
  import warnings

  def old_function():
      warnings.warn("This function is deprecated", DeprecationWarning)

  old_function()
  ```

## 4. logging – Flexible Logging System
  - **Purpose:** Standardized logging with levels and handlers.
- Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
- Example:
  ```python
  import logging

  logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")
  logging.info("This is an info message")
  logging.warning("This is a warning")
  ```

## 5. timeit – Timing Small Code Snippets
- **Purpose:** Measure execution time of code snippets.
- Example:
  ```python
  import timeit

  code = "sum(range(1000))"
  print(timeit.timeit(code, number=1000))
  ```

## 6. cProfile – Deterministic Profiling
- **Purpose:** Profile Python programs to find bottlenecks.
- Example:
  ```python
  import cProfile

  def test():
      return sum(i*i for i in range(10000))

  cProfile.run("test()")
  ```

## 7. profile & pstats
- **profile:** Pure Python profiler (slower than cProfile).
- **pstats:** Analyze profile results, sort by time, calls, etc.

## 8. faulthandler
- **Purpose:** Dumps Python traceback on fatal errors (segfaults).

- Example:
  ```python
  import faulthandler
  faulthandler.enable()
  ```

## Quirks & Notes
- pdb is line-oriented; for modern projects, IDE-integrated debuggers (PyCharm, VSCode) may be more practical.
- warnings can be turned into errors (python -W error) for stricter debugging.
- logging is highly configurable but can get complex, supports handlers (file, stream, syslog, HTTP).
- timeit defaults to disabling garbage collection to avoid noise in timing.
- Profilers add overhead; always measure results with caution.
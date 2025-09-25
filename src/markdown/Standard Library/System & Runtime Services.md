# Standard Library – System & Runtime Services

Python provides a wide set of modules to interact with the interpreter, the operating system, and runtime internal## s. These modules let you control the Python runtime environment, inspect system resources, and work with processes, signals, and execution control.

## 1. sys – System-Specific Parameters and Functions

Provides access to interpreter internals.

- Common uses:
    - `sys.argv` → command-line arguments.
    - `sys.exit([code])` → exit program.
    - `sys.path` → module search path.
    - `sys.version` → Python version.
    - `sys.getsizeof(obj)` → size of object in bytes.
- Example:
  ```python
    import sys

    print("Arguments:", sys.argv)
    print("Python version:", sys.version)
    print("Path entries:", sys.path[:3])

## 2. os – Operating System Interfaces

- Low-level OS interactions.
- File system manipulation: `os.listdir()`, `os.remove()`, `os.rename()`.
- Environment variables: `os.environ`.
- Process management: `os.getpid()`, `os.fork()` (Unix), `os.spawn*`.

- Example:
  ```python
    import os

    print("PID:", os.getpid())
    print("Current directory:", os.getcwd())
    print("Home directory:", os.environ.get("HOME"))

## 3. platform – Platform and System Information

- Identifies the underlying platform (OS, Python build, hardware).
  - `platform.system()` → OS name.
  - `platform.machine()` → architecture.
  - `platform.python_implementation()` → "CPython", "PyPy", etc.
- Example:
  ```python
  import platform

  print(platform.system())
  print(platform.release())
  print(platform.python_implementation())

## 4. subprocess – Spawning Processes

- Allows running external programs.
- Replaces older `os.system`, `os.spawn*`, `popen`.
- Safer and more flexible.
- Example:
  ```python
  import subprocess

  result = subprocess.run(["echo", "Hello subprocess"], capture_output=True, text=True)
  print(result.stdout)

## 5. signal – Handling OS Signals

- Manage Unix signals (e.g., SIGINT, SIGTERM).
- Useful for clean shutdowns.
- Example:
  ```python
  import signal
  import time

  def handler(signum, frame):
      print("Signal received:", signum)

  signal.signal(signal.SIGINT, handler)

  print("Press Ctrl+C...")
  while True:
      time.sleep(1)

## 6. atexit – Exit Handlers

- Register functions to be called on program termination.
- Example:
  ```python
  import atexit

  def goodbye():
      print("Exiting program!")

  atexit.register(goodbye)

## 7. faulthandler – Crash Debugging

- Prints Python traceback on low-level faults (segfaults, fatal errors).
- Very useful for debugging C extensions.
- Example:
  ```python
  import faulthandler
  faulthandler.enable()

## 8. gc – Garbage Collector Interface

- Control and inspect the garbage collector.
- gc.collect() → force collection.
- gc.get_stats() → memory statistics.
- Useful in debugging memory leaks.
- Example:
  ```python
  import gc

  print("GC stats:", gc.get_stats())

## 9. sysconfig – Build and Configuration Data

- Provides access to Python’s build-time variables.
- Useful when building C extensions.
- Example:
  ```python
  import sysconfig

  print("Include path:", sysconfig.get_path("include"))
  print("Platform:", sysconfig.get_platform())

## 10. Other Related Modules

- `uuid` – generate universally unique identifiers.
- `time` – low-level time access.
- `sched` – event scheduler.
- `resource` (Unix) – system resource usage and limits.

## Summary

- The System & Runtime Services cluster of the standard library enables:
- System interaction (os, platform, sys).
- Process control (subprocess, signal).
- Runtime behavior control (gc, atexit, faulthandler).
- Environment insights (sysconfig, uuid, time).
- This group of modules is essential for writing programs that need to:
- Adapt to the runtime environment.
- Work closely with the operating system.
- Manage processes and signals.
- Debug, profile, and monitor runtime state.
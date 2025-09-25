# Coding Challenge: Standard Library – System & Runtime Services

This challenge will test your ability to use Python’s runtime and system service modules (`sys`, `os`, `subprocess`, `platform`, `signal`, `atexit`, `gc`, `faulthandler`, `sysconfig`).

---

## Part 1 – Command-Line Arguments and System Info (`sys`, `platform`)
1. Write a script that prints:
   - The program name and all arguments passed.
   - The Python version and implementation.
   - The OS name and machine architecture.
2. Bonus: Exit the script with code `42` if an argument `--fail` is provided.

---

## Part 2 – Environment and OS Interaction (`os`)
1. Print the current working directory.
2. List all files in the current directory.
3. Change into the home directory using `os.environ["HOME"]` (or `USERPROFILE` on Windows).
4. Create a subdirectory called `demo_sys_runtime` and remove it at the end.

---

## Part 3 – Subprocess Management (`subprocess`)
1. Run an external command to print `Hello World` (use `echo`).
2. Capture the output and print it in uppercase.
3. Bonus: Run `python --version` and parse the output.

---

## Part 4 – Signal Handling (`signal`)
1. Write a program that runs in an infinite loop until interrupted with `Ctrl+C`.
2. Catch the `SIGINT` signal and print `"Graceful shutdown"` before exiting.
3. Bonus: Also handle `SIGTERM` and print `"Termination requested"`.

---

## Part 5 – Exit Handlers (`atexit`)
1. Register an exit handler that always prints `"Program exiting cleanly"`.
2. Run a loop that prints `"Running..."` every second, then break after 3 iterations.

---

## Part 6 – Garbage Collector (`gc`)
1. Force a garbage collection using `gc.collect()`.
2. Print GC statistics (`gc.get_stats()`).
3. Bonus: Create a simple reference cycle (object referencing itself) and show how GC handles it.

---

## Part 7 – Fault Handling (`faulthandler`)
1. Enable `faulthandler` at the start of your program.
2. Bonus: Write a function that deliberately causes a `ZeroDivisionError` and observe how Python reports it.

---

## Part 8 – System Configuration (`sysconfig`)
1. Print the Python installation’s include path.
2. Print the current platform string.
3. Bonus: Use `sysconfig.get_config_vars()` to list all configuration keys.

---

## Extra Challenge – Combined Utility Script
Write a **system diagnostic script** that:
- Prints Python and platform info.
- Lists current working directory and files.
- Runs a subprocess (`python --version`) to verify Python version.
- Registers an exit handler that logs the script termination.
- Handles `SIGINT` and `SIGTERM` gracefully.
- Forces a garbage collection at the end and prints statistics.

This script should demonstrate **integration of at least 5 system/runtime modules**.

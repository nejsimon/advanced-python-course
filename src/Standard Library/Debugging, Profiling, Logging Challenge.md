# Coding Challenge: Debugging, Profiling & Logging

This challenge will help you practice using Python’s debugging, profiling, and logging tools from the standard library.  

---

## Part 1: Debugging with `pdb`
1. Write a function `process_data(data)` that:
   - Takes a list of numbers.
   - Normalizes them by dividing each by the maximum value.
   - Intentionally includes a bug: division by zero if the list is empty.
2. Insert a `pdb.set_trace()` call inside the function.
3. Run the function with `[]` and step through the debugger to:
   - Inspect variable values.
   - Identify the cause of the bug.

---

## Part 2: Handling Exceptions with `traceback`
1. Wrap your `process_data` call in a `try/except` block.
2. If an exception occurs, print a full formatted traceback using `traceback.format_exc()`.

---

## Part 3: Using `warnings`
1. Create a function `legacy_api_call()` that raises a `DeprecationWarning` via the `warnings` module.
2. Configure Python so that warnings are displayed every time the function is called.
3. Test that calling it multiple times always prints a warning.

---

## Part 4: Logging
1. Configure a `logging` system that:
   - Logs to both the console and a file `app.log`.
   - Uses `INFO` as the minimum level.
   - Prints messages in the format: `%(asctime)s [%(levelname)s] %(message)s`.
2. Add logging to your `process_data` function:
   - Log at `INFO` level when starting/finishing processing.
   - Log at `ERROR` level if an exception occurs.

---

## Part 5: Measuring Execution with `timeit`
1. Use `timeit` to measure:
   - The performance of summing numbers with a `for` loop.
   - The performance of using Python’s built-in `sum()`.
2. Compare the timings and explain why one is faster.

---

## Part 6: Profiling with `cProfile`
1. Write a function `compute()` that:
   - Generates all prime numbers below 50,000 using a naive algorithm.
   - Returns the list of primes.
2. Profile this function with `cProfile`.
3. Sort the results by cumulative time and identify the most expensive function call.

---

## Part 7: `faulthandler`
1. Enable `faulthandler` in your script.
2. Intentionally cause a recursion depth error (e.g., with a recursive function that never terminates).
3. Observe how the traceback is printed when the crash occurs.

# Multiprocessing in Python: Coding Challenges

These challenges cover process creation, synchronization, inter-process communication (IPC), and performance considerations.

---

## Challenge 1: Simple Process Spawning

**Objective:**
Write a program that spawns 3 processes using `multiprocessing.Process`, each printing its process ID and a custom message.

---

## Challenge 2: Parallel Computation

**Objective:**
Use `multiprocessing.Pool` to compute squares of numbers from 1 to 10 in parallel.

**Bonus:** Compare runtime vs. sequential execution.

---

## Challenge 3: Shared Memory with `Value` and `Array`

**Objective:**
Create multiple processes that increment a shared counter (`multiprocessing.Value`).

**Bonus:** Demonstrate race conditions and fix them with `multiprocessing.Lock`.

---

## Challenge 4: Producer–Consumer with Queue

**Objective:**
Implement a producer-consumer system:

* One producer generates numbers and puts them into a `multiprocessing.Queue`.
* Multiple consumers process the numbers.

---

## Challenge 5: Pipes for Communication

**Objective:**
Use `multiprocessing.Pipe` for two-way communication between parent and child process.

---

## Challenge 6: Process Synchronization

**Objective:**
Demonstrate the use of `multiprocessing.Event`:

* Parent process waits until a child process signals completion.

---

## Challenge 7: Process Pool with Async

**Objective:**
Use `apply_async` or `map_async` to run tasks in the background and collect results later.

---

## Challenge 8: Deadlock Simulation and Resolution

**Objective:**
Simulate a deadlock scenario with multiple locks.

**Bonus:** Fix the deadlock using `multiprocessing.Lock` acquisition order or `multiprocessing.Semaphore`.

---

## Challenge 9: Benchmarking Multiprocessing vs Threading

**Objective:**
Write a program that performs CPU-bound tasks with both `threading` and `multiprocessing`.

**Goal:** Show how the GIL limits threading performance for CPU-heavy tasks, but multiprocessing scales better.

---

## Challenge 10: Real-World Mini Project

**Objective:**
Write a program that:

* Uses multiple processes to download web pages (or simulate long-running tasks)
* Uses a manager `dict` or `list` to collect results
* Ensures graceful shutdown with `join()`


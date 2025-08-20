# Python Threading: Coding Challenges

These challenges are designed to reinforce a deep understanding of Python’s `threading` module and concepts like race conditions, synchronization primitives, daemon threads, thread pools, and the Global Interpreter Lock (GIL).

---

## Challenge 1: Threaded File Logger

**Objective**: Implement a logger that writes log messages to a file from multiple threads.

**Requirements**:

* Use a `threading.Thread` per log producer
* Use a shared queue to collect log messages
* A dedicated thread should consume the queue and write to file
* Use `threading.Event` to signal graceful shutdown

**Bonus**:

* Support rotating log files every N lines

---

## Challenge 2: Race Condition Demonstration

**Objective**: Illustrate a race condition and fix it using synchronization.

**Part A**:

* Implement a `BankAccount` class with `deposit` and `withdraw` methods
* Spawn 100 threads to deposit money concurrently
* Observe incorrect final balance due to race condition

**Part B**:

* Fix it using a `threading.Lock`

**Bonus**:

* Use a `RLock` and simulate nested locking for audit logging

---

## Challenge 3: Thread-Safe Bounded Buffer (Producer-Consumer)

**Objective**: Build a bounded buffer using threads.

**Requirements**:

* Use a shared list of max size N
* Implement `Producer` and `Consumer` threads
* Use `threading.Condition` to handle wait/notify logic

**Bonus**:

* Add timeout behavior for consumers
* Use `queue.Queue` and compare complexity

---

## Challenge 4: Periodic Polling Daemon

**Objective**: Create a background daemon thread that periodically polls a resource.

**Requirements**:

* Daemon thread runs every 5 seconds and prints simulated CPU load
* Main thread runs a long computation
* Program exits cleanly when main thread ends

**Bonus**:

* Add signal handling (`signal.SIGINT`) to allow graceful exit

---

## Challenge 5: Parallel Web Fetcher

**Objective**: Download multiple URLs in parallel using threads.

**Requirements**:

* Accept a list of 10 URLs
* Spawn 5 worker threads
* Each thread downloads URLs from a shared queue
* Use `queue.Queue` and `threading.Thread`

**Bonus**:

* Add per-domain request throttling using a `threading.Semaphore`

---

## Challenge 6: Thread Pool from Scratch

**Objective**: Implement a basic thread pool executor without using `concurrent.futures`.

**Requirements**:

* Create a fixed number of worker threads
* Tasks submitted via `submit(func, *args, **kwargs)`
* Use `queue.Queue` for task distribution
* Support graceful shutdown

**Bonus**:

* Return `Future`-like objects with `.result()`

---

## Challenge 7: GIL and CPU-bound Tasks

**Objective**: Demonstrate GIL limitations in multithreaded CPU tasks.

**Requirements**:

* Run a CPU-heavy task (e.g. prime checking) in multiple threads
* Measure wall-clock vs CPU time
* Observe that adding threads does not scale

**Bonus**:

* Rewrite with `multiprocessing` and compare

---

## Challenge 8: Thread-local Data

**Objective**: Use `threading.local()` to keep per-thread data.

**Requirements**:

* Create a thread-local object to store thread-specific request IDs
* Simulate 10 threads setting and using different values

**Bonus**:

* Log all accesses and show thread identity via `threading.get_ident()`

---

## Challenge 9: Readers-Writers Lock

**Objective**: Implement a basic readers-writers lock.

**Requirements**:

* Allow multiple readers but only one writer
* Use `Lock`, `Condition`, or `Semaphore`
* Simulate 10 readers and 2 writers

**Bonus**:

* Add starvation prevention (e.g. writers-first policy)

---

## Challenge 10: Deadlock Simulation and Prevention

**Objective**: Simulate and prevent a deadlock scenario.

**Part A**:

* Create two threads trying to acquire two locks in different orders
* Observe deadlock

**Part B**:

* Prevent deadlock using `try/acquire(timeout)` or consistent lock order

---

## Challenge 11: Barrier Synchronization

**Objective**: Use `threading.Barrier` to coordinate thread phases.

**Requirements**:

* Simulate 5 worker threads that perform 3 phases of work
* All must finish a phase before any moves to the next

**Bonus**:

* Add timeout and error recovery if a thread hangs
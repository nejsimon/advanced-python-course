# Python `threading` Module

The `threading` module in Python provides a way to run multiple operations concurrently in the same process space using threads. While Python threads are subject to the Global Interpreter Lock (GIL), they are still useful for I/O-bound tasks.

## 🔰 Overview

- **Module**: `threading`
- **Core use-case**: Concurrent execution of code using threads (mostly for I/O-bound tasks).
- **Limitation**: Python's GIL prevents true parallelism in CPU-bound threads (for CPython).
- **Good for**: File/network I/O, background polling, UI responsiveness.

## 📦 Importing

```python
import threading
```

## 🧵 Creating Threads

### Using `Thread` class directly

```python
def worker():
    print("Thread is running")

t = threading.Thread(target=worker)
t.start()
t.join()  # Wait for thread to finish
```

### Subclassing `Thread`

```python
class MyThread(threading.Thread):
    def run(self):
        print("Thread is running from subclass")

t = MyThread()
t.start()
t.join()
```

## ⚙️ Key `Thread` Parameters

| Parameter   | Description |
|-------------|-------------|
| `target`    | Callable to run in thread |
| `args`      | Tuple of arguments for `target` |
| `kwargs`    | Dict of keyword args for `target` |
| `name`      | Optional thread name |
| `daemon`    | Run as daemon thread (terminates with main program) |

## 📌 Daemon Threads

Daemon threads are terminated when the main thread exits.

```python
t = threading.Thread(target=worker, daemon=True)
```

Use them with caution—resources may not be cleaned up.

## 🧰 Common Thread Methods

| Method      | Description |
|-------------|-------------|
| `.start()`  | Start thread execution |
| `.join(timeout=None)` | Wait until thread finishes or timeout occurs |
| `.is_alive()` | Check if thread is running |
| `.name`     | Get/set thread name |
| `.daemon`   | Get/set daemon status |

## 🔄 Synchronization Primitives

### `Lock`

```python
lock = threading.Lock()

with lock:
    # Critical section
    ...
```

### `RLock` (Reentrant Lock)

Allows the same thread to acquire the lock multiple times.

```python
rlock = threading.RLock()
```

### `Semaphore` / `BoundedSemaphore`

Control access to a pool of resources.

```python
sem = threading.Semaphore(3)  # max 3 threads allowed
```

### `Event`

Simple signaling mechanism between threads.

```python
event = threading.Event()

def wait_for_event():
    event.wait()  # blocks
    print("Event triggered")

event.set()  # unblocks any waiting threads
```

### `Condition`

Used for more advanced signaling and coordination.

```python
condition = threading.Condition()

with condition:
    condition.wait()  # wait until notified
    condition.notify()  # wake one
    condition.notify_all()  # wake all
```

### `Barrier`

Useful for multi-thread phase synchronization.

```python
barrier = threading.Barrier(3)

def wait_at_barrier():
    print("Waiting...")
    barrier.wait()
    print("Passed barrier")
```

## 📣 Thread-Local Data

```python
thread_data = threading.local()

def worker():
    thread_data.value = 42
    print(thread_data.value)
```

Each thread gets its own independent copy of `thread_data`.

## ⚠️ GIL and Threading Quirks

- **GIL**: Only one thread runs Python bytecode at a time (CPython). Use multiprocessing for CPU-bound tasks.
- **No true parallelism**: Threading is best for I/O-bound operations.
- **Race conditions**: Common if shared data isn't properly synchronized.
- **Deadlocks**: Always possible with poor locking design (especially with nested locks).
- **Debugging**: Thread bugs are non-deterministic and difficult to reproduce. Use `faulthandler`, logging, or debugging tools carefully.

## 🧪 Debugging Tips

- Use `threading.enumerate()` to list active threads.
- Use `threading.current_thread()` for debugging thread context.
- Consider using logging with thread name:

```python
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(threadName)s: %(message)s')
```

## 🚫 Don't Use `thread` / `_thread`

These are legacy modules from Python 2. Use `threading` instead unless you're doing low-level stuff for compatibility or experimentation.

## 🧪 Example: Thread Pool with `threading`

```python
import threading
import queue

def worker(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Processing {item}")
        q.task_done()

q = queue.Queue()
threads = []

# Start 4 worker threads
for _ in range(4):
    t = threading.Thread(target=worker, args=(q,))
    t.start()
    threads.append(t)

# Enqueue tasks
for i in range(10):
    q.put(i)

# Block until all tasks are done
q.join()

# Stop workers
for _ in threads:
    q.put(None)

for t in threads:
    t.join()
```

## 🧭 Alternatives

| Library          | Use-case                         |
|------------------|----------------------------------|
| `concurrent.futures.ThreadPoolExecutor` | Higher-level thread pool |
| `multiprocessing` | CPU-bound tasks |
| `asyncio`        | Cooperative multitasking for async I/O |

## 📚 Further Reading

- [Python threading docs](https://docs.python.org/3/library/threading.html)
- [GIL explained (realpython.com)](https://realpython.com/python-gil/)

---

## ✅ Summary

- Threads are powerful for I/O concurrency but limited by the GIL in CPU-bound tasks.
- Use synchronization primitives to manage shared state.
- Prefer `ThreadPoolExecutor` for simpler APIs.
- Be careful with daemon threads and shared state.

```python
# Quick pattern:
with threading.Lock():
    # safe section
    ...
```

Use threads when appropriate—but be aware of their limitations.

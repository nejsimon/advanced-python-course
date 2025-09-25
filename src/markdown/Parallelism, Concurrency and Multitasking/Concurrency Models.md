# Concurrency Models

Python supports multiple concurrency paradigms, each with distinct characteristics, use cases, and tradeoffs.

---

## 🧠 Key Concepts

| Term             | Description                                                  |
|------------------|--------------------------------------------------------------|
| **Concurrency**  | Tasks making progress simultaneously (not necessarily in parallel) |
| **Parallelism**  | Tasks executing at the same time (true simultaneity)         |
| **I/O-bound**    | Waiting on input/output (disk, network, etc.)                |
| **CPU-bound**    | Heavy computation occupying CPU cycles                       |
| **GIL**          | Global Interpreter Lock — allows only one thread at a time   |

---

## 🧵 Model 1: Multithreading

- Uses `threading.Thread`
- Shares memory space
- Ideal for **I/O-bound** tasks
- Blocked by GIL for **CPU-bound** tasks

### Example

```python
import threading

def worker(n):
    print(f"Worker {n} running")

threads = [threading.Thread(target=worker, args=(i,)) for i in range(5)]
[t.start() for t in threads]
[t.join() for t in threads]
```

### Notes

- Lightweight
- No true parallelism due to GIL
- Use with blocking I/O (e.g. file, network, API)

---

## ⚙️ Model 2: Multiprocessing

- Uses `multiprocessing.Process`
- True parallelism with multiple OS processes
- Best for **CPU-bound** tasks

### Example

```python
from multiprocessing import Process

def compute(n):
    print(n * n)

p = Process(target=compute, args=(5,))
p.start()
p.join()
```

### Notes

- Each process has its own memory
- Slower inter-process communication (IPC)
- Avoids GIL

---

## 🔁 Model 3: Async I/O with `asyncio`

- Single-threaded, event-loop-based concurrency
- Ideal for **I/O-bound** tasks
- Uses `async def`, `await`, coroutines

### Example

```python
import asyncio

async def fetch(url):
    print(f"Fetching {url}")
    await asyncio.sleep(1)
    print(f"Done {url}")

async def main():
    await asyncio.gather(fetch("a"), fetch("b"))

asyncio.run(main())
```

### Notes

- Cooperatively scheduled coroutines
- High throughput for network services
- Requires async-aware libraries (e.g. `aiohttp`, `aiosqlite`)

---

## 🧰 Model 4: `concurrent.futures`

- High-level interface for threads and processes

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def task(x): return x * 2

with ThreadPoolExecutor() as executor:
    result = list(executor.map(task, range(5)))
```

### Notes

- Abstracts away threads/processes
- Use `submit()` for fine-grained control
- Integrates with `asyncio` via `loop.run_in_executor()`

---

## ⚖️ Choosing a Model

| Task Type       | Best Model              | Notes                         |
|------------------|--------------------------|-------------------------------|
| Network I/O      | `asyncio`, threads       | Non-blocking = better scale   |
| File I/O         | threads, asyncio         | File ops still block sometimes|
| CPU-bound        | multiprocessing          | Bypass GIL                    |
| Mixed            | Hybrid                   | `asyncio` + thread pool       |

---

## 🧱 Queues and Coordination

### Thread-safe Queue

```python
from queue import Queue
from threading import Thread

q = Queue()

def worker():
    while True:
        item = q.get()
        print(item)
        q.task_done()

Thread(target=worker, daemon=True).start()
q.put("Hello")
```

### `asyncio.Queue`

```python
q = asyncio.Queue()

await q.put(item)
item = await q.get()
```

---

## 🧬 `asyncio` Event Loop Internals

```python
import asyncio

loop = asyncio.get_event_loop()
loop.run_until_complete(coro())
```

Coroutines are **suspended** at `await` points, allowing other tasks to run.

---

## 🕸 Libraries for Async I/O

| Library     | Purpose                      |
|-------------|------------------------------|
| `aiohttp`   | Async HTTP client/server     |
| `aiomysql`  | Async MySQL access           |
| `asyncpg`   | Fast async PostgreSQL driver |
| `aiosqlite` | Async SQLite                 |
| `trio`      | Alternative async framework  |
| `curio`     | Experimental coroutine lib   |

---

## 🧠 GIL: Global Interpreter Lock

- CPython's mechanism to protect internal memory
- Only one thread executes Python bytecode at a time
- I/O-bound threads still benefit
- Use `multiprocessing` for CPU-bound parallelism

### Alternatives

- Use C extensions (NumPy, Cython, etc.)
- Use other interpreters (e.g., PyPy, Jython)

---

## 🧪 Testing and Debugging Concurrency

- Use `pytest-asyncio` for `async` test functions
- Watch for race conditions, deadlocks
- Use tools like `threading.settrace`, `faulthandler`, and logging
- Tools: `py-spy`, `viztracer`, `concurrent-log-handler`

---

## 🧨 Common Pitfalls

### 1. Blocking call inside `async def`

```python
async def foo():
    time.sleep(1)  # ❌ blocks event loop
```

→ Use `await asyncio.sleep(1)` instead.

---

### 2. Shared state without locks

Use `threading.Lock`, `multiprocessing.Lock`, or queues.

---

### 3. Mixing threads and asyncio without care

Use:

```python
loop.run_in_executor(None, blocking_function)
```

---

## 🧬 Hybrid Example: Async + Thread Pool

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor

def blocking_io():
    ...

async def main():
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, blocking_io)
```

---

## ✅ Summary

| Model            | Best for           | Parallel? | GIL?   | Notes                         |
|------------------|--------------------|-----------|--------|-------------------------------|
| `threading`      | I/O-bound          | No        | Yes    | Simple, shared memory         |
| `multiprocessing`| CPU-bound          | Yes       | No     | True parallelism              |
| `asyncio`        | I/O-bound, scalable| No        | N/A    | Best for async-compatible APIs|
| `futures`        | High-level API     | Varies    | Depends| Works with both threads/procs |

---

## 📚 Further Reading

- [asyncio official docs](https://docs.python.org/3/library/asyncio.html)
- [concurrent.futures docs](https://docs.python.org/3/library/concurrent.futures.html)
- [Python threading](https://docs.python.org/3/library/threading.html)
- [Python multiprocessing](https://docs.python.org/3/library/multiprocessing.html)
- [Understanding the GIL (David Beazley)](https://www.dabeaz.com/python/UnderstandingGIL.pdf)
- Fluent Python — Chapter 18–21

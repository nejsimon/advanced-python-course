# Python Async/Await

Python's `async`/`await` syntax enables **asynchronous programming** using **coroutines**. It provides concurrency without threads by suspending function execution during I/O or `await` points, allowing the event loop to run other tasks.

---

## 🔰 What Is Async/Await?

- `async def`: defines a coroutine function
- `await`: suspends execution until an `awaitable` is done

```python
import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(1)
    print("World")
```

> Coroutines must be scheduled and run in an event loop.

---

## ⚙️ The Event Loop

The **event loop** is the central scheduler for async tasks. It:
- Manages coroutine execution
- Waits on I/O (sockets, files, timers)
- Resumes paused coroutines

```python
asyncio.run(greet())
```

Equivalent to:

```python
loop = asyncio.get_event_loop()
loop.run_until_complete(greet())
```

---

## 🧱 Declaring Coroutines

```python
async def fetch_data():  # coroutine function
    return 42

coro = fetch_data()  # coroutine object
```

You must:
- `await` the coroutine
- or run it via `asyncio.create_task()` or `asyncio.run()`

---

## 🧪 Awaitables

An object is **awaitable** if it is:
- a coroutine
- a `Future`
- an object with an `__await__()` method

### You can only `await` inside `async def`:

```python
async def foo():
    await asyncio.sleep(1)  # ✅ OK

def bar():
    await asyncio.sleep(1)  # ❌ SyntaxError
```

---

## 🔀 Scheduling and Running Tasks

### Concurrent Tasks with `asyncio.create_task()`

```python
async def main():
    task1 = asyncio.create_task(greet())
    task2 = asyncio.create_task(greet())
    await task1
    await task2

asyncio.run(main())
```

> `create_task()` schedules coroutine execution but does not await it immediately.

---

## 🧩 `await` vs `create_task()`

| Operation         | Purpose                            |
|-------------------|-------------------------------------|
| `await coro()`    | Run coroutine, wait for result      |
| `create_task()`   | Schedule coroutine concurrently     |
| `gather()`        | Wait for multiple tasks concurrently|
| `sleep()`         | Non-blocking delay                  |

---

## 🧪 asyncio.gather()

Run coroutines concurrently and collect results:

```python
async def main():
    results = await asyncio.gather(
        fetch_data(),
        fetch_data(),
        return_exceptions=True
    )
```

---

## 🔄 Parallelism with `asyncio.to_thread`

Run blocking code in a thread without blocking the event loop:

```python
import time

def blocking_io():
    time.sleep(1)
    return "done"

async def main():
    result = await asyncio.to_thread(blocking_io)
```

---

## 🧵 Async Context Managers and Iterators

### Async Context Manager

```python
class Resource:
    async def __aenter__(self):
        ...
    async def __aexit__(self, exc_type, exc_val, tb):
        ...

async with Resource() as r:
    ...
```

### Async Iterator

```python
class AsyncCounter:
    def __init__(self, limit): self.i = 0; self.limit = limit

    def __aiter__(self): return self

    async def __anext__(self):
        if self.i >= self.limit: raise StopAsyncIteration
        await asyncio.sleep(0.1)
        self.i += 1
        return self.i
```

```python
async for num in AsyncCounter(3):
    print(num)
```

---

## 🔄 Mixing Sync and Async

- **You cannot call `await` from sync code.**
- Wrap coroutines in `asyncio.run()`, or use `loop.run_until_complete()` in sync functions.
- Wrap blocking code in `asyncio.to_thread()` or run it in a process.

---

## 🧪 Timeout and Cancellation

### Timeout with `asyncio.wait_for`

```python
await asyncio.wait_for(fetch_data(), timeout=2)
```

### Cancelling Tasks

```python
task = asyncio.create_task(fetch_data())
task.cancel()
```

---

## 🛠️ `asyncio.run()` vs `loop.run_until_complete()`

Use `asyncio.run()` for high-level APIs (Python 3.7+). Older style (before 3.7):

```python
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
```

---

## ⚠️ Gotchas and Quirks

### 1. Forgetting to `await`

```python
async def foo(): return 42

result = foo()   # coroutine object, not 42!
```

### 2. `await` only in `async def`

You can't `await` in regular `def`.

### 3. Blocking Functions Freeze the Event Loop

```python
def slow():
    time.sleep(5)  # ❌ Blocks event loop

await asyncio.to_thread(slow)  # ✅
```

### 4. Don't Mix `asyncio.run()` Inside Event Loops

You can't call `asyncio.run()` from inside an already running loop (e.g., in Jupyter).

---

## ✅ Summary

| Feature                   | Description                         |
|----------------------------|-------------------------------------|
| `async def`               | Defines coroutine                   |
| `await`                   | Suspends until awaitable finishes   |
| `create_task()`           | Schedules coroutine                 |
| `async with / async for`  | Asynchronous context/iteration      |
| `gather()`                | Parallel execution, ordered results |
| `to_thread()`             | Run blocking code in thread         |
| `wait_for()`              | Timeout management                  |
| `cancel()`                | Task cancellation                   |

---

## 📚 Further Reading

- [Python asyncio docs](https://docs.python.org/3/library/asyncio.html)
- [PEP 492 – Coroutines with async/await](https://peps.python.org/pep-0492/)
- [Real Python: Async IO](https://realpython.com/async-io-python/)
- Fluent Python – Chapters 18–21


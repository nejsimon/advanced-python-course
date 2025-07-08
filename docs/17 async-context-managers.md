# Async Context Managers in Python

Python supports **asynchronous context managers** through the `async with` syntax. These allow for resource management within `async` functions, especially when working with asynchronous I/O, databases, and network clients.

---

## 🤔 What Is an Async Context Manager?

An **async context manager** is an object that implements:

```python
__aenter__(self)
__aexit__(self, exc_type, exc_val, exc_tb)
```

Used via:

```python
async with some_async_manager() as resource:
    await do_something(resource)
```

---

## 🚀 Use Cases

| Use Case          | Example                     |
| ----------------- | --------------------------- |
| Async file access | `aiofiles.open()`           |
| DB connections    | `asyncpg.connect()`         |
| Web clients       | `aiohttp.ClientSession()`   |
| Background tasks  | `anyio.create_task_group()` |

---

## 🔧 Example: Using `aiofiles`

```python
import aiofiles

async def read_file():
    async with aiofiles.open("file.txt", mode='r') as f:
        contents = await f.read()
        print(contents)
```

---

## 🔧 Example: Custom Async Context Manager (Class-based)

```python
class AsyncTimer:
    async def __aenter__(self):
        self.start = time.perf_counter()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        duration = time.perf_counter() - self.start
        print(f"Async elapsed: {duration:.2f}s")
```

---

## 🔧 Example: Custom Async Context Manager via `@asynccontextmanager`

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def async_timer():
    start = time.perf_counter()
    yield
    duration = time.perf_counter() - start
    print(f"Async elapsed: {duration:.2f}s")
```

---

## 📅 Nesting Async Contexts

```python
async with aiofiles.open("a") as a, aiofiles.open("b", "w") as b:
    data = await a.read()
    await b.write(data)
```

---

## ⚠️ Mixing `with` and `async with`

Don't:

```python
with aiofiles.open("file.txt") as f:  # ❌
    ...
```

Use:

```python
async with aiofiles.open("file.txt") as f:
    ...
```

---

## 🏆 Libraries with Async Context Support

| Library    | Async Manager Support      |
| ---------- | -------------------------- |
| `aiofiles` | File operations            |
| `aiohttp`  | HTTP sessions & requests   |
| `asyncpg`  | PostgreSQL connection pool |
| `motor`    | Async MongoDB client       |
| `anyio`    | Structured concurrency     |
| `httpx`    | Async HTTP client          |

---

## 🚫 Limitations

* `__aenter__` and `__aexit__` must be `async def`
* Can only be used inside an `async def` function
* Cannot use `await` inside regular `__enter__`/`__exit__`

---

## 📈 Debugging Tips

* Use `print` or logging in `__aenter__`/`__aexit__`
* Wrap logic in `try`/`except` to surface errors
* Remember that `__aexit__` is always called, even on exceptions

---

## 🔍 Summary

| Feature                | Notes                                 |
| ---------------------- | ------------------------------------- |
| `async with`           | Like `with` but in `async def`        |
| `__aenter__()`         | Awaited at entry                      |
| `__aexit__()`          | Awaited at exit (even on exception)   |
| `@asynccontextmanager` | Easy generator-based managers         |
| Use cases              | Async I/O, DB, HTTP, background tasks |

---

## 📚 Further Reading

* [contextlib.asynccontextmanager](https://docs.python.org/3/library/contextlib.html#contextlib.asynccontextmanager)
* [PEP 492 — Coroutines with async and await syntax](https://peps.python.org/pep-0492/)
* [aiohttp documentation](https://docs.aiohttp.org/en/stable/)
* Fluent Python – Chapter 21: Concurrency with asyncio

# Python Async Contexts: Coding Challenges

These challenges focus on working with asynchronous context managers (`async with`), using `asyncio` constructs, and handling asynchronous resource management.

---

## Challenge 1: Basic `async with` Statement

**Objective**: Use an asynchronous context manager.

```python
import asyncio
from contextlib import asynccontextmanager

@asynccontextmanager
async def acontext():
    print("Enter")
    yield
    print("Exit")

async def main():
    async with acontext():
        print("Inside")

asyncio.run(main())
```

---

## Challenge 2: Async Resource Manager with Delay

**Objective**: Create an `async` context manager that simulates resource acquisition and release with `await`.

```python
class AsyncResource:
    async def __aenter__(self):
        await asyncio.sleep(0.1)
        print("Resource acquired")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await asyncio.sleep(0.1)
        print("Resource released")

async def main():
    async with AsyncResource():
        print("Working")

asyncio.run(main())
```

---

## Challenge 3: Async Context with Exception Handling

**Objective**: Ensure `__aexit__` is called even when an exception occurs.

```python
class SafeAsync:
    async def __aenter__(self):
        print("Entering")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("Exiting")
        if exc_type:
            print(f"Handled {exc_type.__name__}")
        return True  # Suppress the exception

async def main():
    async with SafeAsync():
        raise ValueError("oops")

asyncio.run(main())
```

---

## Challenge 4: Reusing `@asynccontextmanager`

**Objective**: Use `@asynccontextmanager` to yield a reusable async context manager.

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def open_stream(name):
    print(f"Opening {name}")
    yield name
    print(f"Closing {name}")

async def main():
    async with open_stream("log.txt") as f:
        assert f == "log.txt"

asyncio.run(main())
```

---

## Challenge 5: Nesting Async Contexts

**Objective**: Combine multiple async context managers in a single `async with`.

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def one():
    print("Enter one")
    yield
    print("Exit one")

@asynccontextmanager
async def two():
    print("Enter two")
    yield
    print("Exit two")

async def main():
    async with one(), two():
        print("Inside both")

asyncio.run(main())
```

---

## Challenge 6: Async File Mock

**Objective**: Simulate async file access using an async context manager.

```python
class AsyncFile:
    def __init__(self, path):
        self.path = path

    async def __aenter__(self):
        print(f"Opening {self.path}")
        return self

    async def __aexit__(self, *args):
        print(f"Closing {self.path}")

    async def read(self):
        await asyncio.sleep(0.1)
        return "data"

async def main():
    async with AsyncFile("demo.txt") as f:
        data = await f.read()
        assert data == "data"

asyncio.run(main())
```

---

## Challenge 7: Using `AsyncExitStack`

**Objective**: Dynamically enter a variable number of async contexts.

```python
from contextlib import AsyncExitStack, asynccontextmanager

@asynccontextmanager
async def resource(name):
    print(f"Open {name}")
    yield name
    print(f"Close {name}")

async def main():
    async with AsyncExitStack() as stack:
        res1 = await stack.enter_async_context(resource("R1"))
        res2 = await stack.enter_async_context(resource("R2"))
        print(res1, res2)

asyncio.run(main())
```

---

## Challenge 8: Async Context in Real Usage (Semaphore)

**Objective**: Control concurrency using an async context manager like `Semaphore`.

```python
import asyncio

sem = asyncio.Semaphore(2)

async def worker(i):
    async with sem:
        print(f"Worker {i} start")
        await asyncio.sleep(1)
        print(f"Worker {i} done")

async def main():
    await asyncio.gather(*(worker(i) for i in range(4)))

asyncio.run(main())
```

---

## Challenge 9: Async Generator Context

**Objective**: Combine async generator with `async with` for streaming data.

```python
class AsyncSource:
    def __init__(self, limit):
        self.limit = limit

    async def __aiter__(self):
        for i in range(self.limit):
            await asyncio.sleep(0.1)
            yield i

async def main():
    async for item in AsyncSource(3):
        print(item)

asyncio.run(main())
```

---

## Challenge 10: Exception Propagation with `async with`

**Objective**: Let exceptions bubble through an async context manager.

```python
class LogContext:
    async def __aenter__(self):
        print("Start")
        return self

    async def __aexit__(self, exc_type, exc_val, tb):
        print("Exit")
        if exc_type:
            print(f"Error: {exc_val}")
        return False  # Don't suppress

async def main():
    try:
        async with LogContext():
            raise RuntimeError("Boom")
    except RuntimeError:
        print("Caught")

asyncio.run(main())
```


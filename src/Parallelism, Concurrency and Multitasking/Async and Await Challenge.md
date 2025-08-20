# Python async/await: Coding Challenges

These challenges are designed to help you master Python's asynchronous programming model using `async`/`await`, `asyncio`, tasks, concurrency control, and asynchronous context managers.

---

## Challenge 1: Basic async function

**Objective**: Write a simple async function that returns a greeting.

```python
import asyncio

async def greet(name):
    return f"Hello, {name}"

assert asyncio.run(greet("Alice")) == "Hello, Alice"
```

---

## Challenge 2: Awaiting asyncio.sleep

**Objective**: Simulate I/O delay using `await asyncio.sleep`.

```python
async def wait_and_print():
    print("Waiting...")
    await asyncio.sleep(1)
    print("Done")

asyncio.run(wait_and_print())
```

---

## Challenge 3: Sequential vs Concurrent

**Objective**: Show the time difference between sequential and concurrent execution of async calls.

```python
import time

async def wait(n):
    await asyncio.sleep(n)
    return n

async def run_sequential():
    start = time.time()
    await wait(1)
    await wait(1)
    return time.time() - start

async def run_concurrent():
    start = time.time()
    await asyncio.gather(wait(1), wait(1))
    return time.time() - start

print(asyncio.run(run_sequential()))  # ~2 seconds
print(asyncio.run(run_concurrent()))  # ~1 second
```

---

## Challenge 4: Using asyncio.create\_task

**Objective**: Launch multiple async operations as tasks and await their results.

```python
async def print_delayed(text, delay):
    await asyncio.sleep(delay)
    print(text)

async def main():
    t1 = asyncio.create_task(print_delayed("first", 1))
    t2 = asyncio.create_task(print_delayed("second", 0.5))
    await t1
    await t2

asyncio.run(main())
```

---

## Challenge 5: Canceling Tasks

**Objective**: Cancel a running task.

```python
async def never_ending():
    try:
        while True:
            print("Running...")
            await asyncio.sleep(0.1)
    except asyncio.CancelledError:
        print("Cancelled")

async def main():
    task = asyncio.create_task(never_ending())
    await asyncio.sleep(0.3)
    task.cancel()
    await task

asyncio.run(main())
```

---

## Challenge 6: Async Generator

**Objective**: Write an async generator that yields values with delay.

```python
async def ticker():
    for i in range(3):
        await asyncio.sleep(0.1)
        yield i

async def main():
    async for value in ticker():
        print(value)

asyncio.run(main())
```

---

## Challenge 7: Timeout Handling

**Objective**: Use `asyncio.wait_for` to enforce timeout on an async function.

```python
async def slow():
    await asyncio.sleep(2)

async def main():
    try:
        await asyncio.wait_for(slow(), timeout=1)
    except asyncio.TimeoutError:
        print("Timeout!")

asyncio.run(main())
```

---

## Challenge 8: Semaphore for Concurrency Limits

**Objective**: Use `asyncio.Semaphore` to limit concurrent access.

```python
sem = asyncio.Semaphore(2)

async def limited_task(n):
    async with sem:
        print(f"Start {n}")
        await asyncio.sleep(0.5)
        print(f"End {n}")

async def main():
    await asyncio.gather(*(limited_task(i) for i in range(5)))

asyncio.run(main())
```

---

## Challenge 9: Async Context Manager

**Objective**: Create an async context manager using `__aenter__` and `__aexit__`.

```python
class AsyncTimer:
    async def __aenter__(self):
        print("Starting")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Exiting")

async def main():
    async with AsyncTimer():
        await asyncio.sleep(0.1)

asyncio.run(main())
```

---

## Challenge 10: Combining sync and async

**Objective**: Safely call an async function from a sync context (e.g. script entry point).

```python
async def async_greet():
    return "Hello async!"

# Safe top-level call in main guard
if __name__ == "__main__":
    print(asyncio.run(async_greet()))
```


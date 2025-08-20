# Python Concurrency Models: Coding Challenges

These challenges cover different concurrency models in Python, including threads, asyncio, multiprocessing, and cooperative multitasking.

---

## Challenge 1: Threading Model - Basic Threads

**Objective**: Run multiple threads to execute parallel tasks.

```python
import threading
import time

def worker(name):
    time.sleep(1)
    print(f"Finished {name}")

threads = [threading.Thread(target=worker, args=(f"T{i}",)) for i in range(3)]
for t in threads: t.start()
for t in threads: t.join()
```

---

## Challenge 2: Thread Safety with Lock

**Objective**: Use `threading.Lock` to avoid race conditions.

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(1000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(10)]
for t in threads: t.start()
for t in threads: t.join()
assert counter == 10000
```

---

## Challenge 3: AsyncIO - Concurrent Tasks

**Objective**: Run async functions concurrently.

```python
import asyncio

async def work(name):
    await asyncio.sleep(1)
    print(f"Done: {name}")

async def main():
    await asyncio.gather(work("a"), work("b"), work("c"))

asyncio.run(main())
```

---

## Challenge 4: AsyncIO with Semaphore

**Objective**: Limit concurrency with `asyncio.Semaphore`.

```python
import asyncio

sem = asyncio.Semaphore(2)

async def task(i):
    async with sem:
        await asyncio.sleep(1)
        return i

async def main():
    results = await asyncio.gather(*(task(i) for i in range(5)))
    print(results)

asyncio.run(main())
```

---

## Challenge 5: Multiprocessing Pool

**Objective**: Run CPU-bound tasks with `multiprocessing.Pool`.

```python
from multiprocessing import Pool

def square(x): return x * x

with Pool(4) as p:
    results = p.map(square, range(5))

assert results == [0, 1, 4, 9, 16]
```

---

## Challenge 6: Communicating Between Processes

**Objective**: Use `multiprocessing.Queue` to pass data.

```python
from multiprocessing import Process, Queue

def worker(q):
    q.put("Hello from process")

q = Queue()
p = Process(target=worker, args=(q,))
p.start()
p.join()
assert q.get() == "Hello from process"
```

---

## Challenge 7: Coroutine Pipeline (Generator-Based Concurrency)

**Objective**: Chain coroutines using `yield`.

```python
def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start

@coroutine
def printer():
    while True:
        value = (yield)
        print(f"Received: {value}")

p = printer()
p.send("Hello")
```

---

## Challenge 8: `concurrent.futures.ThreadPoolExecutor`

**Objective**: Execute a batch of IO-bound tasks concurrently.

```python
from concurrent.futures import ThreadPoolExecutor
import time

def fetch(url):
    time.sleep(1)
    return f"data from {url}"

with ThreadPoolExecutor() as executor:
    results = list(executor.map(fetch, ["/a", "/b", "/c"]))

assert len(results) == 3
```

---

## Challenge 9: Deadlock Scenario (And Fix)

**Objective**: Simulate a deadlock and then fix it.

```python
# Avoid acquiring multiple locks in inconsistent order.
```

```python
lock1 = threading.Lock()
lock2 = threading.Lock()

def task1():
    with lock1:
        with lock2:
            pass

def task2():
    with lock2:
        with lock1:
            pass

# Now reverse one of the orders to fix the deadlock
```

---

## Challenge 10: Compare Concurrency Models

**Objective**: Time and compare threading, multiprocessing, and asyncio.

```python
# Run equivalent tasks with each model and measure performance.
# Discuss trade-offs: CPU-bound vs IO-bound, startup cost, GIL implications.
```


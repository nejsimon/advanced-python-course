# Concurrency & Parallelism in the Standard Library

Python’s standard library provides multiple tools for handling tasks concurrently (tasks appear to run at the same time) or in parallel (tasks actually run at the same time on multiple CPU cores). Choosing the right model depends on whether your workload is I/O-bound (waiting for input/output) or CPU-bound (intensive computation).

## threading — Lightweight Concurrency
- Threads share memory and are best suited for I/O-bound tasks.
- Python’s Global Interpreter Lock (GIL) prevents true CPU parallelism with threads, but they are excellent for waiting on network, disk, or other I/O.
- Example:
  ```python
  import threading
  import time

  def worker(name):
      print(f"{name} starting")
      time.sleep(1)
      print(f"{name} done")

  threads = [threading.Thread(target=worker, args=(f"Thread-{i}",)) for i in range(3)]
  for t in threads: t.start()
  for t in threads: t.join()
  ```

## multiprocessing — True Parallelism with Processes

- Each process has its own Python interpreter and memory space.
- Great for CPU-bound work (e.g., heavy computation).
- Avoids the GIL by running code in separate processes.
- Example:
  ```python
  from multiprocessing import Process, cpu_count

  def compute(n):
      return sum(i * i for i in range(n))

  if __name__ == "__main__":
      processes = [Process(target=compute, args=(10_000_000,)) for _ in range(cpu_count())]
      for p in processes: p.start()
      for p in processes: p.join()
  ```

## concurrent.futures — High-Level Concurrency
- Unified API for threads and processes.
- Provides `ThreadPoolExecutor` and `ProcessPoolExecutor`.
- Easy to submit tasks and collect results. 
- Example (`ThreadPoolExecutor`):
  ```python
  from concurrent.futures import ThreadPoolExecutor

  def fetch(url):
      import requests
      return requests.get(url).status_code

  urls = ["https://example.com", "https://httpbin.org/get"]

  with ThreadPoolExecutor(max_workers=5) as executor:
      results = list(executor.map(fetch, urls))
  print(results)
  ```

## asyncio — Asynchronous I/O
- Best for large numbers of concurrent I/O-bound tasks.
- Uses event loop and coroutines (async def, await).
- Tasks cooperate instead of preemptively interrupting each other.
- Example:
  ```python
  import asyncio
  import aiohttp  # third-party, but asyncio is stdlib

  async def fetch(session, url):
      async with session.get(url) as resp:
          return await resp.text()

  async def main():
      urls = ["https://example.com", "https://httpbin.org/get"]
      async with aiohttp.ClientSession() as session:
          tasks = [fetch(session, u) for u in urls]
          results = await asyncio.gather(*tasks)
          print([len(r) for r in results])

  asyncio.run(main())
  ```

## queue — Thread-Safe Queues

- Provides FIFO (Queue), LIFO, and Priority queues.
- Used for producer–consumer patterns.
- Example:
  ```python
  import threading, queue, time

  q = queue.Queue()

  def producer():
      for i in range(5):
          q.put(i)
          time.sleep(0.5)

  def consumer():
      while True:
          item = q.get()
          if item is None: break
          print("Consumed", item)

  threading.Thread(target=producer).start()
  threading.Thread(target=consumer).start()
  ```

## Choosing the Right Tool
- I/O-bound, few tasks: threading
- I/O-bound, many tasks: asyncio
- CPU-bound: multiprocessing or ProcessPoolExecutor
- Unified interface: concurrent.futures
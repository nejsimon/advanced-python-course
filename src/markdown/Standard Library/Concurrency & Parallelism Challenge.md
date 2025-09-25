# Challenge: Concurrency & Parallelism in the Standard Library

This challenge will test your ability to use Python’s built-in concurrency and parallelism tools (threading, multiprocessing, concurrent.futures, and asyncio). You’ll practice identifying the right tool for different workloads and implementing small concurrent programs.

## Part 1: Threading – Producer/Consumer

Implement a program that uses threading and queue.Queue to:
- Spawn one producer thread that generates 10 random integers (0–100) and puts them in a queue.
- Spawn two consumer threads that each take items from the queue, square them, and print the result with the consumer’s name.
- Ensure that all threads finish cleanly.

## Part 2: Multiprocessing – CPU-Bound Task

Write a program using multiprocessing.Process that:
- Spawns as many processes as CPU cores on your machine.
- Each process computes the sum of squares up to N=10_000_000.
- Prints how long the computation takes in total compared to running sequentially.
- Hint: Use time.perf_counter() to measure execution time.

## Part 3: Futures – Web Fetching

Using concurrent.futures.ThreadPoolExecutor:
- Fetch the contents of the following URLs concurrently:
  - https://httpbin.org/get
  - https://httpbin.org/uuid
  - https://httpbin.org/delay/2
- Collect all responses and print the length of each response body.

## Part 4: Asyncio – Concurrent Sleep

- Write an asyncio program that:
- Starts 5 tasks, each sleeping for a random time between 1 and 3 seconds.
- Prints a message when each task finishes.
- Measures total runtime and shows that it’s shorter than running them sequentially.

## Stretch Goal 🔥

Mix threads and async by starting an asyncio event loop in the main thread and running blocking file I/O (writing logs) in a thread pool via loop.run_in_executor.

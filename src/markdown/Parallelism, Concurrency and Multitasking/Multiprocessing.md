# Multiprocessing

Python's `multiprocessing` module enables the creation of separate processes to execute code concurrently, bypassing the limitations of the Global Interpreter Lock (GIL). This is essential for CPU-bound tasks that cannot fully benefit from multithreading.

---

## 1. Basics

* **Process-based parallelism:** Each process has its own Python interpreter and memory space.
* **Import:**

  ```python
  import multiprocessing
  ```
* **Creating a Process:**

  ```python
  from multiprocessing import Process

  def worker(name):
      print(f"Hello from {name}")

  if __name__ == "__main__":
      p = Process(target=worker, args=("process-1",))
      p.start()
      p.join()
  ```

---

## 2. Key Concepts

### Processes

* Similar to threads, but fully independent.
* Memory is **not shared** by default.

### Queues and Pipes

* Use `multiprocessing.Queue` or `Pipe` for inter-process communication (IPC).

### Shared Memory

* `multiprocessing.Value` and `multiprocessing.Array` allow sharing simple values/arrays between processes.

### Pool of Workers

* `multiprocessing.Pool` provides convenient worker pool abstraction for parallel map/reduce.

  ```python
  from multiprocessing import Pool

  def square(x):
      return x * x

  if __name__ == "__main__":
      with Pool(4) as p:
          print(p.map(square, [1, 2, 3, 4]))
  ```

### Managers

* `multiprocessing.Manager` allows sharing Python objects (lists, dicts, namespaces) across processes.

---

## 3. Synchronization

* `Lock`, `RLock`, `Semaphore`, `Event`, and `Condition` exist, similar to `threading` equivalents, but process-safe.
* Prevent race conditions across processes.

---

## 4. Multiprocessing vs Threading

* Multiprocessing bypasses GIL → true parallelism.
* Higher memory usage since each process has its own memory space.
* Best for **CPU-bound** tasks (e.g., math, simulations).
* Threads remain better for **I/O-bound** tasks.

---

## 5. Advanced Features

### Process Pools with Async

```python
with Pool() as p:
    result = p.apply_async(square, (10,))
    print(result.get())
```

### Contexts

* Start methods: `fork`, `spawn`, `forkserver` (availability depends on OS).
* Example:

  ```python
  multiprocessing.set_start_method("spawn")
  ```

### Error Handling

* Exceptions in child processes propagate via `get()` in async results.

### Termination

* `terminate()` stops processes abruptly.
* Always prefer graceful shutdown using `join()`.

---

## 6. Common Pitfalls

* **Windows vs Unix:** `fork` is only available on Unix. On Windows, processes always start fresh (`spawn`).
* **Pickling:** Functions/objects sent to child processes must be picklable.
* **Global variables:** Not shared between processes; must use IPC or shared memory.
* **Debugging:** Harder than threads; print/logging often used for debugging.

---

## 7. Alternatives and Related Libraries

* **concurrent.futures.ProcessPoolExecutor**: Higher-level abstraction, easier than raw `multiprocessing.Pool`.
* **joblib**: Popular in scientific Python, simplifies parallel loops.
* **Dask, Ray**: Distribute workloads beyond a single machine.

---

## 8. Best Practices

* Always guard multiprocessing code with:

  ```python
  if __name__ == "__main__":
      ...
  ```

  to avoid recursive spawning.
* Use context managers for pools.
* Prefer `concurrent.futures` when simplicity is needed.
* Profile before parallelizing; sometimes multiprocessing overhead exceeds benefits.

---

## 9. Summary

* Multiprocessing enables CPU-bound parallelism in Python.
* Provides processes, IPC mechanisms, pools, and synchronization tools.
* Must handle platform differences, pickling constraints, and higher memory usage.
* Ideal for CPU-intensive workloads, simulations, and data processing pipelines.

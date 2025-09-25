# Coding Challenge: Python Standard Library — Data Types & Collections

This challenge will test your understanding of specialized containers and data types provided by the Python standard library.

---

## Part 1: Word Frequency Counter
1. Write a function `word_frequencies(text: str) -> list[tuple[str, int]]` that:
   - Uses `collections.Counter` to count the frequency of each word in a string.
   - Returns the top 5 most common words as a list of `(word, count)` tuples.
2. Test your function on the following string:
"python python code code code collections counter counter deque heapq"


---

## Part 2: Task Queue with `deque`
1. Simulate a simple task queue:
- Use `collections.deque` to enqueue and dequeue tasks.
- Implement functions `add_task(queue, task)` and `process_task(queue)` that:
  - Add a task string to the right side of the queue.
  - Remove and return a task from the left side of the queue.
2. Add tasks `"task1"`, `"task2"`, `"task3"`, then process them in order.

---

## Part 3: Priority Queue with `heapq`
1. Create a list of tasks represented as tuples `(priority, task_name)` where **lower numbers mean higher priority**.
2. Use `heapq` to:
- Push at least 5 tasks with varying priorities.
- Pop and print tasks in correct priority order.

---

## Part 4: Sorted Insert with `bisect`
1. Maintain a sorted list of integers.
2. Write a function `insert_sorted(sorted_list: list[int], value: int)` that uses `bisect.insort` to insert numbers while keeping the list sorted.
3. Insert values `[5, 2, 9, 1, 7]` into an initially empty list and show the final result.

---

## Part 5: Layered Config with `ChainMap`
1. You have three dictionaries:
```python
default_config = {"theme": "light", "debug": False}
env_config = {"debug": True}
cli_config = {"theme": "dark"}
Use collections.ChainMap to combine them so that:

CLI settings override environment settings.

Environment settings override default settings.

Print the resulting values for "theme" and "debug".

Part 6: Weak References
Create a simple class User with a name attribute.

Create a weakref.WeakValueDictionary to store users by ID.

Demonstrate that when you delete the original reference, the entry in the dictionary disappears automatically.

Bonus Challenge: Custom Counter with defaultdict
Re-implement Part 1 (Word Frequency Counter) without Counter, using collections.defaultdict(int).

Expected Skills
Choosing the right data structure for the problem.

Using deque for FIFO queues.

Implementing priority queues with heapq.

Maintaining sorted sequences with bisect.

Combining multiple configurations with ChainMap.

Understanding memory management with weak references.

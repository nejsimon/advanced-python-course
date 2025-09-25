# Coding Challenge: Algorithms & Utilities

This challenge will help you practice Python’s standard library modules that provide iteration tools, functional programming helpers, heaps, binary search, random utilities, and statistics.

---

## Part 1: `itertools`
1. Use `itertools.permutations` to generate all possible **3-letter codes** from the letters `"A", "B", "C", "D"`.
2. Use `itertools.groupby` to group the numbers `[1, 1, 2, 2, 2, 3, 3, 4]` by value.
3. Create an infinite cycle of `"YES", "NO"` using `itertools.cycle`, and take the first 10 outputs.

---

## Part 2: `functools`
1. Write a recursive Fibonacci function and apply `functools.lru_cache` to speed it up. Benchmark it with and without caching.
2. Use `functools.partial` to create a `multiply_by_3` function from a generic `multiply(x, y)` function.
3. Implement a `@functools.singledispatch` function `describe(obj)` with different implementations for `int`, `list`, and `str`.

---

## Part 3: `operator`
1. Sort a list of dictionaries `[{ "name": "Alice", "age": 30 }, { "name": "Bob", "age": 25 }]` by the `"age"` key using `operator.itemgetter`.
2. Use `operator.attrgetter` to sort a list of `Person` objects by their `age` attribute.

---

## Part 4: `heapq`
1. Implement a priority queue of tasks, where each task is a tuple `(priority, task_name)`.
2. Insert tasks into the heap and always pop the task with the **lowest priority number** first.
3. Extend the queue with new tasks dynamically and ensure it remains ordered.

---

## Part 5: `bisect`
1. Maintain a sorted list of numbers.
2. Use `bisect.insort` to insert numbers `[5, 3, 7, 1, 9]` into an initially empty list.
3. Write a function `find_closest(arr, x)` that returns the closest number to `x` using `bisect`.

---

## Part 6: `statistics`
1. Given a dataset `[2, 4, 4, 4, 5, 5, 7, 9]`, calculate:
   - Mean
   - Median
   - Mode
   - Standard deviation
2. Compare results against NumPy (if available) to confirm correctness.

---

## Part 7: `random`
1. Generate a random password of 12 characters consisting of letters and digits.
2. Simulate rolling two dice 1,000 times and estimate the probability of getting a sum of 7.
3. Shuffle a deck of 52 playing cards and deal 5 random cards.


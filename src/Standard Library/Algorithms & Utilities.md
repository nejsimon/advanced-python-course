# Standard Library – Algorithms & Utilities

Python’s standard library includes a powerful set of modules that provide **general-purpose algorithms, utilities, and tools for efficiency**. These modules help implement sorting, searching, functional programming patterns, and performance-critical tasks without needing third-party libraries.


## 1. `itertools` – Iteration Tools
- **Purpose**: High-performance building blocks for working with iterators.
- Highlights:
  - Infinite iterators: `count`, `cycle`, `repeat`
  - Combinatorics: `permutations`, `combinations`, `product`
  - Iterator algebra: `chain`, `islice`, `accumulate`, `groupby`
- Example:
  ```python
  from itertools import permutations, cycle, islice

  print(list(permutations("abc", 2)))  
  # [('a','b'), ('a','c'), ('b','a'), ...]

  cyc = cycle("XY")
  print(list(islice(cyc, 5)))  # ['X','Y','X','Y','X']

## 2. functools – Higher-Order Functions
- **Purpose:** Tools for functional programming and callable manipulation. 
- Key features:
  - lru_cache: Memoization for function calls.
  - partial: Fix arguments of a function.
  - reduce: Apply a function cumulatively to a sequence.
  - singledispatch: Generic function overloading by type.
- Example:
  ```python
  from functools import lru_cache, reduce

  @lru_cache(maxsize=None)
  def fib(n):
      return n if n < 2 else fib(n-1) + fib(n-2)

  print(fib(10))  # 55

  nums = [1, 2, 3, 4]
  product = reduce(lambda x, y: x * y, nums)
  print(product)  # 24

## 3. operator – Functional Access to Operators
- **Purpose:** Functions corresponding to Python’s built-in operators (e.g., add, getitem, attrgetter).
- Useful for:
  - Sorting and key functions.
  - Cleaner functional programming style.

- Example:
  ```python
  from operator import itemgetter, attrgetter

  data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
  print(sorted(data, key=itemgetter("age")))

  class Person:
      def __init__(self, name, age): self.name, self.age = name, age
  people = [Person("Charlie", 40), Person("Dave", 20)]
  print(sorted(people, key=attrgetter("age")))

## 4. heapq – Heap Queue (Priority Queue)
- **Purpose:** Implements min-heaps for efficient priority queues.

- Example:
  ```python
  import heapq

  nums = [5, 1, 7, 3]
  heapq.heapify(nums)
  heapq.heappush(nums, 2)
  print(heapq.heappop(nums))  # 1

## 5. bisect – Binary Search
- **Purpose:** Maintain sorted lists efficiently.
- Example:
  ```python
  import bisect

  arr = [1, 3, 4, 7]
  pos = bisect.bisect(arr, 5)  # position to insert
  print(pos)  # 3

6. statistics – Statistics Functions
- **Purpose:** Basic statistical calculations.
- Example:
  ```python
  import statistics

  data = [10, 20, 30, 40]
  print(statistics.mean(data))     # 25
  print(statistics.median(data))   # 25.0
  print(statistics.pstdev(data))   # population std deviation


7. random – Pseudo-Random Numbers
- **Purpose:** Generate pseudo-random numbers, shuffle data, and simulate randomness.

- Example:
  ```python
  import random

  print(random.randint(1, 10))  # random integer
  print(random.choice(["apple", "banana", "cherry"]))
  random.shuffle([1, 2, 3, 4])


## Quirks & Notes
- itertools produces lazy iterators — many results must be materialized with list().
- functools.lru_cache caches per interpreter run — can lead to memory growth.
- random is not cryptographically secure — use secrets for security purposes.
- statistics is fine for small datasets but not optimized for big data (use NumPy for that).
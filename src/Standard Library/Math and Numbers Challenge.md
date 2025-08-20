# Coding Challenges: Standard Library — Math & Numbers

These exercises cover the `math`, `cmath`, `decimal`, `fractions`, `random`, `secrets`, `statistics`, `numbers`, `array`, `bisect`, and `heapq` modules. They focus on precision, performance, and correct use of numeric tools.

---

## Challenge 1 — `math` Essentials

1. Write a function `circle_area(radius)` that returns the area using `math.pi` and `math.pow`.
2. Implement `angle_between(v1, v2)` that computes the angle in radians between two 2D vectors using `math.atan2` and `math.hypot`.

---

## Challenge 2 — `cmath` for Complex Arithmetic

1. Create a function `roots_quadratic(a, b, c)` that returns the two roots of a quadratic equation using complex math (works for discriminant < 0).
2. Compute magnitude and phase of the root using `abs()` and `cmath.phase()`.

---

## Challenge 3 — High Precision with `decimal`

1. Compute `1 / 7` with 50 decimal places using `decimal.Decimal` and set the context precision appropriately.
2. Demonstrate the difference between `float(1/7)` and the `Decimal` result.
3. Use `Decimal.quantize()` to round a `Decimal` to 2 decimal places with `ROUND_HALF_UP`.

---

## Challenge 4 — Exact Rational Arithmetic (`fractions`)

1. Using `fractions.Fraction`, compute the sum `1/3 + 1/6` and assert it equals `Fraction(1,2)`.
2. Convert a decimal string `'0.1'` to `Fraction` exactly using `Fraction(Decimal('0.1'))` and explain the result difference vs `Fraction(0.1)`.

---

## Challenge 5 — Random vs Secrets

1. Generate a random password of length 12 using `random.choice` and characters from `string.ascii_letters + string.digits`.
2. Generate a cryptographically secure token using `secrets.token_urlsafe(16)` and explain when to prefer `secrets` over `random`.

---

## Challenge 6 — Statistics

1. Given the dataset `[2, 4, 4, 4, 5, 5, 7, 9]`, compute mean, median, mode, variance, and standard deviation using the `statistics` module.
2. Implement a function `trimmed_mean(data, proportion)` that removes the top and bottom `proportion` of the sorted data (e.g., 0.1 means drop 10% smallest and 10% largest) and returns the mean of the remainder.

---

## Challenge 7 — Numeric Type Checking (`numbers`)

1. Write a function `is_real_number(x)` that returns `True` if `x` is an instance of `numbers.Real` but not `bool`.
2. Show that `True` is an instance of `numbers.Integral` and explain why `is_real_number(True)` should usually return `False`.

---

## Challenge 8 — Efficient Storage with `array`

1. Create an `array.array` of type `'d'` (double) and append 1\_000\_000 floats to it; measure memory usage roughly with `sys.getsizeof()` vs a regular list of floats.
2. Demonstrate slicing and `tofile()` / `fromfile()` for binary I/O.

---

## Challenge 9 — Sorted Insert and Search (`bisect`)

1. Maintain a sorted list and write `insert_sorted(lst, value)` using `bisect.insort_left`.
2. Implement `find_nearest(sorted_list, value)` that returns the closest element to `value` using `bisect` to achieve O(log n) search.

---

## Challenge 10 — Priority Queues (`heapq`)

1. Implement a task scheduler using `heapq` where each task is a tuple `(priority, count, task_fn)`; use `count` as a tie-breaker.
2. Push several tasks and pop them in priority order, executing the callable for each.

---

## Bonus Challenge: Benchmark Numeric Approaches

1. Compare summing a large list of floats using `sum()` vs `math.fsum()` and report relative difference and timings.
2. Explain why `math.fsum()` is more accurate.


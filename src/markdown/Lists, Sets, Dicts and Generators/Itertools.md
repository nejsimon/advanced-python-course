# Advanced Python: itertools

The `itertools` module in Python provides a collection of fast, memory-efficient tools for creating and working with iterators. These functions are inspired by functional programming and are especially useful for data processing, combinatorics, and constructing complex iteration patterns.

---

## 1. Core Itertools Functions

### Infinite Iterators

* `itertools.count(start=0, step=1)`: Generates an infinite sequence of numbers.
* `itertools.cycle(iterable)`: Cycles through the elements of an iterable infinitely.
* `itertools.repeat(object, times=None)`: Repeats an object either infinitely or a given number of times.

### Example:

```python
import itertools

for i in itertools.count(10, 2):
    if i > 20:
        break
    print(i)  # 10, 12, 14, 16, 18, 20
```

---

### Combinatoric Iterators

* `itertools.product(iterable, repeat=n)`: Cartesian product.
* `itertools.permutations(iterable, r)`: All r-length permutations.
* `itertools.combinations(iterable, r)`: r-length combinations without replacement.
* `itertools.combinations_with_replacement(iterable, r)`: r-length combinations with replacement.

### Example:

```python
list(itertools.combinations([1,2,3], 2))  # [(1,2), (1,3), (2,3)]
```

---

### Iterators for Filtering

* `itertools.compress(data, selectors)`: Filters elements based on selectors.
* `itertools.dropwhile(predicate, iterable)`: Skips elements until predicate fails.
* `itertools.takewhile(predicate, iterable)`: Takes elements while predicate holds.
* `itertools.filterfalse(predicate, iterable)`: Opposite of `filter()`.

---

### Iterators for Grouping

* `itertools.groupby(iterable, key=None)`: Groups consecutive items with the same key.

### Example:

```python
from itertools import groupby

animals = ["cat", "cow", "dog", "donkey"]
for key, group in groupby(animals, key=lambda x: x[0]):
    print(key, list(group))
# c -> ['cat', 'cow']
# d -> ['dog', 'donkey']
```

---

### Iterators for Combining

* `itertools.chain(*iterables)`: Concatenates multiple iterables.
* `itertools.islice(iterable, start, stop, step)`: Slice an iterator.
* `itertools.starmap(function, iterable)`: Like `map`, but unpacks arguments.
* `itertools.zip_longest(*iterables, fillvalue=None)`: Zips iterables, filling missing values.

---

## 2. Recipes (Patterns Using itertools)

The Python docs include recipes like:

* `grouper(iterable, n, fillvalue=None)` → Chunk data into fixed-length pieces.
* `roundrobin(*iterables)` → Alternate elements from each iterable.
* `powerset(iterable)` → All subsets of a set.

---

## 3. Advanced Usage

* **Performance**: Itertools avoids creating large intermediate data structures.
* **Lazy Evaluation**: Items are produced one at a time, on demand.
* **Composability**: Functions can be chained together.

---

## 4. Quirks & Notes

* `groupby` only groups consecutive items. To group all by key, you must sort first.
* Infinite iterators must be combined with conditions (`islice`, `takewhile`) to avoid unbounded loops.
* Itertools functions return iterators, not lists. Convert explicitly if needed.

---

## 5. When to Use itertools

* Data transformation pipelines.
* Efficient combinatorics.
* Lazy evaluation of large datasets.
* Replacements for verbose `for`-loops.


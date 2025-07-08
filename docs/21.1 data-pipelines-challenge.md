# Python Data Pipelines: Coding Challenges

These challenges explore how to build and structure data pipelines using iterators, generators, comprehensions, functional programming tools, and streaming patterns.

---

## Challenge 1: Chained List Comprehensions

**Objective**: Transform and filter data using a comprehension pipeline.

```python
data = [1, 2, 3, 4, 5, 6]
result = [x * 2 for x in data if x % 2 == 0]
assert result == [4, 8, 12]
```

---

## Challenge 2: Generator Pipeline

**Objective**: Use generator functions to create a lazy evaluation pipeline.

```python
def numbers():
    for i in range(100):
        yield i

def evens(it):
    for i in it:
        if i % 2 == 0:
            yield i

def squared(it):
    for i in it:
        yield i * i

pipeline = squared(evens(numbers()))
assert next(pipeline) == 0
```

---

## Challenge 3: Composing with `itertools`

**Objective**: Use `itertools` to build a streaming pipeline.

```python
import itertools

data = itertools.count(1)
filtered = itertools.islice((x for x in data if x % 3 == 0), 5)
assert list(filtered) == [3, 6, 9, 12, 15]
```

---

## Challenge 4: Function Pipeline Composition

**Objective**: Chain function calls to apply transformations.

```python
def add1(x): return x + 1
def square(x): return x * x

def pipe(data, *funcs):
    for f in funcs:
        data = map(f, data)
    return list(data)

assert pipe([1, 2, 3], add1, square) == [4, 9, 16]
```

---

## Challenge 5: Data Class Streaming Transform

**Objective**: Use `dataclasses` to carry structured data in a pipeline.

```python
from dataclasses import dataclass

@dataclass
class Record:
    name: str
    score: int

data = [Record("Alice", 85), Record("Bob", 92)]
filtered = (r for r in data if r.score > 90)
assert next(filtered).name == "Bob"
```

---

## Challenge 6: Stream CSV Line-by-Line

**Objective**: Read a CSV file lazily with filtering and transformation.

```python
import csv

def stream_csv(path):
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row['score']) > 50:
                yield row['name']
```

---

## Challenge 7: Custom Pipeline Class

**Objective**: Build a custom class for chaining operations.

```python
class Pipeline:
    def __init__(self, data):
        self.data = data

    def map(self, func):
        self.data = map(func, self.data)
        return self

    def filter(self, func):
        self.data = filter(func, self.data)
        return self

    def collect(self):
        return list(self.data)

p = Pipeline(range(10)).filter(lambda x: x % 2 == 0).map(lambda x: x * x)
assert p.collect() == [0, 4, 16, 36, 64]
```

---

## Challenge 8: Parallel Processing with `concurrent.futures`

**Objective**: Process data chunks concurrently.

```python
from concurrent.futures import ThreadPoolExecutor

def process(x): return x * 10

data = [1, 2, 3, 4]
with ThreadPoolExecutor() as pool:
    results = list(pool.map(process, data))

assert results == [10, 20, 30, 40]
```

---

## Challenge 9: Side Effects with `tee`

**Objective**: Split a data stream to be consumed in multiple ways.

```python
import itertools

data = iter(range(5))
a, b = itertools.tee(data)
assert list(a) == list(range(5))
assert list(b) == list(range(5))
```

---

## Challenge 10: Lazy Stream with Context Manager

**Objective**: Combine a generator with a context manager to manage pipeline lifecycle.

```python
from contextlib import contextmanager

@contextmanager
def stream():
    try:
        yield (x for x in range(3))
    finally:
        print("Stream closed")

with stream() as gen:
    assert list(gen) == [0, 1, 2]
```


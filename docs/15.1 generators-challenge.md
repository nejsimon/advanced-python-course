# Python Generators: Coding Challenges

These challenges are designed to help you master Python generators, including generator functions, expressions, delegation, and advanced use of `yield` and `send()`.

---

## Challenge 1: Simple Generator

**Objective**: Write a generator function `count_up_to(n)` that yields numbers from 1 to `n`.

```python
def count_up_to(n):
    for i in range(1, n + 1):
        yield i

assert list(count_up_to(3)) == [1, 2, 3]
```

---

## Challenge 2: Generator Expression

**Objective**: Rewrite a list comprehension as a generator expression.

```python
squares = (x * x for x in range(5))
assert next(squares) == 0
assert list(squares) == [1, 4, 9, 16]
```

---

## Challenge 3: Infinite Generator

**Objective**: Write a generator `infinite_odds()` that yields odd numbers forever.

```python
def infinite_odds():
    n = 1
    while True:
        yield n
        n += 2

odds = infinite_odds()
assert next(odds) == 1
assert next(odds) == 3
```

---

## Challenge 4: Fibonacci Generator

**Objective**: Implement a generator `fibonacci()` that yields the infinite Fibonacci sequence.

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
assert [next(fib) for _ in range(6)] == [0, 1, 1, 2, 3, 5]
```

---

## Challenge 5: Generator with `send()`

**Objective**: Create a generator `accumulator()` that adds values sent to it and yields the total.

```python
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is not None:
            total += value

acc = accumulator()
next(acc)           # Start generator
assert acc.send(10) == 10
assert acc.send(5) == 15
```

---

## Challenge 6: Delegation with `yield from`

**Objective**: Write a generator that uses `yield from` to delegate to another generator.

```python
def inner():
    yield 1
    yield 2

def outer():
    yield 0
    yield from inner()
    yield 3

assert list(outer()) == [0, 1, 2, 3]
```

---

## Challenge 7: Generator with Cleanup Using `try/finally`

**Objective**: Write a generator that prints a message on close using `try/finally`.

```python
def managed():
    try:
        yield 1
        yield 2
    finally:
        print("Cleanup")

m = managed()
next(m)
m.close()  # Should print "Cleanup"
```

---

## Challenge 8: Filtering Generator

**Objective**: Create a generator `filter_even` that only yields even numbers from an iterable.

```python
def filter_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n

assert list(filter_even(range(5))) == [0, 2, 4]
```

---

## Challenge 9: Generator Composition

**Objective**: Chain multiple generators to transform a data stream.

```python
def nums():
    for i in range(3):
        yield i

def square(iterable):
    for x in iterable:
        yield x * x

def double(iterable):
    for x in iterable:
        yield x * 2

assert list(double(square(nums()))) == [0, 2, 8]
```

---

## Challenge 10: Peekable Generator Wrapper

**Objective**: Create a class `Peekable` that wraps a generator and allows peeking at the next value without advancing.

```python
class Peekable:
    def __init__(self, gen):
        self._gen = gen
        self._peek = None
        self._has_peek = False

    def __iter__(self): return self

    def __next__(self):
        if self._has_peek:
            self._has_peek = False
            return self._peek
        return next(self._gen)

    def peek(self):
        if not self._has_peek:
            self._peek = next(self._gen)
            self._has_peek = True
        return self._peek

p = Peekable(iter([1, 2, 3]))
assert p.peek() == 1
assert next(p) == 1
assert next(p) == 2
```


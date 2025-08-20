# `functools`: Python's Functional Programming Toolkit

The `functools` module in Python provides higher-order functions and utilities that operate on or return functions. It enables powerful functional programming patterns, code reuse, memoization, decorators, and dynamic function composition.

---

## 🤖 Core Concepts

| Feature          | Purpose                                    |
| ---------------- | ------------------------------------------ |
| `@lru_cache`     | Cache return values of pure functions      |
| `partial()`      | Freeze some function arguments             |
| `wraps()`        | Preserve metadata in decorators            |
| `reduce()`       | Apply a rolling computation to a sequence  |
| `cache()`        | Lightweight caching (Python 3.9+)          |
| `total_ordering` | Fill in comparison methods from one or two |
| `singledispatch` | Generic function dispatch based on type    |
| `update_wrapper` | Low-level function metadata preservation   |

---

## 🚀 `functools.lru_cache()`

Memoize function calls with a bounded cache.

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```

* `maxsize=None` = unbounded
* Use `.cache_clear()` to reset

> Python 3.9+: `@cache` as an unbounded version

---

## ❄️ `functools.partial()`

Create a new function with fixed arguments:

```python
from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
print(square(4))  # 16
```

---

## 🔧 `functools.wraps()`

Used inside decorators to preserve function metadata:

```python
from functools import wraps

def decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Calling", fn.__name__)
        return fn(*args, **kwargs)
    return wrapper
```

Without `@wraps`, `__name__`, `__doc__`, etc. may be lost.

---

## 🔹 `functools.reduce()`

Apply a function cumulatively:

```python
from functools import reduce
import operator

result = reduce(operator.mul, [1, 2, 3, 4])  # 24
```

Use `functools.reduce()` only when a loop or generator expression isn't clearer.

---

## 🚪 `functools.total_ordering`

Auto-fill comparison methods:

```python
from functools import total_ordering

@total_ordering
class Person:
    def __init__(self, age):
        self.age = age
    def __eq__(self, other):
        return self.age == other.age
    def __lt__(self, other):
        return self.age < other.age
```

Defines: `__le__`, `__gt__`, `__ge__`

---

## 🤠 `functools.singledispatch`

Single-dispatch generic function (like function overloading):

```python
from functools import singledispatch

@singledispatch
def describe(obj):
    return f"Object: {obj}"

@describe.register
def _(obj: int):
    return f"Integer: {obj}"

@describe.register
def _(obj: list):
    return f"List of length {len(obj)}"
```

> Python 3.8+: `singledispatchmethod` for methods

---

## 📌 `functools.update_wrapper()`

Manual version of `@wraps`:

```python
from functools import update_wrapper

def decorator(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return update_wrapper(wrapper, fn)
```

---

## ⚠️ Caveats and Notes

* `@lru_cache` only works with **hashable** arguments
* `partial()` creates a **new function object** with fixed arguments
* `singledispatch` dispatches based on **first argument type only**
* `wraps()` is essential for introspection, debugging, and tooling

---

## 🏛 Advanced Patterns

### Memoization with Custom Key

Use `cachetools` or subclass `lru_cache` to customize key behavior

### Function Composition

Combine functions using `partial` + closures

### Dispatch on Multiple Args

Use libraries like `multipledispatch`, or type guards manually

---

## 📚 Further Reading

* [functools documentation](https://docs.python.org/3/library/functools.html)
* [PEP 443: Single Dispatch](https://peps.python.org/pep-0443/)
* [Python's `wraps` best practices](https://realpython.com/primer-on-python-decorators/)
* Fluent Python – Chapter 7 and 9

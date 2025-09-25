# Python `functools` Module: Coding Challenges

These challenges explore core functionality from the `functools` module, including decorators, memoization, partial functions, method dispatching, and advanced composition techniques.

---

## Challenge 1: Using `partial`

**Objective**: Use `functools.partial` to create specialized functions.

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
assert square(5) == 25
```

---

## Challenge 2: Using `lru_cache` for Memoization

**Objective**: Improve performance of recursive functions using memoization.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

assert fib(35) == 9227465
```

---

## Challenge 3: Custom Key with `lru_cache`

**Objective**: Use `lru_cache` with a custom key via argument normalization.

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def greet(name):
    return f"Hello {name.lower()}"

assert greet("ALICE") == greet("alice")
```

---

## Challenge 4: Decorating with `wraps`

**Objective**: Use `functools.wraps` to preserve metadata of decorated functions.

```python
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    return a + b

assert add.__name__ == "add"
```

---

## Challenge 5: `cached_property` for Lazy Evaluation

**Objective**: Use `functools.cached_property` to cache computed attributes.

```python
from functools import cached_property

class Circle:
    def __init__(self, r):
        self.r = r

    @cached_property
    def area(self):
        print("Calculating area")
        return 3.14 * self.r ** 2

c = Circle(3)
_ = c.area  # Triggers calculation
_ = c.area  # Uses cached value
```

---

## Challenge 6: Single Dispatch

**Objective**: Create a function that behaves differently depending on argument type.

```python
from functools import singledispatch

@singledispatch
def describe(obj):
    return f"Object: {obj}"

@describe.register
def _(x: int):
    return f"Integer: {x}"

@describe.register
def _(x: list):
    return f"List of {len(x)} elements"

assert describe(5) == "Integer: 5"
assert describe([1, 2, 3]) == "List of 3 elements"
```

---

## Challenge 7: Update Wrapper Metadata

**Objective**: Use `update_wrapper` manually.

```python
from functools import update_wrapper

def outer(fn):
    def wrapper(*args):
        return fn(*args)
    return update_wrapper(wrapper, fn)

@outer
def hello():
    return "hi"

assert hello.__name__ == "hello"
```

---

## Challenge 8: Total Ordering with `total_ordering`

**Objective**: Use `@total_ordering` to minimize boilerplate.

```python
from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, major):
        self.major = major

    def __eq__(self, other):
        return self.major == other.major

    def __lt__(self, other):
        return self.major < other.major

assert Version(1) < Version(2)
assert Version(2) >= Version(1)
```

---

## Challenge 9: Combine Partial and Decorators

**Objective**: Use `partial` to create decorators with fixed parameters.

```python
def log_with(level):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(f"[{level}] {fn.__name__}")
            return fn(*args, **kwargs)
        return wrapper
    return decorator

info = partial(log_with, "INFO")

@info()
def greet():
    return "hello"

assert greet() == "hello"
```

---

## Challenge 10: Compose Functions Dynamically

**Objective**: Use higher-order functions and closures to compose reusable logic.

```python
from functools import reduce

def compose(*funcs):
    return reduce(lambda f, g: lambda x: f(g(x)), funcs)

def inc(x): return x + 1

def square(x): return x * x

f = compose(inc, square)
assert f(3) == 10  # inc(square(3)) = inc(9) = 10
```


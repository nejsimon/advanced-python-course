# Python Decorators: Coding Challenges

These challenges are designed to build understanding of Python decorators, from syntax basics to advanced use cases involving metadata, parameterized decorators, composition, and class decoration.

---

## Challenge 1: Basic Function Decorator

**Objective**: Write a decorator `log_call` that prints the function name and arguments when called.

```python
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_call
def add(x, y):
    return x + y

add(2, 3)  # Logs before returning 5
```

---

## Challenge 2: Decorator with Arguments

**Objective**: Implement a decorator factory `repeat(n)` that repeats the call `n` times.

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello")
```

---

## Challenge 3: Preserve Metadata with functools.wraps

**Objective**: Fix the decorator so that it preserves the original function’s `__name__` and `__doc__`.

```python
from functools import wraps

def preserve(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@preserve
def my_function():
    """This is my function."""
    pass

assert my_function.__name__ == "my_function"
assert my_function.__doc__ == "This is my function."
```

---

## Challenge 4: Timing Decorator

**Objective**: Write a decorator that measures execution time of a function.

```python
import time

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow():
    time.sleep(1)

slow()
```

---

## Challenge 5: Conditional Execution Decorator

**Objective**: Create a decorator `only_if(condition)` that only runs the function if `condition()` returns True.

```python
def only_if(condition):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if condition():
                return func(*args, **kwargs)
        return wrapper
    return decorator

flag = True

@only_if(lambda: flag)
def say_hi():
    print("Hi")
```

---

## Challenge 6: Memoization Decorator

**Objective**: Write a `@memoize` decorator that caches function results.

```python
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

---

## Challenge 7: Decorate Class Methods

**Objective**: Apply a logging decorator to a method within a class.

```python
def log_method(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f"Calling {func.__name__} on {self} with {args}, {kwargs}")
        return func(self, *args, **kwargs)
    return wrapper

class Greeter:
    @log_method
    def greet(self, name):
        print(f"Hello, {name}")
```

---

## Challenge 8: Decorate Entire Class

**Objective**: Write a class decorator that adds a class method `info()` returning class name.

```python
def add_info(cls):
    cls.info = classmethod(lambda cls: cls.__name__)
    return cls

@add_info
class Example:
    pass

assert Example.info() == "Example"
```

---

## Challenge 9: Chained Decorators

**Objective**: Apply multiple decorators to a single function and verify order of execution.

```python
def A(func):
    def wrapper(*args, **kwargs):
        print("A")
        return func(*args, **kwargs)
    return wrapper

def B(func):
    def wrapper(*args, **kwargs):
        print("B")
        return func(*args, **kwargs)
    return wrapper

@A
@B
def test():
    print("Test")

# Output: A B Test
```

---

## Challenge 10: Decorator for Argument Validation

**Objective**: Create a decorator `validate_types` that enforces type hints.

```python
import inspect

def validate_types(func):
    sig = inspect.signature(func)
    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        for name, value in bound.arguments.items():
            if name in sig.parameters:
                expected = sig.parameters[name].annotation
                if expected is not inspect._empty and not isinstance(value, expected):
                    raise TypeError(f"{name} must be {expected}")
        return func(*args, **kwargs)
    return wrapper

@validate_types
def multiply(x: int, y: int) -> int:
    return x * y
```



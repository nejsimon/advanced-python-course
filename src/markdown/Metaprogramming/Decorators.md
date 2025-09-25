# Python Decorators

Decorators allow you to **wrap** functions, methods, or classes to modify their behavior — without changing their code.

They’re widely used for:
- Logging, caching, validation
- Authorization
- Metrics
- DSLs and frameworks (Flask, Django, FastAPI)

---

## 🔰 What Is a Decorator?

A **decorator** is a callable that takes a function or class and returns a new function or class.

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@decorator
def greet(name):
    return f"Hello, {name}"
```

> `@decorator` is syntactic sugar for: `greet = decorator(greet)`

---

## 🧱 Function Decorators

```python
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")
        return func(*args, **kwargs)
    return wrapper

@debug
def add(x, y):
    return x + y
```

---

## 🧪 Decorator with Arguments (Decorator Factory)

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi")
```

> The outer function `repeat(n)` creates and returns the actual decorator.

---

## 🧠 Preserving Function Metadata

Without help, a decorator replaces the original function:

```python
print(add.__name__)  # "wrapper", not "add"
```

Use `functools.wraps` to fix this:

```python
from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ...
    return wrapper
```

---

## 🔄 Multiple Decorators

Decorators stack from the **bottom up**:

```python
@auth
@log
def view(): ...
```

Equivalent to:

```python
view = auth(log(view))
```

> The function is first passed to `log`, then that result is passed to `auth`.

---

## 🧩 Common Built-in Decorators

| Decorator         | Purpose                            |
|-------------------|-------------------------------------|
| `@staticmethod`   | No `self` or `cls` needed           |
| `@classmethod`    | Passes class (`cls`) instead of instance |
| `@property`       | Makes method behave like attribute  |
| `@lru_cache`      | Caches return values                |

---

## 🧵 Class Decorators

Decorators can wrap or modify **classes** too.

```python
def tagged(cls):
    cls.tagged = True
    return cls

@tagged
class MyClass:
    pass

print(MyClass.tagged)  # True
```

Or return a subclass or entirely new type.

---

## ⚙️ Decorating Class Methods

### Instance method

```python
class A:
    @log
    def method(self): ...
```

### Static method

```python
class A:
    @staticmethod
    @log
    def static(): ...
```

Order matters. You usually want:

```python
@staticmethod
@decorator
def method(): ...
```

---

## 🧪 Decorators with Optional Arguments

```python
def tag(label=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Label = {label}")
            return func(*args, **kwargs)
        return wrapper

    if callable(label):
        return decorator(label)  # Used as @tag
    return decorator            # Used as @tag("name")
```

Usage:

```python
@tag
def foo(): ...

@tag("important")
def bar(): ...
```

---

## 🔍 Introspecting Decorated Functions

To access the original function:

```python
@wraps(func)
def wrapper(*args, **kwargs):
    ...

# This sets:
# - __name__, __doc__, __module__
# - __wrapped__ attribute

print(decorated_func.__wrapped__)  # original func
```

You can use `inspect.unwrap()` to strip all wrappers.

---

## 🧪 Stateful Decorators (Closures or Classes)

### Using Closure

```python
def counter():
    count = 0
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal count
            count += 1
            print(f"Call #{count}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

### Using Class

```python
class Timer:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func

    def __call__(self, *args, **kwargs):
        import time
        start = time.time()
        result = self.func(*args, **kwargs)
        print(f"Elapsed: {time.time() - start:.3f}")
        return result

@Timer
def slow(): ...
```

> Using a class is more flexible for tracking state.

---

## ⚠️ Common Pitfalls

### 1. Forgetting `@wraps`
- Breaks docstrings and introspection
- Hides the identity of the original function

### 2. Misusing Arguments

```python
@my_decorator  # OK if my_decorator is a decorator
@my_decorator()  # Requires a decorator factory
```

### 3. Using decorators on mutable methods (e.g. `classmethod`, `staticmethod`) without proper ordering

```python
# Correct:
@staticmethod
@my_decorator
def m(): ...

# Wrong:
@my_decorator
@staticmethod
def m(): ...  # `my_decorator` wraps a descriptor, not the function!
```

---

## 🔧 Debugging Tips

- Use `functools.wraps` religiously
- Set `__wrapped__` manually if necessary
- Use `inspect.getsource()` to view decorated code
- Wrap your decorator in `try/except` to trace hidden bugs

---

## ✅ Summary

| Feature                  | Support |
|---------------------------|---------|
| Function decorators       | ✅       |
| Decorators with arguments | ✅       |
| Class decorators          | ✅       |
| Multiple decorators       | ✅       |
| State-tracking decorators | ✅       |
| Metadata preservation     | ✅ (`@wraps`) |

Python decorators are a lightweight and elegant metaprogramming tool — they encourage separation of concerns, code reuse, and dynamic behavior modification.

---

## 📚 Further Reading

- [Python Decorators — Real Python](https://realpython.com/primer-on-python-decorators/)
- [functools.wraps — Official Docs](https://docs.python.org/3/library/functools.html#functools.wraps)
- Fluent Python — Chapter 7 (Function Decorators and Closures)
- `inspect` module for introspection


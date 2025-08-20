# Python Reflection and Introspection: Coding Challenges

These challenges focus on Python’s dynamic capabilities, including inspecting objects at runtime, modifying behavior, creating decorators dynamically, and using metaprogramming constructs.

---

## Challenge 1: Use `type()` to Create a Class

**Objective**: Dynamically create a class using `type()`.

```python
MyClass = type('MyClass', (), {'x': 42, 'get_x': lambda self: self.x})
obj = MyClass()
assert obj.get_x() == 42
```

---

## Challenge 2: Use `getattr`, `setattr`, `hasattr`

**Objective**: Access and mutate attributes dynamically.

```python
class Person:
    def __init__(self):
        self.name = "Alice"

p = Person()
assert getattr(p, 'name') == 'Alice'
setattr(p, 'age', 30)
assert p.age == 30
assert hasattr(p, 'age')
```

---

## Challenge 3: Inspecting Function Signature with `inspect`

**Objective**: Use the `inspect` module to retrieve a function’s signature.

```python
import inspect

def greet(name: str, age: int = 0):
    return f"Hello {name}"

sig = inspect.signature(greet)
assert list(sig.parameters) == ['name', 'age']
```

---

## Challenge 4: Custom `__getattr__` and `__setattr__`

**Objective**: Override attribute access to intercept reads and writes.

```python
class Logged:
    def __getattr__(self, name):
        print(f"Accessing {name}")
        return 42

    def __setattr__(self, name, value):
        print(f"Setting {name} = {value}")
        super().__setattr__(name, value)
```

---

## Challenge 5: Dynamic Method Addition

**Objective**: Add a method to a class or instance at runtime.

```python
class Dynamic:
    pass

def speak(self):
    return "Hello"

Dynamic.speak = speak
obj = Dynamic()
assert obj.speak() == "Hello"
```

---

## Challenge 6: Use `__dict__` and `vars()`

**Objective**: Access object internals directly.

```python
class X:
    def __init__(self):
        self.foo = 10

x = X()
assert x.__dict__['foo'] == 10
assert vars(x)['foo'] == 10
```

---

## Challenge 7: Use `dir()` and `callable()`

**Objective**: Enumerate object attributes and detect callable members.

```python
class Y:
    def method(self): pass
    val = 5

items = dir(Y())
assert 'method' in items
assert callable(getattr(Y(), 'method'))
```

---

## Challenge 8: Decorator Factory with Introspection

**Objective**: Write a decorator that uses `inspect` to modify behavior based on argument names.

```python
import functools
import inspect

def check_args(expected):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            for name in expected:
                if name not in bound.arguments:
                    raise ValueError(f"Missing argument: {name}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@check_args(['x'])
def f(x): return x
assert f(5) == 5
```

---

## Challenge 9: Metaclass That Logs Class Creation

**Objective**: Use a metaclass to print/log whenever a class is defined.

```python
class LoggerMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=LoggerMeta):
    pass  # Should trigger logging at definition time
```

---

## Challenge 10: Enumerate and Call All Methods

**Objective**: Programmatically list all methods in a class and call them.

```python
class Commands:
    def start(self): return "started"
    def stop(self): return "stopped"

cmd = Commands()

methods = [name for name in dir(cmd) if callable(getattr(cmd, name)) and not name.startswith("__")]
results = [getattr(cmd, m)() for m in methods]
assert sorted(results) == ["started", "stopped"]
```

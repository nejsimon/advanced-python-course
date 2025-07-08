# Reflection, Metaprogramming, and Introspection in Python

Python offers **first-class support** for reflection, dynamic introspection, and metaprogramming. These techniques let you inspect and modify objects, types, and behavior at runtime — enabling powerful frameworks, dynamic APIs, decorators, ORMs, and more.

---

## 🧠 Definitions

| Term             | Description                                                       |
|------------------|--------------------------------------------------------------------|
| **Introspection**| Examining objects, functions, classes at runtime                   |
| **Reflection**   | Accessing/modifying structure based on names/metadata              |
| **Metaprogramming** | Code that generates or modifies code or class structure          |

---

## 🔍 Introspection Tools

### Built-ins

```python
type(obj)      # Get type
id(obj)        # Memory identity
dir(obj)       # Attributes and methods
vars(obj)      # __dict__ (if defined)
hasattr(obj, "foo")
getattr(obj, "foo", default)
setattr(obj, "foo", value)
delattr(obj, "foo")
```

### Example

```python
class User:
    def __init__(self): self.name = "Alice"

u = User()
for attr in dir(u):
    print(attr, getattr(u, attr))
```

---

## 📦 `inspect` Module

The `inspect` module provides deep introspection of live objects.

```python
import inspect

def foo(x): return x

inspect.getsource(foo)      # source code
inspect.signature(foo)      # call signature
inspect.getdoc(foo)         # docstring
inspect.getmembers(foo)     # all attributes
inspect.isfunction(foo)     # True
```

### Signature Introspection

```python
sig = inspect.signature(foo)
for name, param in sig.parameters.items():
    print(name, param.annotation)
```

---

## 🧬 Runtime Type Info

```python
isinstance(obj, SomeClass)
issubclass(SubClass, SuperClass)
type(obj) is SomeClass
```

Use `typing.get_type_hints()` to extract type annotations at runtime (Python 3.10+):

```python
from typing import get_type_hints

def f(x: int, y: str) -> bool: ...
get_type_hints(f)  # {'x': int, 'y': str, 'return': bool}
```

---

## 🧩 Reflection Examples

### Dynamic Method Dispatch

```python
def call_method(obj, method_name):
    method = getattr(obj, method_name)
    return method()
```

### Dynamic Class Instantiation

```python
cls_name = "MyClass"
cls = globals()[cls_name]
obj = cls()
```

Or use:

```python
import importlib

mod = importlib.import_module("mymodule")
cls = getattr(mod, "MyClass")
```

---

## 🧪 Dynamic Attribute Control via `__getattr__`, `__setattr__`

```python
class Logger:
    def __getattr__(self, name):
        print(f"Accessed missing attribute {name}")
        return None

    def __setattr__(self, name, value):
        print(f"Set {name} = {value}")
        super().__setattr__(name, value)
```

- `__getattr__`: called when attribute is **not found**
- `__getattribute__`: called **always** (use with caution)

---

## 🧠 Metaprogramming Techniques

### 1. Function Decorators

```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

---

### 2. Class Decorators

```python
def add_repr(cls):
    cls.__repr__ = lambda self: f"<{cls.__name__}>"
    return cls
```

---

### 3. Metaclasses

Metaclasses control **class creation** — they’re "classes of classes".

```python
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        namespace["created_by_meta"] = True
        return super().__new__(mcs, name, bases, namespace)

class MyClass(metaclass=Meta):
    pass

print(MyClass.created_by_meta)  # True
```

Metaclass use cases:
- Enforcing coding conventions
- Auto-registering classes
- Dynamic method injection
- Validation of subclass structure

---

### 4. Class Modification at Runtime

```python
def add_method(cls):
    cls.greet = lambda self: f"Hello from {self.__class__.__name__}"
    return cls

@add_method
class Foo:
    pass

Foo().greet()  # "Hello from Foo"
```

---

### 5. Code Generation with `type()`

```python
Dynamic = type("Dynamic", (object,), {"x": 42})
d = Dynamic()
print(d.x)  # 42
```

---

## 🧪 Function Introspection

```python
def f(a, b: int = 5, *args, **kwargs) -> str:
    """Example function"""
    return "ok"

inspect.signature(f)
f.__annotations__   # {'b': <class 'int'>, 'return': <class 'str'>}
f.__defaults__      # (5,)
f.__code__.co_varnames  # ('a', 'b', 'args', 'kwargs')
```

---

## 📤 Runtime Code Execution

### `eval`, `exec`

```python
eval("1 + 2")  # 3
exec("x = 5")  # defines x in current scope
```

Use with **extreme caution**. Prefer `ast.literal_eval` for safety:

```python
from ast import literal_eval
literal_eval("{'a': 1}")  # ✅ safe
```

---

## 📜 Class and Module Introspection

```python
import math
print(math.__doc__)
print(math.__name__)
print(math.__file__)
print(dir(math))
```

---

## 🧵 Use Cases

- ORMs (e.g., SQLAlchemy, Django ORM)
- Dependency injection frameworks
- RPC systems and API gateways
- Test discovery (`pytest`, `unittest`)
- Code generation (e.g., `dataclass`, `attrs`)
- Schema generation (e.g., `pydantic`, OpenAPI)

---

## ⚠️ Pitfalls

### 1. `__getattribute__` is dangerous

- Always call `super().__getattribute__` or risk infinite recursion.

### 2. `globals()` / `eval()` abuse

- Prefer safe lookup tables or dispatch maps.

### 3. Fragile code introspection

- `inspect.getsource()` can fail on dynamically defined or C-extension functions.

### 4. Metaclass overuse

- Metaclasses are powerful, but often unnecessary — try decorators or descriptors first.

---

## ✅ Summary

| Technique           | Description                             |
|---------------------|-----------------------------------------|
| `getattr` / `setattr` | Dynamic attribute access               |
| `inspect`           | Runtime metadata on functions/classes   |
| Decorators          | Inject logic into functions/classes     |
| Metaclasses         | Alter class creation behavior           |
| `type()`            | Dynamic class generation                |
| `eval` / `exec`     | Execute arbitrary code at runtime       |

---

## 🧰 Useful Modules and Tools

| Module      | Purpose                                 |
|-------------|------------------------------------------|
| `inspect`   | Source, signature, members               |
| `types`     | Dynamic function/class creation          |
| `ast`       | Safe parsing and transformation of code  |
| `functools` | Wrappers, `partial`, `singledispatch`   |
| `dis`       | Bytecode disassembly                    |

---

## 📚 Further Reading

- [inspect — standard library docs](https://docs.python.org/3/library/inspect.html)
- [Data Model (dunder methods)](https://docs.python.org/3/reference/datamodel.html)
- [Metaclass programming in Python](https://realpython.com/python-metaclasses/)
- Fluent Python — Chapters 21–23
- Raymond Hettinger: *"Super considered super"* (YouTube)


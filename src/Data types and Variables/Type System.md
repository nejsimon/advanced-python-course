# Python Type System

Python is a **dynamically typed**, **strongly typed**, and increasingly **gradually typed** language.

- **Dynamically typed**: variables don't have types — objects do.
- **Strongly typed**: operations on mismatched types fail.
- **Gradually typed**: optional static typing via `typing`.

---

## 🧠 Core Principles

| Feature          | Python Behavior                     |
|------------------|--------------------------------------|
| Dynamic typing   | Types enforced at runtime            |
| Strong typing    | Type errors not silently ignored     |
| Gradual typing   | Type hints are optional, checked by tools like `mypy` |
| Duck typing      | Structural compatibility ("quacks like a duck") |

---

## 🔍 Runtime Typing

```python
x = 42
type(x)         # <class 'int'>
isinstance(x, int)  # True
```

No type enforcement happens at **compile time** — unless you use a **type checker** (e.g., `mypy`, `pyright`).

---

## 🧾 Static Typing with Type Hints

Type hints provide optional annotations:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

- Ignored at runtime
- Used by tools like `mypy`, `pyright`, IDEs, linters

---

## 🧰 Built-in Type Hints

| Type        | Usage                          |
|-------------|--------------------------------|
| `int`, `str`| Primitive types                |
| `bool`      | Boolean                        |
| `list[int]` | Homogeneous lists (Python 3.9+)|
| `dict[str, int]` | Dicts with fixed key/value types |
| `Optional[str]` | `str` or `None`            |
| `Union[str, int]` | One of multiple types     |
| `Callable[[int, str], bool]` | Function signature |

---

## 🧪 `typing` Module (Pre-3.9)

For older Python versions (<3.9), use:

```python
from typing import List, Dict, Tuple, Optional, Union

def get_scores() -> List[int]:
    ...
```

---

## 🧠 Type Inference and Defaults

Type checkers can infer many types:

```python
def add(x: int, y: int):
    return x + y  # inferred: int
```

But not always:

```python
x = []  # type: List[int]  # explicit annotation often required
```

---

## 🧬 `Any`, `object`, and Top Types

| Type     | Meaning                                  |
|----------|------------------------------------------|
| `Any`    | Skip type checking                       |
| `object` | Supertype of all types                   |
| `NoReturn` | Function never returns (e.g., `raise`) |

---

## 📦 Advanced Typing Features

### ✅ `NewType` – Semantic Distinction

```python
from typing import NewType

UserId = NewType("UserId", int)

def get_user(uid: UserId): ...
```

Still behaves like `int` at runtime but gives a **type checker distinction**.

---

### ✅ `TypedDict` – Typed Dictionaries

```python
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int
```

- Structurally typed
- Useful for JSON-like objects

---

### ✅ `Literal` – Fixed values

```python
from typing import Literal

def set_mode(mode: Literal["dark", "light"]): ...
```

---

### ✅ `Protocol` – Structural Interfaces (Duck Typing)

```python
from typing import Protocol

class Greeter(Protocol):
    def greet(self) -> str: ...

class User:
    def greet(self): return "hi"

def call_greet(g: Greeter): ...
```

---

### ✅ `Final` – Prevent override or reassignment

```python
from typing import Final

PI: Final = 3.14
```

---

## 🧬 Generics and TypeVars

```python
from typing import TypeVar, Generic

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self):
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()
```

---

## 🧪 ParamSpec and Concatenate (Python 3.10+)

Useful for decorators and higher-order functions.

```python
from typing import ParamSpec, Concatenate, Callable, TypeVar

P = ParamSpec("P")
R = TypeVar("R")

def log_args(f: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(args, kwargs)
        return f(*args, **kwargs)
    return wrapper
```

---

## 🧵 Typing `self` and Class Methods

Python 3.11+ adds `Self` type:

```python
from typing import Self

class Builder:
    def set(self, key: str, value: str) -> Self:
        ...
```

---

## 🔍 Runtime vs Static Typing

Python’s runtime ignores type hints:

```python
def f(x: int) -> int:
    return x + "a"  # No error at runtime!
```

Use `mypy`, `pyright`, or IDE plugins to enforce typing statically.

---

## 📏 Type Checkers

| Tool     | Notes                          |
|----------|---------------------------------|
| `mypy`   | Widely used, mature             |
| `pyright`| Fast, TypeScript-inspired       |
| `pyre`   | Facebook’s static checker       |

---

## ⚠️ Pitfalls and Gotchas

### 1. Misusing `Any`

```python
x: Any = dangerous()
x.do_something()  # No checking!
```

### 2. Optional misuse

```python
def f(x: Optional[str]):
    print(x.upper())  # ❌ Error if None
```

### 3. Overly rigid types

Type-checking should aid development — not make the code brittle or verbose.

---

## 🧱 Runtime Type Enforcement (Optional)

Python does **not** enforce types at runtime, but third-party tools can:

### `typeguard`

```bash
pip install typeguard
```

```python
from typeguard import typechecked

@typechecked
def add(x: int, y: int) -> int:
    return x + y
```

Raises runtime `TypeError` on violations.

---

## 🧮 PEP Index

| PEP        | Feature                        |
|------------|--------------------------------|
| PEP 484    | Type hints                     |
| PEP 526    | Variable annotations           |
| PEP 544    | Protocols (structural typing)  |
| PEP 563    | Postponed evaluation (`from __future__`) |
| PEP 586    | `Literal` types                |
| PEP 591    | `Final`                        |
| PEP 604    | `X | Y` union syntax           |
| PEP 647    | `TypeGuard`                    |
| PEP 695    | Generic syntax (Python 3.12+)  |

---

## ✅ Summary

| Concept           | Notes                                         |
|-------------------|-----------------------------------------------|
| Dynamic Typing     | Default mode — runtime types only            |
| Static Typing      | Optional — use `typing` + `mypy`, etc.       |
| Type Hints         | Aid documentation, tooling, refactoring      |
| Duck Typing        | Works by structure, not inheritance          |
| Generics           | Generic classes/functions with `TypeVar`     |
| Protocols          | Structural interfaces (like Go, TypeScript)  |

---

## 📚 Further Reading

- [typing — standard library docs](https://docs.python.org/3/library/typing.html)
- [mypy documentation](https://mypy.readthedocs.io/)
- [Type Hints Cheat Sheet (mypy)](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- [PEP 484 – Type hints](https://peps.python.org/pep-0484/)
- [Pyright](https://github.com/microsoft/pyright)
- Fluent Python – Chapter 16–18

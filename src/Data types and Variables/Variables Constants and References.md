# Variables, Constants, and References

Python’s variables are **names bound to objects** — not containers. Understanding Python’s variable model is crucial for mastering reference semantics, mutation, identity, and immutability.

---

## 🧠 Variable Model

### ✅ Variables are **names**, not containers

```python
x = [1, 2, 3]
y = x  # y is now another name bound to the same list
```

Both `x` and `y` point to **the same object** in memory.

---

## 🧬 Reference Semantics

- Variables store **references to objects**, not the objects themselves.
- Assignment **binds** a name to an object.

```python
a = [1, 2, 3]
b = a
b.append(4)

print(a)  # [1, 2, 3, 4]
```

### Use `id()` to inspect identity:

```python
id(a) == id(b)  # True — same object
```

---

## 🔁 Mutability vs Reassignment

```python
x = [1, 2, 3]
x.append(4)  # modifies the object
x = [9, 8, 7]  # rebinds the name to a new object
```

- `.append()` mutates the object
- `=` creates a new binding

---

## ⚠️ Aliasing and Side Effects

```python
def mutate(data):
    data.append(999)

lst = [1]
mutate(lst)
print(lst)  # [1, 999]
```

If you don’t want this:

```python
def safe_mutate(data):
    data = data.copy()  # new reference
    data.append(999)
```

---

## 🧾 Constants

Python has **no true constants** — by convention:

```python
PI = 3.14159  # All uppercase = constant by convention
```

But:

```python
PI = 2.0  # Valid Python, no enforcement
```

### Enforced Constants (Pattern)

You can emulate constants with:
- Naming conventions (`UPPERCASE`)
- Custom classes or enums
- Type hints and linters

```python
from typing import Final

HOST: Final = "localhost"
```

> `Final` is **ignored at runtime**, but enforced by `mypy`.

---

## 🚫 Making Objects Immutable

Use `@dataclass(frozen=True)`, tuples, or `types.MappingProxyType`:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int
```

---

## 🔧 Assignment Behavior

### Chained assignment

```python
a = b = [1, 2]  # both point to same object
```

### Tuple unpacking

```python
x, y = 1, 2
a, *b = [1, 2, 3, 4]  # a = 1, b = [2, 3, 4]
```

### Swapping values

```python
a, b = b, a
```

---

## 🧵 References vs Copies

### Shallow Copy

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)

a[0][0] = 99
print(b)  # [[99, 2], [3, 4]]  ← inner lists are shared
```

### Deep Copy

```python
c = copy.deepcopy(a)
```

---

## 🧪 Name Binding in Functions

### Local by default

```python
x = 10

def f():
    x = 20  # new local binding

f()
print(x)  # 10
```

### `global` and `nonlocal`

```python
count = 0

def inc():
    global count
    count += 1
```

```python
def outer():
    x = 5
    def inner():
        nonlocal x
        x += 1
```

---

## 🧱 Variable Storage

Variables live in **namespaces**:
- `locals()`: local variables
- `globals()`: module/global scope
- `vars(obj)`: object's `__dict__`

---

## 🧠 Identity vs Equality

```python
a = [1, 2]
b = a
c = [1, 2]

a == c  # True — value equality
a is c  # False — different objects
```

Use `is` for identity, `==` for equality.

---

## 🧨 Common Pitfalls

### 1. Mutable default arguments

```python
def f(x=[]):  # ⚠️ only created once
    x.append(1)
    return x
```

Fix:

```python
def f(x=None):
    if x is None:
        x = []
```

---

### 2. Confusing reference and value

```python
a = [1, 2, 3]
b = a
b = [4, 5]  # new object — a is unchanged
```

---

### 3. Misusing `is` vs `==`

```python
x = 256
y = 256
x is y  # True (interned)

x = 257
y = 257
x is y  # ❓ may be False
```

---

### 4. Constant mutation

```python
CONFIG = {"debug": True}
CONFIG["debug"] = False  # still allowed
```

If you want to freeze:

```python
from types import MappingProxyType
CONFIG = MappingProxyType({"debug": True})
```

---

## ✅ Summary

| Concept       | Python Behavior                        |
|---------------|-----------------------------------------|
| Variables     | Names bound to object references        |
| Constants     | Convention only; use `Final` or frozen dataclasses |
| Assignment    | Creates or rebinds names, never copies  |
| Identity      | `is` checks if two names point to same object |
| Equality      | `==` checks value equivalence           |
| Aliasing      | Multiple names pointing to same object  |
| Mutability    | Applies to object, not variable name    |

---

## 📚 Further Reading

- [Python Data Model (official docs)](https://docs.python.org/3/reference/datamodel.html)
- [PEP 591 – Final qualifier](https://peps.python.org/pep-0591/)
- Fluent Python – Chapter 1 & 6
- [The Python Language Reference – Execution Model](https://docs.python.org/3/reference/executionmodel.html)

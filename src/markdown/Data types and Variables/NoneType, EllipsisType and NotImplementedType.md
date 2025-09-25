# NoneType, EllipsisType, and NotImplementedType

This document explores three often-overlooked singleton types in Python: `NoneType`, `EllipsisType`, and `NotImplementedType`. Each of these types has a distinct role in Python’s semantics, special methods, and runtime behavior.

---

## 1. `NoneType`

### Definition

* The type of the singleton `None`

```python
x = None
assert type(x) is type(None)
```

### Usage

* Sentinel for absence of value
* Default parameter in functions
* Represents null or undefined in APIs
* Used in conditional checks (`x is None`)

### Comparison

* Always use `is` for comparison:

```python
if result is None:
    handle_missing()
```

### Notes

* Only one instance: `None`
* `None` is falsy (`bool(None) == False`)

---

## 2. `EllipsisType` (`...`)

### Definition

* Singleton object of type `EllipsisType`

```python
assert ... is Ellipsis
assert type(...) is type(Ellipsis)
```

### Usage

#### a) Placeholder

* Temporarily represent incomplete code or stubs:

```python
def future_feature():
    ...  # TODO: implement later
```

#### b) Advanced Slicing (esp. NumPy)

```python
# NumPy: image[..., 0] selects red channel across all dimensions
```

#### c) Type Hints (PEP 484+)

* Used in generic base types

```python
from typing import Callable
f: Callable[..., int]  # accepts any args, returns int
```

### Notes

* Often confused with `None`, but semantically different

---

## 3. `NotImplementedType`

### Definition

* Singleton of type `NotImplementedType`

```python
assert type(NotImplemented) is type(NotImplemented)
```

### Usage

* Returned from special methods (`__eq__`, `__add__`, etc.) to signal unsupported operand types

```python
class Vector:
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y
```

* Enables fallback to `other.__eq__(self)`

### Notes

* **Do not raise** `NotImplemented`, just **return** it
* If both operands return `NotImplemented`, Python raises `TypeError`

---

## Summary

| Singleton        | Type                 | Typical Use Case                   |
| ---------------- | -------------------- | ---------------------------------- |
| `None`           | `NoneType`           | Missing or undefined value         |
| `...`            | `EllipsisType`       | Slicing, placeholder, typing stubs |
| `NotImplemented` | `NotImplementedType` | Binary method fallback signaling   |

These built-in singleton types play critical roles in Python’s object model, control flow, and extension mechanisms.

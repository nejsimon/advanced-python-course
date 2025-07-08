# NoneType, EllipsisType, and NotImplementedType: Coding Challenges

These exercises focus on the practical use and behavior of Python's three special singleton types: `None`, `...` (Ellipsis), and `NotImplemented`.

---

## Challenge 1: Detect and Replace `None`

**Objective:**
Write a function that replaces `None` in a list with a default value:

```python
def replace_none(lst, default=0):
    pass

# Example:
# replace_none([1, None, 2, None], default=-1) => [1, -1, 2, -1]
```

---

## Challenge 2: Type Check for Ellipsis

**Objective:**
Write a function that returns `True` if the input is the Ellipsis object:

```python
def is_ellipsis(obj):
    pass
```

* Test with `...`, `'...'`, and `Ellipsis`

---

## Challenge 3: Ellipsis in Placeholder Functions

**Objective:**
Create three function stubs using `...` as a placeholder:

```python
def func1(): ...
def func2(x): ...
def func3(a, b): ...
```

* Ensure they do not raise errors when called, but return `None`

---

## Challenge 4: Use of Ellipsis in Type Hints

**Objective:**
Annotate a function that accepts any arguments and returns a float:

```python
from typing import Callable
f: Callable[..., float]
```

---

## Challenge 5: Custom Equality and `NotImplemented`

**Objective:**
Create a class that only supports equality with its own type:

```python
class Custom:
    def __eq__(self, other):
        if not isinstance(other, Custom):
            return NotImplemented
        return self.id == other.id
```

* Show that comparing to a different type returns `False` gracefully

---

## Challenge 6: Use `NotImplemented` in a Binary Operator

**Objective:**
Implement a custom `__add__` that returns `NotImplemented` for unsupported types:

```python
class Adder:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Adder):
            return Adder(self.value + other.value)
        return NotImplemented
```

* Add two `Adder` instances and a `str` to see fallback behavior

---

## Challenge 7: Identity Comparison

**Objective:**
Verify that each of the three singletons is unique:

```python
assert None is None
assert ... is Ellipsis
assert NotImplemented is NotImplemented
```

* Try creating new variables and confirming identity


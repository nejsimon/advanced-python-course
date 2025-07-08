# Python Overloading

Overloading in Python refers to the ability to define multiple behaviors for a function or operator based on the number or type of its arguments. Python supports this **dynamically**, unlike statically typed languages such as Java or C++.

---

## 🔰 Types of Overloading

1. **Operator Overloading** — via special methods like `__add__`, `__eq__`, etc.
2. **Function Overloading** — via `functools.singledispatch` or manual inspection.
3. **Method Overloading** — not natively supported; must be emulated.

---

## ⚙️ 1. Operator Overloading

Operator overloading allows user-defined classes to implement behavior for built-in operators.

### Example: `+` Operator

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
```

```python
v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Vector(4, 6)
```

### Common Special Methods

| Operator | Method         |
|----------|----------------|
| `+`      | `__add__`      |
| `-`      | `__sub__`      |
| `*`      | `__mul__`      |
| `/`      | `__truediv__`  |
| `==`     | `__eq__`       |
| `<`      | `__lt__`       |
| `[]`     | `__getitem__`  |
| `in`     | `__contains__` |
| `str()`  | `__str__`      |
| `repr()` | `__repr__`     |

### Reverse Operators

If `__add__` fails (returns `NotImplemented`), Python tries `__radd__` on the right-hand operand.

---

## 🧰 Best Practices

- Always return `NotImplemented` if the other operand type is unsupported.
- Keep operations symmetric when possible (`__add__` and `__radd__`).
- Support rich comparisons (`__lt__`, `__le__`, `__gt__`, `__ge__`) to interoperate with `sorted()`.

---

## 🧪 2. Function Overloading

Python does **not support traditional function overloading** (i.e., multiple functions with the same name but different signatures). The latest and most idiomatic approach is using `functools.singledispatch`.

### Using `@singledispatch`

```python
from functools import singledispatch

@singledispatch
def process(value):
    raise NotImplementedError("Unsupported type")

@process.register
def _(value: int):
    return f"Integer: {value}"

@process.register
def _(value: str):
    return f"String: {value}"
```

```python
process(5)       # "Integer: 5"
process("hello") # "String: hello"
```

> `singledispatch` only works on the **first argument**'s type.

### For Methods: `@singledispatchmethod`

Python 3.8+ adds support for method overloading inside classes:

```python
from functools import singledispatchmethod

class Handler:
    @singledispatchmethod
    def handle(self, value):
        raise NotImplementedError()

    @handle.register
    def _(self, value: int):
        print(f"Handling int: {value}")
```

---

## ⚠️ Limitations and Quirks

### 1. No True Multi-Signature Overload

This fails silently:

```python
def foo(x: int):
    ...

def foo(x: str):
    ...  # overwrites previous `foo`
```

### 2. Manual Argument Inspection

Workaround using `*args` and type checking:

```python
def foo(*args):
    if len(args) == 1 and isinstance(args[0], int):
        ...
    elif len(args) == 2 and all(isinstance(arg, float) for arg in args):
        ...
```

While this works, it can quickly become messy and hard to maintain.

---

## 🧠 Typing Support for Overloads

With `typing.overload` you can declare overload signatures for static type checkers like Mypy.

```python
from typing import overload, Union

@overload
def square(x: int) -> int: ...
@overload
def square(x: float) -> float: ...

def square(x: Union[int, float]) -> Union[int, float]:
    return x * x
```

- **Runtime**: Only one implementation (the last `square`) is used.
- **Static checking**: Helps tools like Mypy infer types properly.

---

## 🧑‍💻 Practical Use-Cases

- Customizing class behavior with intuitive syntax (`+`, `[]`, etc).
- Type-dependent logic using `singledispatch`.
- Interoperability with type hints for libraries and tooling.

---

## ✅ Summary

| Feature                         | Native Support | Notes                                         |
|---------------------------------|----------------|-----------------------------------------------|
| Operator Overloading            | ✅             | Via `__add__`, `__eq__`, etc.                 |
| Function Overloading            | ⚠️             | Use `@singledispatch`; limited to 1st arg     |
| Method Overloading              | ⚠️             | Use `@singledispatchmethod` (Python 3.8+)     |
| Static Overload Signatures      | ✅             | With `typing.overload`, only for type checkers|
| Runtime Multi-Signature Support | ❌             | Must emulate with `*args` and type checks     |

Python supports overloading patterns—but not in the traditional OOP sense. Use idiomatic tools (`singledispatch`, `typing.overload`) and favor clarity over clever API magic.

---

## 📚 Further Reading

- [`functools.singledispatch`](https://docs.python.org/3/library/functools.html#functools.singledispatch)
- [`typing.overload`](https://docs.python.org/3/library/typing.html#typing.overload)
- [Data model (Python docs)](https://docs.python.org/3/reference/datamodel.html)


# Python Classes and Object-Oriented Programming (OOP)

Python supports full object-oriented programming with classes, inheritance, polymorphism, and encapsulation. Its OOP model is flexible, dynamic, and integrates smoothly with functional and procedural paradigms.

---

## 🔰 Basics of Classes

### Defining a Class

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def greet(self):
        return f"Hello, {self.value}!"
```

### Creating an Instance

```python
obj = MyClass("world")
obj.greet()  # "Hello, world!"
```

- `__init__` is the constructor.
- `self` refers to the current instance.
- Attributes are public by default.

---

## 🧰 Instance vs Class Attributes

```python
class Example:
    shared = []  # class attribute

    def __init__(self, item):
        self.instance = [item]  # instance attribute
```

- **Instance attributes** are per-object.
- **Class attributes** are shared across all instances.

```python
a = Example(1)
b = Example(2)

a.shared.append(99)
print(b.shared)  # [99] — shared state!
```

> ⚠️ Use caution with **mutable** class attributes.

---

## 🧩 Method Types

| Type            | Decorator           | First Arg | Notes |
|-----------------|---------------------|-----------|-------|
| Instance Method | none                | `self`    | Accesses object state |
| Class Method    | `@classmethod`      | `cls`     | Accesses class state |
| Static Method   | `@staticmethod`     | none      | No automatic context passed |

```python
class Example:
    def instance_method(self):
        return self

    @classmethod
    def class_method(cls):
        return cls

    @staticmethod
    def static_method():
        return "static"
```

---

## 🔁 Inheritance

```python
class Animal:
    def speak(self):
        return "?"

class Dog(Animal):
    def speak(self):
        return "Woof"
```

- Supports **single** and **multiple** inheritance.
- Uses **Method Resolution Order (MRO)** in `C3 linearization`.

### Checking Class Relationships

```python
isinstance(dog, Animal)     # True
issubclass(Dog, Animal)     # True
```

---

## 🧱 Multiple Inheritance & MRO

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.__mro__)  # Method resolution order
```

> Python uses C3 linearization to avoid the diamond problem.

---

## ⚙️ `super()`

```python
class Base:
    def greet(self):
        return "Hello"

class Derived(Base):
    def greet(self):
        return super().greet() + ", world"
```

- `super()` returns the next method in the MRO.
- Avoid hardcoding parent class names—prefer `super()`.

---

## 🔐 Encapsulation

Python doesn’t enforce access restrictions but follows naming conventions:

| Convention     | Meaning                        |
|----------------|--------------------------------|
| `name`         | Public                         |
| `_name`        | Protected (internal use)       |
| `__name`       | Private (name-mangled)         |
| `__name__`     | Special / magic methods        |

```python
class A:
    def __init__(self):
        self._protected = 1
        self.__private = 2
```

```python
a = A()
print(a._protected)       # Allowed (by convention discouraged)
print(a.__private)        # AttributeError
print(a._A__private)      # Works due to name mangling
```

---

## 🧠 Special Methods ("Dunder" Methods)

Define custom behavior for built-in operations.

| Purpose        | Method        |
|----------------|---------------|
| Constructor    | `__init__`    |
| String repr    | `__str__`, `__repr__` |
| Equality       | `__eq__`, `__ne__` |
| Arithmetic     | `__add__`, `__sub__`, etc. |
| Iteration      | `__iter__`, `__next__` |
| Context mgr    | `__enter__`, `__exit__` |
| Length         | `__len__`     |

Example:

```python
class Counter:
    def __init__(self, start=0):
        self.count = start

    def __str__(self):
        return str(self.count)

    def __add__(self, other):
        return Counter(self.count + other)
```

---

## 🔄 Polymorphism

Python is **dynamically typed** and **duck-typed**. Objects are interchangeable if they support the same interface.

```python
def describe(obj):
    print(obj.describe())

# Works with any object that defines `.describe()`
```

---

## 🧪 Abstract Base Classes (ABCs)

Use `abc` module to define formal interfaces.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

- Can't instantiate `Shape` directly.
- Enforces subclasses to implement `area()`.

---

## 🔄 Data Classes (Python 3.7+)

Provides boilerplate reduction for simple classes.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
```

Auto-generates `__init__`, `__repr__`, `__eq__`, and more.

---

## 🧵 Common Idioms and Quirks

### 1. Dynamic Attributes

```python
obj.new_attr = 42  # Allowed anytime unless __slots__ is used
```

### 2. `__slots__` to prevent dynamic attributes and reduce memory

```python
class Compact:
    __slots__ = ('x', 'y')
```

### 3. Object Identity vs Equality

```python
a is b      # Object identity (same memory)
a == b      # Equality via __eq__
```

### 4. No Private Enforcement

Use naming conventions. There is no `private` or `protected` keyword.

---

## 📚 Best Practices

- Use `super()` for cooperative multiple inheritance.
- Use `@classmethod` for alternative constructors.
- Consider `@dataclass` for data containers.
- Prefer composition over inheritance when appropriate.
- Avoid deep inheritance trees.
- Encapsulate state with properties if necessary.

---

## ✅ Summary

| Concept              | Supported | Notes |
|----------------------|-----------|-------|
| Classes              | ✅        | Full OOP support |
| Inheritance          | ✅        | Single & multiple |
| Operator Overload    | ✅        | Via special methods |
| Abstract Classes     | ✅        | Use `abc` module |
| Private Attributes   | ⚠️        | By convention only |
| Method Overload      | ⚠️        | Use `singledispatch` for emulation |
| Data Classes         | ✅        | `@dataclass` (3.7+) |
| Metaclasses          | ✅        | Advanced/custom behaviors |

---

## 🧪 Advanced Topics (Mentioned, not covered here)

- Metaclasses and `__new__`
- Descriptors and property objects
- Multiple dispatch via external libraries
- Custom class decorators and registries
- Dependency injection in OOP Python

---

## 📚 Further Reading

- [Data Model: Python Reference](https://docs.python.org/3/reference/datamodel.html)
- [abc module](https://docs.python.org/3/library/abc.html)
- [dataclasses module](https://docs.python.org/3/library/dataclasses.html)


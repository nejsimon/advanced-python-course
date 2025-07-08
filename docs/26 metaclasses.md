# Python Metaclasses

Metaclasses are classes **of classes** — they define how classes behave. Just as classes define the behavior of instances, **metaclasses define the behavior of classes themselves**.

They’re a core part of Python's object model and allow for powerful customizations in class creation, validation, and control over inheritance trees.

---

## 🔰 What Is a Metaclass?

- **Objects** are instances of **classes**
- **Classes** themselves are instances of **metaclasses**
- By default, the metaclass for all new-style classes is `type`

```python
class MyClass:
    pass

print(type(MyClass))  # <class 'type'>
```

`type` is both:
- The **metaclass** (used to create classes)
- The **base class** of all new-style classes

---

## 🛠 Creating a Metaclass

A metaclass is just a subclass of `type`.

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)
```

Usage:

```python
class MyClass(metaclass=Meta):
    pass
```

---

## ⚙️ Anatomy of a Metaclass

Metaclasses typically override one or more of:

### `__new__(cls, name, bases, dct)`
- Called **before** the class is created.
- Can **modify attributes**, inject methods, validate structure.

### `__init__(cls, name, bases, dct)`
- Called **after** the class object is created.
- Can be used to register classes, modify behavior.

### `__call__(cls, *args, **kwargs)`
- Called when the class itself is **instantiated** (like a factory).
- Rarely overridden, but powerful.

---

## ✅ Example: Auto Uppercase Attribute Names

```python
class UpperAttrMeta(type):
    def __new__(cls, name, bases, dct):
        new_attrs = {
            key.upper() if not key.startswith('__') else key: value
            for key, value in dct.items()
        }
        return super().__new__(cls, name, bases, new_attrs)

class Foo(metaclass=UpperAttrMeta):
    bar = "baz"

print(hasattr(Foo, "bar"))     # False
print(hasattr(Foo, "BAR"))     # True
```

---

## 🧪 Practical Use Cases

| Use Case                      | How Metaclasses Help                              |
|------------------------------|---------------------------------------------------|
| Class validation              | Ensure subclasses implement required attributes   |
| DSLs and ORMs (e.g., Django) | Build custom syntax in class declarations         |
| Class registries              | Auto-register subclasses for plugins etc.         |
| API generation                | Create schema or REST APIs from class structure   |
| Singleton / Factory patterns | Control instantiation logic at the class level    |

---

## 📌 Class Validation Example

```python
class InterfaceMeta(type):
    def __init__(cls, name, bases, dct):
        if "do_something" not in dct:
            raise TypeError(f"{name} must define 'do_something'")
        super().__init__(name, bases, dct)

class Plugin(metaclass=InterfaceMeta):
    def do_something(self):
        print("Working")
```

---

## 🧱 Metaclasses vs `__init_subclass__`

Since Python 3.6, simple class validation and customization can be done more cleanly with:

```python
class Base:
    def __init_subclass__(cls, **kwargs):
        print(f"{cls.__name__} subclass created")
```

| Feature                | `__init_subclass__` | Metaclass (`type`) |
|------------------------|---------------------|---------------------|
| Ease of use            | ✅ Easy              | ❌ Verbose          |
| Global override        | ❌ No                | ✅ Yes              |
| Multiple inheritance   | ✅ Safe              | ⚠️ Complex          |
| Class validation       | ✅ Simple cases      | ✅ Advanced cases    |

Use metaclasses when you need:
- Total control of class creation
- Cross-cutting concerns across multiple base classes

---

## 🧵 Quirks and Caveats

### 1. Conflicting Metaclasses

Multiple base classes with incompatible metaclasses cause errors.

```python
TypeError: metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases
```

💡 Use metaclass **cooperation** with inheritance-aware metaclass composition if needed.

### 2. You Don't Always Need Them

Metaclasses are overkill for many use cases:
- Use decorators for function/method behavior
- Use `__init_subclass__` or `__new__` for instance logic
- Use `attrs`, `dataclasses`, or `pydantic` for structure enforcement

---

## 🧪 Example: Class Registry

```python
class RegistryMeta(type):
    registry = {}

    def __init__(cls, name, bases, dct):
        if not name.startswith("Base"):
            RegistryMeta.registry[name] = cls
        super().__init__(name, bases, dct)

class Base(metaclass=RegistryMeta):
    pass

class A(Base): pass
class B(Base): pass

print(RegistryMeta.registry)  # {'A': <class '__main__.A'>, 'B': <class '__main__.B'>}
```

---

## ⚖️ Summary: When to Use Metaclasses

| Consider Using If...                                  |
|--------------------------------------------------------|
| You need to enforce rules at class definition time     |
| You want to auto-register, auto-wrap, or inject logic  |
| You're building a DSL, ORM, or plugin system           |
| You need full control over class creation              |

Avoid them if:
- You can use simpler mechanisms (`__init_subclass__`, decorators, etc.)
- You're not 100% sure they’re the right tool

---

## 📚 Further Reading

- [Data Model: `type` and metaclasses](https://docs.python.org/3/reference/datamodel.html#metaclasses)
- [Raymond Hettinger's talk — "Python’s Class Development Toolkit"](https://www.youtube.com/watch?v=HTLu2DFOdTg)
- [Fluent Python — Luciano Ramalho (Ch. 21)](https://www.oreilly.com/library/view/fluent-python/9781491946237/)

---

## ✅ TL;DR

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        # modify or validate the class
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    ...
```

- Metaclasses are for modifying **classes** at creation time.
- Think of them as decorators for class definitions, but more powerful.
- Use with care: powerful, but often unnecessary.


# Python Descriptors

Descriptors are low-level hooks that define how attribute access works. They are one of Python’s most powerful and foundational features, enabling properties, computed fields, method binding, and more.

If you're using `@property`, `staticmethod`, or `classmethod`, you're already using descriptors — often without realizing it.

---

## 🔰 What Is a Descriptor?

A **descriptor** is any object that defines one or more of the following methods:

```python
__get__(self, instance, owner)
__set__(self, instance, value)
__delete__(self, instance)
```

Descriptors are typically defined as **class attributes** and control the behavior of instance attributes.

---

## 🛠 Creating a Descriptor

### Example: Logging Descriptor

```python
class LoggedAttribute:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print(f"Accessing {self.name}")
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        print(f"Setting {self.name} to {value}")
        instance.__dict__[self.name] = value
```

Usage:

```python
class MyClass:
    x = LoggedAttribute('x')

obj = MyClass()
obj.x = 42    # Setting x to 42
print(obj.x)  # Accessing x → 42
```

---

## 📚 Descriptor Protocol

| Method       | Purpose                            |
|--------------|-------------------------------------|
| `__get__`    | Called on attribute access          |
| `__set__`    | Called on attribute assignment      |
| `__delete__` | Called on `del obj.attr`            |

Arguments:
- `instance`: The object being accessed.
- `owner`: The class the descriptor was accessed through.

---

## 🧩 Types of Descriptors

| Descriptor Type | Implements             | Example             |
|------------------|------------------------|---------------------|
| Non-data         | Only `__get__`         | `staticmethod`      |
| Data             | `__get__` + `__set__`  | `property`, `field` |

### ⚠️ Data descriptor overrides instance attributes.  
### Non-data descriptor does not.

```python
class ND:
    def __get__(self, instance, owner):
        return "non-data"

class D:
    def __get__(self, i, o): return "data"
    def __set__(self, i, v): pass

class C:
    nd = ND()
    d = D()

obj = C()
obj.nd = "shadowed"
obj.d = "not shadowed"

print(obj.nd)  # "shadowed" — non-data is shadowed
print(obj.d)   # "data" — data descriptor overrides
```

---

## 🧠 How Python Resolves Attribute Access

When accessing `obj.attr`, Python searches:

1. `obj.__dict__`
2. Class's **data descriptors** (`__get__` + `__set__`)
3. Class’s `__dict__`
4. Class's **non-data descriptors** (`__get__` only)
5. `__getattr__()` fallback
6. Raises `AttributeError`

---

## 🛠 Custom `@property` with Descriptor

```python
class Celsius:
    def __init__(self, temp):
        self._temp = temp

    def get_temp(self):
        print("Getting")
        return self._temp

    def set_temp(self, value):
        print("Setting")
        self._temp = value

    temperature = property(get_temp, set_temp)
```

Or, manually via descriptor:

```python
class Temperature:
    def __get__(self, instance, owner):
        return instance._temp

    def __set__(self, instance, value):
        instance._temp = value

class Celsius:
    temperature = Temperature()

    def __init__(self, temp):
        self._temp = temp
```

---

## 🔁 Reusable Descriptors

### Example: Type-checked field

```python
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type}")
        instance.__dict__[self.name] = value
```

Usage:

```python
class Person:
    age = Typed('age', int)

    def __init__(self, age):
        self.age = age
```

---

## 🧰 Real-World Uses

| Feature              | Powered by Descriptors? |
|----------------------|--------------------------|
| `@property`          | ✅ Yes                   |
| `@staticmethod`      | ✅ Yes (`__get__`)       |
| `@classmethod`       | ✅ Yes (`__get__`)       |
| ORMs (e.g., Django)  | ✅ Yes (Field descriptors)|
| Attribute validation | ✅ Yes                   |
| Lazy evaluation / caching | ✅ Yes             |

---

## 🧵 Gotchas and Quirks

### 1. Descriptors must live on the class, not the instance

```python
class A:
    attr = LoggedAttribute("attr")

a = A()
a.attr = 5  # Triggers __set__

a.__dict__["attr"] = 10  # Bypasses descriptor completely
```

### 2. Circular logic in `__get__`

Avoid infinite recursion:

```python
class Broken:
    def __get__(self, instance, owner):
        return instance.attr  # ❌ calls self again
```

Fix by using `instance.__dict__`.

---

## 🧪 Descriptor Lifecycle

```python
# Creation
descriptor = LoggedAttribute("x")

# Class assignment
class C:
    x = descriptor

# On attribute access:
value = C().x  # triggers __get__(descriptor, instance, C)

# On assignment:
C().x = 123     # triggers __set__
```

---

## 🪛 Debugging Tips

- Use `instance.__dict__` to inspect actual stored values.
- Use logging inside descriptor methods to trace calls.
- Use `type(obj).__dict__['attr']` to access the descriptor object.

---

## ✅ Summary

| Feature             | Description |
|---------------------|-------------|
| Descriptor          | Object implementing `__get__`, `__set__`, or `__delete__` |
| Data Descriptor     | Implements `__set__` → overrides instance vars |
| Non-data Descriptor | Only `__get__` → can be shadowed |
| Use cases           | Validation, computed properties, lazy loading, method binding |

---

## 🧪 When to Use Descriptors

Use descriptors if:
- You want reusable field logic across classes
- You want to enforce constraints/validation
- You want to implement computed fields or caching
- You're building a framework (ORM, schema validator, etc.)

---

## 📚 Further Reading

- [Python Data Model Docs (Descriptors)](https://docs.python.org/3/howto/descriptor.html)
- [Raymond Hettinger — "Understanding Descriptors"](https://nbviewer.org/github/rhettinger/python-descriptor/blob/master/descriptor.ipynb)
- [Fluent Python — Luciano Ramalho (Ch. 20)](https://www.oreilly.com/library/view/fluent-python/9781491946237/)


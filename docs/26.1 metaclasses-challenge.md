# Python Metaclasses: Coding Challenges

These challenges are designed to help you understand and apply Python metaclasses. They focus on customizing class creation, enforcing constraints, registering types, injecting functionality, and modifying class attributes.

---

## Challenge 1: Class Logger Metaclass

**Objective**: Create a metaclass `LoggingMeta` that logs every class it creates.

```python
class LoggingMeta(type):
    ...

class Foo(metaclass=LoggingMeta):
    pass

# Output:
# Creating class Foo
```

---

## Challenge 2: Enforce Method Existence

**Objective**: Use a metaclass to enforce that any class using it must define a `run()` method.

```python
class RequiresRunMeta(type):
    ...

class Valid(metaclass=RequiresRunMeta):
    def run(self): pass

class Invalid(metaclass=RequiresRunMeta):
    pass  # Should raise TypeError
```

---

## Challenge 3: Attribute Name Validation

**Objective**: Prevent all-uppercase attribute names in a class definition.

```python
class NoUpperCaseMeta(type):
    ...

# This should raise an error:
class BadClass(metaclass=NoUpperCaseMeta):
    BAD = 123
```

---

## Challenge 4: Auto-Register Classes

**Objective**: Use a metaclass to auto-register all subclasses in a global registry.

```python
REGISTRY = {}

class AutoRegisterMeta(type):
    ...

class A(metaclass=AutoRegisterMeta): pass
class B(metaclass=AutoRegisterMeta): pass

assert REGISTRY['A'] is A
```

---

## Challenge 5: Inject Class Attributes

**Objective**: Use a metaclass to add a default class attribute `created_by = "metaclass"` to every class.

```python
class InjectMeta(type):
    ...

class MyClass(metaclass=InjectMeta):
    pass

assert MyClass.created_by == "metaclass"
```

---

## Challenge 6: Prevent Subclassing

**Objective**: Create a metaclass that makes a class final (cannot be subclassed).

```python
class FinalMeta(type):
    def __new__(mcs, name, bases, namespace):
        for base in bases:
            if isinstance(base, FinalMeta):
                raise TypeError("Cannot subclass a final class")
        return super().__new__(mcs, name, bases, namespace)

class FinalClass(metaclass=FinalMeta): pass
class SubClass(FinalClass): pass  # Should raise
```

---

## Challenge 7: Singleton via Metaclass

**Objective**: Enforce the singleton pattern using a metaclass.

```python
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DBConnection(metaclass=SingletonMeta): pass

a = DBConnection()
b = DBConnection()
assert a is b
```

---

## Challenge 8: Method Wrapper Injection

**Objective**: Automatically wrap all methods of a class with a logger.

```python
class WrapMethodsMeta(type):
    def __new__(mcs, name, bases, namespace):
        for attr, val in namespace.items():
            if callable(val):
                def wrap(f):
                    def inner(*args, **kwargs):
                        print(f"Calling {f.__name__}")
                        return f(*args, **kwargs)
                    return inner
                namespace[attr] = wrap(val)
        return super().__new__(mcs, name, bases, namespace)

class MyClass(metaclass=WrapMethodsMeta):
    def hello(self):
        print("hi")

MyClass().hello()  # Logs method call
```

---

## Challenge 9: Class Freezing

**Objective**: Prevent any further attribute assignments to the class object after creation.

```python
class FrozenMeta(type):
    def __setattr__(cls, key, value):
        raise AttributeError("Class is frozen")

class Config(metaclass=FrozenMeta):
    version = "1.0"

Config.new_attr = 42  # Should raise
```

---

## Challenge 10: Metaclass Inheritance Hierarchy

**Objective**: Understand how metaclasses compose in multi-class hierarchies.

* Define `MetaA`, `MetaB`, and create a class that inherits from both with compatible metaclasses.

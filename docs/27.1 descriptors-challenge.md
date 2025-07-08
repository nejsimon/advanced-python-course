# Python Descriptors: Coding Challenges

These challenges focus on creating and using Python descriptors to implement custom attribute access, validation, computed properties, and reusable logic through data descriptors and non-data descriptors.

---

## Challenge 1: Read-Only Descriptor

**Objective**: Create a descriptor `ReadOnly` that allows getting a value but raises `AttributeError` on assignment.

```python
class ReadOnly:
    def __init__(self, value):
        self._value = value
    def __get__(self, instance, owner):
        return self._value
    def __set__(self, instance, value):
        raise AttributeError("Read-only attribute")

class MyClass:
    const = ReadOnly(42)

obj = MyClass()
assert obj.const == 42
obj.const = 10  # Raises AttributeError
```

---

## Challenge 2: Type-Enforcing Descriptor

**Objective**: Create a descriptor `Typed` that enforces the attribute type.

```python
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type}")
        instance.__dict__[self.name] = value

class Person:
    name = Typed("name", str)
    age = Typed("age", int)

p = Person()
p.name = "Alice"
p.age = 30
p.age = "old"  # Raises TypeError
```

---

## Challenge 3: Computed Property Descriptor

**Objective**: Implement a descriptor `Fahrenheit` that computes the value based on a Celsius attribute.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    @property
    def celsius(self):
        return self._celsius
    @celsius.setter
    def celsius(self, value):
        self._celsius = value
    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

# Rewrite this using a custom descriptor for fahrenheit
```

---

## Challenge 4: Descriptor With Storage

**Objective**: Create a `Counter` descriptor that counts how many times an attribute has been accessed.

```python
class Counter:
    def __init__(self):
        self.counts = {}
    def __get__(self, instance, owner):
        self.counts[instance] = self.counts.get(instance, 0) + 1
        return self.counts[instance]

class Usage:
    hits = Counter()

obj = Usage()
obj.hits
obj.hits
assert obj.hits == 3
```

---

## Challenge 5: Lazy Evaluation Descriptor

**Objective**: Implement `@lazy_property` that computes a value only once.

```python
class lazy_property:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = self.func(instance)
        setattr(instance, self.name, value)
        return value

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazy_property
    def area(self):
        print("Computing area")
        return 3.14 * self.radius ** 2

c = Circle(10)
c.area  # Computes
c.area  # Cached
```

---

## Challenge 6: Descriptor for Validation With Decorator Syntax

**Objective**: Write a `@validate` decorator for descriptors to inject custom validation functions.

```python
class Validated:
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if hasattr(self, "_validator"):
            self._validator(value)
        instance.__dict__[self.name] = value

def validate(validator):
    def wrapper(desc):
        desc._validator = validator
        return desc
    return wrapper

@validate(lambda x: x > 0)
class Positive(Validated): pass
```

---

## Challenge 7: Descriptor for Attribute Alias

**Objective**: Implement a descriptor that acts as an alias to another attribute.

```python
class Alias:
    def __init__(self, target_name):
        self.target_name = target_name
    def __get__(self, instance, owner):
        return getattr(instance, self.target_name)
    def __set__(self, instance, value):
        setattr(instance, self.target_name, value)

class Config:
    port = 8080
    alt_port = Alias("port")

cfg = Config()
assert cfg.alt_port == 8080
cfg.alt_port = 9090
assert cfg.port == 9090
```

---

## Challenge 8: Bound and Unbound Descriptor Access

**Objective**: Demonstrate the difference between descriptor access through the class and through an instance.

* Implement a descriptor with print statements in `__get__`
* Show `MyClass.attr` vs `MyClass().attr` access

---

## Challenge 9: Data vs Non-data Descriptors

**Objective**: Create one data descriptor and one non-data descriptor.

* Demonstrate that data descriptors take precedence over instance attributes
* Demonstrate that non-data descriptors do not

```python
class DataDescriptor:
    def __get__(self, instance, owner):
        return "data"
    def __set__(self, instance, value): pass

class NonDataDescriptor:
    def __get__(self, instance, owner):
        return "non-data"

class Demo:
    x = DataDescriptor()
    y = NonDataDescriptor()

obj = Demo()
obj.x = "instance value"  # Ignored because of data descriptor
obj.y = "instance value"  # Stored on instance
```

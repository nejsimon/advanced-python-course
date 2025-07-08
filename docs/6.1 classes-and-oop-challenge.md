# Python Classes and OOP: Coding Challenges

These challenges are designed to thoroughly exercise Python's object-oriented programming features, including class design, inheritance, encapsulation, composition, polymorphism, special methods, and advanced OOP idioms.

---

## Challenge 1: Simple Class with Methods

**Objective**: Create a `Rectangle` class with:

* Attributes: `width`, `height`
* Method: `area()`
* Method: `perimeter()`

```python
r = Rectangle(5, 3)
assert r.area() == 15
assert r.perimeter() == 16
```

---

## Challenge 2: Inheritance and Method Overriding

**Objective**: Create a base class `Animal` and a derived class `Dog`.

* `Animal` has `speak()` returning `"..."`
* `Dog` overrides `speak()` to return `"Woof!"`

```python
assert Animal().speak() == "..."
assert Dog().speak() == "Woof!"
```

---

## Challenge 3: Encapsulation and Properties

**Objective**: Create a `BankAccount` class with:

* A private attribute `_balance`
* A property `balance` (read-only)
* A method `deposit(amount)`
* A method `withdraw(amount)`

```python
account = BankAccount()
account.deposit(100)
assert account.balance == 100
```

---

## Challenge 4: Class and Static Methods

**Objective**: Add class-level tracking to a class `User`:

* Use a `@classmethod` to return total number of users
* Use a `@staticmethod` to validate email addresses

```python
assert User.is_valid_email("foo@example.com")
assert User.count() == 2
```

---

## Challenge 5: Dunder Methods and Equality

**Objective**: Create a class `Point(x, y)` with:

* `__eq__` to compare by value
* `__repr__` for readable output
* `__add__` to support `+` operator

```python
assert Point(1, 2) + Point(3, 4) == Point(4, 6)
```

---

## Challenge 6: Multiple Inheritance and `super()`

**Objective**: Create a `FlyingSwimmingCreature` that inherits from both `FlyingAnimal` and `SwimmingAnimal`.

* Ensure both parent `__init__()` methods are called
* Use `super()` appropriately

---

## Challenge 7: Composition over Inheritance

**Objective**: Create a class `Car` that uses a composed `Engine` object.

* `Engine` has a method `start()`
* `Car.start()` delegates to `Engine.start()`

---

## Challenge 8: Custom Iterators with `__iter__` and `__next__`

**Objective**: Create a class `RangeStepper(start, stop, step)` that mimics `range()`.

* Must support iteration with `for` loop

---

## Challenge 9: Abstract Base Classes

**Objective**: Define an abstract base class `Shape` with abstract method `area()`.

* Subclasses `Circle` and `Rectangle` must implement `area()`

Use `abc.ABC` and `@abstractmethod`

---

## Challenge 10: Callable Objects

**Objective**: Create a class `Multiplier(factor)` that returns the product when called like a function.

```python
m = Multiplier(10)
assert m(5) == 50
```

---

## Challenge 11: Fluent Interface via Method Chaining

**Objective**: Implement a class `QueryBuilder`:

* Methods: `.select()`, `.where()`, `.order_by()`
* Each method returns `self` to allow chaining

```python
query = QueryBuilder().select("*" ).where("id=1").order_by("name")
assert str(query) == "SELECT * WHERE id=1 ORDER BY name"
```

---

## Challenge 12: Slots for Memory Optimization

**Objective**: Implement a class `Point2D` using `__slots__`.

* Prevent dynamic attribute creation
* Save memory in tight loops


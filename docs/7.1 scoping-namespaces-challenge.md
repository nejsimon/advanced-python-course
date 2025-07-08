# Python Scoping and Namespaces: Coding Challenges

These challenges explore Python's scope resolution, the LEGB rule (Local, Enclosing, Global, Built-in), and manipulating and understanding namespaces.

---

## Challenge 1: Local and Global Variables

**Objective**: Understand the difference between local and global variable scopes.

```python
x = 10

def foo():
    x = 5
    return x

assert foo() == 5
assert x == 10
```

---

## Challenge 2: Using the `global` Keyword

**Objective**: Modify a global variable inside a function.

```python
counter = 0

def increment():
    global counter
    counter += 1

increment()
assert counter == 1
```

---

## Challenge 3: Using the `nonlocal` Keyword

**Objective**: Modify an enclosing (non-global) variable inside a nested function.

```python
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
    inner()
    return count

assert outer() == 1
```

---

## Challenge 4: LEGB Scope Rule

**Objective**: Trace variable lookup using LEGB rule.

```python
x = 'global'

def outer():
    x = 'enclosing'
    def inner():
        x = 'local'
        return x
    return inner()

assert outer() == 'local'
```

---

## Challenge 5: Shadowing Built-in Names

**Objective**: Show what happens when a built-in name is shadowed.

```python
len = 10  # Shadowing built-in function

try:
    len("abc")
except TypeError:
    pass  # Correctly shadowed

del len  # Restore built-in
assert len("abc") == 3
```

---

## Challenge 6: Inspecting Namespaces with `locals()` and `globals()`

**Objective**: Explore variable visibility using introspection.

```python
def show_vars():
    a = 5
    return 'a' in locals()

assert show_vars() == True
assert 'show_vars' in globals()
```

---

## Challenge 7: Function Factory with `nonlocal`

**Objective**: Use `nonlocal` to maintain state across calls.

```python
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = make_counter()
assert c() == 1
assert c() == 2
```

---

## Challenge 8: Class vs Instance Namespace

**Objective**: Differentiate between class-level and instance-level attributes.

```python
class Thing:
    shared = []

    def __init__(self):
        self.own = []

x = Thing()
y = Thing()
x.shared.append(1)
x.own.append(2)

assert y.shared == [1]
assert y.own == []
```

---

## Challenge 9: Module Namespace Isolation

**Objective**: Simulate isolated namespaces between modules.

```python
# File: a.py
value = 42

# File: b.py
import a
assert hasattr(a, 'value')
assert 'value' not in globals()
```

---

## Challenge 10: Dynamic Namespace Manipulation

**Objective**: Add/remove symbols from `globals()` or `locals()`.

```python
globals()['dynamic'] = 99
assert dynamic == 99

del globals()['dynamic']
assert 'dynamic' not in globals()
```

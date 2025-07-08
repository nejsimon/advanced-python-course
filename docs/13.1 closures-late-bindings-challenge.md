# Python Closures and Late Binding: Coding Challenges

These challenges help you understand how closures work in Python and how to deal with late binding issues that often occur in function factories and loops.

---

## Challenge 1: Basic Closure

**Objective**: Create a closure that captures a local variable.

```python
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
assert double(4) == 8
```

---

## Challenge 2: Closure with Mutable State

**Objective**: Maintain internal state in a closure.

```python
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c = make_counter()
assert c() == 1
assert c() == 2
```

---

## Challenge 3: Late Binding in Loop

**Objective**: Understand how late binding causes all closures to share the same reference.

```python
funcs = []
for i in range(3):
    funcs.append(lambda: i)

assert [f() for f in funcs] == [2, 2, 2]  # All refer to final value of i
```

---

## Challenge 4: Fixing Late Binding Using Default Args

**Objective**: Capture loop variable immediately by using a default argument.

```python
funcs = [lambda i=i: i for i in range(3)]
assert [f() for f in funcs] == [0, 1, 2]
```

---

## Challenge 5: Closure Inside Class

**Objective**: Create closures that reference class or instance data.

```python
class Greeter:
    def __init__(self, name):
        self.name = name

    def make_greeting(self):
        def greet():
            return f"Hello, {self.name}!"
        return greet

g = Greeter("Alice")
greet_fn = g.make_greeting()
assert greet_fn() == "Hello, Alice!"
```

---

## Challenge 6: Closure Factory for Decorators

**Objective**: Use closures to create a parameterized decorator.

```python
def repeat(n):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                fn(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("hi")

# Output: "hi" printed 3 times
```

---

## Challenge 7: Inspecting Free Variables

**Objective**: Use the `__closure__` attribute to inspect closed-over values.

```python
def outer():
    x = 42
    def inner():
        return x
    return inner

f = outer()
assert f.__closure__[0].cell_contents == 42
```

---

## Challenge 8: Closure with Dynamic Code

**Objective**: Build closures dynamically with `exec`.

```python
def build_func(var):
    code = f"def inner(): return {var}"
    local_ns = {}
    exec(code, {}, local_ns)
    return local_ns['inner']

f = build_func("42")
assert f() == 42
```

---

## Challenge 9: Multiple Closures Sharing State

**Objective**: Have multiple closures share and mutate the same nonlocal variable.

```python
def make_pair():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    def dec():
        nonlocal count
        count -= 1
        return count
    return inc, dec

inc, dec = make_pair()
assert inc() == 1
assert dec() == 0
```

---

## Challenge 10: Using `functools.partial` Instead of Closures

**Objective**: Use `functools.partial` as an alternative to closures for simple currying.

```python
from functools import partial

def multiply(x, y):
    return x * y

double = partial(multiply, 2)
assert double(5) == 10
```


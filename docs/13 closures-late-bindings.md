# Closures and Late Binding in Python

Closures and late binding are foundational to Python's handling of nested functions, lambdas, and deferred evaluation. These concepts power decorators, factories, and functional-style programming. They also introduce subtle bugs when misunderstood.

---

## 🐞 What Is a Closure?

A **closure** is a function that *remembers the environment in which it was defined*, even if it is called outside that scope.

### Example:

```python
def outer():
    x = 10
    def inner():
        print(x)  # x is "closed over"
    return inner

f = outer()
f()  # prints 10
```

* The inner function **closes over** the `x` variable.
* The lifetime of `x` extends beyond the `outer()` call.

---

## 🚀 Uses of Closures

| Use Case           | Example                              |
| ------------------ | ------------------------------------ |
| Callback functions | GUI, async calls                     |
| Function factories | `make_adder(x)` returning adder func |
| Decorators         | Wrap behavior in closures            |
| Memoization/cache  | Store previous calls in closure vars |

```python
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

triple = make_multiplier(3)
print(triple(10))  # 30
```

---

## 🤔 Late Binding: The Gotcha

**Late binding** means that variables in closures are looked up **when the inner function is called**, not when it is defined.

### Classic Bug:

```python
def make_funcs():
    funcs = []
    for i in range(3):
        def f():
            return i  # i is bound *late*
        funcs.append(f)
    return funcs

f1, f2, f3 = make_funcs()
print(f1(), f2(), f3())  # 2 2 2 (not 0 1 2)
```

Each function references the same `i`, which becomes 2 at loop end.

---

## ✅ Fixing Late Binding with Default Arguments

```python
def make_funcs():
    return [lambda i=i: i for i in range(3)]

f1, f2, f3 = make_funcs()
print(f1(), f2(), f3())  # 0 1 2
```

Here, `i` is **captured by value** via default argument.

---

## 🪡 Fixing with `functools.partial`

```python
from functools import partial

def add(a, b):
    return a + b

add5 = partial(add, 5)
print(add5(10))  # 15
```

---

## 🎮 Inspecting Closures

Each closure is stored in `__closure__`:

```python
def outer():
    x = 42
    def inner():
        return x
    return inner

f = outer()
print(f.__closure__[0].cell_contents)  # 42
```

---

## 🏛 When Closures Are Created

Closures are formed:

* When an inner function uses **non-local** variables
* And the outer function returns that inner function

Closures can also appear in:

* Lambdas
* Comprehensions
* Decorators

---

## 🚫 Closures vs Classes

Sometimes, classes are clearer and safer for maintaining state:

```python
class Adder:
    def __init__(self, inc):
        self.inc = inc
    def __call__(self, x):
        return x + self.inc
```

Use when:

* You need multiple methods or mutable state
* Debuggability or readability matters

---

## ⚠️ Common Pitfalls

### 1. Late binding in loops

Fix with default args or `partial`

### 2. Mutable captured variables

```python
def counter():
    count = [0]
    def inc():
        count[0] += 1
        return count[0]
    return inc
```

### 3. Unintended closure

Closures persist longer than you may think. Avoid excessive captures.

---

## 🔍 Summary

| Feature      | Notes                                      |
| ------------ | ------------------------------------------ |
| Closure      | Inner function + closed-over vars          |
| Late binding | Names looked up at call time               |
| Workaround   | Use default args or `partial`              |
| Debugging    | Use `__closure__` to inspect captured vars |
| Alternatives | Use classes for complex state              |

---

## 📚 Further Reading

* [Python Reference: Nested Scopes](https://docs.python.org/3/reference/executionmodel.html#naming-and-binding)
* [PEP 227: Statically Nested Scopes](https://peps.python.org/pep-0227/)
* Fluent Python – Chapter 7
* [Late Binding Closures](https://docs.python-guide.org/writing/gotchas/#late-binding-closures)

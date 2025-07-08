# Python Functions

Functions in Python are **first-class objects** — they can be created, passed around, returned, and introspected. Python supports a wide range of functional constructs, from simple definitions to decorators, closures, and dynamic invocation.

---

## 🔰 Function Basics

```python
def greet(name):
    return f"Hello, {name}"
```

### Functions Are First-Class

```python
def add(x, y): return x + y

f = add
print(f(2, 3))  # 5

def apply(func, x, y): return func(x, y)
```

---

## ⚙️ Function Parameters

### Parameter Types

```python
def example(pos1, pos2, /, named_only, *, kw_only): ...
```

| Syntax                 | Meaning                             |
|------------------------|-------------------------------------|
| `pos1`                 | Positional argument                 |
| `/`                    | All before must be positional       |
| `*args`                | Variadic positional args (tuple)    |
| `kw_only`              | Keyword-only after `*`              |
| `**kwargs`             | Variadic keyword args (dict)        |
| `=`                    | Default values                      |

### Example

```python
def f(a, b=2, *args, kw, **kwargs):
    ...
```

> Introduced in Python 3.8+: the `/` to enforce positional-only args.

---

## 🧪 Function Annotations

```python
def square(x: int) -> int:
    return x * x

print(square.__annotations__)  # {'x': <class 'int'>, 'return': <class 'int'>}
```

Annotations are optional and **not enforced** at runtime (unless using a type checker like `mypy`).

---

## 🧠 Variable Scope and Closures

Python uses **lexical scoping**.

```python
def outer():
    x = 10
    def inner():
        print(x)  # captures x from outer scope
    return inner
```

> Closures retain references to variables, not their values.

---

### Nonlocal vs Global

```python
x = "global"

def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "inner"
    inner()
    print(x)  # inner

def another():
    global x
    x = "modified"
```

- `nonlocal`: refer to the nearest enclosing non-global scope
- `global`: refer to the module-level global

---

## 🧩 Lambdas (Anonymous Functions)

```python
square = lambda x: x * x
```

- Expression-only
- No statements or annotations
- Use `def` if logic is complex

---

## 🔄 Function Decorators

A **decorator** is a function that takes a function and returns a modified function.

```python
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")
        return func(*args, **kwargs)
    return wrapper

@debug
def add(x, y):
    return x + y
```

### Chaining Decorators

```python
@auth
@cache
def query(): ...
```

---

## 🔍 Introspection

Python functions carry metadata:

```python
def f(a: int, b: str = "x") -> str:
    pass

print(f.__name__)         # 'f'
print(f.__defaults__)     # ('x',)
print(f.__code__.co_varnames)  # ('a', 'b')
print(f.__annotations__)  # {'a': int, 'b': str, 'return': str}
```

Use the `inspect` module for detailed inspection.

---

## 🧱 Inner Functions & Closures

```python
def outer():
    secret = 42
    def inner():
        return secret
    return inner

f = outer()
f()  # 42
```

Useful for:
- Encapsulation
- Lazy evaluation
- Decorators

---

## 🔃 Generators (Functions that Yield)

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(3): print(i)
```

- Use `yield` to produce a generator object
- Maintain internal state across pauses

---

## 🧵 Async Functions

```python
async def fetch():
    return await http_get()
```

- Must be `await`ed
- Return coroutine objects
- Use `async for` and `async with` in compatible contexts

---

## 🧪 Partial Application

```python
from functools import partial

def power(base, exp): return base ** exp

square = partial(power, exp=2)
print(square(4))  # 16
```

---

## 🧰 Common Built-in Functional Tools

| Tool                   | Purpose                          |
|------------------------|----------------------------------|
| `map(func, iterable)`  | Apply function to each item      |
| `filter(func, iterable)` | Filter items                    |
| `zip(*iterables)`      | Combine sequences                |
| `enumerate(iterable)`  | Index + value iterator           |
| `functools.reduce()`   | Reduce iterable to one value     |
| `functools.lru_cache`  | Memoization decorator            |
| `operator.methodcaller` | Dynamic method calls            |

---

## 🧵 Quirks and Gotchas

### 1. Mutable Default Arguments

```python
def append(item, lst=[]):  # ⚠️ BAD
    lst.append(item)
    return lst

print(append(1))  # [1]
print(append(2))  # [1, 2] — shared list!
```

**Fix**:

```python
def append(item, lst=None):
    if lst is None:
        lst = []
    ...
```

### 2. Closures Capture by Reference

```python
funcs = []
for i in range(3):
    funcs.append(lambda: i)

print([f() for f in funcs])  # [2, 2, 2], not [0, 1, 2]
```

Fix with default argument:

```python
funcs.append(lambda i=i: i)
```

### 3. `*args` and `**kwargs` Ordering

```python
def f(pos, /, a, b=2, *args, kw, **kwargs): ...
```

Be careful with order: Positional-only → Pos-or-kw → *args → kw-only → **kwargs

---

## ✅ Summary

| Feature             | Support Level |
|---------------------|----------------|
| First-class         | ✅ Yes          |
| Closures            | ✅ Yes          |
| Annotations         | ✅ Yes (optional) |
| Decorators          | ✅ Yes          |
| Async               | ✅ Yes          |
| Partial application | ✅ Yes          |
| Lambda              | ✅ Limited       |
| Introspection       | ✅ Rich support  |

Python functions are dynamic, composable, introspectable, and support both imperative and functional paradigms.

---

## 📚 Further Reading

- [Python `def` statement](https://docs.python.org/3/reference/compound_stmts.html#function-definitions)
- [PEP 570 – Positional-Only Parameters](https://peps.python.org/pep-0570/)
- [`inspect` module](https://docs.python.org/3/library/inspect.html)
- Fluent Python — Ch. 5, 7, 15


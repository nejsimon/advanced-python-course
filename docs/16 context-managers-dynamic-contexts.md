# Context Managers and Dynamic Contexts in Python

Python’s `with` statement and the `contextlib` module provide elegant, readable syntax for **scoped resource management** and **dynamic context propagation**.

This guide covers:
- Creating and using context managers
- `contextlib` utilities
- Context variable isolation
- Advanced techniques and pitfalls

---

## 🧠 What Is a Context Manager?

A **context manager** is any object that defines:
- `__enter__(self)`
- `__exit__(self, exc_type, exc_value, traceback)`

Used via the `with` statement:

```python
with open("file.txt") as f:
    data = f.read()
```

---

## ✅ Basic Context Manager Example

```python
class ManagedFile:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.file = open(self.path)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
```

---

## 📦 `contextlib` Module

The `contextlib` module simplifies context manager creation.

### `@contextmanager`

```python
from contextlib import contextmanager

@contextmanager
def open_file(path):
    f = open(path)
    try:
        yield f
    finally:
        f.close()
```

> Supports `try`/`finally` logic using generator syntax.

---

### `contextlib.ExitStack`

Dynamically manage **a variable number** of context managers:

```python
from contextlib import ExitStack

with ExitStack() as stack:
    files = [stack.enter_context(open(f)) for f in paths]
```

---

### `contextlib.nullcontext`

Acts as a no-op context manager:

```python
from contextlib import nullcontext

with nullcontext() if optional else my_resource() as res:
    ...
```

---

### `contextlib.suppress`

Suppress specific exceptions:

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove("temp.txt")
```

---

## ⚙️ Context Propagation: `contextvars`

Introduced in Python 3.7, `contextvars` allow dynamic, per-task values.

```python
import contextvars

user = contextvars.ContextVar("user")

def log_action():
    print(f"User: {user.get()}")

def set_context():
    token = user.set("alice")
    log_action()  # User: alice
    user.reset(token)
```

Each async task has **its own isolated context** — unlike thread locals.

---

## 🧪 Context Propagation in Async Code

```python
import asyncio

request_id = contextvars.ContextVar("request_id")

async def handler():
    print(f"Handling request {request_id.get()}")

async def main():
    request_id.set("abc123")
    await handler()

asyncio.run(main())
```

> Unlike `threading.local()`, `contextvars` maintain consistency across `await` boundaries.

---

## 🔍 How the `with` Statement Works

```python
with manager() as x:
    body
```

Equivalent to:

```python
ctx = manager()
x = ctx.__enter__()
try:
    body
finally:
    ctx.__exit__(*sys.exc_info())
```

---

## 🧨 Common Pitfalls

### 1. Forgetting `__exit__`

```python
class Bad:
    def __enter__(self): ...
    # Missing __exit__
```

→ Will raise `AttributeError` at runtime.

---

### 2. Using `@contextmanager` improperly

Don’t call `.close()` manually — the decorator handles it:

```python
@contextmanager
def broken():
    yield open("file.txt")  # ❌ if not closed in finally
```

Fix:

```python
@contextmanager
def safe():
    f = open("file.txt")
    try:
        yield f
    finally:
        f.close()
```

---

### 3. Relying on context for cleanup without `with`

```python
f = open("file.txt")
data = f.read()
# ❌ file not closed if exception occurs
```

Always use `with` or `try/finally`.

---

## 🔄 Custom Exit Behavior

Can suppress exceptions by returning `True` from `__exit__`.

```python
def __exit__(self, exc_type, exc_val, exc_tb):
    if exc_type:
        log_error(exc_val)
        return True  # suppress
```

---

## 🧱 Real-World Use Cases

| Use Case          | Example                                    |
|-------------------|--------------------------------------------|
| File handling     | `open()`, `gzip.open()`                    |
| Lock management   | `threading.Lock()`                         |
| DB transactions   | `sqlalchemy.session.begin()`               |
| Temporary config  | `contextvars`, `unittest.mock.patch()`     |
| Logging contexts  | request ID injection, tracing              |
| Resource pooling  | Redis connections, API clients             |

---

## 🧮 Nesting and Reentrancy

Nested `with` statements:

```python
with A() as a, B() as b:
    ...
```

Reentrant managers must handle `__enter__` being called multiple times per instance — most are **not** reentrant unless explicitly designed to be.

---

## 🧵 Thread-local vs ContextVar

| Feature            | `threading.local()`     | `contextvars.ContextVar()` |
|--------------------|--------------------------|-----------------------------|
| Thread safety      | ✅                        | ✅                          |
| Async safe         | ❌ (leaks context)        | ✅ (preserves context)      |
| Context isolation  | Shared across awaitables | Per-task                    |
| Typical use        | Legacy code, Flask       | Modern async frameworks     |

---

## ✅ Summary

| Tool                     | Purpose                                 |
|--------------------------|------------------------------------------|
| `__enter__` / `__exit__` | Classic context manager protocol         |
| `@contextmanager`        | Generator-based, elegant setup/teardown |
| `contextvars`            | Dynamic per-task variables               |
| `ExitStack`              | Manage multiple unknown context objects  |
| `suppress`, `nullcontext`| Control exception or behavior defaults   |

---

## 📚 Further Reading

- [contextlib — Context manager utilities](https://docs.python.org/3/library/contextlib.html)
- [contextvars — PEP 567](https://peps.python.org/pep-0567/)
- Fluent Python – Chapter 15
- [Understanding Python Context Managers](https://realpython.com/python-with-statement/)
- [David Beazley: Generators, Coroutines, and Context Managers (PyCon talk)](https://www.youtube.com/watch?v=1QXjXoy3-cs)

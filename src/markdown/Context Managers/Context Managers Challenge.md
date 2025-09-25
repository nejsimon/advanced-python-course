# Python Context Managers: Coding Challenges

These challenges explore the use of `with` blocks, custom context managers using `__enter__`/`__exit__`, the `contextlib` module, and dynamically scoped context behaviors.

---

## Challenge 1: Basic `with` Statement

**Objective**: Use a context manager to open and read a file.

```python
with open("test.txt", "w") as f:
    f.write("hello")

with open("test.txt") as f:
    assert f.read() == "hello"
```

---

## Challenge 2: Custom Context Manager Class

**Objective**: Implement a context manager with `__enter__` and `__exit__`.

```python
class Resource:
    def __enter__(self):
        print("Acquiring")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Releasing")

with Resource():
    pass  # Should print acquiring and releasing
```

---

## Challenge 3: Handle Exceptions in `__exit__`

**Objective**: Catch and suppress exceptions inside the context manager.

```python
class Suppress:
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_val, exc_tb):
        return True  # Suppress all exceptions

with Suppress():
    raise ValueError("Suppressed")

print("Continued")  # Should print
```

---

## Challenge 4: Use `contextlib.contextmanager`

**Objective**: Write a generator-based context manager.

```python
from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")

with tag("h1"):
    print("Title")
```

---

## Challenge 5: Nested Context Managers

**Objective**: Nest multiple context managers using a single `with` line.

```python
from contextlib import ExitStack

with ExitStack() as stack:
    f1 = stack.enter_context(open("a.txt", "w"))
    f2 = stack.enter_context(open("b.txt", "w"))
    f1.write("A")
    f2.write("B")
```

---

## Challenge 6: Dynamic Variable Context

**Objective**: Create a context manager that dynamically overrides a global setting.

```python
setting = {"debug": False}

@contextmanager
def set_debug(value):
    original = setting["debug"]
    setting["debug"] = value
    try:
        yield
    finally:
        setting["debug"] = original

with set_debug(True):
    assert setting["debug"] is True
assert setting["debug"] is False
```

---

## Challenge 7: Thread-Local Context Data

**Objective**: Use thread-local storage to hold context-specific state.

```python
import threading
from contextlib import contextmanager

_ctx = threading.local()

@contextmanager
def user_context(user):
    _ctx.user = user
    try:
        yield
    finally:
        _ctx.user = None

def get_user():
    return getattr(_ctx, 'user', None)

with user_context("alice"):
    assert get_user() == "alice"
assert get_user() is None
```

---

## Challenge 8: Context Manager Stack Behavior

**Objective**: Implement a context stack class to push and pop custom contexts.

```python
class ContextStack:
    def __init__(self):
        self.stack = []

    def __enter__(self):
        self.stack.append(True)
        return self

    def __exit__(self, *args):
        self.stack.pop()

with ContextStack() as cs:
    assert cs.stack == [True]
assert cs.stack == []
```

---

## Challenge 9: Reentrant Contexts

**Objective**: Create a context manager that can be re-entered safely.

```python
from threading import RLock

lock = RLock()

with lock:
    with lock:
        print("Reentrant lock works")
```

---

## Challenge 10: Context Propagation (advanced)

**Objective**: Implement a basic dynamic scoping mechanism via context stack.

```python
class DynamicContext:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        self.stack.pop()

    def get(self):
        return self.stack[-1] if self.stack else None

    @contextmanager
    def override(self, value):
        self.push(value)
        try:
            yield
        finally:
            self.pop()

ctx = DynamicContext()
with ctx.override("a"):
    assert ctx.get() == "a"
    with ctx.override("b"):
        assert ctx.get() == "b"
    assert ctx.get() == "a"
```


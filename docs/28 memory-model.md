# Python Memory Model

Python's memory model governs how **objects are allocated, referenced, mutated, and garbage-collected**. It's crucial for understanding behavior around variables, performance, multithreading, and object identity.

This guide applies to **CPython**, the reference implementation.

---

## 🔧 Memory Basics

- All data in Python is **object-based**.
- Variables are **references to objects**, not the objects themselves.
- Object lifetime is managed via **reference counting** and **cyclic GC**.

---

## 🧱 Object Model

Each object has:
- **Type**: defined by `type(obj)`
- **ID**: unique identity (`id(obj)` → memory address in CPython)
- **Value**: internal data/state
- **Reference count**: how many references point to the object

```python
a = [1, 2, 3]
b = a  # both refer to same list
print(id(a) == id(b))  # True
```

---

## 🔁 Reference Counting

CPython uses **reference counting** as the primary memory management strategy.

```python
import sys

a = []
print(sys.getrefcount(a))  # typically > 1 due to temporary refs
```

### When ref count hits zero → object is immediately deallocated.

---

## 🔄 Garbage Collection

Reference counting fails with **cyclic references**:

```python
class Node:
    def __init__(self): self.ref = self

a = Node()
del a  # not enough!
```

Python uses **cyclic GC** to find and clean unreachable reference cycles.

```python
import gc
gc.collect()
```

You can tune GC behavior via `gc.set_threshold(...)`.

---

## 🧵 Variable Binding Model

```python
x = [1, 2, 3]
y = x  # y points to the same list
x.append(4)
print(y)  # [1, 2, 3, 4]
```

### Variables are **names** in namespaces:
- `x = 10` binds name `x` to object `10`
- Assignment does **not** copy values, just references

---

## 🔁 Identity vs Equality

```python
a = [1, 2]
b = a
c = [1, 2]

a is b  # True
a == c  # True
a is c  # False
```

| Operator | Checks         |
|----------|----------------|
| `is`     | Identity (`id()`) |
| `==`     | Value equality (via `__eq__`) |

---

## 🧊 Mutable vs Immutable Types

### Immutable:
- `int`, `float`, `str`, `tuple`, `frozenset`, `bytes`
- Cannot change after creation
- "Modification" creates a new object

### Mutable:
- `list`, `dict`, `set`, `bytearray`, `user-defined classes`

### Consequences:
```python
x = (1, 2)
x += (3,)  # creates new tuple

a = [1, 2]
b = a
a.append(3)
print(b)  # [1, 2, 3]
```

---

## 🔄 Memory Reuse (Interning)

Python interns some immutable objects for performance:

```python
a = 256
b = 256
a is b  # True (interned small int)

a = 257
b = 257
a is b  # May be False
```

Also applies to some strings:

```python
'a' * 3 is 'aaa'  # True in CPython, but not guaranteed
```

---

## 📦 Memory Allocation Internals

CPython uses:

- **PyObject_HEAD**: common structure for all objects
- **Small Object Allocator**: arena-based allocator (`obmalloc.c`)
- **Malloc-based** fallback for large objects

Memory layout:

```
+------------------+
| Ref count        |
| Type pointer     |
| Object data ...  |
+------------------+
```

Use `sys.getsizeof()` to inspect memory use:

```python
import sys
sys.getsizeof([])  # 56 bytes (platform-dependent)
```

> `getsizeof()` doesn't account for referenced objects (e.g., contents of a list).

---

## 📉 Memory Leaks in Python

Python *can* leak memory due to:

- **Reference cycles with `__del__`**
- **C extension modules** (e.g., NumPy)
- **Global variables in long-lived processes**
- **Caching and interning strategies**

### Detecting Leaks

```python
import tracemalloc
tracemalloc.start()

# Run app
snapshot = tracemalloc.take_snapshot()
snapshot.statistics('filename')
```

---

## 🧪 Weak References

Avoid strong reference ownership:

```python
import weakref

class A:
    pass

obj = A()
r = weakref.ref(obj)
print(r())  # A instance
del obj
print(r())  # None
```

Used in:
- Caches
- Observer patterns
- Graphs

---

## 🧵 Concurrency and Memory

Python’s memory model is **not thread-safe** due to shared mutable objects.

- CPython has a **Global Interpreter Lock (GIL)** to serialize bytecode execution
- Multiple threads → shared memory space
- Use `threading.Lock` or `multiprocessing` for safety

---

## ⚠️ Common Pitfalls

### 1. Shared Mutable Defaults

```python
def f(x=[]):  # ⚠️ mutable default
    x.append(1)
    return x

f()  # [1]
f()  # [1, 1]
```

Fix:

```python
def f(x=None):
    if x is None:
        x = []
```

---

### 2. Reference Cycles with `__del__`

If two objects reference each other and define `__del__`, Python can't automatically break the cycle.

> Avoid `__del__` unless absolutely necessary.

---

### 3. Leaky Global State

```python
cache = {}

def lookup(key):
    if key not in cache:
        cache[key] = compute_expensive_value(key)
```

Fix with `WeakValueDictionary`, `lru_cache`, or cache expiry.

---

## 🧠 Summary

| Concept              | Detail                                 |
|----------------------|-----------------------------------------|
| Variables            | Names referencing objects               |
| Ref Counting         | Immediate deallocation at 0 refs        |
| Garbage Collection   | Cycles broken by mark-and-sweep GC      |
| Memory Interning     | Small ints and some strings reused      |
| Object Identity      | `id(obj)` == memory address in CPython  |
| Mutability           | Affects aliasing and performance        |
| Memory Leaks         | Mostly from cycles, globals, extensions |
| Tools                | `gc`, `sys`, `tracemalloc`, `weakref`  |

---

## 🛠️ Useful Modules and Tools

| Module        | Purpose                                |
|---------------|----------------------------------------|
| `gc`          | Garbage collector tuning and inspection|
| `sys`         | Refcounts, object size, memory info    |
| `tracemalloc` | Snapshot-based memory tracing          |
| `weakref`     | Weak references for non-owning pointers|
| `resource`    | OS-level memory usage (Unix)           |
| `objgraph`    | Visualize object reference graphs      |

---

## 📚 Further Reading

- [Python Data Model](https://docs.python.org/3/reference/datamodel.html)
- [CPython's Memory Management Internals](https://devguide.python.org/internals/memory-management/)
- [tracemalloc docs](https://docs.python.org/3/library/tracemalloc.html)
- Fluent Python — Chapter 8 (Object References, Mutability, and Recycling)


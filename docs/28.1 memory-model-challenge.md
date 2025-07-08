# Python Memory Model: Coding Challenges

These challenges explore Python's memory model, including object identity, mutability, reference counting, garbage collection, memory leaks, and shared references. Understanding these is key to writing efficient and correct Python programs.

---

## Challenge 1: Identity vs Equality

**Objective**: Demonstrate the difference between `is` (identity) and `==` (equality).

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

assert a == b      # Equality
assert a is not b   # Different objects
assert a is c       # Same object
```

---

## Challenge 2: Shared Mutable State

**Objective**: Show how mutable default arguments can lead to shared state.

```python
def append_to(element, target=[]):
    target.append(element)
    return target

first = append_to(1)
second = append_to(2)
assert second == [1, 2]  # Bug from shared state
```

Fix this using `None` as a sentinel.

---

## Challenge 3: Reference Counting

**Objective**: Use the `sys.getrefcount()` function to explore object reference counts.

```python
import sys
x = []
print(sys.getrefcount(x))  # Count includes temporary reference passed to getrefcount
```

---

## Challenge 4: Circular References

**Objective**: Create a pair of objects that reference each other and show how they can form a cycle.

```python
class Node:
    def __init__(self):
        self.ref = None

a = Node()
b = Node()
a.ref = b
b.ref = a  # Cycle
```

Use `gc.collect()` to trigger collection.

---

## Challenge 5: Deleting References

**Objective**: Show that deleting a reference does not necessarily delete the object.

```python
x = [1, 2, 3]
y = x

assert id(x) == id(y)
del x
assert y == [1, 2, 3]
```

---

## Challenge 6: Weak References

**Objective**: Use `weakref` to create a weak reference that does not prevent garbage collection.

```python
import weakref

class MyObject:
    pass

obj = MyObject()
ref = weakref.ref(obj)
assert ref() is obj

del obj
assert ref() is None  # Object was collected
```

---

## Challenge 7: Interning and Small Integer Caching

**Objective**: Observe interning behavior for small integers and strings.

```python
a = 256
b = 256
assert a is b  # Cached

x = 1000
y = 1000
assert x is not y  # Not cached

s1 = "hello"
s2 = "hello"
assert s1 is s2  # Interned
```

---

## Challenge 8: Memory Leak via Closures

**Objective**: Create a memory leak-like pattern using a closure that holds a reference longer than expected.

```python
def make_leaky():
    big_data = [1] * 10**6
    def inner():
        return big_data
    return inner

leak = make_leaky()
# big_data is still alive because `inner` closes over it
```

---

## Challenge 9: Object Life Cycle Logging

**Objective**: Use `__del__` to print when an object is garbage collected.

```python
class Tracked:
    def __del__(self):
        print("Deleted")

x = Tracked()
del x  # Should print
```

---

## Challenge 10: Investigate Memory Use with `tracemalloc`

**Objective**: Use `tracemalloc` to monitor memory allocation.

```python
import tracemalloc

tracemalloc.start()

lst = [i for i in range(10000)]

current, peak = tracemalloc.get_traced_memory()
print(f"Current: {current} bytes; Peak: {peak} bytes")

tracemalloc.stop()
```

# Python Variables, Constants, and References: Coding Challenges

These challenges explore how variables work in Python, including binding, mutability, identity, shared references, and best practices for defining constants.

---

## Challenge 1: Variable Binding and Rebinding

**Objective**: Understand how variables point to objects and how rebinding affects them.

```python
a = [1, 2, 3]
b = a
b.append(4)
assert a == [1, 2, 3, 4]  # Shared reference

b = [9, 9, 9]
assert a != b  # b is now bound to a new object
```

---

## Challenge 2: Identity vs Equality

**Objective**: Differentiate between `is` (identity) and `==` (value equality).

```python
x = [1, 2]
y = [1, 2]
z = x

assert x == y
assert x is not y
assert x is z
```

---

## Challenge 3: Mutable vs Immutable Objects

**Objective**: Show how mutating an object affects references.

```python
nums = [1, 2, 3]
def mutate(lst):
    lst.append(4)

mutate(nums)
assert nums == [1, 2, 3, 4]
```

Try doing the same with an `int`.

---

## Challenge 4: Copying vs Referencing

**Objective**: Create a copy of an object that doesn't share the reference.

```python
import copy

original = [1, 2, [3]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[2].append(4)
assert shallow[2] == [3, 4]  # Shared nested list
assert deep[2] == [3]        # Deep copy isolated it
```

---

## Challenge 5: Constants Convention

**Objective**: Define constants and follow naming conventions.

```python
PI = 3.14159
MAX_RETRIES = 5

# Convention only: Python does not enforce immutability
```

---

## Challenge 6: Function Argument Behavior

**Objective**: Observe how passing mutable vs immutable objects affects results.

```python
def try_to_change(x):
    x += x
    return x

assert try_to_change([1]) == [1, 1]  # Mutates inside local scope
assert try_to_change(10) == 20       # Returns new int
```

---

## Challenge 7: Variable Scope

**Objective**: Explore local, nonlocal, and global variable scopes.

```python
def outer():
    x = 'outer'
    def inner():
        nonlocal x
        x = 'inner'
    inner()
    return x

assert outer() == 'inner'
```

---

## Challenge 8: Variable Annotations (PEP 526)

**Objective**: Annotate variables with types.

```python
count: int = 0
name: str = "Alice"

# Not enforced at runtime but useful for tooling
```

---

## Challenge 9: Shared References in Lists

**Objective**: Demonstrate how shared references can lead to bugs.

```python
matrix = [[0] * 3] * 3  # All rows share the same object
matrix[0][0] = 1
assert matrix[1][0] == 1  # Unexpected behavior
```

Fix with a list comprehension:

```python
matrix = [[0 for _ in range(3)] for _ in range(3)]
```

---

## Challenge 10: Name Binding in Loops (Late Binding)

**Objective**: Understand late binding in loop variable closures.

```python
funcs = []
for i in range(3):
    funcs.append(lambda: i)

assert [f() for f in funcs] == [2, 2, 2]  # All refer to last i
```

Fix by binding immediately:

```python
funcs = [(lambda i=i: i) for i in range(3)]
assert [f() for f in funcs] == [0, 1, 2]
```

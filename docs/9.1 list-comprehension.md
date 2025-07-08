# Python List Comprehension

List comprehensions provide a concise and expressive way to create lists in Python. They combine mapping, filtering, and iteration into a single, readable syntax.

## 🔰 Overview

- **List comprehension** is a syntactic construct to create a new list from an iterable.
- It is generally more compact and often faster than using `for` loops.
- Syntax:  
  ```python
  [expression for item in iterable if condition]
  ```

---

## 🛠 Basic Syntax

```python
squares = [x * x for x in range(10)]
```

Equivalent to:

```python
squares = []
for x in range(10):
    squares.append(x * x)
```

## 🧪 With Conditionals

```python
evens = [x for x in range(10) if x % 2 == 0]
```

- **Note**: The `if` clause filters the values.

---

## ⚙️ Nested Loops

```python
pairs = [(x, y) for x in range(3) for y in range(2)]
# => [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
```

Order of nesting is the same as writing nested `for` loops.

```python
for x in range(3):
    for y in range(2):
        ...
```

---

## 🔄 Conditional Expressions

```python
labels = ['even' if x % 2 == 0 else 'odd' for x in range(5)]
# => ['even', 'odd', 'even', 'odd', 'even']
```

> You can use an `if-else` expression, but it must go **before** the `for`.

Correct:
```python
[x if x > 0 else 0 for x in numbers]
```

Incorrect:
```python
[x for x in numbers if x > 0 else 0]  # ❌ SyntaxError
```

---

## 🔁 Rewriting Common Patterns

### Map

```python
# map with lambda
list(map(lambda x: x * 2, range(5)))

# list comprehension equivalent
[x * 2 for x in range(5)]
```

### Filter

```python
# filter with lambda
list(filter(lambda x: x % 2 == 0, range(10)))

# list comprehension equivalent
[x for x in range(10) if x % 2 == 0]
```

### Map + Filter

```python
[x * 2 for x in range(10) if x % 2 == 0]
```

---

## 🧵 Quirks and Gotchas

### 1. **Scope Leak (Python 2.x)**

In Python 2, the loop variable leaked into the outer scope:

```python
[x for x in range(5)]
print(x)  # x is 4 in Python 2 — not in Python 3
```

**Python 3** fixed this—comprehension variables are now local.

---

### 2. **Multiple `if` Statements**

```python
[x for x in range(20) if x % 2 == 0 if x % 3 == 0]
# => [0, 6, 12, 18]
```

This is equivalent to:

```python
[x for x in range(20) if (x % 2 == 0 and x % 3 == 0)]
```

But arguably less readable.

---

### 3. **Don't Abuse Readability**

```python
# Avoid:
[func(x, y) for x in list1 for y in list2 if cond1(x) if cond2(y)]

# Prefer breaking into helper functions or classic loops if it gets too dense
```

---

## 📦 List vs Set vs Dict Comprehension

Python also supports:

```python
# Set comprehension
{x * x for x in range(5)}

# Dict comprehension
{k: k * k for k in range(5)}
```

---

## 🧵 Comprehensions Inside Functions

You can return a list from a function using a comprehension:

```python
def get_evens(n):
    return [x for x in range(n) if x % 2 == 0]
```

---

## 💡 Advanced Trick: Flattening

```python
nested = [[1, 2], [3, 4], [5]]
flat = [item for sublist in nested for item in sublist]
# => [1, 2, 3, 4, 5]
```

Nested `for` loops = flattening a list of lists.

---

## 🧪 Performance

List comprehensions are typically:
- **Faster** than using `for` + `.append()`
- **Less flexible** than full `for` loops (you can’t break or continue)
- **More memory intensive** than generators (see below)

---

## 🐍 Generator Expressions

Use `()` instead of `[]` to build **lazy** generators:

```python
(x * x for x in range(10))  # returns a generator object
```

Useful for large data or streaming.

---

## 🧪 Examples

```python
# All odd numbers from 1 to 20
odds = [x for x in range(1, 21) if x % 2 == 1]

# Cartesian product
cartesian = [(x, y) for x in 'abc' for y in '123']

# Strip and lowercase a list of strings
processed = [s.strip().lower() for s in strings]
```

---

## 🧼 Style Tips

- Keep comprehensions **single-purpose** and **simple**.
- Avoid deeply nested comprehensions—use helper functions.
- Add comments if the expression is non-obvious.

---

## ✅ Summary

| Feature              | Supported |
|----------------------|-----------|
| Basic list creation  | ✅        |
| Filtering (`if`)     | ✅        |
| Nested loops         | ✅        |
| Conditional expr     | ✅        |
| Dict/Set variants    | ✅        |
| Scope isolation (Py3)| ✅        |

Use list comprehensions to write concise, performant, and expressive Python—**but favor clarity over cleverness**.


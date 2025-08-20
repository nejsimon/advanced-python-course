# Sequences, Sets, and Dicts

Python includes powerful, built-in collection types that enable efficient storage, access, mutation, and iteration over data. These include sequences (like lists and tuples), sets, and maps (dictionaries).

---

## 1. Sequences

### Types

* `list`: Mutable ordered sequence
* `tuple`: Immutable ordered sequence
* `range`: Immutable sequence of numbers

### Common Operations

```python
s = [1, 2, 3]
s.append(4)
s[0] = 10
len(s), s[1:], s[::-1]
```

### Shared Protocols

* Indexing: `s[0]`
* Slicing: `s[1:3]`
* Iteration: `for x in s:`
* Membership: `x in s`
* Length: `len(s)`

### Tuple Packing/Unpacking

```python
x, y = (1, 2)
a, *rest = [1, 2, 3, 4]
```

---

## 2. Lists

* Dynamic arrays, support heterogeneous types
* Methods:

  ```python
  .append(), .extend(), .insert(), .remove(), .pop(), .sort(), .reverse()
  ```
* Sorting with key:

  ```python
  sorted(data, key=lambda x: x[1])
  ```

---

## 3. Tuples

* Immutable, hashable if all elements are hashable
* Used as keys in dicts, elements of sets
* Can simulate fixed-size records
* Named tuples via `collections.namedtuple`

---

## 4. Range Objects

* Memory-efficient integer sequences

```python
range(5)            # 0..4
range(2, 10, 2)     # 2, 4, 6, 8
```

* Supports iteration, slicing

---

## 5. Sets

* Unordered, unique elements
* Mutable (`set`), immutable (`frozenset`)

```python
s = {1, 2, 3}
s.add(4); s.remove(1)
```

### Set Operations

| Operation      | Operator | Method                    |
| -------------- | -------- | ------------------------- |
| Union          | `|`      | `.union()`                |
| Intersection   | `&`      | `.intersection()`         |
| Difference     | `-`      | `.difference()`           |
| Symmetric Diff | `^`      | `.symmetric_difference()` |

---

## 6. Dictionaries (Maps)

* Key-value pairs, fast lookup

```python
d = {"a": 1, "b": 2}
d["c"] = 3
```

### Dict Methods

```python
.keys(), .values(), .items(), .get(), .pop(), .update(), .setdefault()
```

### Dict Comprehensions

```python
squares = {x: x*x for x in range(5)}
```

---

## 7. Advanced Features

### `collections` Enhancements

* `defaultdict`
* `OrderedDict` (no longer needed in 3.7+)
* `Counter` for tallying elements

### Immutable Structures

* `tuple`, `frozenset`
* Use for dictionary keys, set elements

---

## 8. Identity, Equality, Membership

* `==` checks value equality
* `is` checks identity
* Mutable objects like lists/sets are not hashable

---

## 9. Performance and Pitfalls

* Use `set` for fast membership tests
* Dict key lookup is amortized O(1)
* List insertions at the front are O(n)
* Don’t rely on order of sets
* Copy with `.copy()` or slicing (`[:]`), not `=`

---

## 10. Best Practices

* Prefer tuples for fixed-size, immutable data
* Prefer sets for unique membership
* Use `dict.get()` or `defaultdict` to avoid `KeyError`
* Use comprehensions for concise transformations

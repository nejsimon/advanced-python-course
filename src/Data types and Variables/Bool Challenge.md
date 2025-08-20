# The `bool` Type in Python: Coding Challenges

These exercises help reinforce understanding of Python's `bool` type, its interaction with other types, and its use in control flow and evaluation.

---

## Challenge 1: Falsy Filter

**Objective:**
Write a function that removes all falsy values from a list.

```python
values = [0, 1, '', 'text', [], [1], None]
```

---

## Challenge 2: Short-Circuit Behavior

**Objective:**
Write two expressions that:

* Return the second value only if the first is truthy
* Return the second value only if the first is falsy

---

## Challenge 3: Custom Boolean Class

**Objective:**
Create a class whose instances are falsy if the internal count is zero.

```python
class Counter:
    ...
```

* Test in an `if` statement

---

## Challenge 4: Count Boolean Truths

**Objective:**
Given a list of booleans, count how many are `True`.

```python
votes = [True, False, True, True, False]
```

---

## Challenge 5: Coerce to Bool

**Objective:**
Write a function that takes any input and returns either `"truthy"` or `"falsy"` depending on how Python sees it.

---

## Challenge 6: Boolean Identity vs Equality

**Objective:**
Evaluate the difference between identity and equality:


---

## Challenge 7: Boolean Evaluation of Objects

**Objective:**
Create a class with only `__len__` that returns 0. Confirm that it's falsy.

```python
class Empty:
    ...
```

---

## Challenge 8: Validate Input

**Objective:**
Write a function that accepts user input and prints whether it's considered truthy or falsy.

* Use `input("Enter something: ")` to get user input

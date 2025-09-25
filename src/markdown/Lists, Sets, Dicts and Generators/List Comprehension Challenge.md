# Python List Comprehension: Coding Challenges

These challenges explore list comprehension capabilities in Python, including conditionals, nested comprehensions, generator equivalents, scope behavior, performance considerations, and more.

---

## Challenge 1: Basic List Transformation

**Objective**: Convert a list of strings to lowercase using a list comprehension.

```python
words = ["Hello", "WORLD", "Python"]
# Result: ['hello', 'world', 'python']
```

---

## Challenge 2: Conditional Filtering

**Objective**: Create a list of squares for even numbers between 1 and 20.

```python
# Result: [4, 16, 36, ..., 400]
```

---

## Challenge 3: Matrix Transpose

**Objective**: Transpose a 3x3 matrix using nested list comprehensions.

```python
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Result: [[1,4,7],[2,5,8],[3,6,9]]
```

---

## Challenge 4: Prime Numbers

**Objective**: Generate all prime numbers under 100 using list comprehensions and a helper function.

```python
def is_prime(n):
    ...

primes = [x for x in range(2, 100) if is_prime(x)]
```

---

## Challenge 5: Flatten Nested List

**Objective**: Flatten a list of lists with list comprehension.

```python
nested = [[1, 2], [3, 4], [5]]
# Result: [1, 2, 3, 4, 5]
```

---

## Challenge 6: Cartesian Product

**Objective**: Generate all pairs (x, y) where x in \[1,2,3], y in \["a","b"]

```python
# Result: [(1, 'a'), (1, 'b'), ..., (3, 'b')]
```

---

## Challenge 7: Dictionary Comprehension

**Objective**: Build a dictionary mapping words to their lengths using a comprehension.

```python
words = ["apple", "banana", "kiwi"]
# Result: {'apple': 5, 'banana': 6, 'kiwi': 4}
```

---

## Challenge 8: Set Comprehension for Uniqueness

**Objective**: Extract unique lowercase characters from a string.

```python
s = "Mississippi"
# Result: {'m', 'i', 's', 'p'}
```

---

## Challenge 9: List Comprehension vs Generator Expression

**Objective**: Rewrite a list comprehension as a generator and compare memory usage with `sys.getsizeof`.

---

## Challenge 10: Variable Scope Test

**Objective**: Demonstrate that loop variables inside list comprehensions don’t leak into the outer scope (Python 3).

```python
x = "outside"
[x for x in range(5)]
print(x)  # 'outside'
```

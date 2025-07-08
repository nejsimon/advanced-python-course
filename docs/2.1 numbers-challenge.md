# Numbers in Python: Coding Challenges

These exercises cover Python's numeric types, operations, conversion, and precision control.

---

## Challenge 1: Type Identification

**Objective:** Given a mixed list of values, classify each as int, float, or complex.

```python
values = [5, 3.14, 2 + 3j, -7, 1.0, 0j]
```

* Use `isinstance()`

---

## Challenge 2: Safe Division

**Objective:** Implement a function that performs division but catches division-by-zero.

```python
def safe_div(a, b):
    # return float('inf') on ZeroDivisionError
    pass
```

---

## Challenge 3: Use `divmod` and `pow`

**Objective:**

* Calculate quotient and remainder using `divmod()`
* Compute modular exponentiation with `pow(a, b, mod)`

---

## Challenge 4: Floating-Point Comparison

**Objective:**

* Write a function that checks if two floats are approximately equal
* Use `math.isclose()`

```python
def are_equal(a, b):
    pass
```

---

## Challenge 5: Bitwise Manipulation

**Objective:**

* Set, clear, and toggle the 3rd bit of an integer
* Use `|`, `&`, `^`, `~`, `<<`

---

## Challenge 6: Use `fractions` and `decimal`

**Tasks:**

* Add `1/3 + 1/6` using `Fraction`
* Divide `1 / 7` with 50-digit precision using `Decimal`

---

## Challenge 7: Custom Rounding Logic

**Objective:** Round a float to the nearest 0.05

```python
def round_to_nearest_0_05(x):
    pass
```

---

## Challenge 8: Parse Numeric Strings Safely

**Objective:** Convert a list of strings to floats, skipping invalid entries

```python
inputs = ["3.14", "42", "NaN", "hello", "1e-5"]
```

* Use try/except with `float()`

---

## Challenge 9: Complex Number Arithmetic

**Objective:**

* Create two complex numbers
* Compute their product and magnitude
* Use `abs()`, `.real`, and `.imag`

---

## Challenge 10: Infinite Loop Escape with Infinity

**Objective:**

* Implement a loop that stops when a running total exceeds infinity (simulate)
* Use `math.inf`


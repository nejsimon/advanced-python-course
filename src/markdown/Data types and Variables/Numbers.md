# Numbers in Python: Comprehensive Overview

Python provides a flexible and robust set of numeric types, operations, and tools that support both basic arithmetic and advanced mathematical computation. Understanding Python's number system is foundational for performance, precision, and correctness.

---

## 1. Core Numeric Types

### Integer (`int`)

* Arbitrary precision
* Supports binary (`0b`), octal (`0o`), hexadecimal (`0x`)

```python
n = 12345678901234567890123456789
```

### Floating-Point (`float`)

* IEEE-754 double-precision (64-bit)
* Approximate real number representation

```python
f = 3.1415
```

### Complex (`complex`)

* Represented as `real + imagj`

```python
z = 3 + 4j
abs(z)  # magnitude = 5.0
```

---

## 2. Type Conversion

```python
int("42")        # str to int
float("3.14")     # str to float
complex(1, 2)     # real + imag
```

---

## 3. Numeric Operators

| Operation      | Operator | Example     |
| -------------- | -------- | ----------- |
| Addition       | `+`      | `a + b`     |
| Subtraction    | `-`      | `a - b`     |
| Multiplication | `*`      | `a * b`     |
| Division       | `/`      | `a / b`     |
| Floor Division | `//`     | `a // b`    |
| Modulo         | `%`      | `a % b`     |
| Exponentiation | `**`     | `a ** b`    |
| Negation       | `-a`     | Unary minus |

---

## 4. Math Functions

### Built-in Functions

```python
abs(), pow(), round(), divmod(), min(), max(), sum()
```

### `math` Module (Real numbers)

```python
import math
math.sqrt(16)
math.pi
math.log10(1000)
```

### `cmath` Module (Complex numbers)

```python
import cmath
cmath.sqrt(-1)  # 1j
```

---

## 5. Rounding and Precision

* `round(x, n)` rounds to `n` decimal places
* `decimal.Decimal` provides arbitrary-precision fixed-point arithmetic

```python
from decimal import Decimal, getcontext
getcontext().prec = 50
Decimal("1") / Decimal("7")
```

---

## 6. Fractions

Exact rational arithmetic:

```python
from fractions import Fraction
Fraction(1, 3) + Fraction(1, 6)  # -> Fraction(1, 2)
```

---

## 7. Bitwise Operations (on `int` only)

| Operation | Symbol      | Example  |
| --------- | ----------- | -------- |
| AND       | `&`         | `a & b`  |
| OR        | `\|`        | `a \| b` |
| XOR       | `^`         | `a ^ b`  |
| NOT       | `~`         | `~a`     |
| Shift L/R | `<<` / `>>` | `a << 2` |

---

## 8. Special Constants

```python
math.inf       # Positive infinity
math.nan       # Not a Number
float("inf")   # Also valid
```

NaN is not equal to anything, including itself:

```python
x = float("nan")
x == x  # False
```

---

## 9. Performance Tips

* Use `math.fsum()` for numerically stable summation
* Avoid floating-point equality checks — use `math.isclose()`
* For heavy math, prefer NumPy or `numba`

---

## 10. Best Practices

* Use `decimal` or `fractions` when precision matters (e.g. currency)
* Be aware of float rounding errors
* Prefer `divmod()` for division + remainder
* Never compare floats directly with `==`


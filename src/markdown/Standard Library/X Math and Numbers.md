# Standard Library – Math & Numbers

Python’s standard library includes a wide range of modules for mathematical operations, numerical computing, and working with specialized numeric types. While Python’s built-in arithmetic is sufficient for many cases, these modules provide additional power, precision, and domain-specific functionality.

---

## 1. `math` – Mathematical Functions
- Provides access to common mathematical functions.
- Works with floats (`int` is auto-converted to float).
- Includes:
  - Trigonometry: `sin`, `cos`, `tan`, `atan2`.
  - Exponentials & logarithms: `exp`, `log`, `log10`.
  - Constants: `pi`, `e`, `tau`, `inf`, `nan`.
  - Rounding: `ceil`, `floor`, `trunc`, `fmod`.

**Example**
```python
import math

print(math.sqrt(16))        # 4.0
print(math.pi * (3 ** 2))   # Area of circle
print(math.log(100, 10))    # 2.0
```

## 2. cmath – Complex Numbers
Like math but for complex numbers (complex type).

Supports:
cmath.sqrt(-1) → (0+1j)
Trigonometric and hyperbolic functions.
Polar/cartesian conversions: phase, polar, rect.

**Example**

```python
import cmath

z = cmath.sqrt(-1)
print(z)                     # 1j
print(cmath.phase(z))        # π/2
3. decimal – Fixed-Point and Arbitrary Precision
Provides decimal floating-point arithmetic with user-defined precision.

Avoids issues with binary floating-point rounding.

Context-sensitive:

Precision: decimal.getcontext().prec

Rounding modes: ROUND_HALF_UP, etc.

Slower than float, but precise.

📌 Example

```python
from decimal import Decimal, getcontext

getcontext().prec = 4
print(Decimal(1) / Decimal(7))   # 0.1429
4. fractions – Rational Numbers
Represents numbers as numerator/denominator (Fraction).

Exact representation of rational values.

Interoperates with int, float, and Decimal.

📌 Example

```python
from fractions import Fraction

f = Fraction(3, 4) + Fraction(5, 6)
print(f)          # 19/12
print(float(f))   # 1.583...
5. random – Pseudo-Random Numbers
Implements Mersenne Twister PRNG (deterministic).

Functions:

random.random() → float in [0.0, 1.0).

random.randint(a, b) → int in [a, b].

random.choice(seq), random.shuffle(seq).

random.seed() for reproducibility.

For cryptographic randomness → use secrets.

📌 Example

```python
import random

random.seed(42)
print(random.randint(1, 6))   # Dice roll
6. statistics – Descriptive Statistics
Functions for statistical analysis.

Mean, median, mode, variance, stdev.

Works with any iterable of numbers.

📌 Example

```python
import statistics

data = [2, 4, 4, 4, 5, 5, 7, 9]
print(statistics.mean(data))     # 5
print(statistics.stdev(data))    # 2.138...
7. numbers – Abstract Base Classes for Numeric Types
Defines numeric type hierarchy:

numbers.Number → base class

Complex, Real, Rational, Integral

Useful for type checking:

```python
import numbers

print(isinstance(3.14, numbers.Real))   # True
print(isinstance(3+2j, numbers.Real))   # False
8. secrets – Cryptographically Secure Random Numbers
Safer than random for security-sensitive use.

Provides:

secrets.randbelow(n)

secrets.choice(seq)

secrets.token_bytes(), secrets.token_hex(), secrets.token_urlsafe()

📌 Example

```python
import secrets

print(secrets.token_hex(16))   # Random 32-char hex string
9. Other Numeric-Related Modules
array – compact numeric storage (fixed type).

bisect – efficient sorted list insertion.

heapq – heap queue algorithm.

operator – functional operators (operator.add, operator.itemgetter).

functools – higher-order functions for math-like tasks (see separate doc).

Summary
The Math & Numbers cluster of the standard library provides:

Core math (math, cmath).

High-precision and exact types (decimal, fractions).

Randomness (random for general use, secrets for cryptography).

Statistics (statistics).

Type hierarchy (numbers).
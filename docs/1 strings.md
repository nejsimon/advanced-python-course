# Strings

Strings are one of Python’s most fundamental and flexible data types. Despite their simplicity, they support a rich API, powerful formatting, immutability, and can behave differently based on encoding, memory usage, and internal optimizations.

---

## 1. String Basics

* Immutable sequences of Unicode code points.
* Declared with single (`'`), double (`"`), or triple quotes (`'''` or `"""`).
* Examples:

  ```python
  s1 = 'hello'
  s2 = "world"
  s3 = '''multi\nline'''
  ```

---

## 2. String Immutability

* Strings cannot be modified in-place:

  ```python
  s = "hello"
  s[0] = "H"  # TypeError
  ```
* Operations return new strings.

---

## 3. Common String Methods

| Category        | Methods                                                      |
| --------------- | ------------------------------------------------------------ |
| Case conversion | `.upper()`, `.lower()`, `.title()`, `.capitalize()`          |
| Whitespace      | `.strip()`, `.lstrip()`, `.rstrip()`                         |
| Search/Check    | `.find()`, `.index()`, `.startswith()`, `.endswith()`, `.in` |
| Replace/Split   | `.replace()`, `.split()`, `.join()`                          |
| Validation      | `.isalnum()`, `.isdigit()`, `.isidentifier()`                |

---

## 4. String Formatting

### f-strings (Python 3.6+)

```python
name = "Alice"
print(f"Hello {name}")
```

### `str.format()`

```python
"{0} scored {1:.2f}".format("Alice", 93.456)
```

### Old-style `%` formatting (legacy)

```python
"%s scored %.2f" % ("Alice", 93.456)
```

### Format Spec Mini-Language

```python
f"{42:08d}"   # zero-padded int -> '00000042'
f"{3.1415:.2f}" # float to 2 decimals -> '3.14'
```

---

## 5. Escape Sequences & Raw Strings

* `\n`, `\t`, `\u1234`, `\\`
* Raw strings: prefix with `r` to disable escape handling

  ```python
  path = r"C:\\Users\\Name"
  ```

---

## 6. Encoding and Unicode

* All strings are Unicode in Python 3.
* Encoding/decoding:

  ```python
  b = "text".encode("utf-8")
  s = b.decode("utf-8")
  ```
* Common encodings: `utf-8`, `utf-16`, `ascii`, `latin-1`

---

## 7. Multiline and Indented Strings

```python
s = """
    line 1
    line 2
    """
```

Use `textwrap.dedent()` to normalize:

```python
from textwrap import dedent
s = dedent(s)
```

---

## 8. Interning and Performance

* Python interns short strings (e.g. identifiers, literals).
* Use `sys.intern()` for deduplication in large datasets.
* `is` can be used to test identity of interned strings:

  ```python
  a = sys.intern("hello")
  b = sys.intern("hello")
  assert a is b
  ```

---

## 9. Pattern Matching (Structural)

```python
match s:
    case "yes":
        print("Affirmative")
    case "no":
        print("Negative")
```

---

## 10. Quirks & Edge Cases

* Strings are iterable:

  ```python
  for char in "abc": ...
  ```
* Strings are truthy unless empty: `bool("") == False`
* `join()` is faster than repeated concatenation
* Slicing returns new string objects

---

## 11. Best Practices

* Prefer f-strings for formatting
* Always handle encoding/decoding explicitly with external data
* Avoid using `eval()` on string inputs
* Use `str.casefold()` for case-insensitive comparison

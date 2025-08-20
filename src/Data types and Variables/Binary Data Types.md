# Binary Data Types in Python: Comprehensive Overview

Python supports powerful binary data manipulation tools for handling raw bytes, structured binary formats, encoding/decoding, and low-level I/O. These types are foundational in systems programming, networking, and file parsing.

---

## 1. Core Binary Types

### `bytes`

* Immutable sequence of bytes
* Commonly used for binary data, file I/O, encoding

```python
b = b"hello"
b[0]  # 104
```

### `bytearray`

* Mutable variant of `bytes`

```python
ba = bytearray(b"hello")
ba[0] = 72
```

### `memoryview`

* Zero-copy view of binary data

```python
m = memoryview(b"abc")
m[0]  # 97
```

---

## 2. Encoding and Decoding Strings

```python
s = "hello"
b = s.encode("utf-8")
s2 = b.decode("utf-8")
```

* Common encodings: `utf-8`, `ascii`, `latin-1`, `utf-16`

---

## 3. Hex and Base64 Encoding

### Hexadecimal

```python
b = b"abc"
b.hex()        # '616263'
bytes.fromhex("616263")
```

### Base64

```python
import base64
base64.b64encode(b"hello")
base64.b64decode(b"aGVsbG8=")
```

---

## 4. Struct Packing/Unpacking

Use `struct` module to convert between Python values and C structs (fixed-size binary formats).

```python
import struct
packed = struct.pack('i f', 42, 3.14)
value = struct.unpack('i f', packed)
```

* Format characters: `i` (int), `f` (float), `h` (short), `s` (char\[]), etc.
* Endianness: `>` = big-endian, `<` = little-endian

---

## 5. Bitwise Operations

Binary types can be combined with integers for bitwise logic:

```python
a = 0b1010
b = 0b1100
c = a & b  # 0b1000
```

---

## 6. Binary File I/O

```python
with open("file.bin", "rb") as f:
    data = f.read()

with open("file.bin", "wb") as f:
    f.write(b"hello")
```

---

## 7. `memoryview` and Buffer Protocol

* `memoryview` provides efficient slices or views without copying.
* Can be used with `bytearray`, `array.array`, NumPy, etc.

```python
ba = bytearray(b"abcdef")
mv = memoryview(ba)
mv[1:3] = b"XY"
```

---

## 8. Quirks and Edge Cases

* `bytes` and `bytearray` are indexed by integers
* Slicing returns same type
* Many string methods also exist on `bytes`, but require `b"..."` literals
* Bit-level manipulations often require `int.from_bytes()` and `to_bytes()`

---

## 9. Best Practices

* Use `bytes` for immutability and file/network I/O
* Use `bytearray` for efficient binary mutation
* Always encode/decode explicitly with correct encoding
* Use `struct` when working with binary file formats or network protocols
* Use `memoryview` for zero-copy slices of large binary blobs

# Binary Data Types in Python: Coding Challenges

These challenges reinforce working with `bytes`, `bytearray`, `memoryview`, file I/O, encoding, and the `struct` module.

---

## Challenge 1: Encode and Decode

**Objective:**
Convert a string into bytes using UTF-8 and back.

```python
text = "Python 🐍"
```

* Encode to bytes
* Decode back to a string

---

## Challenge 2: Modify a Bytearray

**Objective:**

* Create a `bytearray` from `b"hello"`
* Change the first character to uppercase `'H'`
* Print the modified bytearray as a string

---

## Challenge 3: Hex Encoding

**Objective:**
Convert `b"binary data"` into a hexadecimal string and back.

* Use `.hex()` and `bytes.fromhex()`

---

## Challenge 4: Base64 Roundtrip

**Objective:**

* Encode the string `"secret message"` into base64
* Decode it back to the original string

---

## Challenge 5: Pack and Unpack Struct

**Objective:**
Use `struct` to pack the following values:

```python
id = 42
score = 3.14
```

* Use format `'<if'`
* Unpack and print the result

---

## Challenge 6: Write and Read Binary File

**Objective:**

* Write `b"binary\x00file"` to a file
* Read it back and confirm equality

---

## Challenge 7: Slice with Memoryview

**Objective:**

* Create a `bytearray(b"abcdef")`
* Use `memoryview` to change slice \[1:4] to `XYZ`

---

## Challenge 8: Count Byte Frequency

**Objective:**
Count how many times each byte value appears in a binary string.

```python
data = b"abracadabra"
```

* Output: `{97: 5, 98: 2, ...}`

---

## Challenge 9: Convert Integer to Bytes

**Objective:**
Convert the number `1025` to 2-byte little-endian bytes and back.

* Use `.to_bytes()` and `int.from_bytes()`

---

## Challenge 10: Validate UTF-8 Bytes

**Objective:**
Write a function that:

* Takes a `bytes` object
* Returns `True` if it is valid UTF-8, `False` otherwise
* Use a `try/except` block


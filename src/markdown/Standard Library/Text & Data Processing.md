# Advanced Python Course: Standard Library — Text & Data Processing

The Python Standard Library provides a rich set of modules for working with text, encodings, and structured data. These are foundational tools for almost all Python projects.

---

## 1. `string`

* Provides constants like `ascii_letters`, `digits`, `punctuation`.
* Template-based string substitution via `string.Template`.
* Helper functions for common string manipulations.

**Quirks:**

* Template strings are safer than f-strings for untrusted input (they don’t allow arbitrary expression evaluation).

```python
import string

values = {"name": "Alice", "lang": "Python"}
t = string.Template("Hello $name, welcome to $lang!")
print(t.substitute(values))
```

---

## 2. `textwrap`

* Formatting multi-line strings (wrapping, filling, indenting).
* Useful for CLI tools and formatting text blocks.

```python
import textwrap

long_text = """Python provides batteries-included functionality for text processing."""
print(textwrap.fill(long_text, width=20))
```

---

## 3. `re` (Regular Expressions)

* Full-featured regex support.
* Methods: `match`, `search`, `findall`, `sub`.
* Flags for case insensitivity, multiline, Unicode-aware matching.

**Gotchas:**

* Use raw strings (`r"pattern"`) to avoid conflicts with Python escapes.
* Prefer `re.compile` for performance on repeated matches.

```python
import re
pattern = re.compile(r"\bPython\b")
print(bool(pattern.search("I love Python")))
```

---

## 4. `difflib`

* Finding differences between sequences (text, lists).
* `ndiff`, `unified_diff` for producing human-readable diffs.
* `SequenceMatcher` for similarity ratios.

```python
import difflib

a = "Python 3.10"
b = "Python 3.11"
for line in difflib.unified_diff(a.split(), b.split(), lineterm=""):
    print(line)
```

---

## 5. `unicodedata`

* Access Unicode character metadata.
* Functions: `name()`, `lookup()`, `normalize()`.
* Important for Unicode normalization (NFC vs. NFD).

```python
import unicodedata

s = "café"
print(unicodedata.normalize("NFC", s))
print(unicodedata.name("é"))
```

---

## 6. `codecs`

* Legacy interface for encoding/decoding.
* Often replaced by `str.encode()` and `bytes.decode()`.
* Still useful for stream-based encoding wrappers.

```python
import codecs

with codecs.open("example.txt", "w", encoding="utf-8") as f:
    f.write("hello world")
```

---

## 7. `base64`

* Encode/decode binary data in Base16/32/64.
* Used for data transfer in text-based protocols.

```python
import base64

msg = b"python"
encoded = base64.b64encode(msg)
print(encoded)
print(base64.b64decode(encoded))
```

---

## 8. `hashlib` & `hmac`

* Cryptographic hashes: MD5, SHA1, SHA256, SHA512, etc.
* HMAC: secure keyed message authentication.

```python
import hashlib, hmac

msg = b"hello"
hash_val = hashlib.sha256(msg).hexdigest()
print(hash_val)

key = b"secret"
h = hmac.new(key, msg, hashlib.sha256)
print(h.hexdigest())
```

---

## 9. `json`

* Encoding and decoding JSON.
* Functions: `json.loads`, `json.dumps`, `json.load`, `json.dump`.
* Supports custom encoders and decoders.

```python
import json

data = {"name": "Alice", "age": 30}
text = json.dumps(data)
print(text)
print(json.loads(text))
```

---

## 10. `csv`

* Reading and writing CSV files.
* Reader/writer objects handle quoting, delimiters, etc.

```python
import csv

with open("people.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["Alice", 30])
```

---

## 11. `configparser`

* Parsing INI-style config files.
* Sections, keys, and values with type casting.

```python
import configparser

config = configparser.ConfigParser()
config.read_dict({"settings": {"debug": "true"}})
print(config["settings"]["debug"])
```

---

# Summary

This cluster covers **text, encodings, and structured data** tools:

* Low-level text handling (`string`, `textwrap`, `re`).
* Data diffs (`difflib`), Unicode (`unicodedata`), codecs, encodings.
* Structured formats (`json`, `csv`, `configparser`).
* Security (`hashlib`, `hmac`, `base64`).


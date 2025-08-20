# Python Standard Library — File Formats & Serialization

Python’s standard library includes powerful modules for reading, writing, and serializing data in different formats. These are essential for interoperability, configuration, persistence, and communication between programs.

---

## 1. JSON (`json`)
- Supports JavaScript Object Notation (JSON).
- Provides `dump`, `dumps`, `load`, `loads`.
- Maps Python types to JSON types:
  - `dict` → object
  - `list`, `tuple` → array
  - `str` → string
  - `int`, `float` → number
  - `True`/`False` → true/false
  - `None` → null
- Custom serialization with `default` parameter.

```python
import json

data = {"user": "alice", "active": True}
json_str = json.dumps(data)
print(json_str)  # {"user": "alice", "active": true}
```

## 2. CSV (csv)
* Reads and writes comma-separated values and similar tabular formats.
* Handles quoting, delimiters, dialects.
* Provides csv.reader, csv.writer, csv.DictReader, csv.DictWriter.

```python
import csv

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["Alice", 30])

with open("data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
```

## 3. Pickle (pickle)
* Serializes and deserializes arbitrary Python objects.
* Faster than JSON but not secure (never unpickle untrusted input).
* Provides dump, dumps, load, loads.

```python
import pickle

obj = {"x": [1, 2, 3], "y": (4, 5)}
serialized = pickle.dumps(obj)
restored = pickle.loads(serialized)
print(restored)
```

## 4. ConfigParser (configparser)
* Reads and writes .ini configuration files.
* Provides hierarchical sections and key/value pairs.
* Supports defaults and interpolation.

```python
from configparser import ConfigParser

config = ConfigParser()
config.read_dict({"general": {"debug": "true"}})

with open("settings.ini", "w") as f:
    config.write(f)

print(config["general"]["debug"])  # "true"
```

## 5. Shelve (shelve)
* Persistent storage of Python objects using a dict-like interface.
* Backed by pickle and a database (e.g., dbm).
* Useful for quick-and-dirty persistence.

```python
import shelve

with shelve.open("storage.db") as db:
    db["user"] = {"name": "Alice", "age": 30}

with shelve.open("storage.db") as db:
    print(db["user"])  # {"name": "Alice", "age": 30}
```

## 6. XML (xml.etree.ElementTree)
* Parses and creates XML trees.
* Provides DOM-like tree traversal and modification.
* Limited but sufficient for many XML tasks.

```python
import xml.etree.ElementTree as ET

root = ET.Element("root")
child = ET.SubElement(root, "item", attrib={"id": "1"})
child.text = "Hello XML"
tree = ET.ElementTree(root)
tree.write("output.xml")
```

## Advanced Notes
* marshal is a lower-level serializer (used internally for .pyc files) — not recommended for persistence.
* plistlib supports Apple .plist property lists.
* tomllib (Python 3.11+) reads TOML configuration files.

## When to Use What
* JSON → interoperable, human-readable, widely used in APIs.
* CSV → tabular data exchange with spreadsheets/databases.
* Pickle → Python-only object persistence (careful with security).
* ConfigParser / TOML / INI → configuration management.
* Shelve → persistent key-value storage without a database.
* XML → interoperating with legacy systems or standards.
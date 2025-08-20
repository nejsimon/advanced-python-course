# Python Standard Library: File and OS Interfaces

The Python Standard Library provides a wide range of modules for interacting with the file system, operating system, and general file operations. This cluster includes modules like `os`, `pathlib`, `shutil`, `glob`, `tempfile`, `zipfile`, `tarfile`, `io`, and `fileinput`.

---

## 1. `os` — Operating System Interfaces
The `os` module provides a way to use operating system–dependent functionality.

### Key Features
- Environment variables: `os.environ`, `os.getenv()`
- Process management: `os.fork()`, `os.exec*()`, `os.system()`
- File and directory operations: `os.mkdir()`, `os.remove()`, `os.rename()`
- Path utilities (delegated to `os.path`).

```python
import os

print(os.getcwd())          # Current working directory
os.makedirs("example_dir", exist_ok=True)
print(os.listdir("."))      # List directory contents
```

# Python Standard Library: File and OS Interfaces

The Python Standard Library provides a wide range of modules for interacting with the file system, operating system, and general file operations. This cluster includes modules like `os`, `pathlib`, `shutil`, `glob`, `tempfile`, `zipfile`, `tarfile`, `io`, and `fileinput`.

---

## 1. `os` — Operating System Interfaces
The `os` module provides a way to use operating system–dependent functionality.

### Key Features
- Environment variables: `os.environ`, `os.getenv()`
- Process management: `os.fork()`, `os.exec*()`, `os.system()`
- File and directory operations: `os.mkdir()`, `os.remove()`, `os.rename()`
- Path utilities (delegated to `os.path`).

```python
import os

print(os.getcwd())          # Current working directory
os.makedirs("example_dir", exist_ok=True)
print(os.listdir("."))      # List directory contents
```

2. pathlib — Object-Oriented Filesystem Paths
Introduced in Python 3.4, pathlib provides a modern, object-oriented way to work with file paths.

```python
from pathlib import Path

p = Path("example.txt")
p.write_text("Hello, World!")
print(p.read_text())
print(p.exists())
```

Key advantages over os.path:

Cleaner API

Supports different path implementations (PosixPath, WindowsPath)

Operator overloading for joining paths: Path("a") / "b"

3. shutil — High-Level File Operations
The shutil module helps with high-level operations such as copying, moving, and removing directories.

```python
import shutil

shutil.copy("example.txt", "example_copy.txt")
shutil.move("example_copy.txt", "backup/example_copy.txt")
```

Also supports:

Archiving (shutil.make_archive(), shutil.unpack_archive())

Disk usage (shutil.disk_usage())

4. glob — Filename Pattern Matching
The glob module finds files using Unix shell–style wildcards.

```
import glob

print(glob.glob("*.txt"))   # Matches all text files in current directory
```

5. tempfile — Temporary Files and Directories
The tempfile module provides a secure way to create temporary files and directories.

```python
import tempfile

with tempfile.NamedTemporaryFile(delete=False) as tmp:
    tmp.write(b"temporary data")
    print(tmp.name)
```

6. zipfile and tarfile — Working with Archives
Python can read and write common archive formats without external tools.

Zip
```python
import zipfile

with zipfile.ZipFile("archive.zip", "w") as zf:
    zf.write("example.txt")

with zipfile.ZipFile("archive.zip", "r") as zf:
    print(zf.namelist())
```

Tar
```python
import tarfile

with tarfile.open("archive.tar.gz", "w:gz") as tf:
    tf.add("example.txt")

with tarfile.open("archive.tar.gz", "r:gz") as tf:
    print(tf.getnames())
```

7. io — Core Tools for Streams
The io module provides Python’s main interface for handling file streams.

io.StringIO for text-based in-memory streams

io.BytesIO for binary in-memory streams

```python
import io

buffer = io.StringIO()
buffer.write("hello")
buffer.seek(0)
print(buffer.read())   # hello
```

8. fileinput — Iterate Over Lines from Multiple Input Streams
Useful for command-line tools that process multiple files as a stream.

```python
import fileinput

for line in fileinput.input(files=("example.txt", "another.txt")):
    print(line, end="")
```

Advanced Use Cases & Quirks
Use pathlib instead of os.path for more readable and cross-platform path manipulation.

tempfile defaults to secure file creation, unlike manual open() with guessed names.

shutil.rmtree() should be used cautiously—it deletes entire directory trees.

The zipfile module doesn’t compress directories by default; you must add each file.

Summary
These modules form the backbone of file and OS interaction in Python:

os: low-level OS interface

pathlib: modern path handling

shutil: high-level file operations

glob: pattern-based file search

tempfile: secure temporary files

zipfile/tarfile: archive handling

io: core stream abstraction

fileinput: line iteration across files
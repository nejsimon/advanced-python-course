# Python Module System

Python’s module system enables **modular programming**, **namespace isolation**, and **code reuse**. It supports both script-style and fully-packaged application structures.

---

## 🧱 What Is a Module?

A **module** is any `.py` file that can be imported.

```python
# utils.py
def greet(name):
    return f"Hello, {name}"
```

```python
# main.py
import utils
utils.greet("Alice")
```

### Module Object
When a module is imported:
- A module object is created
- The module’s code is executed **once**
- The result is cached in `sys.modules`

---

## 📦 What Is a Package?

A **package** is a directory containing a `__init__.py` file (can be empty).

```
myproject/
│
├── main.py
└── utils/
    ├── __init__.py
    └── math.py
```

You can now import:

```python
from utils import math
```

---

## 📂 Module Search Path

When importing `foo`, Python searches:

1. Built-ins
2. Current working directory
3. `sys.path` entries:
    - `PYTHONPATH` env var
    - Site-packages
    - `.pth` files

```python
import sys
print(sys.path)
```

---

## 📥 Import Forms

```python
import math
from math import sqrt
from math import sqrt as square_root
```

### Import entire module

```python
import foo.bar.baz
```

### Import names into current namespace

```python
from foo.bar import baz
```

> Use `import ...` over `from ... import *` for clarity and safety.

---

## ⚖️ Absolute vs Relative Imports

Inside packages:

```python
from . import sibling_module           # relative
from ..subpackage import other_module  # relative
import mypkg.sibling_module            # absolute
```

Rules:
- Relative imports only work **inside packages**
- Don't use relative imports in scripts run with `python myscript.py`

---

## 🧪 `__init__.py`: Package Initialization

Executed when the package is imported.

- Can define public API
- Can run initialization logic
- Can import submodules

```python
# utils/__init__.py
from .math import add, subtract
```

Now you can:

```python
from utils import add
```

---

## 🧪 `__main__.py`: Entry Point for Packages

When a package is run with:

```bash
python -m mypkg
```

Python executes `mypkg/__main__.py`.

Useful for CLI tools, apps, etc.

---

## 📜 The `__all__` Variable

Defines what gets imported on `from module import *`.

```python
__all__ = ['foo', 'bar']
```

Only affects `import *` behavior — does **not** restrict access.

---

## 🔁 Module Re-Execution

Modules are imported **once per session** and cached in `sys.modules`.

To reload:

```python
import importlib
importlib.reload(my_module)
```

---

## 🧩 Import System Internals

Steps Python takes to import a module:

1. Check `sys.modules` (cache)
2. Use `sys.meta_path` to find a loader
3. Use the loader to load the module
4. Add it to `sys.modules`
5. Execute top-level code

Can customize import behavior by writing custom **import hooks** (advanced).

---

## 🧪 Namespace Packages (PEP 420)

Packages **without** `__init__.py` are namespace packages.

```python
mypkg/
  plugin_a/
  plugin_b/
```

If both directories are on `sys.path`, they form a single logical package.

```python
import mypkg.plugin_a
```

---

## 🧠 Module Identity and Side Effects

```python
# mymod.py
print("loaded")

# main.py
import mymod      # prints once
import mymod      # no output (cached)
```

> Be aware of import-time side effects — they can cause subtle bugs or performance issues.

---

## 🧱 Using `if __name__ == "__main__"` Idiom

```python
def main():
    ...

if __name__ == "__main__":
    main()
```

- `__name__` is `"__main__"` when script is run directly
- `"module_name"` when imported

---

## 🧵 Thread Safety of Imports

- Module imports are thread-safe **after Python 3.3**
- During cyclic imports, `sys.modules[module]` is populated with a **partially initialized module**
- Avoid writing top-level code with side effects

---

## ⚠️ Common Pitfalls

### 1. Module name shadowing

Avoid naming files like built-in modules:

```python
# math.py
import math  # may import self!
```

### 2. Mixing script and package behavior

Don’t run package-internal modules like scripts:

```bash
python mypkg/utils/math.py  # breaks relative imports
```

Use:

```bash
python -m mypkg.utils.math
```

### 3. Using relative imports in standalone scripts

Relative imports only work in packages, not standalone `.py` files.

---

## ✅ Best Practices

- Use **absolute imports** within packages
- Keep **side effects** out of top-level module code
- Organize large projects as **packages**
- Use `__all__` to define clean public APIs
- Avoid wildcard imports (`from module import *`)
- Use `importlib.reload()` for dynamic reloading

---

## 🧰 Useful Modules

| Module         | Purpose                         |
|----------------|----------------------------------|
| `importlib`    | Dynamic importing and reloading |
| `sys`          | Access to `sys.path`, `sys.modules` |
| `pkgutil`      | Package resource introspection  |
| `pkg_resources`| Package metadata access (setuptools) |

---

## 📚 Further Reading

- [Python import system (docs)](https://docs.python.org/3/reference/import.html)
- [PEP 8 – Import style guide](https://peps.python.org/pep-0008/#imports)
- [PEP 328 – Absolute and Relative Imports](https://peps.python.org/pep-0328/)
- [PEP 420 – Implicit Namespace Packages](https://peps.python.org/pep-0420/)
- Real Python: [Python Imports Explained](https://realpython.com/python-import/)


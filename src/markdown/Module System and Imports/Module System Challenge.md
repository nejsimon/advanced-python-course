# Python Module System: Coding Challenges

These challenges explore Python’s module system, including imports, packages, relative imports, `__init__.py`, `__main__`, and dynamic importing.

---

## Challenge 1: Create and Import a Module

**Objective**: Create a module `math_utils.py` that exports an `add(a, b)` function and import it from another file.

```python
# math_utils.py
def add(a, b):
    return a + b
```

```python
# main.py
from math_utils import add
assert add(2, 3) == 5
```

---

## Challenge 2: Use `__name__ == '__main__'`

**Objective**: Add logic to a module that only runs when executed directly.

```python
# cli.py
def main():
    print("Running as script")

if __name__ == '__main__':
    main()
```

---

## Challenge 3: Import from a Package

**Objective**: Create a package `utils/` with an `__init__.py` and a submodule `math_tools.py`.

```
utils/
├── __init__.py
└── math_tools.py
```

```python
# utils/math_tools.py
def square(x):
    return x * x
```

```python
# test.py
from utils.math_tools import square
assert square(4) == 16
```

---

## Challenge 4: Relative Imports

**Objective**: Use relative imports to import from sibling modules inside a package.

```
my_package/
├── __init__.py
├── core.py
└── helper.py
```

```python
# core.py
from .helper import greet

def run():
    print(greet("world"))
```

```python
# helper.py
def greet(name):
    return f"Hello, {name}!"
```

---

## Challenge 5: Dynamic Import with `importlib`

**Objective**: Dynamically import a module and call a function from it.

```python
import importlib

math_utils = importlib.import_module("math")
assert math_utils.sqrt(9) == 3.0
```

---

## Challenge 6: Module Reimport with `importlib.reload`

**Objective**: Reload a module to reflect runtime changes (in a REPL or script).

```python
import importlib, my_module

# Change something in `my_module.py` externally
importlib.reload(my_module)
```

---

## Challenge 7: Use `__all__` for Export Control

**Objective**: Define `__all__` in a module to limit what gets imported with `from module import *`.

```python
# my_mod.py
__all__ = ["foo"]

def foo(): ...
def bar(): ...
```

```python
from my_mod import *
foo()  # OK
bar()  # NameError
```

---

## Challenge 8: Script vs Module Behavior

**Objective**: Observe `__name__` when a file is run vs imported.

```python
# observe.py
print(f"__name__ is {__name__}")
```

```bash
$ python observe.py       # __name__ is __main__
$ python -c 'import observe'  # __name__ is observe
```

---

## Challenge 9: Importing Standard Library Modules

**Objective**: List five useful standard modules and write a small snippet using each.

Examples:

* `math`
* `os`
* `sys`
* `datetime`
* `itertools`

---

## Challenge 10: Custom Import Hooks (Advanced)

**Objective**: Write a custom importer that logs module imports.

```python
import sys

class LoggingFinder:
    def find_spec(self, name, path, target=None):
        print(f"Importing: {name}")
        return None  # Let default importer handle it

sys.meta_path.insert(0, LoggingFinder())

import math  # Logs "Importing: math"
```

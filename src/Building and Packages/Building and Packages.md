# Python Building and Packages

This guide explores Python's packaging and build ecosystem, focusing on the tools, formats, and best practices for creating and distributing Python projects.

---

## 1. Key Concepts

### Module vs Package

* **Module**: A single `.py` file containing Python code.
* **Package**: A directory with an `__init__.py` file (may be implicit in Python 3.3+).

### Distribution Package vs Import Package

* **Import Package**: The Python code you `import`.
* **Distribution Package**: The installable archive (`.whl`, `.tar.gz`) that contains the import package.

---

## 2. Project Structure Example

```text
my_package/
├── my_package/
│   ├── __init__.py
│   ├── core.py
│   └── utils.py
├── tests/
│   └── test_core.py
├── pyproject.toml
└── README.md
```

---

## 3. Build Systems

### `setuptools`

* Classic tool
* Configurable via `setup.py`, `setup.cfg`, or `pyproject.toml`

### `flit`

* Simple builds for pure Python packages

### `poetry`

* Dependency and build management
* Lockfile and virtualenv support

### `hatch`

* Modern build tool with project scaffolding and environment management

---

## 4. `pyproject.toml`

Central file for specifying build system requirements and configuration.

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
```

Common sections:

* `[tool.poetry]` – project metadata
* `[tool.setuptools]` – configuration
* `[tool.hatch]` – build and metadata

---

## 5. Package Formats

### Wheel (.whl)

* Binary distribution format
* Installable via `pip`
* Faster installation

### Source Distribution (.tar.gz)

* Used for building from source

---

## 6. Versioning

### Semantic Versioning

* MAJOR.MINOR.PATCH (e.g., 1.2.3)

### Dynamic Versioning

* Use `setuptools_scm` or `hatchling` to derive versions from VCS tags

---

## 7. Dependencies

### Runtime vs Dev Dependencies

* Runtime: Needed to use the package
* Dev: Needed for testing, linting, building

### Declaring Dependencies

* `pyproject.toml` (e.g., Poetry)
* `requirements.txt`
* `setup.cfg`

---

## 8. Publishing

### Repositories

* [PyPI](https://pypi.org) – the Python Package Index
* TestPyPI – sandbox for testing uploads

### Tools

* `twine`: Upload wheels and source archives
* `poetry publish`
* `hatch publish`

### Metadata Requirements

* Name, version, author, license, classifiers

---

## 9. Namespace Packages

Used to split a logical package across multiple distributions.

```python
# pkg1/__init__.py
__path__ = __import__('pkgutil').extend_path(__path__, __name__)
```

Or use implicit namespace packages (Python 3.3+): omit `__init__.py`

---

## 10. Best Practices

* Prefer `pyproject.toml` over legacy `setup.py`
* Use `poetry` or `hatch` for modern workflows
* Keep a clean project structure
* Use virtual environments
* Pin exact versions for reproducibility
* Include `README.md`, `LICENSE`, and classifiers

---

## 11. Related Tools

| Tool                   | Purpose                       |
| ---------------------- | ----------------------------- |
| `build`                | PEP 517 build frontend        |
| `twine`                | Secure uploading to PyPI      |
| `check-wheel-contents` | Validates wheel metadata      |
| `tox`                  | Multi-environment test runner |


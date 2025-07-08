# Python Testing

Testing in Python is flexible, powerful, and ecosystem-rich. The core testing strategies include:
- Unit testing with `unittest` or `pytest`
- Integration and system testing
- Property-based testing
- Coverage analysis
- Mocking and patching

This guide focuses on `unittest` and `pytest`, the most widely used frameworks.

---

## 📦 Standard Library: `unittest`

Python includes a built-in xUnit-style testing framework.

```python
import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 2, 3)

if __name__ == "__main__":
    unittest.main()
```

### Common Assertions

| Method                 | Description                      |
|------------------------|----------------------------------|
| `assertEqual(a, b)`    | `a == b`                         |
| `assertTrue(x)`        | `bool(x) is True`                |
| `assertIs(a, b)`       | `a is b`                         |
| `assertIn(a, b)`       | `a in b`                         |
| `assertRaises(exc)`    | Context manager for exceptions   |

---

## 🧪 `pytest`: The De Facto Standard

Install via:

```bash
pip install pytest
```

### Basic Test Example

```python
# test_math.py
def add(x, y):
    return x + y

def test_add():
    assert add(2, 3) == 5
```

Then run:

```bash
pytest
```

> `pytest` auto-discovers files named `test_*.py` and functions starting with `test_`.

---

## ⚙️ Test Discovery Rules

| Tool      | Discovery by default                 |
|-----------|--------------------------------------|
| `unittest`| Class-based, named `Test*`           |
| `pytest`  | Files: `test_*.py`, Funcs: `test_*`  |

Use `pytest.ini` or `pyproject.toml` to configure markers, paths, etc.

---

## 🧩 `pytest` Fixtures

Fixtures provide **injected, reusable setup and teardown**.

```python
import pytest

@pytest.fixture
def db():
    conn = connect_to_test_db()
    yield conn
    conn.close()

def test_query(db):
    result = db.query("SELECT 1")
    assert result == 1
```

- Fixtures can be scoped (`function`, `module`, `session`)
- Fixtures can depend on other fixtures

---

## 🧪 Parametrized Tests

```python
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert a + b == expected
```

---

## 🔁 Setup and Teardown

### `unittest`

```python
def setUp(self):
    ...

def tearDown(self):
    ...
```

### `pytest`

Use fixtures or `setup_function`, `teardown_module`, etc.

---

## 🧪 Mocking with `unittest.mock`

### Basic Mock

```python
from unittest.mock import Mock

api = Mock()
api.get_user.return_value = {"name": "Alice"}

assert api.get_user(123)["name"] == "Alice"
```

### Patching

```python
from unittest.mock import patch

@patch("myapp.api.fetch_user")
def test_api(mock_fetch):
    mock_fetch.return_value = {"name": "Bob"}
    ...
```

> Use `patch` as a **decorator**, **context manager**, or **manual start/stop**.

---

## 📈 Test Coverage

```bash
pip install coverage
coverage run -m pytest
coverage report
coverage html
```

> Helps find untested code paths.

---

## 🧪 Property-Based Testing with `hypothesis`

```bash
pip install hypothesis
```

```python
from hypothesis import given
import hypothesis.strategies as st

@given(st.integers(), st.integers())
def test_add_commutative(x, y):
    assert x + y == y + x
```

> Automatically generates test cases to falsify properties.

---

## 🧵 Async Test Support

### `pytest`

```python
import asyncio
import pytest

@pytest.mark.asyncio
async def test_async_func():
    result = await async_add(1, 2)
    assert result == 3
```

Or use the built-in `pytest-asyncio` plugin.

---

## 🧪 Temporary Files and Isolation

### `pytest` provides:

```python
def test_tmp_file(tmp_path):
    file = tmp_path / "data.txt"
    file.write_text("hello")
    assert file.read_text() == "hello"
```

---

## 🧠 Test Structuring Best Practices

```
tests/
├── __init__.py
├── test_core.py
├── test_utils.py
├── fixtures/
│   └── conftest.py
```

Use `conftest.py` to share fixtures across test files.

---

## 🧨 Common Pitfalls

### 1. Test Code Is Not Executed

- File or function doesn’t follow naming convention.
- Forgetting `pytest` discovers `test_*.py` and `test_*` functions only.

### 2. Mocking Wrong Import Path

```python
# In myapp.py
from service import fetch_user

# In test
@patch("myapp.fetch_user")  # ✅ not "service.fetch_user"
```

### 3. Overuse of Fixtures

- Keep fixtures minimal and focused.
- Avoid deeply nested fixtures unless necessary.

---

## ✅ Summary

| Tool             | Use Case                              |
|------------------|----------------------------------------|
| `unittest`       | Built-in, xUnit style                  |
| `pytest`         | Popular, expressive, extensible        |
| `mock`           | Isolate side effects, patching         |
| `coverage`       | Code coverage analysis                 |
| `hypothesis`     | Property-based testing                 |
| `pytest-asyncio` | Async testing                          |

---

## 📚 Further Reading

- [Python `unittest` docs](https://docs.python.org/3/library/unittest.html)
- [pytest documentation](https://docs.pytest.org/en/stable/)
- [unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
- [Coverage.py](https://coverage.readthedocs.io/)
- [Hypothesis](https://hypothesis.readthedocs.io/)
- Real Python: [Python Testing Tutorials](https://realpython.com/tutorials/testing/)


# Python Testing: Coding Challenges

These challenges help you gain proficiency in writing unit tests, integration tests, and using Python’s built-in and third-party testing tools like `unittest`, `pytest`, mocking, fixtures, and parameterized tests.

---

## Challenge 1: Basic Unit Test with `unittest`

**Objective**: Write a test for a simple math function using the built-in `unittest` module.

```python
# calculator.py
def add(a, b):
    return a + b
```

```python
# test_calculator.py
import unittest
from calculator import add

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
```

---

## Challenge 2: Testing Exceptions

**Objective**: Ensure that a function raises an expected exception.

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

```python
import pytest

def test_divide_raises():
    with pytest.raises(ValueError):
        divide(10, 0)
```

---

## Challenge 3: Parameterized Tests with Pytest

**Objective**: Use `@pytest.mark.parametrize` to test multiple inputs and outputs.

```python
import pytest

@pytest.mark.parametrize("a,b,result", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0)
])
def test_add(a, b, result):
    assert add(a, b) == result
```

---

## Challenge 4: Mocking with `unittest.mock`

**Objective**: Mock an external dependency in your test.

```python
from unittest.mock import patch
import requests

def fetch_data(url):
    return requests.get(url).json()

@patch("requests.get")
def test_fetch_data(mock_get):
    mock_get.return_value.json.return_value = {"key": "value"}
    assert fetch_data("http://test") == {"key": "value"}
```

---

## Challenge 5: Temporary File Fixture

**Objective**: Use `tmp_path` fixture in `pytest` to write and read temporary files.

```python
def test_tempfile(tmp_path):
    file = tmp_path / "data.txt"
    file.write_text("hello")
    assert file.read_text() == "hello"
```

---

## Challenge 6: Test Class Setup and Teardown

**Objective**: Use `setup_method` and `teardown_method` to manage test resources.

```python
class TestExample:
    def setup_method(self):
        self.data = [1, 2, 3]

    def teardown_method(self):
        self.data = None

    def test_length(self):
        assert len(self.data) == 3
```

---

## Challenge 7: Coverage Measurement

**Objective**: Use `coverage` tool to measure test coverage.

```bash
$ pip install coverage
$ coverage run -m pytest
$ coverage report -m
```

---

## Challenge 8: Parametrize Fixtures

**Objective**: Use `@pytest.fixture(params=...)` to create parameterized fixtures.

```python
import pytest

@pytest.fixture(params=["a", "b"])
def letter(request):
    return request.param

def test_letter(letter):
    assert letter in ["a", "b"]
```

---

## Challenge 9: Integration Test

**Objective**: Test multiple modules working together.

```python
# math_utils.py
def square(x): return x * x

def add_squares(a, b): return square(a) + square(b)
```

```python
# test_integration.py
from math_utils import add_squares

def test_add_squares():
    assert add_squares(2, 3) == 13
```

---

## Challenge 10: Skip and Expected Failures

**Objective**: Use `pytest.mark.skip` and `pytest.mark.xfail` for incomplete or flaky tests.

```python
import pytest

@pytest.mark.skip(reason="Not yet implemented")
def test_skip():
    assert False

@pytest.mark.xfail(reason="Known bug")
def test_fail():
    assert 1 == 2
```

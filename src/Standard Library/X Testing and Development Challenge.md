Challenge: Testing & Development in Python
1. Unit Testing with unittest

Write a small module calculator.py with functions:

def add(a, b):
    return a + b

def divide(a, b):
    return a / b


Task:

Create a test_calculator.py using unittest.

Test both functions, including edge cases like division by zero.

2. Doctest

Modify the add() function to include a docstring with doctest examples:

def add(a, b):
    """
    Adds two numbers.

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b


Task:

Run the doctest suite (python -m doctest calculator.py).

Add at least one failing test on purpose and fix it.

3. Mocking

Imagine your app fetches data from an API:

import requests

def get_status(url):
    response = requests.get(url)
    return response.status_code


Task:

Write a test that uses unittest.mock to mock requests.get.

Ensure get_status("http://fakeurl") returns the mocked status code 200 without making a real network request.

4. Debugging with pdb

You have this buggy function:

def buggy_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return n   # bug: should return total


Task:

Use pdb.set_trace() to step through and identify the bug.

Correct the function.

5. Code Coverage with trace

Task:

Run your test_calculator.py with trace:

python -m trace --count test_calculator.py


Inspect which lines of calculator.py are not covered by your tests.

Add missing tests until coverage is complete.

6. Virtual Environments

Task:

Create a new virtual environment called testenv.

Install requests inside it.

Verify that requests is not available outside the environment.

✅ Bonus: Use py_compile to precompile your calculator.py into bytecode. Check the __pycache__ directory for the .pyc file.
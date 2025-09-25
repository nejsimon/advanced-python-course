Python Standard Library — Testing & Development

Python includes tools in the standard library to support testing, code quality, and development workflows. These modules help you ensure correctness, maintainability, and reliability of your projects.

1. unittest

Built-in xUnit-style testing framework.

Supports test discovery, test cases, test suites, and fixtures.

Example:

import unittest

class MathTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)

if __name__ == "__main__":
    unittest.main()

2. doctest

Runs examples embedded in docstrings.

Ensures documentation and code stay in sync.

def square(x):
    """
    Returns the square of a number.

    >>> square(3)
    9
    >>> square(0)
    0
    """
    return x * x

if __name__ == "__main__":
    import doctest
    doctest.testmod()

3. unittest.mock

Create mock objects for unit testing.

Supports patching objects during tests.

from unittest.mock import MagicMock

mock = MagicMock()
mock.greet.return_value = "Hello!"

print(mock.greet("World"))  # "Hello!"

4. pdb — Python Debugger

Interactive debugging tool.

Provides breakpoints, stepping, and variable inspection.

def divide(a, b):
    import pdb; pdb.set_trace()
    return a / b

divide(4, 0)  # Debugger starts before error

5. trace

Tracks program execution.

Useful for code coverage and execution tracing.

python -m trace --trace myscript.py

6. venv

Creates isolated Python environments.

Useful for dependency management in development.

python -m venv myenv
source myenv/bin/activate   # Linux/macOS
myenv\Scripts\activate      # Windows

7. py_compile & compileall

Compile Python source files into bytecode (.pyc).

Ensures syntax correctness before deployment.

python -m py_compile script.py
python -m compileall .

8. site

Manages environment-specific configuration.

Useful for inspecting paths where Python looks for modules.

import site
print(site.getsitepackages())

Summary
Module	Purpose
unittest	Write and run unit tests
doctest	Verify code in documentation
mock	Mock objects and patching
pdb	Interactive debugging
trace	Code execution tracing and coverage
venv	Isolated virtual environments
py_compile	Precompile Python source code
site	Environment configuration and paths
# Python Building and Packaging: Coding Challenges

These challenges focus on practical tasks related to building, packaging, and distributing Python projects using modern tools and best practices.

---

## Challenge 1: Create a Basic Package Structure

**Objective:**  
Create a Python package named `mypackage` with the following structure:

```
mypackage/
├── mypackage/
│ ├── __init__.py
│ └── utils.py
├── tests/
│ └── test_utils.py
├── pyproject.toml
└── README.md
```

- `utils.py` should contain a function `add(a, b)` that returns the sum of two numbers.
- `test_utils.py` should contain a test for the `add` function using `unittest`.
- `pyproject.toml` should specify `setuptools` as the build backend.

---

## Challenge 2: Build a Wheel Distribution

**Objective:**  
Using your package from Challenge 1, build a wheel distribution:

- Use the `build` package (`python -m build`) to create `.whl` and `.tar.gz` files.
- Verify that the `dist/` folder contains the built artifacts.

---

## Challenge 3: Specify Dependencies with Poetry

**Objective:**  
Initialize the project using `poetry` and add `requests` as a runtime dependency.

- Run `poetry init` and configure the project.
- Add `requests` as a dependency.
- Write a small script inside the package that uses `requests` to fetch https://httpbin.org/get and prints the status code.

---

## Challenge 4: Create and Use a Namespace Package

**Objective:**  
Create a namespace package `mycompany.utils` split across two distributions:

- Package `utils1` with `mycompany/utils/func1.py` containing a function `func1()`.
- Package `utils2` with `mycompany/utils/func2.py` containing a function `func2()`.
- Use implicit namespace packages (no `__init__.py` files).
- Write a script that imports both `func1` and `func2` and calls them.

---

## Challenge 5: Publish to TestPyPI

**Objective:**  
Publish your package to [TestPyPI](https://test.pypi.org/):

- Register an account on TestPyPI.
- Use `twine` to upload the built distributions.
- Install your package from TestPyPI in a fresh virtual environment.
- Verify that your package installs and runs correctly.

---

## Challenge 6: Versioning with setuptools_scm

**Objective:**  
Configure your package to use `setuptools_scm` for automatic versioning based on Git tags:

- Add `setuptools_scm` as a build requirement.
- Tag your Git repository (e.g., `v0.1.0`).
- Build the package and verify that the version is automatically derived from the tag.

---

## Challenge 7: Write a `setup.cfg` for Your Package

**Objective:**  
Replace `setup.py` with a declarative `setup.cfg` that includes:

- Metadata (name, version, author, description).
- Package discovery.
- Entry points for a console script named `mypkg-cli` that runs a function inside your package.

---

## Challenge 8: Create a Console Script Entry Point

**Objective:**  
Add a console script entry point `mypkg-cli`:

- The script should call a function `main()` inside your package that prints `"Hello from mypackage!"`.
- Test the script by installing the package locally and running `mypkg-cli` from the command line.

---

## Challenge 9: Pin Exact Versions in `requirements.txt`

**Objective:**  
Generate a `requirements.txt` file with pinned versions of your dependencies, suitable for reproducible installs:

- Use `pip freeze` or equivalent.
- Explain the difference between pinned dependencies and flexible version specifiers.

---

## Challenge 10: Use `tox` for Multi-Environment Testing

**Objective:**  
Configure `tox` to test your package under Python 3.8 and 3.10 environments:

- Write a `tox.ini` file specifying these environments.
- Configure it to run your unit tests using `pytest`.
- Run `tox` and verify tests execute in both environments.


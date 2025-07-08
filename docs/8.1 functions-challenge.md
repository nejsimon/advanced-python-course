# Python Functions: Coding Challenges

These challenges are designed to exercise all aspects of Python functions, from definition and calling conventions to advanced features like closures, default values, annotations, variable argument lists, and more.

---

## Challenge 1: Positional and Keyword Arguments

**Objective**: Write a function `describe_person` that takes a name and age and prints them, supporting both positional and keyword arguments.

```python
def describe_person(name, age):
    ...

describe_person("Alice", 30)
describe_person(age=25, name="Bob")
```

---

## Challenge 2: Default Parameter Pitfalls

**Objective**: Implement a function `append_item(item, container=[])` that appends `item` to `container` and returns it. Demonstrate the default-mutable-argument pitfall and fix it.

```python
def append_item(item, container=None):
    if container is None:
        container = []
    container.append(item)
    return container
```

---

## Challenge 3: \*args and \*\*kwargs

**Objective**: Implement `log_call` that prints all arguments and keyword arguments passed to it.

```python
def log_call(*args, **kwargs):
    print(f"Positional: {args}")
    print(f"Keywords: {kwargs}")

log_call(1, 2, a=3, b=4)
```

---

## Challenge 4: Return Multiple Values

**Objective**: Write a function that returns both the minimum and maximum of a list.

```python
def min_max(values):
    return min(values), max(values)

lo, hi = min_max([5, 1, 9])
assert lo == 1 and hi == 9
```

---

## Challenge 5: Closures and Factory Functions

**Objective**: Write a `make_multiplier(factor)` function that returns a new function which multiplies its input by `factor`.

```python
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

triple = make_multiplier(3)
assert triple(10) == 30
```

---

## Challenge 6: Function Annotations and Type Hints

**Objective**: Annotate a function with type hints for input and output.

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

---

## Challenge 7: Lambdas and Higher-Order Functions

**Objective**: Use a lambda and `map` to square a list of integers.

```python
nums = [1, 2, 3]
squares = list(map(lambda x: x ** 2, nums))
assert squares == [1, 4, 9]
```

---

## Challenge 8: Recursion

**Objective**: Write a recursive factorial function.

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

assert factorial(5) == 120
```

---

## Challenge 9: Function Attributes

**Objective**: Create a function that tracks how many times it's been called using an attribute on itself.

```python
def counter():
    counter.calls += 1
    return counter.calls

counter.calls = 0

assert counter() == 1
assert counter() == 2
```

---

## Challenge 10: Introspection with inspect

**Objective**: Use the `inspect` module to print the names of arguments of a given function.

```python
import inspect

def example(a, b, c=5):
    pass

sig = inspect.signature(example)
assert list(sig.parameters.keys()) == ["a", "b", "c"]
```


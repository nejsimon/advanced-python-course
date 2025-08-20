# Python Generators

Generators are a type of iterable that compute values **lazily**. Instead of returning all values at once, a generator yields values one at a time using the `yield` keyword. This allows efficient iteration over large or infinite sequences.

---

## 🔰 What Is a Generator?

A generator is a function that contains at least one `yield` statement. Calling it returns a **generator iterator**, which computes the next value on demand.

```python
def count_up_to(n):
    i = 0
    while i < n:
        yield i
        i += 1

gen = count_up_to(3)
next(gen)  # 0
next(gen)  # 1  
```

---

## 🔄 How Generators Work

- `yield` pauses the function and saves its state.
- On the next `next()` call, execution resumes after the last `yield`.

Generators implement:
```python
__iter__() → self
__next__() → value or raise StopIteration
```

---

## ⚙️ Generator vs List

| Feature        | Generator          | List            |
|----------------|--------------------|-----------------|
| Evaluation     | Lazy               | Eager           |
| Memory usage   | Constant (per item)| O(n)            |
| Mutability     | Immutable          | Mutable         |
| Reuse          | Single use         | Reusable        |

---

## 🧩 Generator Expressions

Compact syntax, similar to list comprehensions:

```python
squares = (x * x for x in range(5))
next(squares)  # 0
```

> Use parentheses `()` instead of square brackets.

---

## 🧪 Real-World Use Cases

| Use Case               | Benefit                       |
|------------------------|-------------------------------|
| Streaming large files  | Memory efficiency             |
| Infinite sequences     | Feasible with lazy evaluation |
| Pipelines (e.g., ETL)  | Composable transformation     |
| Tree/graph traversal   | Avoid stack overflow          |
| Asynchronous programming | Foundation for `async def`  |

---

## 🔀 Chaining Generators

```python
def read_lines():
    with open("log.txt") as f:
        for line in f:
            yield line.strip()

def filter_errors(lines):
    for line in lines:
        if "ERROR" in line:
            yield line

for line in filter_errors(read_lines()):
    print(line)
```

---

## 🧪 `yield from`: Delegating to Sub-Generators

```python
def subgen():
    yield 1
    yield 2

def delegator():
    yield "start"
    yield from subgen()
    yield "end"

list(delegator())  # ['start', 1, 2, 'end']
```

- Flattens nested generators
- Propagates exceptions, return values, and `send()` calls

---

## 📥 Two-Way Generators: `send()`, `throw()`, `close()`

```python
def echo():
    received = yield
    while True:
        received = yield received

gen = echo()
next(gen)            # Prime the generator
print(gen.send(42))  # 42
```

### Generator methods:

| Method     | Description                                 |
|------------|---------------------------------------------|
| `send(val)` | Sends value into generator, resumes to next `yield` |
| `throw(exc)`| Raises exception inside generator           |
| `close()`   | Raises `GeneratorExit`, used for cleanup    |

---

## 🔚 Generator `return` and `StopIteration`

```python
def f():
    yield 1
    return 99

gen = f()
try:
    while True:
        print(next(gen))
except StopIteration as e:
    print(f"Done: {e.value}")  # 99
```

- `return` from generator raises `StopIteration(value)`
- `yield from` captures this return value

---

## ⚠️ Common Gotchas

### 1. Not Priming Before `send()`

```python
gen = echo()
gen.send("hello")  # TypeError: can't send non-None to a just-started generator
```

Always call `next(gen)` first.

---

### 2. Generators Are Exhausted

```python
g = (x for x in range(3))
list(g)  # [0, 1, 2]
list(g)  # [] – exhausted
```

Generators cannot be reused. Re-create if needed.

---

### 3. `yield` vs `return`

- `yield` emits a value and pauses
- `return` ends the generator, optionally providing a value (caught via `StopIteration.value`)

---

## 🧵 Generators vs Iterators

| Feature       | Generator                     | Iterator                        |
|----------------|-------------------------------|----------------------------------|
| Creation       | Via `def` + `yield`           | Implement `__iter__`, `__next__` manually |
| Syntax         | Concise                       | Verbose                         |
| State tracking | Automatic                     | Manual                          |

---

## 🧪 Generator Pipelines

```python
def numbers():
    yield from range(10)

def evens(source):
    for x in source:
        if x % 2 == 0:
            yield x

def squares(source):
    for x in source:
        yield x * x

pipeline = squares(evens(numbers()))
print(list(pipeline))  # [0, 4, 16, 36, 64]
```

---

## ✅ Best Practices

- Use generators when dealing with large or infinite data
- Compose multiple generators as pipelines
- Use `yield from` to simplify delegation
- Use generator expressions for short one-liners
- Always prime before `send()`

---

## 📚 Further Reading

- [PEP 255 – Simple Generators](https://peps.python.org/pep-0255/)
- [PEP 342 – Coroutines via Enhanced Generators](https://peps.python.org/pep-0342/)
- [PEP 380 – Syntax for Delegating to a Subgenerator](https://peps.python.org/pep-0380/)
- Fluent Python — Chapter 16 (Generators and Coroutines)
- Python Docs — [Generators](https://docs.python.org/3/howto/functional.html#generators)


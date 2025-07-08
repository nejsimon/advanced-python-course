# Python Type System: Coding Challenges

These challenges help you explore Python’s dynamic type system, static typing support via `typing`, and how to use type hints effectively with tools like `mypy`.

---

## Challenge 1: Basic Type Hints

**Objective**: Annotate function arguments and return types.

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

Run `mypy`:

```bash
$ mypy script.py
```

---

## Challenge 2: Union and Optional Types

**Objective**: Accept multiple types with `Union` and `Optional`.

```python
from typing import Union, Optional

def parse_age(age: Union[str, int, None]) -> Optional[int]:
    if age is None:
        return None
    return int(age)
```

---

## Challenge 3: List and Dict Annotations

**Objective**: Add annotations to common collections.

```python
from typing import List, Dict

names: List[str] = ["Alice", "Bob"]
stats: Dict[str, int] = {"views": 100, "likes": 10}
```

---

## Challenge 4: Typed `NamedTuple` and `dataclass`

**Objective**: Define a typed immutable and mutable record.

```python
from typing import NamedTuple
class Point(NamedTuple):
    x: float
    y: float

from dataclasses import dataclass
@dataclass
class User:
    name: str
    age: int
```

---

## Challenge 5: Callable Types

**Objective**: Specify a type for a function argument that takes a function.

```python
from typing import Callable

def apply(func: Callable[[int, int], int], x: int, y: int) -> int:
    return func(x, y)

assert apply(lambda a, b: a + b, 2, 3) == 5
```

---

## Challenge 6: Generics with TypeVar

**Objective**: Create a generic function that preserves type.

```python
from typing import TypeVar, List
T = TypeVar('T')

def first(items: List[T]) -> T:
    return items[0]
```

---

## Challenge 7: Structural Typing with Protocols

**Objective**: Define a protocol that supports duck typing.

```python
from typing import Protocol

class SupportsLen(Protocol):
    def __len__(self) -> int: ...

def describe(x: SupportsLen) -> str:
    return f"Length is {len(x)}"
```

---

## Challenge 8: Literal and Final

**Objective**: Restrict values and create constants.

```python
from typing import Literal, Final

Status = Literal['open', 'closed']
status: Status = 'open'

PI: Final = 3.14159  # Should not be reassigned
```

---

## Challenge 9: Annotating `self` and `cls`

**Objective**: Properly annotate instance and class methods.

```python
class Counter:
    count: int = 0

    def increment(self) -> None:
        self.count += 1

    @classmethod
    def reset(cls) -> None:
        cls.count = 0
```

---

## Challenge 10: Typed `*args` and `**kwargs`

**Objective**: Annotate variadic arguments.

```python
from typing import Any

def log(*args: str, **kwargs: Any) -> None:
    print("ARGS:", args)
    print("KWARGS:", kwargs)
```

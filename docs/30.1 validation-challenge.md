# Python Validation: Coding Challenges

These challenges cover data validation techniques in Python using built-in tools, type hints, `pydantic`, `dataclasses`, and custom validation logic.

---

## Challenge 1: Basic Type Checking

**Objective**: Implement a function that checks whether arguments match expected types.

```python
def validate_person(name, age):
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    if not isinstance(age, int):
        raise TypeError("age must be an integer")
```

---

## Challenge 2: Using Type Hints with `mypy`

**Objective**: Add type hints and run static analysis using `mypy`.

```python
def square(x: int) -> int:
    return x * x
```

```bash
$ mypy script.py  # Should report no errors
```

---

## Challenge 3: Using `dataclasses` with Validation

**Objective**: Add a `__post_init__` method to validate fields.

```python
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")
```

---

## Challenge 4: Pydantic Model Validation

**Objective**: Define a Pydantic model that validates input data.

```python
from pydantic import BaseModel, validator

class User(BaseModel):
    username: str
    age: int

    @validator('age')
    def age_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Age must be positive")
        return v
```

---

## Challenge 5: Optional and Default Fields

**Objective**: Use optional and default fields in a validation model.

```python
from typing import Optional
from pydantic import BaseModel

class Settings(BaseModel):
    host: str = "localhost"
    port: Optional[int] = 8000
```

---

## Challenge 6: Regex Validation

**Objective**: Use regex to validate a string format.

```python
import re

def validate_email(email: str):
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        raise ValueError("Invalid email")
```

---

## Challenge 7: Enum and Value Restriction

**Objective**: Restrict field values using enums.

```python
from enum import Enum
from pydantic import BaseModel

class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"

class Account(BaseModel):
    role: Role
```

---

## Challenge 8: Nested Models

**Objective**: Create nested models for structured validation.

```python
from pydantic import BaseModel

class Address(BaseModel):
    city: str
    zip_code: str

class Person(BaseModel):
    name: str
    address: Address

p = Person(name="Alice", address={"city": "Stockholm", "zip_code": "12345"})
```

---

## Challenge 9: Custom Validators

**Objective**: Write a reusable custom validator for field constraints.

```python
from pydantic import BaseModel, constr

class Item(BaseModel):
    name: constr(min_length=3, max_length=50)
```

---

## Challenge 10: Batch Validation with Error Collection

**Objective**: Validate a batch of inputs and collect errors.

```python
from pydantic import ValidationError

users = [
    {"username": "ok", "age": 25},
    {"username": "fail", "age": -5},
]

for data in users:
    try:
        u = User(**data)
        print("Valid:", u)
    except ValidationError as e:
        print("Invalid:", e.errors())
```

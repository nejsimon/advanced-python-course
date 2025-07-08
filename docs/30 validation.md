# Python Data Validation

Validation ensures **data correctness**, **type safety**, and **application robustness**. It spans simple type checks to full schema enforcement, especially in I/O-heavy code such as APIs, config loaders, CLI tools, and user input.

---

## 🧾 Types of Validation

| Level              | Use Case                             |
|--------------------|--------------------------------------|
| Manual             | Lightweight checks                   |
| Schema-based       | Structured data (e.g. JSON, YAML)    |
| Type-annotated     | Editor/runtime tooling (`pydantic`)  |
| Custom validators  | Domain-specific logic                |

---

## 🧪 Manual Validation (Basic Python)

### Basic Checks

```python
def validate_user(user):
    if not isinstance(user, dict):
        raise TypeError("Expected dict")
    if "name" not in user:
        raise ValueError("Missing name")
    if not isinstance(user["name"], str):
        raise TypeError("Name must be a string")
```

Manual validation:
- ✅ Fine-grained control
- ❌ Verbose, error-prone, inconsistent

---

## 📦 Schema-Based Validation with `pydantic`

Install:

```bash
pip install pydantic
```

### Example

```python
from pydantic import BaseModel, Field, EmailStr, validator

class User(BaseModel):
    id: int
    name: str = Field(..., min_length=1)
    email: EmailStr
    active: bool = True

    @validator("name")
    def strip_name(cls, v):
        return v.strip()

user = User(id=1, name="  Alice  ", email="alice@example.com")
```

### Features

| Feature               | Description                      |
|------------------------|----------------------------------|
| Type validation        | Enforced at runtime              |
| Custom validators      | Field-specific rules             |
| Aliases & renaming     | `alias=...` for input remapping  |
| Nested models          | Recursive schemas                |
| JSON Schema export     | `User.schema()`                  |

---

## 🧠 Pydantic Quirks

- Uses **type coercion** by default:
  ```python
  User(id="123", ...)  # id becomes int
  ```

- Use `strict=True` in `Field(...)` to prevent coercion:
  ```python
  id: int = Field(..., strict=True)
  ```

- Optional fields must use `Optional[...]`:
  ```python
  email: Optional[str] = None
  ```

- Pydantic models are immutable with `Config.frozen = True`

---

## 🔐 Pydantic V2 Differences (Optional Section)

Pydantic v2:
- Built on `pydantic-core` (Rust)
- Much faster
- Stricter defaults (less implicit coercion)
- Custom JSON encoders/decoders

---

## 📦 Other Schema Libraries

### `voluptuous`

```bash
pip install voluptuous
```

```python
from voluptuous import Schema, Required, All, Length

schema = Schema({
    Required("name"): All(str, Length(min=1)),
    "age": int,
})

schema({"name": "Alice", "age": 30})
```

- ✅ Declarative
- ❌ Less type-safe and slower than `pydantic`

---

### `cerberus`

```python
from cerberus import Validator

v = Validator({
    "name": {"type": "string", "minlength": 1},
    "age": {"type": "integer"},
})

v.validate({"name": "Bob", "age": 25})  # True
```

---

## 🧾 Type Hint + Runtime Validation

Python type hints are **not enforced at runtime**:

```python
def add(x: int, y: int) -> int:
    return x + y

add("a", "b")  # TypeError? No — returns "ab"
```

Use **static checkers** (e.g., mypy) for type validation or libraries like `pydantic` for runtime enforcement.

---

## 🧪 Custom Validation Logic

### Validating Constraints

```python
def validate_price(value):
    if value < 0:
        raise ValueError("Price must be non-negative")
```

### In `pydantic`

```python
@validator("price")
def non_negative(cls, v):
    if v < 0:
        raise ValueError("Price must be non-negative")
    return v
```

---

## 📤 Deserialization & Input Validation

Schema libraries can validate:
- JSON inputs (APIs)
- Form data (web apps)
- CLI args (via `typer`, `argparse`)
- Config files (TOML, YAML, INI)

---

## 🧵 Asynchronous Validation

Pydantic v2 supports async validators:

```python
@field_validator("url", mode="before")
@classmethod
async def check_reachability(cls, v):
    ...
```

> Useful for validating references, fetching remote metadata, etc.

---

## 🧪 Composability: Nested and Recursive Models

```python
class Address(BaseModel):
    city: str
    zip: str

class User(BaseModel):
    name: str
    address: Address
```

---

## ⚠️ Pitfalls and Anti-Patterns

### 1. Too much logic in validators

Keep validators fast and side-effect-free.

### 2. Confusing coercion

Pydantic will coerce types unless you explicitly prevent it.

```python
id: int = Field(..., strict=True)
```

### 3. Using type hints for validation — but not enforcing

Type hints alone do nothing at runtime. Use schema libraries or static analysis.

### 4. Forgetting to validate external input

```python
def my_api(data):  # 🔥
    process(data["user"]["email"])  # may crash!
```

---

## ✅ Summary

| Technique        | Tool/Approach       | Use Case                        |
|------------------|---------------------|---------------------------------|
| Manual Checks     | `isinstance`, `if`  | Lightweight validation          |
| Schema-based      | `pydantic`, `voluptuous` | Structured APIs, config       |
| Runtime with hints| `pydantic`          | Combines types + validation     |
| Static Typing     | `mypy`              | Compile-time safety             |
| Input validation  | `argparse`, `typer`, `click` | CLI apps                  |

---

## 🧰 Useful Tools and Libraries

| Library     | Purpose                                  |
|-------------|-------------------------------------------|
| `pydantic`  | Runtime data modeling & validation        |
| `voluptuous`| Schema-based declarative validation       |
| `cerberus`  | Lightweight JSON-like validation          |
| `attrs`     | Declarative classes with validators       |
| `marshmallow`| Validation + serialization               |

---

## 📚 Further Reading

- [Pydantic documentation](https://docs.pydantic.dev/)
- [Voluptuous](https://alecthomas.github.io/voluptuous/)
- [Cerberus](https://docs.python-cerberus.org/en/stable/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [attrs](https://www.attrs.org/en/stable/)
- [Effective Python – Item 29: Validate arguments with decorators and descriptors]


# Working with YAML in Python

YAML (YAML Ain't Markup Language) is a human-friendly data serialization standard commonly used for configuration files, CI pipelines, and data interchange. Python doesn't include YAML support in the standard library, but powerful third-party libraries like `PyYAML` provide full functionality.

---

## 1. YAML vs JSON

| Feature         | YAML                 | JSON            |
| --------------- | -------------------- | --------------- |
| Syntax          | Indentation-based    | Brackets/commas |
| Readability     | More human-friendly  | Verbose         |
| Comments        | Yes (`#`)            | No              |
| Data types      | Extended (e.g. sets) | Limited         |
| Spec strictness | Flexible             | Strict          |

---

## 2. Installing PyYAML

```bash
pip install pyyaml
```

Other libraries include:

* `ruamel.yaml`: YAML 1.2 support, round-tripping
* `yamlpath`: query-like navigation for YAML

---

## 3. Basic Parsing and Dumping

### `yaml.safe_load()` – YAML → Python

```python
import yaml

data = yaml.safe_load('name: Alice\nage: 30')
print(data["name"])  # Alice
```

### `yaml.safe_dump()` – Python → YAML

```python
doc = {"language": "Python", "versions": [3.8, 3.9, 3.10]}
print(yaml.safe_dump(doc))
```

---

## 4. Loading From and Writing to Files

```python
with open("config.yaml") as f:
    config = yaml.safe_load(f)

with open("output.yaml", "w") as f:
    yaml.safe_dump(config, f)
```

---

## 5. Full YAML Spec Features

### Anchors and Aliases

```yaml
default: &defaults
  retries: 3
  timeout: 10

prod:
  <<: *defaults
  timeout: 30
```

PyYAML will merge these automatically if you use `yaml.load()` with `Loader=yaml.FullLoader`.

---

## 6. Custom Python Objects

### Serializing Python Classes

```python
class User:
    def __init__(self, name):
        self.name = name

yaml.dump(User("Alice"))  # Not supported by safe_dump
```

You must register custom serializers or use unsafe methods (`yaml.dump()` with `Dumper=yaml.UnsafeDumper`). Use with caution.

---

## 7. Multiple Documents in One File

```yaml
---
name: Alpha
---
name: Beta
```

```python
list(yaml.safe_load_all(open("multi.yaml")))
```

---

## 8. Data Type Mapping

| YAML               | Python |
| ------------------ | ------ |
| scalar string      | str    |
| integer            | int    |
| float              | float  |
| boolean            | bool   |
| null (`~`, `null`) | None   |
| sequence           | list   |
| mapping            | dict   |

---

## 9. Security Considerations

* **NEVER use `yaml.load()` with untrusted input** — it allows code execution
* Always prefer `yaml.safe_load()`
* Avoid `yaml.UnsafeDumper` unless absolutely necessary

---

## 10. Common Pitfalls

* Indentation is critical (use spaces, not tabs)
* String values like `yes`, `no`, `on`, `off` are interpreted as booleans
* No native support for comments in round-tripping (use `ruamel.yaml`)

---

## 11. Best Practices

* Stick to `yaml.safe_load`/`safe_dump` unless you need advanced features
* Validate structure manually or use schema tools (like `Cerberus` or `pydantic`)
* Prefer YAML for config; use JSON for data exchange
* Normalize data after load (e.g., convert keys to strings)


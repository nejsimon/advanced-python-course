# Working with YAML in Python: Coding Challenges

These exercises help reinforce the concepts of parsing, generating, securing, and manipulating YAML data in Python using PyYAML.

---

## Challenge 1: Load a Simple YAML Document

**Objective:** Use `yaml.safe_load()` to parse a YAML string:

```yaml
name: Alice
skills:
  - Python
  - YAML
```

**Tasks:**

* Load the YAML into a Python object.
* Print the second skill.

---

## Challenge 2: Dump a Dictionary to YAML

**Objective:** Serialize the following Python dictionary to YAML:

```python
user = {"name": "Bob", "age": 40, "languages": ["Python", "Go"]}
```

**Tasks:**

* Use `yaml.safe_dump()`.
* Output to a string and print it.

---

## Challenge 3: Read and Write YAML Files

**Objective:**

* Read from `config.yaml`
* Add a key `version: 1.0`
* Write back to `config_updated.yaml`

**Tasks:**

* Use `yaml.safe_load()` and `yaml.safe_dump()`
* Ensure output is formatted with 2-space indentation

---

## Challenge 4: Parse Multiple YAML Documents

**Input:** `multi.yaml`

```yaml
---
name: First
---
name: Second
```

**Tasks:**

* Use `yaml.safe_load_all()`
* Print all names

---

## Challenge 5: Use Anchors and Aliases

**YAML Input:**

```yaml
base: &defaults
  retries: 3
  timeout: 10

deployment:
  <<: *defaults
  retries: 5
```

**Tasks:**

* Load and access the final `deployment["retries"]`
* Confirm that the value is overridden to `5`

---

## Challenge 6: Unsafe Loading Warning

**Objective:** Demonstrate the danger of `yaml.load()`

**YAML:**

```yaml
!!python/object/apply:os.system ["echo HACKED"]
```

**Tasks:**

* Attempt to load this with `yaml.load()`
* Catch and explain the risk (do not execute it!)

---

## Challenge 7: Custom Object Serialization (Optional)

**Objective:** Serialize a class `User(name)` to YAML

**Tasks:**

* Register a custom representer and constructor using `yaml.add_representer`
* Dump and load the object (if using `yaml.UnsafeDumper`, explain the risk)

---

## Challenge 8: Data Type Coercion

**Input:**

```yaml
count: "10"
flag: "yes"
```

**Tasks:**

* Load the data
* Convert `count` to an integer
* Convert `flag` to a boolean manually

---

## Challenge 9: Handle Invalid YAML Gracefully

**Objective:** Catch parse errors in malformed YAML

**Input:**

```yaml
name: Carol
  age: 29
```

**Tasks:**

* Try `safe_load()`
* Catch `yaml.YAMLError` and print a friendly error message

---

## Challenge 10: Schema Validation (Bonus)

**Objective:** Validate a loaded YAML config using a simple schema (dict key checks)

**Schema:**

* Must have keys: `host` (str), `port` (int)

**Tasks:**

* Manually validate types and presence
* Raise an error if validation fails
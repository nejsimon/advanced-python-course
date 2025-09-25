# Working with JSON in Python: Coding Challenges

These exercises cover parsing, serialization, formatting, schema validation, custom encoders, and third-party JSON libraries.

---

## Challenge 1: Parse and Access Data

**Objective:** Use `json.loads()` to parse a string and extract values.

```python
input_str = '{"name": "Alice", "age": 30, "active": true}'
```

**Tasks:**

* Parse the string.
* Print the name and age.

---

## Challenge 2: Convert Python to JSON

**Objective:** Serialize a dictionary with `json.dumps()`.

```python
data = {"lang": "Python", "version": 3.10}
```

**Tasks:**

* Convert it to a compact JSON string.
* Then format it with indentation and sorted keys.

---

## Challenge 3: Read and Write JSON Files

**Objective:** Use `json.load()` and `json.dump()` to read from and write to files.

**Tasks:**

* Read a file `input.json`.
* Add a new key/value to the object.
* Write it back to `output.json` with indentation.

---

## Challenge 4: Handle Non-Serializable Types

**Objective:** Serialize a `datetime` object using a custom encoder.

**Tasks:**

* Define a function to convert `datetime` to ISO format.
* Use `json.dumps(obj, default=...)`.

---

## Challenge 5: Custom Deserialization with `object_hook`

**Objective:** Convert an ISO string to a `datetime` object after parsing JSON.

```json
{"created": "2024-01-01T12:00:00"}
```

**Tasks:**

* Parse and convert `created` to `datetime`.

---

## Challenge 6: Validate JSON Schema

**Objective:** Use `jsonschema` to validate this object:

```python
obj = {"user": "Bob", "age": 42}
```

**Schema:**

```python
schema = {
  "type": "object",
  "properties": {
    "user": {"type": "string"},
    "age": {"type": "integer", "minimum": 0}
  },
  "required": ["user", "age"]
}
```

**Tasks:**

* Validate `obj`.
* Try modifying it to trigger a validation error.

---

## Challenge 7: Use `orjson` or `ujson`

**Objective:** Benchmark the time to serialize a large list using `json` vs `orjson`.

**Tasks:**

* Create a list of 1,000,000 numbers.
* Time serialization with `json.dumps()` and `orjson.dumps()`.

---

## Challenge 8: Access Nested Data Safely

**Objective:** Parse and access nested values.

```json
{"a": {"b": {"c": 42}}}
```

**Tasks:**

* Access the value at `c`.
* Use `dict.get()` to avoid `KeyError`.

---

## Challenge 9: Handle Bad JSON Input

**Objective:** Catch and handle malformed JSON.

**Input:** `'[1, 2, 3,]'` (note the trailing comma)

**Tasks:**

* Try `json.loads()`.
* Catch and print the error using `json.JSONDecodeError`.

---

## Challenge 10: Round-trip API Simulation

**Objective:** Simulate sending and receiving data in JSON.

**Tasks:**

* Serialize a Python object to a string.
* Simulate sending it over a "network".
* Parse it again and verify the content is preserved.

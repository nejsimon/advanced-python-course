# Coding Challenge: File Formats & Serialization

This challenge will test your ability to work with Python’s standard library for handling different data formats and serialization techniques. You will practice with **JSON, CSV, Pickle, ConfigParser, Shelve, and XML**.

---

## Part 1: JSON
1. Write a function `save_to_json(filename, data)` that saves a Python dictionary to a file in JSON format.
2. Write a function `load_from_json(filename)` that loads and returns the dictionary.
3. Extend your code to handle **custom objects** (e.g., a `User` class) by writing a custom JSON encoder and decoder.

---

## Part 2: CSV
1. Write a function `write_users_csv(filename, users)` that writes a list of dicts (`[{"name": "Alice", "age": 30}, ...]`) into a CSV file with headers.
2. Write a function `read_users_csv(filename)` that reads the file back and returns a list of dicts.
3. Extend your function to allow a **different delimiter** (e.g., `;` instead of `,`).

---

## Part 3: Pickle
1. Serialize an arbitrary Python object (e.g., nested dict with lists) using `pickle.dumps`.
2. Deserialize it back and verify equality.
3. Demonstrate what happens if you **modify the class definition** of a pickled object before loading it back.

---

## Part 4: ConfigParser
1. Write a function `create_config(filename)` that generates a `.ini` configuration file with at least two sections (`[general]`, `[database]`).
2. Write a function `read_config(filename)` that loads and prints values from the `.ini` file.
3. Demonstrate the use of **default values** and **interpolation**.

---

## Part 5: Shelve
1. Implement a persistent key-value store using `shelve` where keys are usernames and values are dicts with user info.
2. Write functions:
   - `add_user(username, info)`
   - `get_user(username)`
   - `delete_user(username)`
3. Demonstrate that the data persists across multiple runs of the program.

---

## Part 6: XML
1. Create an XML document representing a simple **library** with multiple `book` elements (attributes: `id`, `title`, `author`).
2. Write a function `save_library(filename, books)` that generates the XML file.
3. Write a function `load_library(filename)` that parses the XML back into Python dicts.
4. Add a new `book` to the XML file without overwriting the existing ones.

---

## Bonus Challenge
- Compare file size and readability between **JSON, Pickle, and XML** when saving the same dataset.
- Implement a small **conversion script** that takes a `.csv` file and outputs it as `.json`.


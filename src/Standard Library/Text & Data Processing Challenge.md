# Coding Challenges: Python Standard Library — Text & Data Processing

These challenges will test your ability to use `string`, `re`, `textwrap`, `unicodedata`, `difflib`, `pprint`, `json`, `csv`, `configparser`, and `plistlib`. They range from basic manipulations to advanced real-world scenarios.

---

## Challenge 1: String Utilities
1. Using the `string` module:
   - Print all ASCII lowercase letters, uppercase letters, and digits.
   - Generate a random password of 12 characters using only `ascii_letters` and `digits`.

---

## Challenge 2: Regex Extraction
1. Using the `re` module:
   - Extract all email addresses from a block of text.
   - Validate whether a given string is a valid IPv4 address.

---

## Challenge 3: Text Wrapping
1. Use the `textwrap` module to:
   - Format a paragraph to fit within 40 characters per line.
   - Indent each line by 4 spaces.

---

## Challenge 4: Unicode Normalization
1. Use `unicodedata` to:
   - Normalize `"café"` in different forms (`NFC`, `NFD`).
   - Compare equality of normalized vs. non-normalized strings.

---

## Challenge 5: Difference Checker
1. Use the `difflib` module to:
   - Compare two strings and output their differences.
   - Use `difflib.get_close_matches()` to find the closest match for `"appl"` in `["apple", "apply", "ape"]`.

---

## Challenge 6: Pretty Printing
1. Use `pprint` to:
   - Pretty-print a deeply nested dictionary.
   - Compare output of `print()` vs. `pprint.pprint()`.

---

## Challenge 7: JSON Processing
1. Write a script that:
   - Reads a JSON file containing user data (name, age, email).
   - Converts it into Python objects.
   - Modifies one field and writes it back.

2. Extend it to pretty-print the JSON with indentation.

---

## Challenge 8: CSV Handling
1. Use the `csv` module to:
   - Read a CSV file with columns `name,age,city`.
   - Print all names of people older than 30.
   - Write a new CSV file with an added `country` column.

---

## Challenge 9: Config Files
1. Use the `configparser` module to:
   - Read settings from a file `settings.ini` with sections `[database]` and `[server]`.
   - Change a value (`port=8080` → `port=9090`) and write back to file.

---

## Challenge 10: Property List Files
1. Use the `plistlib` module to:
   - Create a `.plist` file containing metadata about a project (`name`, `version`, `author`).
   - Read it back and print the contents.

---

## Bonus Challenge: End-to-End Data Transformation
Write a script that:
1. Reads a CSV file of users.
2. Converts it into JSON.
3. Normalizes all names (remove accents with `unicodedata`).
4. Pretty-prints the result with `pprint`.
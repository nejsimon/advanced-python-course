# Coding Challenges: Python Standard Library — File and OS Interfaces

These challenges will test your ability to use the `os`, `pathlib`, `shutil`, `glob`, `tempfile`, `zipfile`, `tarfile`, `io`, and `fileinput` modules. They range from basic usage to advanced real-world scenarios.

---

## Challenge 1: File Exploration
1. Write a script that:
   - Prints the current working directory (`os.getcwd()`).
   - Creates a new subdirectory called `logs` if it doesn’t exist.
   - Lists all files in the current directory.

2. Extend the script to use **`pathlib`** instead of `os`.

---

## Challenge 2: File Copy & Move Utility
1. Write a script that:
   - Copies a file `example.txt` to `backup/example_copy.txt`.
   - Moves the copied file into a new folder `archive/`.

2. Ensure the script works even if the `backup/` or `archive/` folders don’t exist (create them if needed).

---

## Challenge 3: File Pattern Search with `glob`
1. Write a script that:
   - Finds all `.py` files in the current directory and subdirectories.
   - Prints their absolute paths.

2. Modify the script to instead use **`pathlib`**'s `.glob("**/*.py")`.

---

## Challenge 4: Temporary Files
1. Use the `tempfile` module to:
   - Create a temporary file.
   - Write the string `"Hello, Temp!"` into it.
   - Print its name and contents.

2. Verify the file persists after the script ends (hint: set `delete=False`).

---

## Challenge 5: Archiving with `zipfile`
1. Write a script that:
   - Creates a ZIP archive containing all `.txt` files in the current directory.
   - Lists the files inside the archive.

2. Extend the script to extract the archive into a folder called `unzipped/`.

---

## Challenge 6: Archiving with `tarfile`
1. Write a script that:
   - Creates a `.tar.gz` archive of all `.log` files in the `logs/` directory.
   - Lists all the files in the archive.

2. Extend it to extract into a folder `untarred/`.

---

## Challenge 7: In-Memory Streams
1. Use `io.StringIO` to:
   - Create a fake file-like object.
   - Write `"Python Rocks!"` into it.
   - Reset the pointer and read back the contents.

2. Do the same with `io.BytesIO` for binary data.

---

## Challenge 8: Multi-File Line Reader
1. Use `fileinput` to:
   - Read lines from multiple text files (`file1.txt`, `file2.txt`).
   - Print line numbers alongside content.

2. Extend the script so that if no files are provided, it reads from standard input.

---

## Bonus Challenge: Directory Synchronization
Write a script that:
1. Takes two directories: `source/` and `destination/`.
2. Copies all files from `source/` to `destination/` (overwrite if newer).
3. Creates a `.zip` archive of the `destination/` folder after syncing.

*Hint*: Use `pathlib`, `shutil`, and `zipfile`.

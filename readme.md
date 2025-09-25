# Advanced Python Course

This repository contains a comprehensive course on advanced Python programming topics. It is intended for experienced developers who want to master Python’s powerful and sometimes obscure capabilities.

> **Target Python Version:** This course is written for **Python 3.11+**. Some features (e.g. `Self` from `typing`, improved error messages, `match-case`, performance boosts) require Python 3.10 or later.

**Consider this alpha quality as of now.**

---

## Structure

* All documentation is stored under the `src/markdown` directory.
* Each documentation page is followed by a matching coding challenge (e.g., `Threading.md`, then `Threading Challenge.md`).
* HTML files built from the markdown are stored in the `course/` directory.
* Challenge files built from the markdown are stored in the `challenges/` directory.

---

## Building

Two scripts exsists to convert the markdow to HTML and convert the challenges into python files respectively.

```bash
poetry install
poetry run python scripts/build_html.py # Build HTML pages, will be output in the /course folder
poetry run python scripts/build_code_challenges.py # Build challenge files, will be output in the /challenges folder
```

---

## Contribution & Disclaimer

⚠️ **Note**: Most of this content was generated with the help of AI tools and large language models. It's mostly reviewed it for accuracy and quality, hallucinations, outdated syntax, or weirdness may exist. There are some overlapping content (i.e. the stuff in the `Standard Library` folder) I've spent my tokens on generating this stuff so you don't have to! :)

Please help fix errors, improve clarity, and expand the course! If you find a problem or want to improve something, **please submit a pull request**.

---

Happy learning!

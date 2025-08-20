# Itertools in Python: Coding Challenges

These challenges will help you practice the functionality of the `itertools` module and explore how it can simplify iteration and combinatorial problems.

---

## Challenge 1: Infinite Iterators

**Objective:**
Use `itertools.count` to generate the sequence `10, 20, 30, ...` and stop once you reach 100. Print the values.

---

## Challenge 2: Cycle Through Elements

**Objective:**
Use `itertools.cycle` to repeatedly cycle through the string `"ABC"` and print the first 10 characters.

---

## Challenge 3: Repeated Values

**Objective:**
Use `itertools.repeat` to generate the value `42` exactly 5 times.

---

## Challenge 4: Accumulate

**Objective:**
Given a list `[1, 2, 3, 4]`, use `itertools.accumulate` to produce a running total and print the results.

---

## Challenge 5: Chain Iterables

**Objective:**
Use `itertools.chain` to combine `[1, 2]`, `['a', 'b']`, and `(True, False)` into a single iterator and print the values.

---

## Challenge 6: Compress

**Objective:**
Use `itertools.compress` to filter the data `['A', 'B', 'C', 'D']` with the selector `[1, 0, 1, 0]`. Print the results.

---

## Challenge 7: Dropwhile

**Objective:**
Given the list `[1, 4, 6, 4, 1]`, use `itertools.dropwhile` to drop elements while they are less than 5, then print the remainder.

---

## Challenge 8: Groupby

**Objective:**
Group the sequence `"aaabbcaaa"` using `itertools.groupby` and print each group and its elements.

---

## Challenge 9: Permutations

**Objective:**
Generate all permutations of `[1, 2, 3]` using `itertools.permutations` and print them.

---

## Challenge 10: Combinations

**Objective:**
Generate all 2-element combinations of `[1, 2, 3, 4]` using `itertools.combinations` and print them.

---

## Challenge 11: Cartesian Product

**Objective:**
Use `itertools.product` to generate the Cartesian product of `[1, 2]` and `["A", "B"]`. Print the pairs.

---

## Challenge 12: Advanced Mini-Project

**Objective:**
Write a script that:

* Uses `itertools.combinations` to generate all possible 5-card hands from a deck of 52 cards.
* Filters out hands that contain at least one Ace.
* Prints the first 10 such hands.

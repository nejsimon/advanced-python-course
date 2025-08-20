# Python Standard Library — Data Types & Collections

The Python standard library provides a rich set of modules for working with fundamental data structures beyond built-in lists, sets, and dictionaries. These modules give you more specialized or efficient tools to handle different kinds of data, supporting use cases from immutability to high-performance queues.

---

## Key Modules

### `collections`
- Provides specialized container datatypes:
  - **`namedtuple()`**: Factory function for tuple subclasses with named fields.
  - **`deque`**: Double-ended queue with fast appends/pops on both ends.
  - **`Counter`**: A dictionary subclass for counting hashable objects.
  - **`OrderedDict`**: Dict subclass that remembers insertion order (since Python 3.7, `dict` also preserves order, but `OrderedDict` offers additional features).
  - **`defaultdict`**: Dict subclass that provides default values for missing keys.
  - **`ChainMap`**: Groups multiple dictionaries for a single view.

### `array`
- Space-efficient arrays of basic C data types (e.g., `int`, `float`, `char`).
- Faster than lists when dealing with homogeneous numerical data.

### `heapq`
- Implements a min-heap queue algorithm.
- Commonly used for priority queues.
- Functions: `heappush`, `heappop`, `heapify`, `nlargest`, `nsmallest`.

### `bisect`
- For maintaining sorted lists without repeatedly sorting.
- Functions: `bisect_left`, `bisect_right`, `insort_left`, `insort_right`.

### `queue`
- Thread-safe FIFO queue, LIFO queue, and priority queue classes.
- Useful for multi-threaded or producer/consumer patterns.

### `weakref`
- Support for weak references to objects.
- Useful in caching and when you want objects to be garbage-collected normally even if referenced.

### `types`
- Defines names for various built-in object types.
- Provides `SimpleNamespace` for dynamic attribute assignment.
- Defines function and coroutine types for reflection.

---

## Advanced Usage & Patterns

- **Counting words**: Use `collections.Counter` for natural language processing tasks.
- **Multi-dict view**: Use `ChainMap` for layered configuration management (default config + environment overrides + CLI args).
- **Priority queues**: Combine `heapq` with `dataclasses` for readable task schedulers.
- **Memory efficiency**: Use `array.array('d')` for large numeric datasets to reduce memory footprint compared to `list[float]`.

---

## Quirks & Caveats

- `OrderedDict` is rarely needed now, but its `.move_to_end()` and equality semantics can still be useful.
- `deque` is highly efficient for appends/pops at ends but not for random access (O(n) indexing).
- `heapq` implements only min-heaps. To create a max-heap, negate the values or wrap them in custom classes.
- `queue.Queue` adds locking overhead; for single-threaded code, use `collections.deque` instead.
- Weak references don’t work with all objects (e.g., they can’t be used on most built-in immutable types).

---

## Summary

The **Data Types & Collections** cluster extends Python’s built-in containers with:
- High-performance queues, heaps, and arrays.
- Specialized mappings (default dicts, chain maps).
- Memory-efficient and thread-safe structures.
- Support for weak references and type-related utilities.

These modules should be your go-to tools when built-in containers don’t fully meet your performance or semantic requirements.

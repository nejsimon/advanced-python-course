# Scoping and Namespaces

Python uses a **lexical scoping** model and resolves names using the **LEGB rule** — which defines how variables are resolved based on where they're defined.

A **namespace** is a mapping from names to objects.
A **scope** defines the textual region of code where a namespace is directly accessible.

---

## 🧠 The LEGB Rule

| Scope        | Description                               |
|--------------|-------------------------------------------|
| **Local**    | Inside the current function/method        |
| **Enclosing**| In any outer function enclosing the current one |
| **Global**   | Module-level scope                        |
| **Built-in** | Python’s built-in names (`len`, `sum`, etc.) |

Resolution order: **Local → Enclosing → Global → Built-in**

---

### Example

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()

outer()  # prints: "local"
```

---

## 🔎 Inspecting Namespaces

- `locals()` → current local scope
- `globals()` → module-level globals
- `vars()` → object or module dictionary
- `dir()` → list of names in current scope or object

---

## 🧾 Global Scope

A variable declared at the top level of a module or declared `global` inside a function.

```python
x = 42

def read():
    print(x)  # reads global x

def modify():
    global x
    x = 100  # modifies global x
```

---

## 🔄 `nonlocal`: Modify Enclosing Scope

Use inside a nested function to modify variables from the enclosing (but non-global) scope.

```python
def outer():
    count = 0
    def inc():
        nonlocal count
        count += 1
    inc()
    print(count)  # 1
```

---

## 🔁 Variable Shadowing

A variable in a local scope can **shadow** a variable in an outer scope.

```python
x = 10

def f():
    x = 5  # shadows global x
    print(x)  # 5
```

Be careful with shadowing built-in names:

```python
list = [1, 2, 3]  # shadows built-in `list` type
```

---

## 🧱 Scopes in Class and Function Definitions

### Functions

- Introduce a new **local** scope.
- Inner functions can close over outer variables.

### Classes

- Body executes in its own namespace.
- Methods **don’t** capture outer class-level names automatically.

```python
x = 10
class A:
    x = 20
    def f(self):
        print(x)  # prints global x (10), not A.x
```

---

## 🧬 Closures and Free Variables

```python
def outer():
    msg = "hello"
    def inner():
        print(msg)  # closes over msg
    return inner
```

`inner` is a **closure** — it remembers `msg` from the enclosing scope.

You can inspect them:

```python
f = outer()
print(f.__closure__[0].cell_contents)  # 'hello'
```

---

## 🧰 Dynamic Scope Emulation

Python does **not** support dynamic scope, but you can simulate it:

```python
import contextvars

user = contextvars.ContextVar("user")

def log(msg):
    print(f"{user.get()}: {msg}")

def handler():
    user.set("Alice")
    log("request handled")
```

Or use `threading.local()` for thread-local dynamic data.

---

## 🔐 Scope in List/Dict Comprehensions

### Python 3.x

List/dict/set comprehension variables are **local** to the comprehension:

```python
x = 10
print([x for x in range(3)])  # [0, 1, 2]
print(x)  # 10
```

### Python 2.x

The loop variable would leak into the outer scope (❌ bad practice).

---

## 📦 Modules and Import Scope

Each module has its **own global namespace**.

```python
# module_a.py
x = 1

# module_b.py
import module_a
print(module_a.x)
```

To expose variables:

```python
__all__ = ["x", "y"]
```

---

## 🧾 Built-in Scope

Accessed last in the LEGB chain.

```python
print(len)  # <built-in function len>
```

Use `__builtins__` (module or dict) to inspect or override — **use with care**:

```python
__builtins__.len = lambda x: 42  # ⚠️ do not do this in real code
```

---

## 🧪 Scope and Exec/Eval

`exec()` and `eval()` can modify or read scopes dynamically.

```python
x = 1
exec("x = 2")
print(x)  # 2
```

Use `globals()` and `locals()` explicitly with `exec()` to avoid scope pollution.

---

## 🔍 Scoping Summary

| Name Resolution     | Happens at compile-time (LEGB)         |
|---------------------|-----------------------------------------|
| Assignment          | Always affects **local scope** unless declared `global` or `nonlocal` |
| `global`            | Writes to the module’s namespace        |
| `nonlocal`          | Writes to nearest enclosing function scope |
| Classes             | Have their own scope; methods are closures only over outer scope |
| Lambdas             | Same scoping as nested functions        |
| Comprehensions      | Introduce their own scope (Python 3.x)  |
| Modules             | Each has its own global namespace       |

---

## ✅ Best Practices

- Use `nonlocal` for closures rather than mutable objects
- Avoid `global` unless absolutely necessary
- Don’t shadow built-in names like `list`, `type`, `id`
- Treat module globals as constants or configuration
- Avoid side effects in `exec()` and `eval()`

---

## 📚 Further Reading

- [Python Language Reference – Execution Model](https://docs.python.org/3/reference/executionmodel.html)
- [Python `globals()` and `locals()` docs](https://docs.python.org/3/library/functions.html#globals)
- [LEGB Rule Explained](https://realpython.com/python-scope-legb-rule/)
- Fluent Python — Chapter 7–9
- [PEP 572: Assignment Expressions (:=)](https://peps.python.org/pep-0572/)

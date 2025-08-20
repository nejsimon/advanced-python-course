
# Standard Library: Graphical User Interfaces (GUI)

Python’s standard library includes several modules for creating **graphical** or **interactive** interfaces, both windowed and terminal-based. While modern applications often use external GUI frameworks (PyQt, wxPython, Kivy), the built-in tools are useful for small apps, educational purposes, or terminal UIs.

---

## 1. `tkinter` — GUI Toolkit

- Python’s **de-facto standard GUI library**, a thin object-oriented layer on top of **Tcl/Tk**.
- Available on most Python installations by default.
- Provides windows, buttons, labels, text boxes, menus, dialogs, and event loops.

### Example
```python
import tkinter as tk

root = tk.Tk()
root.title("Hello Tkinter")

label = tk.Label(root, text="Hello, World!", font=("Arial", 16))
label.pack(padx=20, pady=20)

button = tk.Button(root, text="Quit", command=root.quit)
button.pack(pady=10)

root.mainloop()

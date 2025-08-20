# Coding Challenge: Dynamic Plugin Loader
Objective

Create a Python program that can dynamically discover and load plugins from a folder at runtime using the import system.

Tasks
1. Project Structure

Create a folder structure like this:

plugin_loader/
    plugins/
        plugin_a.py
        plugin_b.py
    loader.py


Each plugin defines a function run() that prints a message.

Example plugin_a.py:

def run():
    print("Plugin A executed!")

2. Dynamic Import

In loader.py:

Scan the plugins/ directory for Python files.

Import each module dynamically using importlib.

Call the run() function of each imported plugin.

3. Plugin Caching

Ensure that if a plugin is modified, you can reload it without restarting the program.

Hint: use importlib.reload().

4. Optional Advanced Task: Import Hooks

Implement a custom finder that logs every module imported from the plugins/ directory.

Use sys.meta_path to insert your finder.

Example Run
$ python loader.py
Plugin A executed!
Plugin B executed!

# After modifying plugin_b.py and rerunning:
Plugin A executed!
Plugin B executed!  # updated output

Hints

Use importlib.util.spec_from_file_location() and importlib.util.module_from_spec() for file-based dynamic imports.

Keep track of modules in sys.modules for reloads.

Wrap plugin execution in try/except to handle errors in individual plugins.

✅ Goal

Understand dynamic imports with importlib.

Use caching and module reloading.

Optional: explore meta-path hooks for advanced control.
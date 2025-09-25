# Coding Challenge: Multilingual Greeter
Part 1: Dictionary-based (Warm-up)

Write a Python program that:

Asks the user for their preferred language (en, fr, es, or de).

Prints a greeting message based on a dictionary of translations.

Falls back to English if the language is not supported.

Example dictionary:

translations = {
    "en": "Hello, welcome!",
    "fr": "Bonjour, bienvenue !",
    "es": "¡Hola, bienvenido!",
    "de": "Hallo, willkommen!"
}

Part 2: Using gettext with .po and .mo files

Create a directory structure for translations:

locale/
  fr/LC_MESSAGES/messages.po
  es/LC_MESSAGES/messages.po
  de/LC_MESSAGES/messages.po


In each .po file, add a translation for the message "Hello, welcome!". For example, fr/LC_MESSAGES/messages.po:

msgid "Hello, welcome!"
msgstr "Bonjour, bienvenue !"


Compile the .po files into .mo files using msgfmt (part of GNU gettext or available via Python tools):

msgfmt fr/LC_MESSAGES/messages.po -o fr/LC_MESSAGES/messages.mo
msgfmt es/LC_MESSAGES/messages.po -o es/LC_MESSAGES/messages.mo
msgfmt de/LC_MESSAGES/messages.po -o de/LC_MESSAGES/messages.mo


Write a Python program that:

Uses gettext.translation() to load the correct translation based on user input.

Falls back to English if the translation isn’t available.

Example code skeleton:

import gettext

lang = input("Choose a language (en, fr, es, de): ").strip()
try:
    translation = gettext.translation(
        "messages", localedir="locale", languages=[lang]
    )
    translation.install()
    _ = translation.gettext
except FileNotFoundError:
    _ = lambda s: s  # fallback to identity

print(_("Hello, welcome!"))
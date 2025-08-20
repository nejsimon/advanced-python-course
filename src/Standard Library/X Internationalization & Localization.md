# Standard Library: Internationalization & Localization

Python’s standard library provides several modules for adapting software to different **languages, regions, and cultural conventions**. This includes formatting numbers and dates, translating text, and handling time zones.

---

## 1. `locale` — Cultural Conventions

The `locale` module customizes **number formats, currency, sorting, and date formatting** based on cultural conventions.

### Example
```python
import locale

# Set locale to German (may vary by system)
locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')

# Format numbers
num = 1234567.89
print(locale.format_string("%.2f", num, grouping=True))  # 1.234.567,89

# Currency formatting
print(locale.currency(num, grouping=True))  # 1.234.567,89 €
Features
Formatting numbers, currency, and percentages.

String collation (locale-aware sorting).

Date/time formatting (limited).

Quirks
Locale availability depends on the OS configuration.

Not thread-safe (changing locale affects the whole process).

2. gettext — Message Translation
The gettext module handles translation of text strings into multiple languages.

Example
python
Copy code
import gettext

# Assume translation files are in ./locales/
t = gettext.translation("messages", localedir="locales", languages=["es"])
t.install()

print(_("Hello, World!"))  # "¡Hola, Mundo!" if Spanish translation exists
Features
Supports .po (portable object) and .mo (machine object) files.

Provides _() shorthand for marking translatable strings.

Allows runtime language switching.

Workflow
Mark strings in your code: _("Hello").

Extract strings with tools (xgettext).

Translate into .po files.

Compile to .mo and load with gettext.

3. calendar — Locale-Sensitive Calendars
The calendar module can display calendars with locale-sensitive day and month names.

Example
python
Copy code
import calendar
import locale

locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")

cal = calendar.TextCalendar(firstweekday=0)
print(cal.formatmonth(2025, 9))
This will print the September 2025 calendar with French month/day names.

4. Time Zones — zoneinfo (Python 3.9+)
The zoneinfo module provides IANA time zone support.

Example
python
Copy code
from zoneinfo import ZoneInfo
from datetime import datetime

dt = datetime(2025, 9, 23, 12, 0, tzinfo=ZoneInfo("Europe/Stockholm"))
print(dt)  # 2025-09-23 12:00:00+02:00
Features
Time zone conversion with official IANA database.

Daylight saving time handling.

Modern replacement for third-party pytz.

5. Best Practices
Use gettext for translations.

Use locale for formatting numbers/currency.

Use zoneinfo for time zones.

Don’t hard-code strings — mark them for translation (_("text")).

Always test with multiple locales.

Summary
Internationalization and localization in the standard library include:

locale: Formatting for numbers, currency, sorting.

gettext: Translating messages.

calendar: Locale-aware calendar displays.

zoneinfo: Time zone handling.

Together, these tools allow Python applications to adapt to different languages, regions, and cultures without third-party libraries.
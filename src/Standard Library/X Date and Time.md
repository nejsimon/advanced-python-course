# Standard Library: Date & Time

Python’s standard library provides several modules for working with dates, times, and time-related operations. These modules allow parsing, formatting, arithmetic, and working with time zones.

time — Low-level Time Functions

The time module provides functions for working with timestamps and interacting with the system clock.

import time

# Current Unix timestamp
now = time.time()
print(now)

# Sleep for 2 seconds
time.sleep(2)

# Convert timestamp to struct_time
struct = time.localtime(now)
print(struct.tm_year, struct.tm_mon, struct.tm_mday)

# Format time
print(time.strftime("%Y-%m-%d %H:%M:%S", struct))

datetime — High-level Date & Time Handling

The datetime module provides classes for dates, times, timedeltas, and timezone-aware arithmetic.

from datetime import datetime, timedelta, timezone

# Current date and time
now = datetime.now()
print(now)

# Create specific date
d = datetime(2025, 9, 23, 14, 30)
print(d)

# Arithmetic
tomorrow = now + timedelta(days=1)
print("Tomorrow:", tomorrow)

# Timezones
utc_now = datetime.now(timezone.utc)
print("UTC:", utc_now)


Common classes:

datetime.date — Calendar dates

datetime.time — Time of day

datetime.datetime — Date and time

datetime.timedelta — Duration

datetime.timezone — Time zone handling

calendar — Calendrical Functions

The calendar module helps with textual and logical calendar operations.

import calendar

# Print a text calendar
print(calendar.month(2025, 9))

# Check if a year is a leap year
print(calendar.isleap(2024))

# Weekday (0=Monday)
print(calendar.weekday(2025, 9, 23))

zoneinfo — IANA Time Zone Support (Python 3.9+)

The zoneinfo module provides access to the IANA time zone database.

from datetime import datetime
from zoneinfo import ZoneInfo

# Convert between time zones
dt = datetime(2025, 9, 23, 12, 0, tzinfo=ZoneInfo("UTC"))
local_dt = dt.astimezone(ZoneInfo("Europe/Stockholm"))
print(local_dt)


✅ Summary

Use time for timestamps and low-level operations.

Use datetime for most date/time manipulations.

Use calendar for calendar-related tasks.

Use zoneinfo for time zone conversions.
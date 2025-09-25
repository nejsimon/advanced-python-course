# Coding Challenge: Event Countdown Timer
Task

Write a Python script that:

Asks the user to input a future date and time in the format:

YYYY-MM-DD HH:MM


Parses the input into a datetime object.

Calculates the remaining time until that date.

Prints the result as:

Event starts in X days, Y hours, Z minutes, W seconds


If the input date is in the past, print:

The event has already passed!

Example Run
Enter event date and time (YYYY-MM-DD HH:MM): 2025-12-31 23:59
Event starts in 99 days, 4 hours, 30 minutes, 12 seconds

Hints

Use datetime.strptime to parse the string.

Use datetime.now() to get the current time.

Subtract the two to get a timedelta.

Break down timedelta.total_seconds() into days, hours, minutes, seconds.
# Days until your event - Flexible Date & time parser with live refresh and percentage bar
import os
from datetime import datetime
from dateutil import parser
import time

# ask until user gives a parsable date/time
def get_valid_datetime():
    while True:
        user_input = input("\n Enter your Target date (and optional time): \n"
                           "Example: 2025-08-13, 13/08/2023, Aug 13 2025 15:30, "
                           "Aug 11 15:30\n >> ").strip()
        try:
            target_date = parser.parse(user_input, default=datetime(1900,1, 1)) # Default year 1900 we can detect if year was omitted
            return target_date
        except Exception:
            print(" INVALID FORMAT.  Try again with examples like '2025-08-11' or 'Aug 11, 2025 14:30'.  ")

# resolve missing years and recurrences
def get_next_occurrence(target_date):
    now = datetime.now()

    # if user did not specify year, assume this year
    if target_date.year == 1900:
        target_date = target_date.replace(year=now.year)

    # if the target datetime is in the past , roll forward one year
    if  target_date < now:
        target_date = target_date.replace(year=target_date.year + 1)

    return target_date

# break a timedelta into readable parts
def format_time_difference(delta):
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes = remainder // 60
    seconds = remainder % 60
    return days, hours, minutes, seconds

# The visual bar
def progress_bar(percentage, width=30):
    filled_length = int(width * percentage)
    bar = "|_|" * filled_length + "-" * (width - filled_length)
    return f"|{bar}| {percentage*100:5.1f}%"

# Add everything and run the live loop
def main():
    print(" Countdown Tool -  Live Refresh with progress bar")
    target_date = get_valid_datetime()
    target_date = get_next_occurrence(target_date)

    weekday_name = target_date.strftime("%A")
    is_weekend = weekday_name in ["Saturday", "Sunday"]

    total_seconds = (target_date - datetime.now()).total_seconds()

    try:
        while True:
            os.system("cls" if os.name == "nt" else "clear") # Clear screen for live refresh
            now = datetime.now()
            time_left = target_date - now

            if time_left.total_seconds() <= 0:
                print(" The event time has arrived! ")
                break

            days, hours, minutes, seconds = format_time_difference(time_left)
            elapsed_seconds = total_seconds - time_left.total_seconds()
            percentage = max(0.0, min(1.0, elapsed_seconds / total_seconds))

            print(f" Event Details")
            print(f"Date: {target_date.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Weekday: {weekday_name} {'(weekend)' if is_weekend else '(weekday)'}")
            print(f" Time remaining: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
            print(progress_bar(percentage))

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nCountdown stopped by user. ")

if __name__ == "__main__":
    main()






# Weekly Schedule Builder
import json
import os

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
TIME_BLOCKS = ["Morning", "Afternoon", "Evening"]
SAVE_FILE = "weekly_schedule.json"


def init_schedule(days=DAYS, blocks=TIME_BLOCKS):
    """Return an empty schedule: dict of dicts {day: {block: ''}}."""
    return {day: {tbk: "" for tbk in blocks} for day in days}


def prompt_schedule(schedule):
    """
    Use nested loops to prompt the user to enter a task for each day/time-block.
    Empty input = skip (keeps it blank).
    """
    print("\nEnter tasks for each day/time block. Press Enter to skip a block.\n")
    for day in schedule:
        print(f"--- {day} ---")
        for tbk in schedule[day]:
            prompt = f"{tbk}: "
            val = input(prompt).strip()
            if val:  # non-empty -> save
                schedule[day][tbk] = val
        print()
    return schedule


def display_schedule(schedule):
    """Display schedule in a readable grid (rows = time blocks, columns = days)."""
    # compute column widths
    col_widths = {}
    day_name_width = max(len(day) for day in schedule.keys())
    col_widths["time"] = max(max(len(tbk) for tbk in TIME_BLOCKS), 8)
    for day in schedule:
        max_task_len = max((len(schedule[day][tbk]) for tbk in schedule[day]), default=0)
        col_widths[day] = max(len(day), max_task_len, 10)

    # header
    header = " " * (col_widths["time"] + 3)
    for day in schedule:
        header += day.ljust(col_widths[day] + 3)
    print(header)
    print("-" * len(header))

    # rows (time blocks)
    for tbk in TIME_BLOCKS:
        row = tbk.ljust(col_widths["time"] + 3)
        for day in schedule:
            cell = schedule[day].get(tbk, "")
            row += cell.ljust(col_widths[day] + 3)
        print(row)
    print()  # final newline


def save_schedule(schedule, filename=SAVE_FILE):
    """Save schedule to JSON file."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(schedule, file, indent=2)
        print(f"Schedule saved to {filename}")
    except Exception as err:
        print("Error saving schedule:", err)


def load_schedule(filename=SAVE_FILE):
    """Load schedule from JSON file if it exists, else return None."""
    if not os.path.exists(filename):
        return None
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as err:
        print("Error loading schedule:", err)
        return None


def main():
    print("Weekly Schedule Builder (CLI)")
    loaded = load_schedule()
    if loaded:
        use_loaded = input("Found an existing schedule. Load it? (y/N): ").strip().lower() == "y"
        if use_loaded:
            schedule = loaded
        else:
            schedule = init_schedule()
    else:
        schedule = init_schedule()

    # display blank or loaded schedule
    print("\nCurrent schedule:")
    display_schedule(schedule)

    # prompt user to fill in schedule using nested loops
    prompt_schedule(schedule)

    # final display and save choice
    print("\nFinal schedule:")
    display_schedule(schedule)
    if input("Save schedule to file? (Y/n): ").strip().lower() != "n":
        save_schedule(schedule)


if __name__ == "__main__":
    main()
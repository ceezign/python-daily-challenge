
# Pomodoro / Timebox Tracker (Tkinter)
# ------------------------------------
# A lightweight GUI app to run Focus/Break timeboxes (Pomodoro-style).
# Features:
# - Start / Pause / Resume / Reset / Skip
# - Custom focus & break lengths (minutes)
# - Auto-switch between Focus and Break
# - Optional long break after N focus sessions
# - Optional Task name to tag sessions
# - Optional CSV logging (date, task name, focus minutes)
#
# Dependencies: Only Python 3 standard library (tkinter is bundled).

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import csv
import os
from typing import Optional


def mmss(seconds: int) -> str:
    """Return seconds as MM:SS string."""
    m = seconds // 60
    s = seconds % 60
    return f"{m:02d}:{s:02d}"


class PomodoroApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Timeboxed Task Tracker")
        self.resizable(False, False)

        # -------------------- State & Tk Variables --------------------
        # User-configurable settings
        self.focus_min_var = tk.IntVar(value=25)
        self.break_min_var = tk.IntVar(value=5)
        self.long_break_min_var = tk.IntVar(value=15)
        self.long_break_every_var = tk.IntVar(value=4)
        self.use_long_break_var = tk.BooleanVar(value=True)
        self.log_csv_var = tk.BooleanVar(value=False)  # off by default

        self.task_var = tk.StringVar(value="")

        # Live state
        self.mode_var = tk.StringVar(value="Focus")  # "Focus", "Break", "Long Break"
        self.completed_var = tk.IntVar(value=0)      # completed focus sessions this run
        self.remaining_seconds = self.focus_min_var.get() * 60
        self.running = False
        self._job: Optional[str] = None  # after() job id for the ticking timer

        # CSV path (same folder as this script)
        self.csv_path = os.path.join(os.path.dirname(__file__), "session_history.csv")

        # -------------------- UI --------------------
        self._build_ui()

        # Update timer initially
        self._update_timer_label()

        # When focus/break inputs change and we're idle in that mode, refresh remaining
        self.focus_min_var.trace_add("write", lambda *args: self._maybe_refresh_seconds("Focus"))
        self.break_min_var.trace_add("write", lambda *args: self._maybe_refresh_seconds("Break"))
        self.long_break_min_var.trace_add("write", lambda *args: self._maybe_refresh_seconds("Long Break"))

    # -------------------- UI Construction --------------------
    def _build_ui(self):
        pad = 8

        # Inputs frame
        inputs = ttk.LabelFrame(self, text="Session Settings")
        inputs.grid(row=0, column=0, padx=pad, pady=(pad, 0), sticky="ew")

        ttk.Label(inputs, text="Focus (min)").grid(row=0, column=0, padx=pad, pady=pad, sticky="w")
        ttk.Spinbox(inputs, from_=1, to=180, textvariable=self.focus_min_var, width=6).grid(row=0, column=1, padx=pad, pady=pad)

        ttk.Label(inputs, text="Break (min)").grid(row=0, column=2, padx=pad, pady=pad, sticky="w")
        ttk.Spinbox(inputs, from_=1, to=60, textvariable=self.break_min_var, width=6).grid(row=0, column=3, padx=pad, pady=pad)

        ttk.Label(inputs, text="Task (optional)").grid(row=1, column=0, padx=pad, pady=pad, sticky="w")
        ttk.Entry(inputs, textvariable=self.task_var, width=36).grid(row=1, column=1, columnspan=3, padx=pad, pady=pad, sticky="ew")

        # Long break options
        long_frame = ttk.Frame(inputs)
        long_frame.grid(row=2, column=0, columnspan=4, padx=pad, pady=(0, pad), sticky="w")
        ttk.Checkbutton(long_frame, text="Long break every", variable=self.use_long_break_var).grid(row=0, column=0, padx=(0, 4))
        ttk.Spinbox(long_frame, from_=2, to=12, textvariable=self.long_break_every_var, width=4).grid(row=0, column=1)
        ttk.Label(long_frame, text="focus sessions, for").grid(row=0, column=2, padx=4)
        ttk.Spinbox(long_frame, from_=5, to=60, textvariable=self.long_break_min_var, width=4).grid(row=0, column=3)
        ttk.Label(long_frame, text="min").grid(row=0, column=4, padx=(4, 12))
        ttk.Checkbutton(long_frame, text="Log finished focus sessions to CSV", variable=self.log_csv_var).grid(row=0, column=5)

        # Mode + big timer
        mid = ttk.Frame(self)
        mid.grid(row=1, column=0, padx=pad, pady=pad, sticky="ew")
        ttk.Label(mid, text="Mode:").grid(row=0, column=0, sticky="w")
        self.mode_label = ttk.Label(mid, textvariable=self.mode_var, font=("Helvetica", 12, "bold"))
        self.mode_label.grid(row=0, column=1, sticky="w", padx=(4, 0))

        self.timer_label = ttk.Label(self, text="00:00", font=("Helvetica", 48, "bold"))
        self.timer_label.grid(row=2, column=0, padx=pad, pady=(0, pad), sticky="n")

        # Completed summary
        self.summary_label = ttk.Label(self, text=f"Completed sessions: {self.completed_var.get()}")
        self.summary_label.grid(row=3, column=0, padx=pad, sticky="w")
        # Update this label whenever completed_var changes
        self.completed_var.trace_add("write", lambda *args: self.summary_label.config(
            text=f"Completed sessions: {self.completed_var.get()}")
        )

        # Controls
        controls = ttk.Frame(self)
        controls.grid(row=4, column=0, padx=pad, pady=(0, pad))

        self.start_btn = ttk.Button(controls, text="Start", command=self.start)
        self.start_btn.grid(row=0, column=0, padx=pad, pady=pad)

        self.pause_btn = ttk.Button(controls, text="Pause", command=self.pause_resume, state="disabled")
        self.pause_btn.grid(row=0, column=1, padx=pad, pady=pad)

        self.reset_btn = ttk.Button(controls, text="Reset", command=self.reset, state="disabled")
        self.reset_btn.grid(row=0, column=2, padx=pad, pady=pad)

        self.skip_btn = ttk.Button(controls, text="Skip", command=self.skip, state="disabled")
        self.skip_btn.grid(row=0, column=3, padx=pad, pady=pad)

    # -------------------- Controls --------------------
    def start(self):
        """Start (or restart) a focus session."""
        # Initialize if user presses Start anytime
        self._cancel_job()
        self.completed_var.set(self.completed_var.get())  # no-op to trigger label update
        self._start_focus(fresh=True)

        # Enable relevant buttons
        self.pause_btn.config(state="normal", text="Pause")
        self.reset_btn.config(state="normal")
        self.skip_btn.config(state="normal")

    def pause_resume(self):
        if not self.running:
            # Resume
            self.running = True
            self.pause_btn.config(text="Pause")
            self._schedule_tick()
        else:
            # Pause
            self.running = False
            self.pause_btn.config(text="Resume")
            self._cancel_job()

    def reset(self):
        self._cancel_job()
        self.running = False
        self.mode_var.set("Focus")
        self.remaining_seconds = max(1, int(self.focus_min_var.get())) * 60
        self.completed_var.set(0)
        self._update_timer_label()

        # Disable some controls until Start again
        self.pause_btn.config(state="disabled", text="Pause")
        self.reset_btn.config(state="disabled")
        self.skip_btn.config(state="disabled")

    def skip(self):
        """Jump to the next session type without logging/adding completion."""
        self._cancel_job()
        self.running = False
        current = self.mode_var.get()
        if current == "Focus":
            # go to a break (respect long break cadence), but do NOT increment or log
            if self.use_long_break_var.get() and self.completed_var.get() > 0 and \
               self.completed_var.get() % max(1, int(self.long_break_every_var.get())) == 0:
                self._start_long_break(auto=True)
            else:
                self._start_break(auto=True)
        else:
            # from break -> next focus
            self._start_focus(fresh=False)

    # -------------------- Session Helpers --------------------
    def _start_focus(self, fresh: bool):
        self.mode_var.set("Focus")
        self.remaining_seconds = max(1, int(self.focus_min_var.get())) * 60
        self.running = True
        self._update_timer_label()
        self._schedule_tick()
        if fresh:
            self.bell()  # small cue when (re)starting

    def _start_break(self, auto: bool = False):
        self.mode_var.set("Break")
        self.remaining_seconds = max(1, int(self.break_min_var.get())) * 60
        self.running = True
        self._update_timer_label()
        self._schedule_tick()
        if auto:
            self.bell()

    def _start_long_break(self, auto: bool = False):
        self.mode_var.set("Long Break")
        self.remaining_seconds = max(1, int(self.long_break_min_var.get())) * 60
        self.running = True
        self._update_timer_label()
        self._schedule_tick()
        if auto:
            self.bell()

    def _maybe_refresh_seconds(self, target_mode: str):
        """If currently idle (not running) and in the given mode, refresh the remaining time to new input."""
        if not self.running and self.mode_var.get() == target_mode:
            mins = {
                "Focus": self.focus_min_var.get(),
                "Break": self.break_min_var.get(),
                "Long Break": self.long_break_min_var.get(),
            }[target_mode]
            self.remaining_seconds = max(1, int(mins)) * 60
            self._update_timer_label()

    def _schedule_tick(self):
        self._cancel_job()
        self._job = self.after(1000, self._tick)

    def _cancel_job(self):
        if self._job is not None:
            try:
                self.after_cancel(self._job)
            except Exception:
                pass
        self._job = None

    def _tick(self):
        if not self.running:
            return
        self.remaining_seconds -= 1
        self._update_timer_label()

        if self.remaining_seconds <= 0:
            self._on_session_end()
        else:
            self._schedule_tick()

    def _on_session_end(self):
        """Handle end of current (Focus/Break/Long Break) session: beep, log, switch."""
        self.bell()  # simple cross-platform beep/visual cue

        mode = self.mode_var.get()
        if mode == "Focus":
            # record completion
            self.completed_var.set(self.completed_var.get() + 1)
            if self.log_csv_var.get():
                self._log_focus_session()

            # choose break type
            if self.use_long_break_var.get() and \
               self.completed_var.get() % max(1, int(self.long_break_every_var.get())) == 0:
                self._start_long_break(auto=True)
            else:
                self._start_break(auto=True)

        else:
            # From any break -> start focus
            self._start_focus(fresh=False)

    def _log_focus_session(self):
        """Append a line to CSV with timestamp, task name, and focus minutes."""
        row = [
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            self.task_var.get().strip(),
            int(self.focus_min_var.get())
        ]

        file_exists = os.path.exists(self.csv_path)
        try:
            with open(self.csv_path, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                if not file_exists:
                    writer.writerow(["timestamp", "task", "focus_minutes"])
                writer.writerow(row)
        except Exception as e:
            messagebox.showerror("CSV Logging Error", f"Could not write to CSV:\n{e}")

    def _update_timer_label(self):
        self.timer_label.config(text=mmss(max(0, int(self.remaining_seconds))))


if __name__ == "__main__":
    app = PomodoroApp()
    app.mainloop()

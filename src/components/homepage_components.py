from customtkinter import CTkButton,CTkCheckBox,CTkFrame,CTkEntry,CTkSwitch
from tkinter import Label
from vendor.Rocket import log,add_scrollbar,threaded
import tkinter as tk
from tkinter import Frame,Canvas
from src.helper.database import *
from boxdb.support import get_elements
from boxdb import update_row

global COLORS
# Color theme configuration
COLORS = {
    "bg": "#FFFFFF",        # Pure white background
    "secondary": "#F2F2F2",  # Very light gray background for sections
    "accent": "#DADADA",    # Light gray accent color
    "hover": "#BFBFBF",     # Medium gray hover effect
    "text": "#1C1C1C",      # Dark gray text for better contrast
    "subtext": "#5E5E5E",   # Medium dark gray for subtext
    "input_bg": "#FFFFFF",  # White background for input fields
    "input_text": "#1C1C1C" # Dark gray text for input fields
}


DARK_COLORS = {
    "bg": "#18181B",        # Zinc-900 equivalent
    "secondary": "#27272A",  # Zinc-800 equivalent
    "accent": "#3F3F46",    # Zinc-700 equivalent
    "hover": "#52525B",     # Zinc-600 equivalent
    "text": "#FFFFFF",      # White text
    "subtext": "#A1A1AA",   # Zinc-400 equivalent
    "input_bg": "#FFFFFF",  # White background for input
    "input_text": "#000000" # Black text for input
}
LIGHT_COLORS = {
    "bg": "#FFFFFF",        # White background
    "secondary": "#F0F0F0",  # Very light gray background for sections
    "accent": "#D0D0D0",    # Light gray accent color
    "hover": "#CCCCCC",     # Medium gray hover effect
    "text": "#000000",      # Black text for better contrast
    "subtext": "#333333",   # Darker gray for subtext
    "input_bg": "#FFFFFF",  # White background for input fields
    "input_text": "#000000" # Black text for input fields
}

toggle_state = {"dark_mode": False}

def darkmode(header , window):
    """Create a dark mode toggle switch and check its state."""
    
    toggle = CTkSwitch(header, text="Dark Mode",text_color=COLORS["text"])
    toggle.pack(side="right", padx=10, pady=5)

    if toggle_state["dark_mode"]:
        toggle.select()
    else:
        toggle.deselect()

    toggle.configure(command=lambda: check_toggle_state(window, toggle))

def check_toggle_state(window, toggle):
    """Check the state of the toggle and switch themes accordingly."""
    toggle_state["dark_mode"] = toggle.get()
    if toggle_state["dark_mode"]:
        log("Dark Mode is ON")
        COLORS.update(DARK_COLORS)
    else:  
        log("Light Mode is ON")
        COLORS.update(LIGHT_COLORS)
    toggle_mode(window)

def todo_header(window):
    """Create the header for the to-do list."""
    header_frame = Frame(window, bg=COLORS["secondary"])
    header_frame.pack(fill="x", anchor="n")

    header_label = Label(
        header_frame,
        text="To-Do List",
        font=("Helvetica", 16, "bold"),
        fg=COLORS["text"],
        bg=COLORS["secondary"],
        pady=8
    )
    header_label.pack(side="left", padx=10)

    darkmode(header_frame,window)

def no_tasks_message(window):
    """Display a message when no tasks are available."""
    no_task_frame = Frame(window, bg=COLORS["bg"], pady=20)
    no_task_frame.pack(pady=30, fill="x")

    no_task_label = Label(
        no_task_frame,
        text="No tasks here, why not add one?",
        font=("Helvetica", 12, "italic"),
        fg=COLORS["subtext"],
        bg=COLORS["bg"],
    )
    no_task_label.pack()
@threaded
def todo_list(window, database, table_name):
    """Render the list of tasks."""
    main_frame = Frame(window, bg=COLORS["bg"], name="todolist")
    main_frame.pack(fill="both", expand=True)

    Label(main_frame, text="", bg=COLORS["bg"]).pack(pady=5)

    # Fetch all tasks and statuses at once
    task_status_list = get_all_elements(database, table_name) 
    if not task_status_list:
        no_tasks_message(main_frame)
        return

    # Add scrollbar to the task list
    _, scrollable_frame = add_scrollbar(main_frame, COLORS["bg"])

    def update_task_status(task, status_var):
        new_status = "True" if status_var.get() else "False"
        update_row(database, table_name, task, "status", new_status)

    for task, status in task_status_list:
        frame = Frame(scrollable_frame, bg=COLORS["bg"])
        frame.pack(fill="x", padx=20, pady=5)

        status_var = tk.BooleanVar(value=status)

        CTkCheckBox(
            frame,
            text=f"{task}",
            text_color=COLORS["text"],
            variable=status_var,
            corner_radius=100,
            border_width=2,
            checkbox_height=15,
            checkbox_width=15,
            font=("Arial", 14),
            command=update_task_status(task, status_var)
        ).pack(side="left", padx=5)

        CTkButton(
            frame,
            text="Delete",
            border_width=0,
            hover_color=COLORS["hover"],
            fg_color=COLORS["accent"],
            text_color=COLORS["text"],
            width=60,
            height=28,
            corner_radius=6,
            command=delete_task(task, window)
        ).pack(side="right", padx=5)


def todo_list(window, database, table_name):
    """Render the list of tasks."""
    main_frame = Frame(window, bg=COLORS["bg"], name="todolist")
    main_frame.pack(fill="both", expand=True)

    Label(main_frame, text="", bg=COLORS["bg"]).pack(pady=5)

    task_ = get_elements(database, table_name, "task")
    status_ = get_elements(database, table_name, "status")

    if not task_:
        no_tasks_message(main_frame)
        return

    # Add scrollbar to the task list
    _, scrollable_frame = add_scrollbar(main_frame, COLORS["bg"])

    def update_task_status(task, status_var):
        new_status = "True" if status_var.get() else "False"
        update_row(database, table_name, task, "status", new_status)

    for task, status in zip(task_, status_):
        frame = Frame(scrollable_frame, bg=COLORS["bg"])
        frame.pack(fill="x", padx=20, pady=5)

        status_var = tk.BooleanVar(value=status)

        # Checkbox with aligned label
        CTkCheckBox(
            frame,
            text=f"{task}",
            text_color=COLORS["text"],
            variable=status_var,
            corner_radius=100,
            border_width=2,
            checkbox_height=15,
            checkbox_width=15,
            font=("Arial", 14),
            command=lambda task=task, s_var=status_var: update_task_status(task, s_var)
        ).pack(side="left", padx=5)

        # Delete button
        CTkButton(
            frame,
            text="Delete",
            border_width=0,
            hover_color=COLORS["hover"],
            fg_color=COLORS["accent"],
            text_color=COLORS["text"],
            width=60,
            height=28,
            corner_radius=6,
            command=lambda task=task: delete_task(task, window)
        ).pack(side="right", padx=5)


def add_task(window):
    """Create the add task input field and button."""
    bottom_frame = CTkFrame(
        window,
        bg_color=COLORS["bg"],
        fg_color=COLORS["secondary"],
        border_color=COLORS["secondary"]
    )
    bottom_frame.pack(side="bottom", fill="x", padx=0, pady=0)

    inner_frame = CTkFrame(
        bottom_frame,
        bg_color=COLORS["secondary"],
        fg_color=COLORS["secondary"],
        border_color=COLORS["secondary"]
    )
    inner_frame.pack(fill="x", padx=16, pady=16)

    # Input field
    task_entry = CTkEntry(
        inner_frame,
        placeholder_text="Add task",
        fg_color=COLORS["input_bg"],
        text_color=COLORS["input_text"],
        border_color=COLORS["secondary"],
        placeholder_text_color=COLORS["subtext"],
        height=32
    )
    task_entry.pack(side="left", fill="x", expand=True, padx=(0, 8))

    # Add task button
    add_task_button = CTkButton(
        inner_frame,
        text="Add Task",
        border_width=0,
        hover_color=COLORS["hover"],
        fg_color=COLORS["accent"],
        text_color=COLORS["text"],
        width=80,
        height=32,
        corner_radius=6,
        font=("Helvetica", 11),
        command=lambda: add_task_db(task_entry, window)
    )
    add_task_button.pack(side="right")


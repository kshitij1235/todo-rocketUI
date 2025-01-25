from customtkinter import CTkButton,CTkCheckBox,CTkFrame,CTkEntry,CTkSwitch
from tkinter import Label
from vendor.Rocket import log,add_scrollbar,threaded,component_render
import tkinter as tk
from tkinter import Frame,Canvas
from src.helper.database import *
from boxdb.support import get_elements
from boxdb import update_row
from vendor.Rocket import Components
from src.Theme_controller import app_theme

def add_task(window):
    """Create the add task input field and button."""
    comp= Components(window,app_theme)
    bottom_frame = comp.Rframe(
        window
    )
    bottom_frame.pack(side="bottom", fill="x", padx=0, pady=0)

    inner_frame =  comp.Rframe(
        bottom_frame,
    )
    inner_frame.pack(fill="x", padx=16, pady=16)

    task_entry = comp.Rentry(
        inner_frame,
        placeholder_text="Add task",
        height=32
    )
    task_entry.pack(side="left", fill="x", expand=True, padx=(0, 8))

    # Add task button
    add_task_button = comp.Rbutton(
        inner_frame,
        text="Add Task",
        border_width=0,
        width=80,
        height=32,
        corner_radius=6,
        font=("Helvetica", 11),
        command=lambda: add_task_db(task_entry, window)
    )
    add_task_button.pack(side="right")


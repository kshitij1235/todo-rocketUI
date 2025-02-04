from customtkinter import CTkButton, CTkCheckBox
from boxdb import update_row 
from boxdb.support import get_elements
from vendor.Rocket import add_scrollbar, component_render
from vendor.Rocket.components import Components
from src.ControllerManager import app_theme
import tkinter as tk
from src.helper.database import *


def no_tasks_message(window):
    """Display a message when no tasks are available."""
    comp = Components(window, app_theme)

    no_task_frame = comp.Rframe(window,pady=20)
    no_task_frame.pack(pady=30, fill="x")

    no_task_label = comp.Rlabels(
        no_task_frame,
        text="No tasks here, why not add one?",
        font=("Helvetica", 12, "italic"),
    )
    no_task_label.pack()

    
def todo_list(window, database, table_name):
    """Render the list of tasks."""
    comp = Components(window, app_theme)

    main_frame = comp.Rframe(window, name="todolist")
    main_frame.pack(fill="both", expand=True)

    comp.Rlabels(main_frame, text="").pack(pady=5)

    # Fetch data from database
    task_ = get_elements(database, table_name, "task")
    status_ = get_elements(database, table_name, "status")

    if not task_:
        no_tasks_message(main_frame)  
        return

    _, scrollable_frame = add_scrollbar(main_frame,app_theme.get_color("bg"))

    # Function to update task status in the database
    def update_task_status(task, status_var):
        new_status = "True" if status_var.get() else "False"
        update_row(database, table_name, task, "status", new_status)

    # Create a single frame to hold all the tasks, avoiding re-packing each task in every loop iteration
    task_frames = []

    for task, status in zip(task_, status_):
        task_frame = comp.Rframe(scrollable_frame)
        task_frame.pack(fill="x", padx=20, pady=5)

        task_frame_component(task_frame,window,task,status)

        task_frames.append(task_frame)  
    component_render(task_frames)



def task_frame_component(task_window ,window,task,status):

    comp = Components(window, app_theme)
    status_var = tk.BooleanVar(value=status)
    # Create checkbox for task with the update command in a more efficient way
    checkbox = comp.Rcheckbox(
        task_window,
        text=f"{task}",
        variable=status_var,
        corner_radius=100,
        border_width=2,
        checkbox_height=15,
        checkbox_width=15,
        font=("Arial", 14),
        command=lambda t=task, s=status_var: update_task_status(t, s)
    )
    checkbox.pack(side="left", padx=5)
    # Create delete button for the task with optimized command handling
    delete_button = comp.Rbutton(
        task_window,
        text="Delete",
        border_width=0,
        width=60,
        height=28,
        corner_radius=6,
        command=lambda t=task: delete_task(t, window)
    )
    delete_button.pack(side="right", padx=5)

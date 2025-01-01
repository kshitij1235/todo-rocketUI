from vendor.Rocket import rerender,rerender_component,threaded , get_element_by_name
from boxdb import remove_row,add_row
import tkinter as tk

def add_task_db(task_entry, window):
    from src.components.homepage_components import todo_list
    from src.homepages import homepage
    """Add a new task to the database."""
    from src.homepages import homepage
    task_text = task_entry.get().strip()
    if not task_text:
        print("Task cannot be empty!")
        return
    add_row("rocketdb", "tasks", (task_text, False))
    task_entry.delete(0, tk.END)

    rerender_component(get_element_by_name(window,"todolist"),todo_list,"rocketdb","tasks")

def toggle_mode(window):
    from src.homepages import homepage
    rerender(window,homepage)

def delete_task(task, root):
    """Delete a task and re-render the UI."""    
    from src.components.homepage_components import todo_list
    from src.homepages import homepage
    remove_row("rocketdb", "tasks", task)
    # rerender(window,homepage)
    rerender_component(get_element_by_name(root,"todolist"),todo_list,"rocketdb","tasks")
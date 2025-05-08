from src.components.todo_components import todo_list
from src.components.bottom_bar_component import add_task
from src.navigation_bar import create_bottom_nav
from tkinter import Frame


def homepage(window)->Frame: 
    from src.components.header_components import todo_header

    homepage_frame = Frame(window)
    todo_header(homepage_frame,"To-do List")
    todo_list(homepage_frame, "rocketdb", "tasks")
    add_task(homepage_frame)
    homepage_frame.pack(expand=True , fill="both")
    return homepage_frame

def settings(window)->Frame:
    from src.components.header_components import todo_header
    settings_frame = Frame(window)
    todo_header(settings_frame,"Settings")
    settings_frame.pack(expand=True , fill="both")
    
    return settings_frame


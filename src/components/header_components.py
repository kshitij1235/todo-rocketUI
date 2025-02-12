from customtkinter import CTkSwitch
from tkinter import Label, Frame
import tkinter as tk
from src.ControllerManager import app_theme  
from vendor.Rocket.components import Components
from vendor.Rocket import rerender




def check_toggle_state(window, toggle):
    """Check the state of the toggle and switch themes accordingly."""
    from src.homepages import main_screen
    if app_theme.isdark():
        app_theme.switch_theme(False)  
    else:
        app_theme.switch_theme(True)   
    rerender(window,main_screen)

      

def todo_header(window,title):
    """Create the header for the to-do list."""

    comp = Components(window , app_theme)

    header_frame = comp.Rframe(window)
    header_frame.pack(fill="x", anchor="n")

    header_label = comp.Rlabels(header_frame,
    text=title,
    font=("Helvetica", 16, "bold"),
    pady=8
    )
    header_label.pack(side="left", padx=10)

    toggle = CTkSwitch(header_frame, text="Dark Mode", text_color=app_theme.get_color("text"))
    toggle.pack(side="right", padx=10, pady=5)

    if app_theme.isdark():
        toggle.select()
    else:
        toggle.deselect()
    
    toggle.configure(command=lambda: check_toggle_state(window, toggle))

    return header_frame


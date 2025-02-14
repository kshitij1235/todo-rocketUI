import tkinter as tk
from tkinter import Canvas  ,Frame
from functools import wraps
from vendor.Rocket.components import Components
from app.ControllerManager import app_theme
from vendor.Rocket import log
from customtkinter import CTkFrame, CTkButton
from app.ControllerManager import save_state


def add_scrollbar(parent, bg_color):
    """
    Adds a scrollable frame with a vertical scrollbar to the parent widget.
    
    Parameters:
        parent: The parent widget where the scrollable frame will be added.
        bg_color: Background color for the scrollable frame.
    
    Returns:
        A tuple (canvas, scrollable_frame), where:
        - canvas: The Canvas widget containing the scrollable frame.
        - scrollable_frame: The Frame widget where content can be added.
    """

    
    canvas = Canvas(parent, bg=bg_color, highlightthickness=0)
    scrollbar = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas, bg=bg_color)

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def on_frame_configure(event):
        canvas.update_idletasks()
        bbox = canvas.bbox("all")  
        if bbox:  
            canvas.configure(scrollregion=bbox)

    scrollable_frame.bind("<Configure>", on_frame_configure)

    # Limit mousewheel scrolling to the bounds of the content
    def on_mousewheel(event):
        if canvas.bbox("all"):
            content_height = canvas.bbox("all")[3]
            visible_height = canvas.winfo_height()
            if content_height > visible_height:  # Only scroll if content overflows
                canvas.yview_scroll(-1 * (event.delta // 120), "units")

    canvas.bind_all("<MouseWheel>", on_mousewheel)

    return canvas, scrollable_frame


class BottomNavBar:
    def __init__(self, window, main_frame):
        self.window = window
        self.nav_frame = CTkFrame(self.window, fg_color="gray", height=50)
        self.nav_frame.pack(side="bottom", fill="x")
        self.options = []
        self.pages = {}
        self.main_frame = main_frame

    def add_option(self, text, component, component_name, fg_color="gray", hover_color="black"):
        """
        Add a single navigation option using a builder-like pattern.
        """
        self.options.append({
            "text": text,
            "component": component,
            "component_name": component_name,
            "fg_color": fg_color,
            "hover_color": hover_color
        })
        return self  

    def build(self):
        for option in self.options:
            btn = CTkButton(
                self.nav_frame,
                text=option["text"],
                fg_color=option["fg_color"],
                hover_color=option["hover_color"],
                corner_radius=0,
                command=lambda comp=option["component"], name=option["component_name"]: self.switcher(comp, name)
            )
            btn.pack(side="left", expand=True, fill="both")

    def switcher(self, component, key):
        """
        Clear the window and display the new form.
        """
        if key not in self.pages:
            self.pages[key] = component
        for widget in self.main_frame.winfo_children():
            if widget != self.nav_frame:  
                widget.pack_forget()
        self.pages[key](self.main_frame).pack(expand=True, fill="both")
      
        save_state.AssingValue("global","current_page",component)

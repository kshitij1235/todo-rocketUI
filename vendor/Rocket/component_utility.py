import tkinter as tk
from tkinter import Canvas  ,Frame

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
    # Create a canvas and a scrollbar
    canvas = Canvas(parent, bg=bg_color, highlightthickness=0)
    scrollbar = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas, bg=bg_color)

    # Configure the canvas
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Ensure the scroll region is updated when the contents of the frame change
    def on_frame_configure(event):
        canvas.update_idletasks()
        bbox = canvas.bbox("all")  # Get bounding box of the scrollable frame
        if bbox:  # Ensure bbox is not None
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

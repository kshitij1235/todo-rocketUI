from customtkinter import *
from vendor.Rocket import rerender_component,rerender


pages = {}

def create_bottom_nav(window):

    from src.homepages import homepage, settings
    nav_frame = CTkFrame(window, fg_color="gray", height=100)
    nav_frame.pack(side="bottom", fill="x")

    btn_home = CTkButton(nav_frame, text="New Form",
                         fg_color="gray", 
                         hover_color="black",
                         corner_radius=0,
                         command=lambda: switcher(window,homepage , "homepage"))
    btn_home.pack(side="left", expand=True, fill="both")

    btn_profile = CTkButton(nav_frame, text="Existing Forms",
                            fg_color="gray", 
                            hover_color="black",
                            corner_radius=0,
                            command=lambda:switcher(window,settings,"settings"))
    btn_profile.pack(side="left", expand=True, fill="both")

def switcher(window,component,key):
    """Clear the window and display the new form."""
    try:
        if key not in pages.keys():
            pages[key] = component

        for widget in window.winfo_children():
            widget.pack_forget() 
        pages[key](window).pack()
        print("component active -> ",pages[key])
        print("done foget")
    except Exception as e : 
        print(e)
        # rerender(window,component)
    create_bottom_nav(window)

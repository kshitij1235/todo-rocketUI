from vendor.Rocket.BaseImports import *
from vendor.Rocket.Log import *

# This file make sure the work of how render is 
# going to take palce in the rocket window 
# It contains all the basic function that help 
# rocket window to render components on the screen 

def get_all_widgets(root : Tk)->list[Tk]:
    """
    It return you all the list of componets in the root 
    """
    widgets = root.winfo_children()
    for widget in widgets:
        if widget.winfo_children():
            widgets.extend(widget.winfo_children())
    return widgets

def rerender(root: Tk, new_page) -> None:
    """
    Destroys all the components on the root and renders the components of new_page.
    Ensures proper cleanup of resources like variable traces before destroying widgets.
    
    Args:
        root (Tk): The root Tkinter window.
        new_page (function): The function to render the new page components.
    """
    log("Re-rendering root")

    # Iterate through all widgets and destroy them with cleanup
    for widget in get_all_widgets(root):
        # Clean up variable traces or other widget-specific resources
        try:
            if hasattr(widget, "_variable") and widget._variable:
                # Ensure the variable has a trace callback before removing it
                if hasattr(widget._variable, "trace_remove"):
                    callback_name = widget._variable_callback_name
                    # Check if the callback exists before attempting to remove it
                    if callback_name in widget._variable.trace_vdelete("write"):
                        widget._variable.trace_remove("write", callback_name)
                        log(f"Trace removed from {widget}")
        except Exception as e:
            log(f"Error while cleaning up widget traces: {e}")

        # Safely destroy the widget
        try:
            widget.destroy()
            log(f"Widget {widget} destroyed")
        except Exception as e:
            log(f"Error while destroying widget {widget}: {e}")

    # Render the new page (with new layout)
    try:
        new_page(root)
        log("New page rendered")
    except Exception as e:
        log(f"Error while rendering new page: {e}")

def rerender_component(parent: Tk, component_constructor, *args, **kwargs):
    """
    Re-renders an individual component within the parent window.

    Args:
        parent (tk.Widget): The parent container holding the component.
        component_constructor (callable): A function or class to reinitialize the component.
        *args: Positional arguments to pass to the component constructor.
        **kwargs: Keyword arguments to pass to the component constructor.
    """
    parent.update_idletasks()

    # Destroy existing widgets inside the parent (if any)
    for widget in parent.winfo_children():
        widget.destroy()

    # Create the new component using the constructor passed in
    try:
        new_component = component_constructor(parent, *args, **kwargs)

        # If using grid layout, you might need to define a grid configuration
        # Example: new_component.grid(row=0, column=0, sticky="nsew")
        new_component.grid(row=0, column=0, sticky="nsew")  # Use grid if you're using the grid layout manager
    except Exception as e:
        print(f"Error rendering component: {e}")


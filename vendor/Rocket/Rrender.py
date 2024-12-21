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
        # Clean up traces or other widget-specific resources
        try:
            if hasattr(widget, "_variable") and widget._variable:
                widget._variable.trace_remove("write", widget._variable_callback_name)
        except Exception as e:
            log(f"Error while cleaning up widget traces: {e}")

        # Safely destroy the widget
        try:
            widget.destroy()
        except Exception as e:
            log(f"Error while destroying widget: {e}")

    # Render the new page (with new layout)
    new_page(root)



def rerender_component(parent, component_constructor, *args, **kwargs):
    """
    Re-renders an individual component within the parent window.

    Args:
        parent (Widget): The parent container holding the component.
        component_constructor (callable): A function or class to reinitialize the component.
        *args: Positional arguments to pass to the component constructor.
        **kwargs: Keyword arguments to pass to the component constructor.
    """
    # Clear the parent widget's children
    for widget in parent.winfo_children():
        widget.destroy()

    # Re-add the component
    new_component = component_constructor(parent, *args, **kwargs)
    try : 
        new_component.pack(fill="both", expand=True)  # Adjust layout as needed
    except Exception as e :
        pass 




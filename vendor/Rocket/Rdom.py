def get_element_by_name(window, name):
    for widget in window.winfo_children():
        if widget.winfo_name() == name:  
            return widget
    return None

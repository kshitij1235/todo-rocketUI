from src.components.todo_components import todo_list
from src.components.bottom_bar_component import add_task


def homepage(window): 
    from src.components.header_components import todo_header
    todo_header(window)
    todo_list(window, "rocketdb", "tasks")
    add_task(window)
    

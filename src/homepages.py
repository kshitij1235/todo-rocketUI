from src.components.homepage_components import (todo_header,
                                                todo_list,
                                                add_task)

def homepage(window): 

    todo_header(window)
    todo_list(window, "rocketdb", "tasks")
    add_task(window)
    

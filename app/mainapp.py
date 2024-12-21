from app.Window_managment import *

#page files that contains everything 
from src.homepages import*

import threading
# this is the file where all the main application is strcutured 
# this is the only file which gets all the window acess 

def threaded(func):

    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
    return wrapper

class APP:
    def __init__(self) -> None:
        self.windows = windowManager().get_all_rwindows()  

    # make function in the class  where you club all the components, it is like creating a page of tkinter 


    #this is a demo function which bootstraps all the compoennts from src
    @threaded
    def homescreen(self):
        self.windows["main_window"].config(bg="#2C2C2C")
        homepage(self.windows["main_window"])

        # [TODO] save point for mainloop
        # self.windows["main_window"].mainloop()


from app.Window_managment import *
from vendor.Rocket import threaded
#page files that contains everything 
from src.homepages import*
import importlib
import threading
from app.GlobStorageWindow import *
# this is the file where all the main application is strcutured 
# this is the only file which gets all the window acess 



class APP:
    def __init__(self) -> None:
        self.windows = windowManager().get_all_rwindows()  
        

    # make function in the class  where you club all the components, it is like creating a page of tkinter 


    #this is a demo function which bootstraps all the compoennts from src
    def homescreen(self):

        # all the content wil be shown in the main frame 
        self.windows["main_window"].config(bg="#2C2C2C")
        main_frame  = Frame(self.windows["main_window"], bg="#2C2C2C")
        homepage(main_frame)
        main_frame.pack(expand=True , fill="both")

        # bottom navigation bar in the mainwindow 
        main_screen(self.windows["main_window"])
        # [TODO] save point for mainloop
        # self.windows["main_window"].mainloop()



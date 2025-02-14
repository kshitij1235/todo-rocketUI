from app.Rwindows.Window_managment import *
from vendor.Rocket import threaded
#page files that contains everything 
from src.homepages import*
import importlib
import threading
from vendor.Rocket.component_utility import BottomNavBar
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
        self.main_frame  = Frame(self.windows["main_window"], bg="#2C2C2C")
        self.main_frame.pack(expand=True , fill="both")
      
        # APP.create_BottomNavbar(self)

        #load the first page in to global memory 
        from app.ControllerManager import save_state
        save_state.AssingValue("global","current_page",homepage)

        #load the main_screen 
        APP.main_screen(self)

    def main_screen(self):
        homepage(self.main_frame)


    def create_BottomNavbar(self):
        nav = BottomNavBar(self.windows["main_window"],self.main_frame)
        nav.add_option("Home", homepage, "homepage") \
        .add_option("Profile", settings, "settings") \
        .build()



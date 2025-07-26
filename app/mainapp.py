from app.Rwindows.Window_managment import *
from vendor.Rocket import threaded
#page files that contains everything 
from src.homepages import*
import importlib
import threading
from vendor.Rocket.component_utility import BottomNavBar
from app.GlobStorageWindow import *
from app.ControllerManager import icon
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

        #You can write you screen init logic here
        APP.main_screen(self)
      
    def main_screen(self):
        homepage(self.main_frame)
        self.create_BottomNavbar()
    def create_BottomNavbar(self, window="main_window"):
        nav = BottomNavBar(self.windows[window], self.main_frame)

        home_icon = icon.icon("home.png")
        settings_icon = icon.icon("profile.png")

        nav.add_option("Home", homepage, "homepage", icon=home_icon) \
           .add_option("Profile", settings, "settings", icon=settings_icon) \
           .build()



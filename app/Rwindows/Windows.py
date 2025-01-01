from vendor.Rocket.create import *
from windowConfig import *

# this is the file where you intitae all the windows 

Rwindows_={}


# this is the basic main window of the application
Rwindows_["main_window"]= Rocket().get_window(WindowConfig=MainWindowConfig)
Rwindows_["error"]= Rocket().get_window(title="error",locked=True,visible=False)


# Rwindows_["error"]= Rocket().get_window()


# write the window that you want to create 
# it can be for example a error window or a sucess window 

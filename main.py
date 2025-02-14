from app.mainapp import APP
from Rocket import RELEASE
from app.Rwindows.Window_managment import *
from tkinter import Tk

# running the main app 
def MainApp():
    window:Tk = APP()
    window.homescreen()
    root = windowManager().get_all_rwindows() 

    for window in root.values() : 
        window.mainloop()


if __name__ == '__main__':

    if RELEASE : 
        '''if you want to do some thing in RELEASE before the the MainApp() function''' 
        MainApp()

    if not RELEASE : 
        '''if you want to do some thing in debug before the the MainApp() function''' 
        MainApp()

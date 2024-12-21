from app.mainapp import APP
from Rocket import RELEASE
from app.Window_managment import *
# [TODO] make a debug version 



def MainApp():
    window = APP()
    window.homescreen()
    root = windowManager().get_all_rwindows() 
    root["main_window"].mainloop()


if __name__ == '__main__':

    if RELEASE : 
        '''if you want to do some thing in RELEASE before the the MainApp() function''' 
        MainApp()

    if not RELEASE : 
        '''if you want to do some thing in debug before the the MainApp() function''' 
        MainApp()
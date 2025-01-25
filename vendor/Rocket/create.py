from tkinter import *
from vendor.Rocket.resource_gather import get_resource_images
from windowConfig import *

class Rocket:
    def __init__(self) -> None:
        self.window = Tk()

    def get_window(self,
                   title: str = "Rocket UI",
                   icon: str = None,
                   resolution: str = "500x700",
                   locked: bool = False,
                   visible: bool = True,
                   WindowConfig: dict = None,
                   ) -> Tk:
        '''
        Create a window and return it.
        '''
        window = self.window
        try:
            if icon is None:
                icon = get_resource_images(WindowConfig["icon"])
            photo = PhotoImage(file=icon)
            window.iconphoto(True, photo)
                
        except FileExistsError:
            log("ROCKET : COULD NOT FIND FILE")
        except Exception as e: 
            print(f"ROCKET: {e}")

        # Set the window title from WindowConfig or default to title parameter
        if WindowConfig and  WindowConfig.get("window_name"):
            window.title(WindowConfig["window_name"])
        else:
            window.title(title)

        # Set the window resolution from WindowConfig or default to resolution parameter
        if WindowConfig and WindowConfig.get("resolution"):
            window.geometry(WindowConfig["resolution"])
        else:
            window.geometry(resolution)

        # Lock window resizing if `locked` is True
        if locked:
            window.resizable(False, False)
        if not visible:
            window.withdraw()  
        return window

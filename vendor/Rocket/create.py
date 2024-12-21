from tkinter import *
from vendor.json_extractor.extract_values import *
from vendor.Rocket.resource_gather import get_resource_images
from windowConfig import *
class Rocket:
    def __init__(self) -> None:
        self.window = Tk()

    def get_window(self,
                   WindowConfig=None, 
                   )->Tk:
        '''
        create a window and return it 
        '''
        window = self.window
        try:
            photo = PhotoImage(file=get_resource_images(WindowConfig["icon"]))
            window.iconphoto(True, photo)
        except FileExistsError:
            print("ROCKET : COULD NOT FIND FILE")
        except Exception as e : 
            print(f"ROCKET:  {e}")

        window.title(WindowConfig["window_name"])
        window.geometry(WindowConfig["resolution"])
        return window
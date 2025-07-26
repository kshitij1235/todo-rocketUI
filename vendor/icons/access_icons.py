import os
import tkinter as tk
from tkinter import PhotoImage

folder_path = './resources/icons'
files = tuple(f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)))

class Icons:
    def __init__(self):
        self.available_icons = files
        self.icon_path = folder_path
        self._cache = {}

    def icon(self, icon_name: str) -> PhotoImage:
        if icon_name not in self.available_icons:
            raise ValueError(f"Invalid icon name: '{icon_name}'")
        
        full_path = os.path.join(self.icon_path, icon_name)
        image = PhotoImage(file=full_path)
        self._cache[icon_name] = image
        return image

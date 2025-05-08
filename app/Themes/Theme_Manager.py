from app.Themes.default import *

class ThemeManager:
    def __init__(self, theme="light"):
        
        self.LIGHT_COLORS =LIGHT_COLORS
        self.DARK_COLORS =DARK_COLORS
        self.active_theme = theme
        self.COLORS = self.DARK_COLORS

        if theme == "dark":
            self.active_theme = "dark"
            self.COLORS = self.DARK_COLORS
        else:
            self.active_theme = "light"
            self.COLORS = self.LIGHT_COLORS

    def switch_theme(self, dark_mode: bool):
        """Switch between dark and light themes."""
        if dark_mode:
            self.active_theme = "dark"
            self.COLORS = self.DARK_COLORS
        else:
            self.active_theme = "light"
            self.COLORS = self.LIGHT_COLORS

    def isdark(self):
        """Return if the current theme is dark."""
        return self.active_theme == "dark"
    
    def get_color(self, key):
        """Returns the color hex value for a given key in the current theme."""
        return self.COLORS.get(key, "Key not found")  

    def get_colors(self):
        """Get all colors for the current theme."""
        return self.COLORS

class ThemeManager:
    def __init__(self, theme="light"):
        
        self.LIGHT_COLORS = {
            "bg": "#FFFFFF",  # Light background
            "secondary": "#F0F0F0",  # Light secondary
            "accent": "#D0D0D0",  # Accent color for light mode
            "hover": "#CCCCCC",  # Hover effect in light mode
            "text": "#000000",  # Text color
            "subtext": "#333333",  # Subtext color in light mode
            "input_bg": "#FFFFFF",  # Input field background
            "input_text": "#000000"  # Input text color
        }

        self.DARK_COLORS = {
            "bg": "#18181B",  # Dark background
            "secondary": "#27272A",  # Dark secondary
            "accent": "#3F3F46",  # Accent color for dark mode
            "hover": "#52525B",  # Hover effect in dark mode
            "text": "#FFFFFF",  # Text color
            "subtext": "#A1A1AA",  # Subtext color in dark mode
            "input_bg": "#FFFFFF",  # Input field background
            "input_text": "#000000"  # Input text color
        }
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

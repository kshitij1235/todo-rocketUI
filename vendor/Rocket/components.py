from customtkinter import *
from typing import Optional, Union, Tuple, Callable
import tkinter
from tkinter import Frame


class Components:
    def __init__(self, window, theme) -> None:
        self.window = window
        self.theme = theme 

    def Rlabels(self,
                master: any,
                text: str = "CTkLabel",
                font: Optional[Union[tuple, CTkFont]] = None,
                **kwargs):
        """Create a label component using the theme."""
        return CTkLabel(
            master=master,
            text=text,
            font=font or ("Helvetica", 14),
            text_color=self.theme.get_color("text"),  # Get text color from theme
            bg_color=self.theme.get_color("bg"),  # Get background color from theme
            **kwargs
        )

    def Rcheckbox(self,
                  master: any,
                  text: str = "CTkCheckBox",
                  font: Optional[Union[tuple, CTkFont]] = None,
                  command: Union[Callable[[], None], None] = None,
                  **kwargs):
        """Create a checkbox component using the theme."""
        return CTkCheckBox(
            master=master,
            text=text,
            font=font or ("Helvetica", 12),
            text_color=self.theme.get_color("text"),  # Get text color from theme
            hover_color=self.theme.get_color("hover"),  # Get hover color from theme
            fg_color=self.theme.get_color("primary"),  # Get primary color from theme
            bg_color=self.theme.get_color("bg"),  # Get background color from theme
            command=command,
            **kwargs
        )

    def Rframe(self,
               master: any,
               fg_color: Optional[str] = None,
               **kwargs):
        """Create a frame component using the theme."""
        frame = Frame(
            master=master,
            bg=self.theme.get_color("bg"), 
            **kwargs  
        )
        return frame



    def Rbutton(self, master, text="", command=None, **kwargs):
        """Create a custom button with reusable settings."""
        return CTkButton(
            master=master,
            text=text,
            command=command,
            fg_color=self.theme.get_color("accent"),
            hover_color=self.theme.get_color("hover"),
            text_color=self.theme.get_color("text"),
            **kwargs  # Allow overriding defaults
        )
    def Rentry(self,
               master: any,
               placeholder_text: str = "",
               width: int = 200,
               height: int = 35,
               border_width: int = 1,
               font: Optional[Union[tuple, CTkFont]] = None,
               **kwargs):
        """Create an entry component using the theme."""
        return CTkEntry(
            master=master,
            placeholder_text=placeholder_text,
            width=width,
            height=height,
            border_width=border_width,
            text_color=self.theme.get_color("text"),
            fg_color=self.theme.get_color("bg"),
            corner_radius=5,
            font=font or ("Helvetica", 14),
            **kwargs
        )
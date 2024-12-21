from customtkinter import *
import tkinter
from vendor.json_extractor.extract_values import *
from typing import *
class Components:
    def __init__(self,window,theme) -> None:
        self.window = window 

    def Rlabels(master: any,
                width: int = 0,
                height: int = 28,
                corner_radius: Optional[int] = None,
                bg_color: Union[str, Tuple[str, str]] = "transparent",
                fg_color: Optional[Union[str, Tuple[str, str]]] = None,
                text_color: Optional[Union[str, Tuple[str, str]]] = None,
                text_color_disabled: Optional[Union[str, Tuple[str, str]]] = None,
                text: str = "CTkLabel",
                font: Optional[Union[tuple, CTkFont]] = None,
                image: Union[CTkImage, None] = None,
                compound: str = "center",
                anchor: str = "center",  # label anchor: center, n, e, s, w
                wraplength: int = 0,
                **kwargs):
        CTkLabel()


        
    def check_box(self,
                master: any,
                width: int = 100,
                height: int = 24,
                checkbox_width: int = 24,
                checkbox_height: int = 24,
                corner_radius: Optional[int] = None,
                border_width: Optional[int] = None,
                bg_color: Union[str, Tuple[str, str]] = "transparent",
                fg_color: Optional[Union[str, Tuple[str, str]]] = None,
                hover_color: Optional[Union[str, Tuple[str, str]]] = None,
                border_color: Optional[Union[str, Tuple[str, str]]] = None,
                checkmark_color: Optional[Union[str, Tuple[str, str]]] = None,
                text_color: Optional[Union[str, Tuple[str, str]]] = None,
                text_color_disabled: Optional[Union[str, Tuple[str, str]]] = None,
                text: str = "CTkCheckBox",
                font: Optional[Union[tuple, CTkFont]] = None,
                textvariable: Union[tkinter.Variable, None] = None,
                state: str = tkinter.NORMAL,
                hover: bool = True,
                command: Union[Callable[[], None], None] = None,
                onvalue: Union[int, str] = 1,
                offvalue: Union[int, str] = 0,
                variable: Union[tkinter.Variable, None] = None,
                ):
        CTkCheckBox(self.window,
            text="edit the app/main",
            text_color="black",
            hover_color="#C29130",
            fg_color="#C29130")
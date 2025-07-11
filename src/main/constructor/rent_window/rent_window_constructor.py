from customtkinter import *
from src.views.base_structures.base_frame import BaseFrame
from src.views.base_structures.base_frame import RightFrame
from src.main.constructor.base_structures.go_back_button_constructor import GoBackButtonConstructor
from src.main.constructor.base_structures.left_crud_buttons_constructor import LeftCrudButtonsConstructor
from src.main.constructor.rent_window.rent_create_window_constructor import RentCreateWindowConstructor
from src.main.constructor.rent_window.rent_read_window_constructor import RentReadWindowConstructor
from src.main.constructor.rent_window.rent_update_window_constructor import RentUpdateWindowConstructor
from src.main.constructor.rent_window.rent_delete_window_constructor import RentDeleteWindowConstructor

class RentWindowConstructor():
    def __init__(self, root):
        self.root = root
        self.frame = BaseFrame(root)
        self.right_frame = RightFrame(self.root)
        self.leftFrameLabel(self.frame.left_corner_frame)
        self.create_window = RentCreateWindowConstructor(self.right_frame)
        self.go_back_button = GoBackButtonConstructor(self.root, self.frame,
                                                        self.frame.left_corner_frame)
        self.leftCrudButtonsCommands()

    def leftFrameLabel(self, left_corner_frame):
        self.left_label = CTkLabel(left_corner_frame, text="Aluguéis" , text_color='#2F4F4F', font=('impact', 50), justify='left' )
        self.left_label.place(relx=0.12, rely=0.2, relwidth=0.6, relheight=0.15)

    def createWindowCall(self):
        self.right_frame.place_forget()
        self.right_frame = RightFrame(self.root)
        self.create_window = RentCreateWindowConstructor(self.right_frame)
    
    def readWindowCall(self):
        self.right_frame.place_forget()
        self.right_frame = RightFrame(self.root)
        self.read_window = RentReadWindowConstructor(self.right_frame)

    def updateWindowCall(self):
        self.right_frame.place_forget()
        self.right_frame = RightFrame(self.root)
        self.update_window = RentUpdateWindowConstructor(self.right_frame)

    def deleteWindowCall(self):
        self.right_frame.place_forget()
        self.right_frame = RightFrame(self.root)
        self.update_window = RentDeleteWindowConstructor(self.right_frame)

    def leftCrudButtonsCommands(self):
        self.left_buttons = LeftCrudButtonsConstructor(self.frame.left_corner_frame)
        self.left_buttons.crud_buttons.create_bt.configure(command=self.createWindowCall)
        self.left_buttons.crud_buttons.read_bt.configure(command=self.readWindowCall)
        self.left_buttons.crud_buttons.update_bt.configure(command=self.updateWindowCall)
        self.left_buttons.crud_buttons.delete_bt.configure(command=self.deleteWindowCall)
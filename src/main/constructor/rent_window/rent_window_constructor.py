from src.views.rent_window.rent_base_window import RentBaseWindow
from src.main.constructor.base_structures.go_back_button_constructor import GoBackButtonConstructor
from src.main.constructor.base_structures.left_crud_buttons_constructor import LeftCrudButtonsConstructor
from src.main.constructor.rent_window.rent_create_window_constructor import RentCreateWindowConstructor
from src.main.constructor.rent_window.rent_read_window_constructor import RentReadWindowConstructor
from src.main.constructor.rent_window.rent_update_window_constructor import RentUpdateWindowConstructor
from src.main.constructor.rent_window.rent_delete_window_constructor import RentDeleteWindowConstructor

class RentWindowConstructor():
    def __init__(self, root):
        self.root = root
        self.base_window = RentBaseWindow(self.root)
        self.go_back_button = GoBackButtonConstructor(self.root, self.base_window.frame,
                                                        self.base_window.frame.left_corner_frame)
        self.leftCrudButtonsCommands()

    def createWindowCall(self):
        self.base_window.right_frame.place_forget()
        self.base_window.newRightFrame()
        self.create_window = RentCreateWindowConstructor(self.base_window.new_frame)
    
    def readWindowCall(self):
        self.base_window.right_frame.place_forget()
        self.base_window.newRightFrame()
        self.read_window = RentReadWindowConstructor(self.base_window.new_frame)

    def updateWindowCall(self):
        self.base_window.right_frame.place_forget()
        self.base_window.newRightFrame()
        self.update_window = RentUpdateWindowConstructor(self.base_window.new_frame)

    def deleteWindowCall(self):
        self.base_window.right_frame.place_forget()
        self.base_window.newRightFrame()
        self.update_window = RentDeleteWindowConstructor(self.base_window.new_frame)

    def leftCrudButtonsCommands(self):
        self.left_buttons = LeftCrudButtonsConstructor(self.base_window.frame.left_corner_frame)
        self.left_buttons.crud_buttons.create_bt.configure(command=self.createWindowCall)
        self.left_buttons.crud_buttons.read_bt.configure(command=self.readWindowCall)
        self.left_buttons.crud_buttons.update_bt.configure(command=self.updateWindowCall)
        self.left_buttons.crud_buttons.delete_bt.configure(command=self.deleteWindowCall)
from src.views.client_window.client_base_window import ClientBaseWindow
from src.main.constructor.base_structures.go_back_button_constructor import GoBackButtonConstructor
from src.main.constructor.base_structures.left_crud_buttons_constructor import LeftCrudButtonsConstructor
from src.main.constructor.client_constructors.client_create_window_constructor import ClientCreateWindowConstructor
from src.main.constructor.client_constructors.client_read_window_constructor import ClientReadWindowConstructor
from src.main.constructor.client_constructors.client_update_window_constructor import ClientUpdateWindowConstructor
from src.main.constructor.client_constructors.client_delete_window_constructor import ClientDeleteWindowConstructor

class ClientWindowConstructor():
    def __init__(self, root):
        self.root = root
        self.base_window = ClientBaseWindow(self.root)
        self.go_back_button = GoBackButtonConstructor(self.root, self.base_window.frame,
                                                        self.base_window.frame.left_corner_frame)
        self.leftCrudButtonsCommands()

    def createWindowCall(self):
        self.base_window.right_frame.place_forget()
        self.base_window.newRightFrame()
        self.create_window = ClientCreateWindowConstructor(self.base_window.new_frame)
    
    def readWindowCall(self):
        self.base_window.right_frame.place_forget()
        self.base_window.newRightFrame()
        self.read_window = ClientReadWindowConstructor(self.base_window.new_frame)

    def updateWindowCall(self):
        self.base_window.right_frame.place_forget()
        self.base_window.newRightFrame()
        self.update_window = ClientUpdateWindowConstructor(self.base_window.new_frame)

    def deleteWindowCall(self):
        self.base_window.right_frame.place_forget()
        self.base_window.newRightFrame()
        self.update_window = ClientDeleteWindowConstructor(self.base_window.new_frame)

    def leftCrudButtonsCommands(self):
        self.left_buttons = LeftCrudButtonsConstructor(self.base_window.frame.left_corner_frame)
        self.left_buttons.crud_buttons.create_bt.configure(command=self.createWindowCall)
        self.left_buttons.crud_buttons.read_bt.configure(command=self.readWindowCall)
        self.left_buttons.crud_buttons.update_bt.configure(command=self.updateWindowCall)
        self.left_buttons.crud_buttons.delete_bt.configure(command=self.deleteWindowCall)
        
   
    

    

    

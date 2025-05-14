from src.main.constructor.base_structures.go_back_button_constructor import GoBackButtonConstructor
from src.main.constructor.base_structures.left_crud_buttons_constructor import LeftCrudButtonsConstructor
from src.views.vehicle_window.vehicle_base_window import VehicleBaseWindow
from src.main.constructor.vehicle_window.vehicle_create_window_constructor import VehicleCreateWindowConstructor
from src.main.constructor.vehicle_window.vehicle_read_window_constructor import VehicleReadWindowConstructor
from src.main.constructor.vehicle_window.vehicle_update_window_constructor import VehicleUpdateWindowConstructor
from src.main.constructor.vehicle_window.vehicle_delete_window_constructor import VehicleDeleteWindowConstructor

class VehicleWindowConstructor():
    def __init__(self, root):
        self.root = root
        self.base_window = VehicleBaseWindow(self.root)
        self.go_back_button = GoBackButtonConstructor(self.root, self.base_window.frame,
                                                        self.base_window.frame.left_corner_frame)
        self.leftCrudButtonsCommands()

    def createWindowCall(self):
        self.base_window.right_frame.place_forget()
        self.base_window.newRightFrame()
        self.create_window = VehicleCreateWindowConstructor(self.base_window.new_frame)
    
    def readWindowCall(self):
        self.base_window.right_frame.place_forget()
        self.base_window.newRightFrame()
        self.read_window = VehicleReadWindowConstructor(self.base_window.new_frame)

    def updateWindowCall(self):
        self.base_window.right_frame.place_forget()
        self.base_window.newRightFrame()
        self.update_window = VehicleUpdateWindowConstructor(self.base_window.new_frame)

    def deleteWindowCall(self):
        self.base_window.right_frame.place_forget()
        self.base_window.newRightFrame()
        self.update_window = VehicleDeleteWindowConstructor(self.base_window.new_frame)

    def leftCrudButtonsCommands(self):
        self.left_buttons = LeftCrudButtonsConstructor(self.base_window.frame.left_corner_frame)
        self.left_buttons.crud_buttons.create_bt.configure(command=self.createWindowCall)
        self.left_buttons.crud_buttons.read_bt.configure(command=self.readWindowCall)
        self.left_buttons.crud_buttons.update_bt.configure(command=self.updateWindowCall)
        self.left_buttons.crud_buttons.delete_bt.configure(command=self.deleteWindowCall)
        
from src.views.base_structures.upper_menu_buttons import UpperMenuButtons
from src.main.constructor.client_window.client_window_constructor import ClientWindowConstructor
from src.main.constructor.vehicle_window.vehicle_window_constructor import VehicleWindowConstructor

class UpperMenuButtonsConstructor():
    def __init__(self, upper_frame, root, frame):
        self.upper_frame = upper_frame
        self.root = root
        self.frame = frame
        self.buttons = UpperMenuButtons(self.upper_frame)

    def clientWindowCallBack(self):
        self.frame.place_forget()
        self.client_window = ClientWindowConstructor(self.root)

    def clientWindowCall(self):
        self.buttons.client_bt.configure(command=self.clientWindowCallBack)

    def vehicleWindowCallback(self):
        self.frame.place_forget()
        self.vehicle_window = VehicleWindowConstructor(self.root)
    
    def vehicleWindowCall(self):
        self.buttons.vehicle_bt.configure(command=self.vehicleWindowCallback)
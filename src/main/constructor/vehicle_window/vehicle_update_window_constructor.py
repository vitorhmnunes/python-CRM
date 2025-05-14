from src.views.vehicle_window.vehicle_update_window import VehicleUpdateWindow

class VehicleUpdateWindowConstructor():
    def __init__(self, master):
        self.master = master
        self.read_window = VehicleUpdateWindow(self.master)
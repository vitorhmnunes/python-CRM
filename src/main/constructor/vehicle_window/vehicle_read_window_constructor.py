from src.views.vehicle_window.vehicle_read_window import VehicleReadWindow

class VehicleReadWindowConstructor():
    def __init__(self, master):
        self.master = master
        self.read_window = VehicleReadWindow(self.master)
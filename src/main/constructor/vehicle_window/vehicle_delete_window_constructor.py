from src.views.vehicle_window.vehicle_delete_window import VehicleDeleteWindow

class VehicleDeleteWindowConstructor():
    def __init__(self, master):
        self.master = master
        self.read_window = VehicleDeleteWindow(self.master)

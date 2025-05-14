from src.views.vehicle_window.vehicle_create_window import VehicleCreateWindow

class VehicleCreateWindowConstructor():
    def __init__(self, right_frame):
        self.right_frame = right_frame
        self.create_window = VehicleCreateWindow(self.right_frame)
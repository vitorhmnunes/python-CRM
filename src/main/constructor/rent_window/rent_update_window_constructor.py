from src.views.rent_window.rent_update_window import RentUpdateWindow

class RentUpdateWindowConstructor():
    def __init__(self, right_frame):
        self.right_frame = right_frame
        self.create_window = RentUpdateWindow(self.right_frame)
from src.views.rent_window.rent_create_window import RentCreateWindow

class RentCreateWindowConstructor():
    def __init__(self, right_frame):
        self.right_frame = right_frame
        self.create_window = RentCreateWindow(self.right_frame)
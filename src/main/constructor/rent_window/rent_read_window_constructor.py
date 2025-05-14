from src.views.rent_window.rent_read_window import RentReadWindow

class RentReadWindowConstructor():
    def __init__(self, right_frame):
        self.right_frame = right_frame
        self.create_window = RentReadWindow(self.right_frame)
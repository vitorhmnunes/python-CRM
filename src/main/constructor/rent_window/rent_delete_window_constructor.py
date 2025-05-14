from src.views.rent_window.rent_delete_window import RentDeleteWindow

class RentDeleteWindowConstructor():
    def __init__(self, right_frame):
        self.right_frame = right_frame
        self.create_window = RentDeleteWindow(self.right_frame)
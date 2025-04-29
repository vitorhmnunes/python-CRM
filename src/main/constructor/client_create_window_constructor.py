from src.views.client_window.client_create_window import ClientCreateWindow

class ClientCreateWindowConstructor():
    def __init__(self, right_frame):
        self.right_frame = right_frame
        self.create_window = ClientCreateWindow(self.right_frame)

    
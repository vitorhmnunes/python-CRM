from src.views.client_window.client_read_window import ClientReadWindow

class ClientReadWindowConstructor():
    def __init__(self, master):
        self.master = master
        self.read_window = ClientReadWindow(self.master)
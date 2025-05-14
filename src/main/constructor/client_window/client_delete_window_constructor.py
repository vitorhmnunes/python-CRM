from src.views.client_window.client_delete_window import ClientDeleteWindow

class ClientDeleteWindowConstructor():
    def __init__(self, master):
        self.master = master
        self.delete_window = ClientDeleteWindow(self.master)

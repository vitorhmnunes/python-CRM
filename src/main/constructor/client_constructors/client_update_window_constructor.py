from src.views.client_window.client_update_window import ClientUpdateWindow

class ClientUpdateWindowConstructor():
    def __init__(self, master):
        self.master = master
        self.update_window = ClientUpdateWindow(self.master)
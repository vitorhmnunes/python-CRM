from src.views.client_window.client_base_window import ClienBaseWindow
from src.main.constructor.base_structures.go_back_button_constructor import GoBackButtonConstructor

class ClientWindowConstructor():
    def __init__(self, root):
        self.root = root
        self.client_window = ClienBaseWindow(self.root)
        self.go_back_button = GoBackButtonConstructor(self.root, self.client_window.frame,
                                                        self.client_window.frame.left_corner_frame)
    

    

    

    

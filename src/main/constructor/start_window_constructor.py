from src.views.start_window import StartWindow
from src.main.constructor.base_structures.upper_menu_buttons_constructor import UpperMenuButtonsConstructor

class StartWindowConstructor():
    def __init__(self, root):
        self.root = root
        self.start_window = StartWindow(self.root)
        self.upper_buttons = UpperMenuButtonsConstructor(
                                                          self.start_window.upper_frame, 
                                                          self.root, self.start_window.frame
                                                          )







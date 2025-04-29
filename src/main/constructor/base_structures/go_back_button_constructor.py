from src.views.base_structures.go_back_button import GoBackButton

class GoBackButtonConstructor():
    def __init__(self, root, frame, left_frame):
        self.root = root
        self.frame = frame
        self.left_frame = left_frame
        self.button = GoBackButton(self.left_frame)
        self.buttonConfigure()

    def buttonConfigure(self):
        self.button.goBackButton()
        self.button.go_back_button.configure(command= self.startWindowCall)

    def startWindowCall(self):
        from src.main.constructor.start_window_constructor import StartWindowConstructor
        self.frame.place_forget()
        self.start_window = StartWindowConstructor(self.root)
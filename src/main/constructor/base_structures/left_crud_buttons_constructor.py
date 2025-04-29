from src.views.base_structures.left_crud_buttons import LeftCrudButtons

class LeftCrudButtonsConstructor():
    def __init__(self, master) -> None:
        self._master = master
        self.crud_buttons = LeftCrudButtons(self._master)



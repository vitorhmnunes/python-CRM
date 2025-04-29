from src.views.root import Root
from src.main.constructor.start_window_constructor import StartWindowConstructor

def start() -> None:
    app = Root()
    StartWindowConstructor(app)
    app.mainloop() 
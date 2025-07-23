from src.views.root import Root
from src.main.constructor.start_window_constructor import StartWindowConstructor
from src.models.database_connection import MySQLConnection

def start() -> None:
    app = Root()
    try:
        db = MySQLConnection()
        connection = db.get_db_connection()
        print(f"Starting the connection...\nStatus: {connection.is_connected()}")
    except ConnectionError as err:
        print(f"Error during the connection. Message: {err}")

    StartWindowConstructor(app)
    app.mainloop()
    
    db.closing()


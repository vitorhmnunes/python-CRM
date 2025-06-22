import mysql.connector as mysql_connector
from dotenv import load_dotenv
import os

load_dotenv()

class MySQLConnection:
    def __init__(self):
        self._host = os.getenv("HOST")
        self._username = os.getenv("USERNAME")
        self._password = os.getenv("PASSWORD")
        self._database = os.getenv("DATABASE")
        self.conn = self._connecting()

    def get_database(self):
        return self._database

    def _connecting(self):
        return mysql_connector.connect(
            user = self._user,
            password = self._password,
            host = self._host,
            database = self._database
        )
    

    
    

# try:
#     db = MySQLDatabase()
#     print(f"Starting the connection...\nStatus: {db.connection.is_connected()}")
# except ConnectionError as err:
#     raise f"Error during the connection. Message: {err}"
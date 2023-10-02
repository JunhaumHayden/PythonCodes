
import mysql.conector as connector
from dotenv import load_dotenv

load_dotenv()


class MySQLDatabase:
    
    def __init__(self):    
        self._host = os.getenv("HOST")
        self._username =
        self._passwd =
        self._database =
        self.conn =
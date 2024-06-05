
import os
import mysql.connector as mysql_connector
from dotenv import load_dotenv

#Necessario carregar o arquivo .env
load_dotenv()


class MySQLDatabase:
    """Classe para instanciar uma conexao"""
    def __init__(self):    
        self._host = os.getenv("HOST01") #underline torna o atributo privado
        self._username = os.getenv("USERNAME01")
        self._passwd = os.getenv("PASSWD01")
        self._database = os.getenv("DATABASE01")
        self.conn = self._connecting() 
        
        #Ao instanciar um objeto executa a funcao _connecting que é privada. caso contrario, poderia deixar como nulo e atribuir via aplicacao (self.connecting() e deixaria de ser privado)

    def _connecting(self): #funcao privatada
        return mysql_connector.connect(
            host=self._host,
            user=self._username,
            password=self._passwd,
            database=self._database
        )

if __name__ == '__main__':
    database = MySQLDatabase()
    print(database._host)
    print(database._username)
    print(database._passwd)
    print(database._database)
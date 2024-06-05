from databes_connection import MySQLDatabase

if __name__ == '__main__':
    print('Running')
    #Instanciando uma conexao
    try:
        db=MySQLDatabase()
        print(f"Starting the connection... \nStaus: {db.conn.is_connected()}")
    except ConnectionError as err:
        raise f"Error during the connection. Message: {err}"

print(db)

mycursor = db.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
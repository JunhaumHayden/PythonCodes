import os
import mysql.connector as mysql_connector
from dotenv import load_dotenv

#Necessario carregar o arquivo .env
load_dotenv()

#Instancia uma conexao
mydb = mysql_connector.connect(
  host=os.getenv("HOST01"),
  user=os.getenv("USERNAME01"),
  password=os.getenv("PASSWD01"), database=os.getenv("DATABASE01")
)

#Cria um cursor
mycursor = mydb.cursor()
aba = "produtos"
def criar_tabela(conexao, cursor, table):
    sql = "CREATE TABLE IF NOT EXISTS clientes (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(100), email VARCHAR(150))"
    cursor.execute(sql)
    conexao.commit()
    print("Silence is OK")

def inserir_registro(conexao, cursor, nome, email):
    sql = "INSERT INTO clientes (nome, email) VALUES (%s, %s)"
    val = (nome, email)
    cursor.execute(sql, val)
    conexao.commit()
    print("1 record inserted, ID:", mycursor.lastrowid)

def atualizar_registro(conexao, cursor, nome, email, id):
    sql = "UPDATE clientes  SET nome = %s, email = %s WHERE id = %s"
    val = (nome, email, id)
    cursor.execute(sql, val)
    conexao.commit()
    print(mycursor.rowcount, "record update.")

def excluir_registro(conexao, cursor, id):
    sql = "DELETE FROM clientes WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    conexao.commit()
    print(mycursor.rowcount, "record(s) deleted")

def inserir_lote(conexao, cursor, lote):
    sql = "INSERT INTO clientes (nome, email) VALUES (%s, %s)"
    cursor.executemany(sql, lote)
    conexao.commit()
    print(cursor.rowcount, "was inserted.")    

def consulta_registros(cursor):
    cursor.execute("SELECT * FROM clientes")
    myresult = cursor.fetchall()
    for x in myresult:
     print(x)
    print(cursor.rowcount, "records found.")

def gerenciamento_transacao(conexao, cursor):
    """usa-se a funçao rollback para que todas as operações não sejam concluída no BD"""
    try:
        sql = "INSERT INTO clientes (nome, email) VALUES (%s, %s)"
        val = ("Dani", "dani@mail.com")
        cursor.execute(sql, val)
        sql = "INSERT INTO clientes (nome, email, id) VALUES (%s, %s, %s)"
        val = ("Fabi", "fabi@mail.com", 2)
        cursor.execute(sql, val)
        conexao.commit()
        print("1 record inserted, ID:", mycursor.lastrowid)
    except Exception as exc:
        print(f'Ocorreu um erro ao tentar inserir um registro! {exc}')
        conexao.rollback()

    

if __name__ == '__main__':
    #criar_tabela(mydb, mycursor, aba)
    # inserir_registro(mydb, mycursor, "ANA", "ana@mail.com")
    # consulta_registros(mycursor)

    # atualizar_registro(mydb, mycursor, "bia", "bia@mail.com", 1)
    # consulta_registros(mycursor)

    # excluir_registro(mydb, mycursor, 1)
    # consulta_registros(mycursor)

    # val = [
    # ('Peter', 'Lowstreet 4'),
    # ('Amy', 'Apple st 652'),
    # ('Hannah', 'Mountain 21'),
    # ('Michael', 'Valley 345'),
    # ('Sandy', 'Ocean blvd 2'),
    # ('Betty', 'Green Grass 1'),
    # ('Richard', 'Sky st 331'),
    # ('Susan', 'One way 98'),
    # ('Vicky', 'Yellow Garden 2'),
    # ('Ben', 'Park Lane 38'),
    # ('William', 'Central st 954'),
    # ('Chuck', 'Main Road 989'),
    # ('Viola', 'Sideway 1633')
    # ]

    # inserir_lote(mydb, mycursor, val)
    consulta_registros(mycursor)
    
    gerenciamento_transacao(mydb, mycursor)
    consulta_registros(mycursor)


    # mycursor.execute("SELECT * FROM customers")
    # myresult = mycursor.fetchall()
    # for x in myresult:
    #  print(x)
    # print(mycursor.rowcount, "records found.")

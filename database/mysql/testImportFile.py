import mysql.connector
from pathlib import Path
import os
import mysql.connector as mysql_connector
from dotenv import load_dotenv

#Necessario carregar o arquivo .env
load_dotenv()
#Instancia uma conexao
mydb = mysql.connector.connect(
  host=os.getenv("HOST01"),
  user=os.getenv("USERNAME01"),
  password=os.getenv("PASSWD01"), database=os.getenv("DATABASE01")
)

#testa a conexao, devolve um objeto
#print(db)

#Cria um cursor
mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x)

#ROOT_PATH = Path(__file__).parent
#conexao = mysql.connector.connect(ROOT_PATH / "clientes.bd")

#mycursor.execute("CREATE DATABASE IF NOT EXISTS meubancoteste")
#mycursor.execute("USE meubancoteste")

# # CHECK IF TABLE EXISTS
# # You can check if a table exist by listing all tables in your database with the "SHOW TABLES" statement:
# # Return a list of your system's databases:
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(x)


# # CREATE A TABLE
# # To create a table in MySQL, use the "CREATE TABLE" statement.
# # Make sure you define the name of the database when you create the connection
# # Create a table named "customers":
# mycursor.execute("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(x)


# # INSERT INTO TABLE
# # To fill a table in MySQL, use the "INSERT INTO" statement.
# # Insert a record in the "customers" table:
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")
# ## para retornar o ID com uma entrada
# # print("1 record inserted, ID:", mycursor.lastrowid)
# # Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.


# # INSERT MULTIPLES ROWS
# # To insert multiple rows into a table, use the executemany() method.
# # The second parameter of the executemany() method is a list of tuples, containing the data you want to insert:
# # Fill the "customers" table with data:
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "was inserted.")

## SELECT FROM A TABLE
# #- Select all records from the "customers" table, and display the result
# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)
# print(mycursor.rowcount, "records found.")
# #Note: We use the fetchall() method, which fetches all rows from the last executed statement.


## SELECTING COLUMNS
##- Select only the name and address columns:
# mycursor.execute("SELECT name, address FROM customers")
##- We use the fetchall() method, which fetches all rows from the last executed statement.
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)


# # Using the fetchone() Method
# #- If you are only interested in one row, you can use the fetchone() method.
# #- The fetchone() method will return the first row of the result:
# mycursor.execute(""SELECT * FROM customers"")
# myresult = mycursor.fetchone()
# print(myresult)


# # Select With a Filter
# #- When selecting records from a table, you can filter the selection by using the "WHERE" statement:
# #- Select record(s) where the address is "Park Lane 38": result:
# sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)


# # Wildcard Characters
# #- You can also select the records that starts, includes, or ends with a given letter or phrase.
# #- Use the %  to represent wildcard characters:
# #- Select records where the address contains the word "way":
# sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# # Prevent SQL Injection
# # como boa pratica, realizar comandos SQL prontos
# # #exemplo de como não utilizar
# # nome = "ANA"
# # address = "ana@mail.com"
# # mycursor.execute(f"INSERT INTO customers (name, address) VALUES ({nome}, address})")
# #- When query values are provided by the user, you should escape the values.
# #- This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
# #- The mysql.connector module has methods to escape query values:
# #- Escape query values by using the placholder %s method:
# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )
# mycursor.execute(sql, adr)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)


# # Sort the Result
# # Use the ORDER BY statement to sort the result in ascending or descending order.
# # The ORDER BY keyword sorts the result ascending by default. To sort the result in descending order, use the DESC keyword.
# # Sort the result alphabetically by name: result:
# sql = "SELECT * FROM customers ORDER BY name"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)


# # ORDER BY DESC
# # Use the DESC keyword to sort the result in a descending order.
# # Sort the result reverse alphabetically by name:
# sql = "SELECT * FROM customers ORDER BY name DESC"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)


# # DELETE RECORD
# # You can delete records from an existing table by using the "DELETE FROM" statement:
# # Delete any record where the address is "Mountain 21":
# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")
# # Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.

# # Prevent SQL Injection
# # It is considered a good practice to escape the values of any query, also in delete statements.
# # The mysql.connector module uses the placeholder %s to escape values in the delete statement:
# # Escape values by using the placeholder %s method:
# sql = "DELETE FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )
# mycursor.execute(sql, adr)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")


# # DELETE A TABLE
# # You can delete an existing table by using the "DROP TABLE" statement:
# # Delete the table "customers":
# sql = "DROP TABLE customers"
# mycursor.execute(sql)
# #If this page was executed with no error(s), you have successfully deleted the "customers" table.


# # Drop Only if Exist
# # If the table you want to delete is already deleted, or for any other reason does not exist, you can use the IF EXISTS keyword to avoid getting an error.
# # Delete the table "customers" if it exists:
# sql = "DROP TABLE IF EXISTS customers"
# mycursor.execute(sql)
# #If this page was executed with no error(s), you have successfully deleted the "customers" table.


# # Update Table
# # You can update existing records in a table by using the "UPDATE" statement:
# # Overwrite the address column from "Valley 345" to "Canyon 123":
# sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")
# # Note: We use the fetchall() method, which fetches all rows from the last executed statement.


# # PREVENT SQL INJECTION
# # It is considered a good practice to escape the values of any query, also in update statements.
# # The mysql.connector module uses the placeholder %s to escape values in the update statement:
# # Escape values by using the placeholder %s method:
# sql = "UPDATE customers SET address = %s WHERE address = %s"
# val = ("Valley 345", "Canyon 123")
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")


# # LIMIT THE RESULT
# # You can limit the number of records returned from the query, by using the "LIMIT" statement:
# # Select the 5 first records in the "customers" table:
# mycursor.execute("SELECT * FROM customers LIMIT 5")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)


# # START FROM ANOTHER POSITION
# # If you want to return five records, starting from the third record, you can use the "OFFSET" keyword:
# # Start from position 3, and return 5 records:
# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)


# # JOIN TWO OR MORE TABLES
# # You can combine rows from two or more tables, based on a related column between them, by using a JOIN statement.
# # Consider you have a "users" table and a "products" table:
# # users
# { id: 1, name: 'John', fav: 154},
# { id: 2, name: 'Peter', fav: 154},
# { id: 3, name: 'Amy', fav: 155},
# { id: 4, name: 'Hannah', fav:},
# { id: 5, name: 'Michael', fav:}

# # products
# { id: 154, name: 'Chocolate Heaven' },
# { id: 155, name: 'Tasty Lemons' },
# { id: 156, name: 'Vanilla Dreams' }
# # These two tables can be combined by using users' fav field and products' id field.
# # Example
# # Join users and products to see the name of the users favorite product:
# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   INNER JOIN products ON users.fav = products.id"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)
# # Note: You can use JOIN instead of INNER JOIN. They will both give you the same result.

# # LEFT JOIN
# # In the example above, Hannah, and Michael were excluded from the result, that is because INNER JOIN only shows the records where there is a match.
# # If you want to show all users, even if they do not have a favorite product, use the LEFT JOIN statement:
# # Select all users and their favorite product:
# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   LEFT JOIN products ON users.fav = products.id"

# # RIGHT JOIN
# # If you want to return all products, and the users who have them as their favorite, even if no user have them as their favorite, use the RIGHT JOIN statement:
# # Select all products, and the user(s) who have them as their favorite:
# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   RIGHT JOIN products ON users.fav = products.id"
# # Note: Hannah and Michael, who have no favorite product, are not included in the result.
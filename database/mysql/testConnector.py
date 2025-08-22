import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.100.10",
  user="admin",
  password="admin"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)



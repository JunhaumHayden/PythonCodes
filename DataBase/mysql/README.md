
<div align="center">
<img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" alt="Logo Python" width="80">
<h1>Python</h1>
<img src="https://www.mysql.com/common/logos/logo-mysql-170x115.png" alt="Logo MySql" width="100">
</div>

# #PythonCodes


<h1 align="center"> MySQL with Python </h1>


<p align="center">
<img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>

## Description

#### English
### Python MySQL

Welcome!

Python can be used in database applications. One of the most popular databases is MySQL.

### MySQL Database
To be able to experiment with the code examples in this tutorial, you should have MySQL installed on your computer.

> <img src="https://www.mysql.com/common/logos/logo-mysql-170x115.png" alt="Logo Oracle" width="40"> 
>  
> [You can download a MySQL database here](https://www.mysql.com/downloads/)


### Install MySQL Driver
Python needs a MySQL driver to access the MySQL database. We will use the driver "MySQL Connector".

We recommend that you use `PIP` to install "MySQL Connector". `PIP` is most likely already installed in your Python environment.

Navigate your command line to the location of `PIP`, and type the following:

Download and install "MySQL Connector":
```bash
C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>python -m pip install mysql-connector-python
```
In my case on MacBook:

***Step 1 - install MySQL Connector***

  ```console
  python -m pip install mysql-connector-python 
  Collecting mysql-connector-python
    Downloading mysql_connector_python-8.1.0-cp310-cp310-macosx_12_0_arm64.whl (9.3 MB)
      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.3/9.3 MB 3.6 MB/s eta 0:00:00
  Collecting protobuf<=4.21.12,>=4.21.1
    Downloading protobuf-4.21.12-cp37-abi3-macosx_10_9_universal2.whl (486 kB)
      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 486.2/486.2 kB 9.4 MB/s eta 0:00:00
  Installing collected packages: protobuf, mysql-connector-python
  Successfully installed mysql-connector-python-8.1.0 protobuf-4.21.12
  ```

***Step 2 - install Python library***

  ```console
  pip install python-dotenv
  Collecting python-dotenv
    Downloading python_dotenv-1.0.0-py3-none-any.whl (19 kB)
  Installing collected packages: python-dotenv
  Successfully installed python-dotenv-1.0.0
  ```

>  **&#8505;**
>This library is used to capture connection variables from an environment variable (`.env` file). So that the information stays in another file and not in the application.

Now you have downloaded and installed a MySQL driver.

### Test MySQL Connector
To test if the installation was successful, or if you already have "MySQL Connector" installed, create a Python page with the following content:

demo_mysql_test.py:

```Python
import mysql.connector

#if this page is executed with no errors, you have the "mysql.connector" module installed.
```
### Create Connection
Start by creating a connection to the database. Use the username and password from your MySQL database:

```Python

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

print(mydb)
````

```Python
<mysql.connector.connection_cext.CMySQLConnection object at 0x10090f850>
```

Now you can start querying the database using SQL statements.

### Check if Database Exists
You can check if a database exist by listing all databases in your system by using the ```SHOW DATABASES``` statement:
Return a list of your system's databases:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
```

Or you can try to access the database when making the connection:
Try connecting to the database ***"mydatabase"***:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
```
If the database does not exist, you will get an error.

### Creating a Database
To create a database in MySQL, use the `CREATE DATABASE` statement:
create a database named ***"mydatabase"***:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
```

If the above code was executed with no errors, you have successfully created a database.

### Creating a Table
To create a table in MySQL, use the "CREATE TABLE" statement.
Make sure you define the name of the database when you create the connection

Create a table named "customers":

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
``` 

If the above code was executed with no errors, you have now successfully created a table.

### Check if Table Exists
You can check if a table exist by listing all tables in your database with the `SHOW TABLES` statement:
Return a list of your system's databases:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)
``` 

### 🏞️ Why This Repository?

# MySQL with Python
Crietes CRUD to acess a MySQL Data Base with Python 

## Project Structure

O workspace contém dois diretórios por padrão, onde:

- `.env`: Arquivo com os dados de acesso para o servidor
-  Classe **Calculadora** com os exemplos de comentários
- `lib`: pasta para manter dependências

Enquanto isso, os arquivos compilados serão gerados no diretório `bin` por padrão.

> Se você deseja personalizar a estrutura de diretórios, abra `.vscode/settings.json` a atualize as configurações relacionadas lá.

## How to use

1. Clone this repository
2. Install dependencies with `pip install -r requirements.txt`
3. Run the program with `python main.py`

   
>  **&#8505;**
> ***Requirements files*** are files containing a list of items to be installed using `pip install` like so:
> 
> **Unix/macOS**
> ```Python
>    python -m pip install -r requirements.txt
>    ```
> **Windows**
> ```Python
>    py -m pip install -r requirements.txt
>    ```
> Requirements files are used to hold the result from `pip freeze` for the purpose of achieving Repeatable Installs. In this case, your requirement file contains a pinned version of everything that was installed when pip freeze was run.
> 
>  **Unix/macOS**
> ```Python
>    python -m pip freeze > requirements.txt
>    python -m pip install -r requirements.txt
>    ```
> **Windows**
> ```Python
>    py -m pip freeze > requirements.txt
>    py -m pip install -r requirements.txt
>    ```

### 🌲 Highlights

Dynamic Connections: Easily switch between different types of databases.
Secure Access: Follow best practices for secure database connections.
Sample Queries: Get started quickly with sample queries and operations.

### 🏆 Happy Hunting! 🗺️✨

Unlock the power of Python to connect and manipulate your data realms with ease. Explore, learn, and become the data treasure hunter you were always meant to be!

___________________________________________________________________________--
## Descrição:

#### Português-Br


## Como usar

1. Clone este repositório
2. Instale as dependências com `pip install -r requirements.txt`
3. Execute o programa com `python pomodoro_gemini.py`
4. Comece a estudar e deixe o Pomodoro Gêmini cuidar do resto!
5. OBS: O programa verifica ao final de cada ciclo se o usuário deseja reiniciar


### 🐍🌲🏞️ Python Data Treasure Hunt 🗺️✨

Bem-vindo à garndiosa floresta da conexão de dados!

Neste repositório encantado, nossa aventura com Python nos leva a explorar as profundezas de Bancos de Dados, tanto relacionais quanto não relacionais. Prepare-se para descobrir tesouros de dados escondidos nos antigos bosques de MySQL, nos misteriosos arbustos de SQLite, nas majestosas montanhas de MariaDB e nas vastas planícies de PostgreSQL.

### 🗂️ Estrutura do Projeto

Nossos mapas do tesouro (Diretórios) são organizados para guiar você através de diferentes tipos de bancos de dados:

- 🌳 `MySQL` Grove: Descubra segredos antigos com consultas poderosas.
- 🍃 `SQLite` Shrubland: Soluções leves e eficazes para suas necessidades locais.
- 🏔️ `MariaDB` Mountains: Desvende os mistérios desta fortaleza relacional.
- 🌾 `PostgreSQL` Plains: Explore as vastas possibilidades de manipulação avançada de dados.


### 🏞️ Por Que Este Repositório?

Abrangente: Seja você um explorador iniciante ou um caçador de tesouros experiente, encontrará scripts que atendem às suas necessidades.
Educativo: Aprenda a arte de conectar e manipular bancos de dados em Python, com códigos claros e comentados.
Versátil: Alterne facilmente entre diferentes tipos de bancos de dados.


### 🌟 Contribua

Junte-se à nossa expedição de caçadores de tesouros de dados! Quer você tenha um novo mapa (script) para adicionar ou uma melhoria para sugerir, suas contribuições são bem-vindas.

Fork o Repositório
***Crie sua Branch de Feature:***
```bash
git checkout -b nova-descoberta
```
***Commit suas Mudanças:***
```bash
git commit -m 'Adicionar nova descoberta'
```
***Push para a Branch:***
```bash
git push origin nova-descoberta
```
***Abra um Pull Request***

### 🌲 Destaques

Conexões Dinâmicas: Alterne facilmente entre diferentes tipos de bancos de dados.
Acesso Seguro: Siga as melhores práticas para conexões de banco de dados seguras.
Consultas de Exemplo: Comece rapidamente com consultas e operações de exemplo.

### 🏆 Boa Caça! 🗺️✨

Desbloqueie o poder do Python para conectar e manipular seus reinos de dados com facilidade. Explore, aprenda e torne-se o caçador de tesouros de dados que você sempre sonhou ser!







# Author

| [<img src="https://avatars.githubusercontent.com/u/79289647?v=4" width=115><br><sub>Carlos Hayden</sub>](https://github.com/JunhaumHayden) |
| :---: |



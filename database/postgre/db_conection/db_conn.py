import psycopg2
from psycopg2 import sql, OperationalError

class DBConnection:
    """
       Classe para gerenciar conexão com o banco de dados PostgreSQL.

       Esta classe encapsula as operações básicas de conexão, execução de queries e encerramento da conexão.

       Atributos:
           host (str): Endereço do servidor PostgreSQL.
           port (int): Porta de conexão (padrão: 5432).
           user (str): Usuário do banco.
           password (str): Senha do usuário.
           dbname (str): Nome do banco de dados.
           conn: Objeto de conexão psycopg2.
           cur: Cursor para execução de queries.

       Métodos:
           connect(): Estabelece conexão com o banco.
           execute(query, params=None): Executa uma query SQL.
           fetchall(): Retorna todos os resultados da última query.
           close(): Fecha o cursor e a conexão com o banco.
       """

    def __init__(self, host, port, user, password, dbname, logger=None):
        self.host = host
        self.port = port

        self.user = user
        self.password = password

        self.dbname = dbname
        self.conn = None
        self.cursor = None
        self.logger = logger

    def connect(self):
         """Estabelece a conexão com o banco de dados PostgreSQL."""
         try:
             self.conn = psycopg2.connect(
                 host=self.host,
                 port=self.port,
                 user=self.user,
                 password=self.password,
                 dbname=self.dbname,
                 sslmode='disable'
             )
             self.cursor = self.conn.cursor()
             self.logger.info(f" ✅ Conectado ao banco {self.dbname} ".center(50, "+"))
         except OperationalError as e:
            self.logger.error(f"Erro ao conectar ao banco: {e}")
            raise
    def execute(self, query, params=None):
        """
                Executa uma query SQL no banco de dados.

                Args:
                    query (str): Query SQL a ser executada.
                    params (tuple): Parâmetros opcionais para queries parametrizadas.
                """
        try:
            self.cursor.execute(query, params or ())
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            self.logger.warning(f"Erro na query  causa: {e} acao: rollback ")
            raise
    def fetchall(self):
        """
                Retorna todos os resultados da última query SELECT.

                Returns:
                    list: Lista de tuplas contendo os resultados.
                """
        return self.cursor.fetchall()
    def close(self):
        """Fecha o cursor e a conexão com o banco de dados."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        self.logger.info(f" 🔌 Conexão fechada. ".center(50,"#"))
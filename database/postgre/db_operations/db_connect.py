import os
import logging
from dotenv import load_dotenv

from database.postgre.db_conection.db_conn import DBConnection

# Carregar variáveis do arquivo .env
load_dotenv()

# Configuração global do logger
logging.basicConfig(
    level=logging.INFO,  # pode trocar para DEBUG para ver mais detalhes
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Criando instância do logger
my_logger = logging.getLogger("PipelineTest")

# Criar objeto de conexão usando variáveis de ambiente
db = DBConnection(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT", 5432)),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    dbname=os.getenv("DB_NAME"),
    logger=my_logger
)



if __name__ == "__main__":
    db.connect()

    db.execute("SELECT NOW();")
    print("Conexão bem sucedida! Horário atual:", db.cursor.fetchone()[0])
    db.close()


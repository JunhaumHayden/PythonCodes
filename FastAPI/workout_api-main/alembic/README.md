Generic single-database configuration.

## Alembic 
é uma ferramenta de migração de banco de dados para o SQLAlchemy, usada para gerenciar mudanças no esquema de banco de dados. Aqui estão os passos para instalar e usar o Alembic em um projeto.

#### Passo 1: Instalar Alembic
Primeiro, ative seu ambiente Conda (se necessário) e instale o Alembic. Você pode usar Conda ou Pip para isso.

- Ativar o ambiente Conda:

```sh
conda activate py311
```
- Instalar o Alembic:

```sh
conda install alembic
```
ou, se não estiver disponível via Conda:

```sh
pip install alembic
```
Passo 2: Inicializar o Alembic
Depois de instalar o Alembic, inicialize-o no diretório do seu projeto. Isso criará a estrutura de diretórios necessária e o arquivo de configuração alembic.ini.

- Inicializar o Alembic:
```sh
alembic init alembic
```
Isso criará uma estrutura de diretórios como esta:

```sh
my_project/
├── alembic/
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions/
└── alembic.ini
```
Passo 3: Configurar o Alembic
Edite o arquivo `alembic.ini` para configurar a URL de conexão do banco de dados. Encontre a linha `sqlalchemy.url` e configure-a com a URL do seu banco de dados.

```sh
# alembic.ini
sqlalchemy.url = sqlite:///my_database.db  # Exemplo para SQLite
# sqlalchemy.url = postgresql://user:password@localhost/mydatabase  # Exemplo para PostgreSQL
```
Passo 4: Editar `env.py`
No diretório `alembic`, edite o arquivo `env.py` para configurar o Alembic com seu modelo SQLAlchemy. Você precisa modificar a função run_migrations_online para incluir seu modelo SQLAlchemy.

```python
# alembic/env.py

from myapp import mymodel  # Importe seu modelo SQLAlchemy aqui
from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
import os

# Este é o seu modelo SQLAlchemy
target_metadata = mymodel.Base.metadata

config = context.config

# Este arquivo de configuração pode ser configurado em config.fileConfig() ou
# via linha de comando. Aqui usamos a configuração do arquivo.
fileConfig(config.config_file_name)

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```
Passo 5: Criar uma Revisão
Crie uma nova revisão para capturar mudanças no esquema de banco de dados.

Criar uma revisão:
```sh
alembic revision -m "create initial tables"
```
Isso criará um novo arquivo de migração no diretório alembic/versions.

Passo 6: Editar a Revisão
Edite o novo arquivo de revisão para definir as mudanças no esquema de banco de dados.

```python
# alembic/versions/xxxxxxxxxxxx_create_initial_tables.py

from alembic import op
import sqlalchemy as sa

# Revisão identificadores, usados pelo Alembic
revision = 'xxxxxxxxxxxx'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Código para aplicar a migração
    op.create_table(
        'my_table',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False)
    )

def downgrade():
    # Código para reverter a migração
    op.drop_table('my_table')
```
Passo 7: Aplicar a Migração
Depois de definir a revisão, aplique a migração para atualizar o esquema do banco de dados.

Aplicar a migração:
```sh
alembic upgrade head
```
Passo 8: Gerenciar Migrações
Você pode criar novas revisões sempre que precisar alterar o esquema do banco de dados e aplicar essas revisões usando comandos semelhantes.

Criar uma nova revisão:

```sh
alembic revision -m "descricao_da_mudanca"
```
Aplicar migrações:

```sh
alembic upgrade head
```
Reverter migrações:

```sh
alembic downgrade -1
```
Resumo dos Comandos
Instalar Alembic:

```sh
conda install alembic  # ou pip install alembic
```
Inicializar o Alembic no projeto:

```sh
alembic init alembic
```
Configurar o arquivo alembic.ini com a URL do banco de dados.

Editar alembic/env.py para incluir seu modelo SQLAlchemy.

Criar uma nova revisão:

```sh
alembic revision -m "create initial tables"
```
Editar a revisão para definir as mudanças no esquema de banco de dados.

Aplicar a migração:

```sh
alembic upgrade head
```
Seguindo esses passos, você deve conseguir instalar e usar o Alembic para gerenciar migrações de banco de dados em seu projeto Python.






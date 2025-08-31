# Tutorial: Configuração do PostgreSQL em Instância Multipass

Este guia documenta os passos para configurar, acessar e testar um banco de dados **PostgreSQL** rodando em uma instância Multipass a partir do host (Linux Ubuntu).

---

## 1. Acessar a instância Multipass
```bash
multipass shell db-postgre
```

---

## 2. Verificar se o PostgreSQL está rodando
```bash
sudo pg_isready
```
Saída esperada:
```
/var/run/postgresql:5432 - accepting connections
```

---

## 3. Conectar ao PostgreSQL dentro da instância

Quando se está dentro da instância Multipass (onde o PostgreSQL está rodando), pode se conectar localmente de duas formas:

1. Usando o usuário do sistema postgres

Quando se instalou o PostgreSQL, foi criado um usuário do Linux chamado postgres e um usuário do banco também chamado postgres (superusuário).

Então, dentro da VM:

```bash
# entrar como usuário postgres do Linux
sudo -i -u postgres
``` 
Agora, estando logado como postgres, você pode abrir o cliente do banco:
```bash
psql
```
> Isso conecta diretamente ao banco postgres como o superusuário.
2. Conectar a um banco específico

Se quiser se conectar diretamente ao banco mylessons como postgres:
```bash
psql -d mylessons
``` 
ou, de fora do usuário postgres (se tiver senha definida para o usuário do banco):
```bash
psql -U postgres -d mylessons -h localhost -p 5432
```
3. Conectar com o usuário python

Se você quiser conectar localmente já com o seu usuário python:
```bash
psql -U python -d mylessons -h localhost -p 5432
```
> Ele vai pedir a senha que você definiu para o usuário python.

Caiu direto no banco padrão postgres como usuário postgres:
```bash
postgres=#
```

Resumindo:

sudo -i -u postgres && psql → conecta como superusuário direto.

psql -U python -d mylessons -h localhost → conecta com seu usuário de projeto.

Comandos úteis nesse modo

Dentro do psql:

Listar bancos de dados:
```bash
\l

```
Conectar em um banco específico:
```bash
\c mylessons

```
Listar schemas:
```bash
```
Listar tabelas:
```bash
\dn

```
Sair do psql:
```bash
\q

```
Esse acesso como postgres é importante porque te dá controle total para:

Criar usuários (CREATE ROLE ...).

Dar permissões (GRANT ...).

Alterar schemas (ALTER SCHEMA ...).

Ajustar o search_path de usuários (ALTER ROLE ...).

⚠️ Mas para o dia a dia de desenvolvimento você deve usar seu usuário python — só use postgres quando precisar de privilégios de administração.


```bash
```


```bash
psql -h localhost -p 5432 -U python -d northwind
```

---

## 4. Criação de Banco de Dados e Tabelas

### Criar um novo banco de dados
```sql
CREATE DATABASE exemplo_db;
```

### Conectar ao banco
```bash
\c exemplo_db;
```

### Criar tabela de exemplo
```sql
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Inserir registros
```sql
INSERT INTO clientes (nome, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com');
```

### Consultar registros
```sql
SELECT * FROM clientes;
```

---

## 5. Criar Usuários e Permissões

### Criar um usuário
```sql
CREATE USER python WITH PASSWORD 'sua_senha_segura';
```

### Conceder permissões
```sql
GRANT ALL PRIVILEGES ON DATABASE exemplo_db TO python;
```

---

## 6. Arquivos Importantes de Configuração

### `postgresql.conf`
- Localização: `/etc/postgresql/<versão>/main/postgresql.conf`
- Importante para definir parâmetros como:
  - Porta de escuta (`port = 5432`)
  - Endereços de rede (`listen_addresses = '*'`)

### `pg_hba.conf`
- Localização: `/etc/postgresql/<versão>/main/pg_hba.conf`
- Controla como clientes podem autenticar:
  - Método `md5` → autenticação com senha
  - Método `peer` → autenticação pelo usuário do SO
  - Método `trust` → sem autenticação (apenas para testes!)

Exemplo de entrada para permitir acesso de qualquer IP com senha:
```
host    all             all             0.0.0.0/0               md5
```

> Sempre reinicie o PostgreSQL após mudanças:
```bash
sudo systemctl restart postgresql
```

---

## 7. Acesso ao PostgreSQL a partir do Host

1. Descobrir o IP da instância Multipass:
```bash
multipass info db-postgre
```
Exemplo de saída:
```
IPv4             10.24.238.217
```

2. Conectar a partir do host:
```bash
psql "host=10.24.238.217 port=5432 user=python dbname=northwind sslmode=disable"
```

---

## 8. Testar conexão via Python

```python
import psycopg2

try:
    conn = psycopg2.connect(
        host="10.24.238.217",
        port=5432,
        dbname="northwind",
        user="python",
        password="sua_senha_segura",
        sslmode="disable"
    )
    print("Conexão bem sucedida!")
    conn.close()
except Exception as e:
    print("Erro ao conectar:", e)
```

---

## 9. Observações
- Para desenvolvimento, pode desativar SSL usando `sslmode=disable`.
- Em produção, **sempre** configure SSL.
- `postgresql.conf` + `pg_hba.conf` são os dois principais arquivos de configuração.

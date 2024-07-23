import duckdb
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Obter credenciais do PostgreSQL do arquivo .env
username = os.getenv('POSTGRES_USERNAME')
password = os.getenv('POSTGRES_PASSWORD')
hostname = os.getenv('POSTGRES_HOSTNAME')
port = os.getenv('POSTGRES_PORT')
dbname = os.getenv('POSTGRES_DBNAME')
schema = os.getenv('POSTGRES_SCHEMA')

# Lista de tabelas a serem extraídas
tables = ['orders', 'order_details', 'customers', 'products']

# Conectar ao PostgreSQL usando SQLAlchemy
postgres_engine = create_engine(f'postgresql://{username}:{password}@{hostname}:{port}/{dbname}')

# Conectar ao DuckDB
duckdb_conn = duckdb.connect('my_database.db')

# Iterar sobre as tabelas e extrair dados
for table in tables:
    # Extrair dados do PostgreSQL usando pandas
    query = f'SELECT * FROM {schema}.{table}'
    df = pd.read_sql(query, postgres_engine)
    
    # Criar tabela no DuckDB e inserir dados
    df.to_sql(table, duckdb_conn, if_exists='replace', index=False)

# Fechar a conexão
duckdb_conn.close()

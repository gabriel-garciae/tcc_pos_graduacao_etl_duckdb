import duckdb
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

#credenciais do PostgreSQL
username = os.getenv('POSTGRES_USERNAME')
password = os.getenv('POSTGRES_PASSWORD')
hostname = os.getenv('POSTGRES_HOSTNAME')
port = os.getenv('POSTGRES_PORT')
dbname = os.getenv('POSTGRES_DBNAME')
schema = os.getenv('POSTGRES_SCHEMA')

#tabelas a serem extraídas
tables = ['orders', 'order_details', 'customers', 'products']

#conectar ao PostgreSQL usando SQLAlchemy
postgres_engine = create_engine(f'postgresql://{username}:{password}@{hostname}:{port}/{dbname}')

#conectar ao DuckDB
duckdb_conn = duckdb.connect('my_database.db')

#iterar sobre as tabelas e extrair dados
for table in tables:
    query = f'SELECT * FROM {schema}.{table}'
    df = pd.read_sql(query, postgres_engine)
    
    #criar tabela no DuckDB e inserir dados
    df.to_sql(table, duckdb_conn, if_exists='replace', index=False)


duckdb_conn.close()

import duckdb
from dotenv import load_dotenv
import os
import duckdb

load_dotenv()

# credenciais do MotherDuck
motherduck_token = os.getenv('MOTHERDUCK_TOKEN')

con = duckdb.connect(f"md:?motherduck_token={motherduck_token}")

# rodar a query para verificar se está conectado
con.sql("SHOW DATABASES").show()
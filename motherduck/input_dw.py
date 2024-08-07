from dotenv import load_dotenv
import os
import duckdb

load_dotenv()

# credenciais do MotherDuck
motherduck_token = os.getenv('MOTHERDUCK_TOKEN')

local_con = duckdb.connect("md:my_db")

# código usado para criar o DW no motherduck a partir do banco local duckdb
#local_con.sql("CREATE DATABASE clouddb FROM 'my_database.db'")

# consultando alguma tabela ja no motherduck
local_con.sql("SELECT * FROM clouddb.dim_customers").show(); 
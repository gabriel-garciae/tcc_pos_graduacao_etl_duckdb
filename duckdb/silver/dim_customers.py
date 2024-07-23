import duckdb

# Conectar ao DuckDB
duckdb_conn = duckdb.connect('my_database.db')

# Criar a tabela dim_customers
duckdb_conn.execute('''
CREATE TABLE IF NOT EXISTS dim_customers AS
SELECT DISTINCT
    customer_id,
    company_name AS customer_name,
    contact_name,
    contact_title,
    address,
    city,
    region,
    postal_code,
    country,
    phone
FROM
    customers
''')

# Fechar a conexão
duckdb_conn.close()

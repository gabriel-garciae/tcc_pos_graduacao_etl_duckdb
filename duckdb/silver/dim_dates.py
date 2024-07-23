import duckdb

# Conectar ao DuckDB
duckdb_conn = duckdb.connect('my_database.db')

# Criar a tabela dim_dates
duckdb_conn.execute('''
CREATE TABLE IF NOT EXISTS dim_dates AS
SELECT DISTINCT
    order_date AS date,
    EXTRACT(year FROM order_date) AS year,
    EXTRACT(month FROM order_date) AS month,
    EXTRACT(day FROM order_date) AS day
FROM
    orders
''')

# Fechar a conexão
duckdb_conn.close()

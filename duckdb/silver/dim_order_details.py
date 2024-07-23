import duckdb

# Conectar ao DuckDB
duckdb_conn = duckdb.connect('my_database.db')

# Criar a tabela dim_order_details
duckdb_conn.execute('''
CREATE TABLE IF NOT EXISTS dim_order_details AS
SELECT DISTINCT
    order_id,
    product_id,
    unit_price,
    quantity,
    discount
FROM
    order_details
''')

# Fechar a conexão
duckdb_conn.close()

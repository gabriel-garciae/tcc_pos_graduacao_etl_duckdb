import duckdb

# Conectar ao DuckDB
duckdb_conn = duckdb.connect('my_database.db')

# Criar a tabela dim_products
duckdb_conn.execute('''
CREATE TABLE IF NOT EXISTS dim_products AS
SELECT DISTINCT
    product_id,
    product_name,
    supplier_id,
    category_id,
    quantity_per_unit,
    unit_price,
    units_in_stock,
    units_on_order,
    reorder_level,
    discontinued
FROM
    products
''')

# Fechar a conexão
duckdb_conn.close()

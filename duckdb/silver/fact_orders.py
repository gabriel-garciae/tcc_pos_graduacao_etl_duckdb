import duckdb

'''
execute(query):

Executa a query SQL passada como argumento.
Retorna um cursor que aponta para o conjunto de resultados da query.
fetchall():

Itera sobre o cursor e busca todos os registros do resultado da query.
Retorna esses registros como uma lista de tuplas.
Cada tupla contém os valores de uma linha da tabela.
'''

# Conectar ao DuckDB
duckdb_conn = duckdb.connect('my_database.db')

# Criar a tabela fact_orders
duckdb_conn.execute('''
CREATE TABLE IF NOT EXISTS fact_orders AS
SELECT
*
FROM orders
''')

# Fechar a conexão
duckdb_conn.close()

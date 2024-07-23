import duckdb
from tabulate import tabulate

# Conectar ao DuckDB
duckdb_conn = duckdb.connect('my_database.db')

# Função para exibir os resultados de uma tabela
def display_table_data(conn, table_name):
    query = f'SELECT * FROM {table_name}'
    cursor = conn.execute(query)
    result = cursor.fetchall()

    # Verificar se a query retornou resultados
    if result:
        # Obter os nomes das colunas
        columns = [desc[0] for desc in cursor.description]
        
        # Usar tabulate para exibir os resultados em formato de tabela
        print(f'\nDados da tabela {table_name}:')
        print(tabulate(result, headers=columns, tablefmt='grid'))
    else:
        print(f'Nenhum resultado encontrado para a tabela {table_name}.')

# Exibir os dados das tabelas
tables_to_display = ['fact_orders', 'dim_customers', 'dim_products', 'dim_dates', 'dim_order_details']

for table in tables_to_display:
    display_table_data(duckdb_conn, table)

# Fechar a conexão
duckdb_conn.close()
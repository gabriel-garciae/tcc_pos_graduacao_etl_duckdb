import pandas as pd
import duckdb

# conectar ao DuckDB
conn = duckdb.connect('my_database.db')

# carregar os dados para um DataFrame
df = conn.execute('SELECT * FROM fact_orders').df()

# validar se há valores nulos
print("Valores nulos em 'order_id':", df['order_id'].isnull().sum())

# validar se há valores fora de intervalo
print("Valores fora do intervalo em 'employee_id':", (df['employee_id'] < 0).sum())

# validar se há valores inesperados em 'employee_id'
print("Valores inesperados em 'employee_id':", df[~df['employee_id'].isin([1, 2, 3, 4, 5, 6, 8, 9])].shape[0])

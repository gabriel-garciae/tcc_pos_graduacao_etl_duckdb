import duckdb

local_con = duckdb.connect("md:clouddb")

# Consultando alguma tabela já no MotherDuck
query = """
select
    products.product_name, 
    sum(order_details.unit_price * order_details.quantity * (1.0 - order_details.discount)) as sales
from 
    dim_products products
inner join 
    dim_order_details as order_details on order_details.product_id = products.product_id
group by 
    products.product_name
order by 
    sales desc
limit 10
"""

result = local_con.sql(query).fetchall()

# Exibindo o resultado
for row in result:
    print(row)

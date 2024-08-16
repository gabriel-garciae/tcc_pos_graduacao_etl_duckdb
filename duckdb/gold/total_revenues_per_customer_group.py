import duckdb

local_con = duckdb.connect("md:clouddb")

# Consultando alguma tabela já no MotherDuck
query = """
select 
    customers.customer_name, 
    sum(order_details.unit_price * order_details.quantity * (1.0 - order_details.discount)) as total,
    ntile(5) over (order by sum(order_details.unit_price * order_details.quantity * (1.0 - order_details.discount)) desc) as group_number
from 
    dim_customers as customers
inner join 
    fact_orders as orders on customers.customer_id = orders.customer_id
inner join 
    dim_order_details as order_details on order_details.order_id = orders.order_id
group by 
    customers.customer_name
order by 
    total desc
"""

result = local_con.sql(query).fetchall()

# Exibindo o resultado
for row in result:
    print(row)

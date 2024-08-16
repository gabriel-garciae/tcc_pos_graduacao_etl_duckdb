import duckdb

local_con = duckdb.connect("md:clouddb")

# Consultando alguma tabela já no MotherDuck
query = """
select 
    customers.contact_name, 
    sum(order_details.unit_price * order_details.quantity * (1.0 - order_details.discount) * 100) / 100 as payments
from 
    dim_customers as customers
inner join 
    fact_orders as orders on orders.customer_id = customers.customer_id
inner join 
    dim_order_details as order_details on order_details.order_id = orders.order_id
where 
    lower(customers.country) = 'uk'
group by 
    customers.contact_name
having 
    sum(order_details.unit_price * order_details.quantity * (1.0 - order_details.discount)) > 1000
"""

result = local_con.sql(query).fetchall()

# Exibindo o resultado
for row in result:
    print(row)

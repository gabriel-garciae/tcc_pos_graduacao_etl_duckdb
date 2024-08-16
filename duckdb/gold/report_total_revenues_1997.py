import duckdb

local_con = duckdb.connect("md:clouddb")

# Consultando alguma tabela já no MotherDuck
query = """
with ord as (
    select order_id 
    from fact_orders
    where extract(year from order_date) = 1997
)
select 
    sum(order_details.unit_price * order_details.quantity * (1.0 - order_details.discount)) as total_revenues_1997
from 
    dim_order_details as order_details
inner join 
    ord on ord.order_id = order_details.order_id
"""

result = local_con.sql(query).fetchall()

# Exibindo o resultado
for row in result:
    print(row)

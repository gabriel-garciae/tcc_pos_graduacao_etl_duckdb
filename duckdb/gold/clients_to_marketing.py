import duckdb

local_con = duckdb.connect("md:clouddb")

# Consultando alguma tabela já no MotherDuck
query = """
WITH clientes_para_marketing AS (
    SELECT 
        customers.customer_name,
        SUM(order_details.unit_price * order_details.quantity * (1.0 - order_details.discount)) AS total,
        NTILE(5) OVER (ORDER BY SUM(order_details.unit_price * order_details.quantity * (1.0 - order_details.discount)) DESC) AS group_number
    FROM 
        dim_customers AS customers
    INNER JOIN 
        fact_orders AS orders ON customers.customer_id = orders.customer_id
    INNER JOIN 
        dim_order_details AS order_details ON order_details.order_id = orders.order_id
    GROUP BY 
        customers.customer_name
    ORDER BY 
        total DESC
)
SELECT *
FROM clientes_para_marketing
WHERE group_number >= 3;
"""

result = local_con.sql(query).fetchall()

# Exibindo o resultado
for row in result:
    print(row)

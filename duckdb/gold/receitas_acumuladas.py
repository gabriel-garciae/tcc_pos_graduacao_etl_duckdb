import duckdb

local_con = duckdb.connect("md:clouddb")

# Consultando alguma tabela já no MotherDuck
query = """
with receitas_mensais as (
    select
        extract(year from orders.order_date) as ano,
        extract(month from orders.order_date) as mes,
        sum(order_details.unit_price * order_details.quantity * (1.0 - order_details.discount)) as receita_mensal
    from
        fact_orders as orders
    inner join
        dim_order_details as order_details on orders.order_id = order_details.order_id
    group by
        extract(year from orders.order_date),
        extract(month from orders.order_date)
),
receitas_acumuladas as (
    select
        ano,
        mes,
        receita_mensal,
        sum(receita_mensal) over (partition by ano order by mes) as receita_ytd
    from
        receitas_mensais
)
select
    ano,
    mes,
    receita_mensal,
    receita_mensal - lag(receita_mensal) over (partition by ano order by mes) as diferenca_mensal,
    receita_ytd,
    (receita_mensal - lag(receita_mensal) over (partition by ano order by mes)) / lag(receita_mensal) over (partition by ano order by mes) * 100 as percentual_mudanca_mensal
from
    receitas_acumuladas
order by
    ano, mes
"""

result = local_con.sql(query).fetchall()

# Exibindo o resultado
for row in result:
    print(row)

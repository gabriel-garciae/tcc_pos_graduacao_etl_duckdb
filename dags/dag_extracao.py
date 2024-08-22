from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

# Função para executar o código de extração
#def run_extracao():
#    exec(open("/opt/duckdb/raw/extracao.py").read())

def run_extracao():
    print("Hello Airflowwwwwwwwwwwwww")

# Definição da DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 21),
    'email_on_failure': False,
    'email_on_retry': False,
}

with DAG(
    'dag_extracao',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:

    task_extracao = PythonOperator(
        task_id='run_extracao',
        python_callable=run_extracao,
    )

    task_extracao

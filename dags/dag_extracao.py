from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

#função para executar o código de extração
def run_extracao():
   exec(open("/opt/duckdb/raw/extracao.py").read())

#função para executar o código de extração
def run_carregamento():
   exec(open("/opt/motherduck/input_dw.py").read())


#definição da DAG
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

    task_carregamento = PythonOperator(
        task_id='run_carregamento',
        python_callable=run_carregamento,
    )

    task_extracao >> task_carregamento

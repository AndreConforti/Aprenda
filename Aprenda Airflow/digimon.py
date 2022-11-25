from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from digimon_etl import connect_to_api

defaul_args = {
    'owner': 'airflow',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='digimon',
    default_args=defaul_args,
    start_date=datetime(2022, 11, 23),
    schedule_interval='@daily',
    catchup=False
) as dag:
    task1 = PythonOperator(
        task_id='get_data',
        python_callable=connect_to_api
    )

task1
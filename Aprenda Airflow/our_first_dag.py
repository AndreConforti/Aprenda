from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='our_first_dag_v3',
    default_args=default_args,
    description='This is our first dag that we write',
    start_date=datetime(2022, 11, 10, 2),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id = 'first_task',
        bash_command="echo hello word, this is our first task"
    )
    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo Hey, I am the task2 and will be running after task1"
    )
    task3 = BashOperator(
        task_id='third_task',
        bash_command="echo Hey, I am task3 and will be running after task1 at the same time as task2"
    )

    task1.set_downstream(task2)
    task1.set_downstream(task3)
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from random import randint

default_args = {
    'owner':'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name  = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(f"Hello World! My name is {first_name} {last_name}, "
          f"and I am {age} years old!")
    if age >= 50:
        print("I'm getting old")

def get_name(ti):
    ti.xcom_push(key='first_name', value='Andre')
    ti.xcom_push(key='last_name', value='Conforti')


def get_age(ti):
    age = randint(0, 80)
    ti.xcom_push(key='age', value=age)


with DAG(
    default_args=default_args,
    dag_id='our_dag_with_python_operator_v7',
    description='Our first dag using python operator',
    start_date=datetime(2022, 11, 17),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={'age': 44}
    )
    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )
    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )

    [task2,task3]  >> task1
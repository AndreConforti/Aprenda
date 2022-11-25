import requests
import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def search():
    url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"

    response = requests.get(url).json()
    card = {}
    cartas = []

    for carta in response['data']:
        card.clear()
        card['nome'] = carta['name']
        card['url'] = carta['card_images'][0]['image_url']
        cartas.append(card.copy())

    df = pd.DataFrame(cartas)

    return df.to_csv('./files/YuGiOh.csv')

default_args = {
    'owner': 'Andre',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id = 'YiGiOh',
    default_args=default_args,
    start_date=datetime(2022, 11, 21),
    schedule_interval='@daily',
    catchup=False,
) as dag:
    task1 = PythonOperator(
        task_id='task1',
        python_callable=search
    )

    task1

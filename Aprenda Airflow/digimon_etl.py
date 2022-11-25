import requests
import pandas as pd
import csv

def connect_to_api():
    url = 'https://digimon-api.vercel.app/api/digimon/'

    response = requests.request('GET', url).json()

    df = pd.DataFrame(response)

    df.drop(['level'], axis=1, inplace=True)

    return df.to_csv('./files/digimon.csv')

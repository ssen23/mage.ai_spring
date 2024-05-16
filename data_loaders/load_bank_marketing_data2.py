import pandas as pd
import requests
from io import StringIO

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://github.com/ssen23/mage-ai_spring/raw/master/Bank_Marketing.csv'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.content.decode('utf-8')
        df = pd.read_csv(StringIO(data), sep=';')  # sep 매개변수를 세미콜론으로 설정
        return df
    else:
        raise ValueError("Failed to fetch data from API")

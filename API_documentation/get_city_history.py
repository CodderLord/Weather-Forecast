import requests
from Config import IP, PORT


def api_get_cities_history():
    data_response = requests.get(f'http://{IP}:{PORT}/api/city_stats').json()
    print(f'Вот данные по статистике всех городов \n{data_response}')

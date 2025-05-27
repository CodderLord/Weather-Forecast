import os

from dotenv import load_dotenv

load_dotenv()

CITY_DADATA_URL = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address"

WEATHER_URL = "https://api.open-meteo.com/v1"

CACHE_EXPIRE = 3600  # 1 hour
REQUEST_TIMEOUT = 5  # 5 sec timeout

DADATA_API_KEY = os.getenv('DADATA_API_KEY')
DADATA_SECRET = os.getenv('DADATA_SECRET')

IP = os.getenv('IP')
PORT = os.getenv('PORT')

HISTORY_DB = f"{os.getcwd()}\\DB\\user_history.json"
STATS_DB = f"{os.getcwd()}\\DB\\city_stats.json"

WEATHER_CODES = {
    0: "Ясно",
    1: "Средне ясно",
    2: "Облачно",
    3: "Пасмурно",
    45: "Туман",
    51: "Морось",
    61: "Дождь",
    80: "Ливень",
    95: "Гроза"
}


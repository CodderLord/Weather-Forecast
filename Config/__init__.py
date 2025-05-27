from .config import (CACHE_EXPIRE, REQUEST_TIMEOUT,
                     DADATA_API_KEY, DADATA_SECRET,
                     WEATHER_URL, CITY_DADATA_URL,
                     WEATHER_CODES, HISTORY_DB ,
                     STATS_DB, IP,
                     PORT)

from .log_config import setup_logger


logger = setup_logger()
import openmeteo_requests
import requests_cache
from retry_requests import retry

from Config import CACHE_EXPIRE


cache_session = requests_cache.CachedSession('.cache', expire_after=CACHE_EXPIRE)
retry_session = retry(cache_session, retries=3, backoff_factor=0.5)
open_meteo = openmeteo_requests.Client(session=retry_session)
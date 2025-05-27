import pandas as pd

from Caсhe import open_meteo
from Config import logger, WEATHER_URL, WEATHER_CODES


def get_weather_data(lat, lon):
    """
    Gets weather data from Open-Meteo API by coordinates.
    :param lat: Latitude
    :param lon: Longitude
    :return: response or None
    """
    if lat is None or lon is None:
        logger.error("Invalid coordinates: lat or lon is None")
        return None

    url = f"{WEATHER_URL}/forecast"
    logger.debug(f'Get weather {lat=}, {lon=}')

    try:
        response = open_meteo.weather_api(url, params={
            "latitude": lat,
            "longitude": lon,
            "current": ["temperature_2m", "relative_humidity_2m",
                        "apparent_temperature", "weather_code",
                        "wind_speed_10m"],
            "daily": ["weather_code", "temperature_2m_max",
                      "temperature_2m_min", "precipitation_probability_max"],
            "timezone": "auto",
            "forecast_days": 8
        })[0]
        return response
    except Exception as e:
        logger.error(f"Weather API error for {lat},{lon}: {e}")
        return None


def format_weather_data(response, original_city):
    """
    Converts raw data from the weather API into a format that is easy to display.
    :param response: response from Open-Meteo API
    :param original_city: City name
    :return:
    """
    city_name = original_city.split(",")[0].strip()
    logger.debug(f'Format weather data {city_name=}')

    def convert_value(value):
        if hasattr(value, 'item'):
            return float(value.item())
        return float(value) if isinstance(value, (float, int)) else value
    try:
        current = response.Current()
        logger.debug(f"WEATHER_CODES is {int(current.Variables(3).Value())}")
        current_data = {
            "temperature": int(convert_value(current.Variables(0).Value())),
            "humidity": convert_value(current.Variables(1).Value()),
            "feels_like": int(convert_value(current.Variables(2).Value())),
            "weather": WEATHER_CODES.get(int(current.Variables(3).Value()), "Неизвестно"),
            "wind_speed": int(convert_value(current.Variables(4).Value()))
        }
    except Exception as e:
        logger.error(f"Error processing current weather: {e}")
        current_data = {
            "temperature": 0,
            "humidity": 0,
            "feels_like": 0,
            "weather": "Нет данных",
            "wind_speed": 0
        }

    try:
        daily = response.Daily()
        dates = pd.date_range(
            start=pd.to_datetime(daily.Time(), unit="s", utc=True),
            end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=daily.Interval()),
            inclusive="left"
        )

        forecast = []
        for i in range(min(len(dates), 8)):
            forecast.append({
                "date": dates[i].strftime("%d.%m.%Y"),
                "weather": WEATHER_CODES.get(int(daily.Variables(0).ValuesAsNumpy()[i]), "Неизвестно"),
                "temp_max": int(convert_value(daily.Variables(1).ValuesAsNumpy()[i])),
                "temp_min": int(convert_value(daily.Variables(2).ValuesAsNumpy()[i])),
                "precipitation": convert_value(daily.Variables(3).ValuesAsNumpy()[i])
            })
    except Exception as e:
        logger.error(f"Forecast processing error: {e}")
        forecast = []

    logger.debug(f'Format weather data {city_name=}')
    return {
        "city": city_name,
        "current": current_data,
        "forecast": forecast
    }

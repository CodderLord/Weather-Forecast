import requests
from Config import REQUEST_TIMEOUT, DADATA_API_KEY, DADATA_SECRET, CITY_DADATA_URL, logger

HEADERS = {
    "Authorization": f"Token {DADATA_API_KEY}",
    "X-Secret": DADATA_SECRET,
    "Content-Type": "application/json"
}


def get_city_suggestions(query):
    """
    Gets city suggestions based on partial user input.
    Uses DaData API to accurately search for Russian cities.
    :param query: City name (part)
    :return: list with city names format "City, Region, Country"
    """
    if len(query) < 2:
        return []

    params = {
        "query": query,
        "count": 5,
        "locations": [{"country": "Россия"}],
        "from_bound": {"value": "city"},
        "to_bound": {"value": "city"}
    }

    try:
        logger.debug(f"Requesting city suggestions for query: {query}")
        response = requests.post(CITY_DADATA_URL, headers=HEADERS, json=params, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        logger.debug(f"Received suggestions: {response.json().get('suggestions', [])}")

        suggestions = []
        for item in response.json().get("suggestions", []):
            data = item.get("data", {})
            if "city" in data:
                parts = [
                    data.get("city"),
                    data.get("region_with_type"),
                    data.get("country")
                ]
                suggestion = ", ".join(filter(None, parts))
                suggestions.append(suggestion)

        logger.debug(f"Formatted suggestions: {suggestions}")
        return suggestions

    except requests.RequestException as e:
        logger.error(f"Error getting city suggestions: {str(e)}")
        return []


def get_city_coordinates(city_name):
    """
    Gets geographic coordinates (latitude and longitude) for a city.
    :param city_name: Name city on format "City, Region"
    :return: tuple: (latitude, longitude) or (None, None) if not find city
    """
    try:
        logger.debug(f"Getting coordinates for city: {city_name}")
        response = requests.post(
            CITY_DADATA_URL,
            headers=HEADERS,
            json={
                "query": city_name.split(",")[0].strip(),
                "count": 1,
                "locations": [{"country": "Россия"}]
            },
            timeout=REQUEST_TIMEOUT
        )
        response.raise_for_status()

        location = response.json().get("suggestions", [{}])[0].get("data", {})

        geo_lat = location.get("geo_lat")
        geo_lon = location.get("geo_lon")

        if geo_lat is not None and geo_lon is not None and geo_lat != "" and geo_lon != "":
            try:
                coordinates = (float(geo_lat), float(geo_lon))
                logger.debug(f"Found coordinates for {city_name}: {coordinates}")
                return coordinates
            except (ValueError, TypeError) as e:
                logger.error(f"Invalid coordinate values for {city_name}: lat={geo_lat}, lon={geo_lon}")
                return None, None
        else:
            logger.warning(f"No valid coordinates found for city: {city_name}")
            return None, None

    except requests.RequestException as e:
        logger.error(f"Error getting coordinates: {str(e)}")
        return None, None
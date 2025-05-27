from flask import render_template, request, jsonify, make_response

from APP import weather_app
from City import get_city_suggestions, get_city_coordinates
from UserManager import track_user_history
from UserManager.user_data import get_user_id, load_json_file, save_json_file
from Weather import get_weather_data, format_weather_data
from Config import logger, HISTORY_DB, STATS_DB


@weather_app.route("/")
@track_user_history
def index():
    user_id = get_user_id(request)
    history = load_json_file(HISTORY_DB, {})
    user_history = history.get(user_id, {}).get("cities", [])

    # Get last searched city if exists
    last_city = user_history[-1] if user_history else None

    return render_template("index.html", last_city=last_city)


@weather_app.route("/get_suggestions", methods=["GET"])
def get_suggestions():
    query = request.args.get("query")
    if not query or len(query) < 2:
        return jsonify([])

    suggestions = get_city_suggestions(query)
    return jsonify(suggestions)


@weather_app.route("/get_weather", methods=["POST"])
@track_user_history
def get_weather():
    city = request.form.get("city")
    if not city:
        return jsonify({"error": "Введите название города"}), 400

    logger.info(f"Weather search for city: {city}")

    # Update city statistics
    stats = load_json_file(STATS_DB, {})
    stats[city] = stats.get(city, 0) + 1
    save_json_file(STATS_DB, stats)

    # Update user history
    user_id = get_user_id(request)
    history = load_json_file(HISTORY_DB, {})
    if user_id not in history:
        history[user_id] = {"cities": []}

    # Add city to history if not already the last one
    if not history[user_id]["cities"] or history[user_id]["cities"][-1] != city:
        history[user_id]["cities"].append(city)
        save_json_file(HISTORY_DB, history)

    try:
        lat, lon = get_city_coordinates(city)
        if not lat or not lon:
            logger.warning(f"City not found: {city}")
            return jsonify({
                "error": "Город не найден",
                "details": f"Не удалось найти координаты для: {city}"
            }), 404

        logger.debug(f"Coordinates for {city}: {lat}, {lon}")

        weather_response = get_weather_data(lat, lon)
        if not weather_response:
            logger.error("Weather service unavailable")
            return jsonify({
                "error": "Сервис погоды недоступен",
                "details": "Попробуйте позже"
            }), 503

        try:
            weather_data = format_weather_data(weather_response, city)
            logger.info(f"Weather data retrieved for {city}")
            return jsonify(weather_data)
        except Exception as e:
            logger.error(f"Data formatting error: {str(e)}")
            return jsonify({
                "error": "Ошибка обработки данных",
                "details": "Попробуйте другой город"
            }), 500
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return jsonify({
            "error": "Город не найден",
            "details": "Попробуйте использовать подсказки для ввода города."
        }), 500


@weather_app.route("/api/city_stats", methods=["GET"])
def get_city_stats():
    stats = load_json_file(STATS_DB, {'We don`t have statistic.'})
    return jsonify(stats)
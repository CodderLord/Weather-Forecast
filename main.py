from APP import weather_app
from Config import IP, PORT



if __name__ == "__main__":
    weather_app.run(debug=False, host=IP, port=PORT)
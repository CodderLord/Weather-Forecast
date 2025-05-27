import os

from flask import Flask

weather_app = Flask(__name__,
                    template_folder=fr"{os.getcwd()}/APP/templates")

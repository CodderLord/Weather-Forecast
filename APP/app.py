import os

from flask import Flask

weather_app = Flask(__name__,
                    template_folder=f"{os.getcwd()}\\APP\\templates")

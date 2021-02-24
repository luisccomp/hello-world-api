import os

from flask import Flask
from app.api import welcome, random

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    app.register_blueprint(welcome.routes)
    app.register_blueprint(random.routes)

    return app
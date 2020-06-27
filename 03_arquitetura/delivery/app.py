from flask import Flask
from delivery.ext import site


def create_app():
    """factory principal"""
    app = Flask(__name__)
    site.init_app(app)
    return app

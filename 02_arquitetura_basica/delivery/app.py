"""
estrutura básica do flask
"""
import views
from flask import Flask


def create_app():
    """factory principal"""
    app = Flask(__name__)
    views.init_app(app)
    return app

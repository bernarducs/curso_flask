"""
estrutura básica do flask
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>hello, delivery</h1>'


@app.route('/sobre')
def sobre():
    return '<h1>este é melhor site de delivery</h1>'

from flask import Blueprint
from flask import request, render_template

'''
Blueprints são módulos/extensões ("peças") de códigos 
que você encaixa no app principal do projeto
'''

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    return render_template("index.html",
                           name=request.args['name']
                           )

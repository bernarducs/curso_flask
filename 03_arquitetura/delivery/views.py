"""estensão flask"""


def init_app(app):
    """inicializacao de extensões"""

    @app.route("/")
    def index():
        return "Hello"

    @app.route("/contato")
    def contato():
        return "Contatos"

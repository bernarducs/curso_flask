def init_app(app):
    @app.before_first_request
    def init_everything():
        print("HOOK! Isto roda sempre que iniciar a app!")
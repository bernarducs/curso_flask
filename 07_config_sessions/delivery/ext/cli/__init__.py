""" Criando comandos para o flask no terminal """
import click
from delivery.ext.db import db, models


def init_app(app):

    @app.cli.command()
    def create_db():
        db.create_all()

    @app.cli.command()
    def listar_pedidos():
        # TODO usar tabulate
        click.echo("listar pedidos")

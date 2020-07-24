""" Criando comandos para o flask no terminal """
import click
from delivery.ext.db import db
from delivery.ext.site import models  # noqa


def init_app(app):

    @app.cli.command()
    def create_db():
        db.create_all()

    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--passwd", "-p")
    @click.option("--admin", "-a", is_flag=True, default=False)
    def add_user(email, passwd, admin):
        user = models.User(
            email=email,
            passwd=passwd,
            admin=admin
        )
        db.session.add(user)
        db.session.commit()
        click.echo("Usuário criado com sucesso!")

    @app.cli.command()
    def listar_pedidos():
        # TODO usar tabulate
        click.echo("listar pedidos")

    @app.cli.command()
    def listar_usuarios():
        click.echo("listar usuários")

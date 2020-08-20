import click
from delivery.ext.auth.models import User
from delivery.ext.auth.controller import create_user


@click.option("--email", "-e")
@click.option("--passwd", "-p")
@click.option("--admin", "-a", is_flag=True, default=False)
def add_user(email, passwd, admin):
    create_user(email=email, password=passwd, admin=admin)
    click.echo("Usuário criado com sucesso!")


def list_users():
    users = User.query.all()
    for user in users:
        click.echo(user.email)
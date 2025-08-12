import click

# @click.command()
# @click.option("--name", prompt="Digite seu nome", help="Nome da pessoa a cumprimentar.")
# @click.option("--repeat", default=1, help="Quantas vezes repetir a saudação.")
# def hello(name, repeat):
#     """Exibe uma saudação personalizada."""
#     for _ in range(repeat):
#         click.echo(f"Olá, {name}!")

@click.command()
def hello():
    click.echo("Hello everyone!")

@click.group()
def cli():
    pass

@cli.command()
def dataBaseInfo():
    click.echo("Data base is ready!")

@cli.command()
def dataBaseWarning():
    click.echo("Data base isn't ready!")

cli.add_command(dataBaseInfo)
cli.add_command(dataBaseWarning)

@click.command()
@click.option("--contador", default=1, help="Número de saudações")
@click.argument("nome")
def ola(nome, contador):
    for i in range(contador):
        click.echo(f"Olá, {nome}")


if __name__ == "__main__":
    # cli()
    ola()

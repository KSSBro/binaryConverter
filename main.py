import click

@click.group()
def cli():
    """Made by KSSBro"""

@click.command()
def convert():
    print("Convert function.")

cli.add_command(convert)

if __name__ == "__main__":
    cli()
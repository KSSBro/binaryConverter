import click

@click.group()
def cli():
    """Made by KSSBro"""

@click.command()
@click.option('-from-type', prompt="From", help="The system you want to convert from")
@click.option('-to-type', prompt="To", help="The system you want to convert to")
@click.option('-value', prompt="Value", help="The value you want to convert")
@click.option('-create-file', default="false", help="true/false")
@click.option('--file-type', default="json", help="text/json")
def convert(from_type, to_type, value, create_file, file_type):
    print(from_type, to_type)
    print("Convert function.")

cli.add_command(convert)

if __name__ == "__main__":
    cli()
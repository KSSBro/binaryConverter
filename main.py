import click
import controller

@click.group()
def cli():
    """Made by KSSBro"""

@click.command()
@click.option('-from-type', prompt="From", help="decimal | binary | octal | hexadecimal | ascii")
@click.option('-to-type', prompt="To", help="decimal | binary | octal | hexadecimal | ascii")
@click.option('-value', prompt="Value", help="The value you want to convert")
@click.option('-create-file', default="false", help="true/false")
@click.option('--file-type', default="json", help="text/json")
def convert(from_type, to_type, value, create_file, file_type):
    print(from_type, to_type, int(value))
    data = controller.controller(from_type, to_type, value)

cli.add_command(convert)

if __name__ == "__main__":
    cli()
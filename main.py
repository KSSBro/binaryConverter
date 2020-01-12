import click
import backend

@click.group()
def cli():
    """Made by KSSBro"""

@click.command()
@click.option('-text', prompt="Text", help="The text you want to encode")
@click.option('-form', prompt="Format", help="decimal | binary | octal | hexadecimal | base64")
@click.option('-delimiter', default="space", help="space(default) | any delimiter you want to use")
def encode(form, text, delimiter):
    delim = backend.setDelimiter(delimiter)
    backend.encode(form, text, delim)

@click.command()
@click.option('-text', prompt="Text", help="The text you want to decode")
@click.option('-form', prompt="Format", help="decimal | binary | octal | hexadecimal | base64")
@click.option('-delimiter', default="space", help="space(default) | delimiter used in the encoded text")
def decode(form, text, delimiter):
    delim = backend.setDelimiter(delimiter)
    backend.decode(form, text, delim)

cli.add_command(encode)
cli.add_command(decode)

if __name__ == "__main__":
    cli()
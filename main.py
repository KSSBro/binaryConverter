import click
import backend

@click.group()
def cli():
    """Made by KSSBro"""

@click.command()
@click.option('-text', prompt="Text", help="The text you want to encode")
@click.option('-form', prompt="Format", help="decimal | binary | octal | hexadecimal | base64")
@click.option('-delimiter', default="space", help="space(default) | any delimiter you want to use")
@click.option('-create-file', default="false", help="true: Create a file with the encoded text | false(default): Will not create a file")
def encode(form, text, delimiter, create_file):
    delim = backend.setDelimiter(delimiter)
    result = backend.encode(form, text, delim) 
    if create_file == "false":
        click.echo(result)
    else:
        name = "encoded_"+form+".txt"
        backend.createFile(result, name)

@click.command()
@click.option('-text', prompt="Text", help="The text you want to decode")
@click.option('-form', prompt="Format", help="decimal | binary | octal | hexadecimal | base64")
@click.option('-delimiter', default="space", help="space(default) | delimiter used in the encoded text")
@click.option('-create-file', default="false", help="true: Create a file with the encoded text | false(default): Will not create a file")
def decode(form, text, delimiter, create_file):
    delim = backend.setDelimiter(delimiter)
    result = backend.decode(form, text, delim)
    if create_file == "false":
        click.echo(result)
    else:
        name = "decoded_"+form+".txt"
        backend.createFile(result, name)

cli.add_command(encode)
cli.add_command(decode)

if __name__ == "__main__":
    cli()
import click
import backend

@click.group()
def cli():
    """Made by KSSBro"""

@click.command()
@click.option('-file-path', default="", help="Path of text file")
@click.option('-text', default="", help="The text you want to encode")
@click.option('-form', prompt="Format", help="decimal | binary | octal | hexadecimal | base64")
@click.option('-delimiter', default="space", help="space(default) | Any delimiter you want to use")
@click.option('-create-file', default="false", help="true: Create a file with the encoded text | false(default): Will not create a file")
def encode(file_path, form, text, delimiter, create_file):
    delim = backend.setDelimiter(delimiter)
    if file_path != "":
        text = backend.readFile(file_path)
    result = backend.encode(form, text, delim) 
    if create_file == "false":
        click.echo(result)
    else:
        backend.createFile(result, "encoded_"+form+".txt") 

@click.command()
@click.option('-file-path', default="", help="Path of file with encoded text")
@click.option('-text', prompt="Text", help="The text you want to decode")
@click.option('-form', prompt="Format", help="decimal | binary | octal | hexadecimal | base64")
@click.option('-delimiter', default="space", help="space(default) | delimiter used in the encoded text")
@click.option('-create-file', default="false", help="true: Create a file with the decoded text | false(default): Will not create a file")
def decode(file_path, form, text, delimiter, create_file):
    delim = backend.setDelimiter(delimiter)
    if file_path != "":
        text = backend.readFile(file_path)
    result = backend.decode(form, text, delim)
    if create_file == "false":
        click.echo(result)
    else:
        backend.createFile(result, "decoded_"+form+".txt")

cli.add_command(encode)
cli.add_command(decode)

if __name__ == "__main__":
    cli()
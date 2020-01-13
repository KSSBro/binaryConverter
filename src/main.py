import click
import backend
import util

@click.group()
def cli():
    """Made by KSSBro | v1.0"""

@click.command()
@click.option('-file-path', default="", help="Path of text file")
@click.option('-text', default="", help="The text you want to encode")
@click.option('-form', prompt="Format", help="decimal | binary | octal | hexadecimal | base64")
@click.option('-delimiter', default="space", help="space(default) | Any delimiter you want to use")
@click.option('-create-file', default="false", help="true: Create a file with the encoded text | false(default): Will not create a file")
def encode(file_path, form, text, delimiter, create_file):
    delim = util.setDelimiter(delimiter)
    try:
        if file_path != "":
            text = util.readFile(file_path)
    except:
        return print("Couldn't read file: Invalid path or file name")
    try:
        result = backend.encode(form, text, delim) 
    except:
        return print("Some error occured while encoding!")
    try:
        if create_file == "false":
            click.echo(result)
        else:
            util.createFile(result, "encoded_"+form+".txt") 
    except:
        return print("Couldn't create file")

@click.command()
@click.option('-file-path', default="", help="Path of file with encoded text")
@click.option('-text', prompt="Text", help="The text you want to decode")
@click.option('-form', prompt="Format", help="decimal | binary | octal | hexadecimal | base64")
@click.option('-delimiter', default="space", help="space(default) | delimiter used in the encoded text")
@click.option('-create-file', default="false", help="true: Create a file with the decoded text | false(default): Will not create a file")
def decode(file_path, form, text, delimiter, create_file):
    delim = util.setDelimiter(delimiter)
    try:
        if file_path != "":
            text = util.readFile(file_path)
    except:
        return print("Couldn't read file: Invalid path or file name")
    try:
        result = backend.decode(form, text, delim)
    except:
        return print("Some error occured while decoding!")
    try:
        if create_file == "false":
            click.echo(result)
        else:
            util.createFile(result, "decoded_"+form+".txt")
    except:
        return print("Couldn't create file")

cli.add_command(encode)
cli.add_command(decode)

if __name__ == "__main__":
    cli()
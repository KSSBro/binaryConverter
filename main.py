import click
import controller

@click.group()
def cli():
    """Made by KSSBro"""

@click.command()
@click.option('-form', prompt="Format", help="decimal | binary | octal | hexadecimal | base64")
@click.option('-text', prompt="Text", help="The text you want to encode")
@click.option('-delimiter', default="space", help="space(default) | userd")
@click.option('--delim-ud', default=" ", help="The delimiter you want to use")
def encode(form, text, delimiter, delim_ud):
    if delimiter != "space":
        delim = delim_ud
    else:
        delim = " "

    controller.controller(form, text, delim, "encode")

@click.command()
@click.option('-form', prompt="Format", help="decimal | binary | octal | hexadecimal | base64")
@click.option('-text', prompt="Text", help="The encoded text you want to decode")
@click.option('-delimiter', default="space", help="space(default) | userd")
@click.option('--delim-ud', default=" ", help="The delimiter of the encoded text.")
def decode(form, text, delimiter, delim_ud):
    if delimiter != "space":
        delim = delim_ud
    else:
        delim = " "
    
    controller.controller(form, text, delim, "decode")


cli.add_command(encode)
cli.add_command(decode)

if __name__ == "__main__":
    cli()
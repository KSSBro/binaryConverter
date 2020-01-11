import click
import controller

@click.group()
def cli():
    """Made by KSSBro"""

@click.command()
@click.option('-type', promt="Type", help="encode | decode")
@click.option('-form', prompt="Format", help="decimal | binary | octal | hexadecimal | base64")
@click.option('-text', prompt="Text", help="The text you want to encode")
@click.option('-delimiter', default="space", help="space(default) | userd")
@click.option('--delim-ud', default=" ", help="The delimiter you want to use")
def codec(type_, form, text, delimiter, delim_ud):
    if delimiter != "space":
        delim = delim_ud
    else:
        delim = " "

    result = controller.controller(form, text, delim, type_)

@click.command()


cli.add_command(codec)

if __name__ == "__main__":
    cli()
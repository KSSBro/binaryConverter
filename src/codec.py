'''
    codec.py

    Author: Araekiel
    Copyright:  Copyright © 2020, Kumar Shashwat
    License: MIT
    Version: 1.0
'''

import six  
import packaging
import packaging.version
import packaging.specifiers
import packaging.requirements

import click
import backend
import util

@click.group()
def cli():
    """Made by Araekiel | v1.0"""

@click.command()
@click.option('-filepath', default="", help="Path of text file")
@click.option('-text', default="", help="The text you want to encode")
@click.option('-form', prompt="Format", help="decimal | binary | octal | hexadecimal | base64")
@click.option('-delimiter', default="space", help="space(default) | Any delimiter you want to use")
@click.option('--createfile', default="false", help="true: Create a file with the encoded text | false(default): Will not create a file")
def encode(filepath, form, text, delimiter, createfile):
    delim = util.setDelimiter(delimiter)
    try: 
        if filepath != "":
            text = util.readFile(filepath)
    except:
        return print("Couldn't read file: Invalid path or file name")
    try:
        result = backend.encode(form, text, delim) 
    except:
        return print("Some error occured while encoding!")
    try:
        if createfile == "false":
            click.echo(result)
        else:
            util.createFile(result, "encoded_"+form+".txt") 
    except:
        return print("Couldn't create file")

@click.command()
@click.option('-filepath', default="", help="Path of file with encoded text")
@click.option('-text', prompt="Text", help="The text you want to decode")
@click.option('-form', prompt="Format", help="decimal | binary | octal | hexadecimal | base64")
@click.option('-delimiter', default="space", help="space(default) | delimiter used in the encoded text")
@click.option('--createfile', default="false", help="true: Create a file with the decoded text | false(default): Will not create a file")
def decode(filepath, form, text, delimiter, createfile):
    delim = util.setDelimiter(delimiter)
    try:
        if filepath != "":
            text = util.readFile(filepath)
    except:
        return print("Couldn't read file: Invalid path or file name")
    try:
        result = backend.decode(form, text, delim)
    except:
        return print("Some error occured while decoding!")
    try:
        if createfile == "false":
            click.echo(result)
        else:
            util.createFile(result, "decoded_"+form+".txt")
    except:
        return print("Couldn't create file")

cli.add_command(encode)
cli.add_command(decode)

if __name__ == "__main__":
    cli()
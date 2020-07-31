<img alt="Codec" src="https://raw.githubusercontent.com/Araekiel/codec/gh-pages/public/images/logo.png" height="75">

# Codec
[Codec](https://arekiel.github.io/codec) is a CLI ASCII text encoder/decoder.

Formats currently supported: 
- Base64
- Binary 
- Octal
- Hexadecimal
- Decimal 

## Getting Started

### Prerequisites

To run the app from source - [Git](https://git-scm.com/) is needed to clone the repository on your machine. [Python](https://www.python.org/) and [Click](https://click.palletsprojects.com/en/7.x/) are required to run the app from the source.

### Installing

After installing **git**, clone the repository on your machine

```
git clone https://github.com/KSSBro/codec.git
```

After installing **Python**, install **Click** with **pip**

```
pip install click
```

### Usage

Running from the source:

```
python codec.py
```

To get help use **--help**:

```
codec --help
```

```
codec encode --help
```

#### Encoding ASCII text

Use the command **encode** to encode ASCII text.

Options:

- `-filepath`: path to the file with the text in it 
- `-text`: text to encode if it's not in a file
- `-form`: the format you want to encode the text in (decimal | binary | octal | hecadecimal | base64)
- `-delimiter`: the delimiter you want to use in the encoded text, space is default
- `--createfile`: true: will create a text file with the encoded text, false(defult): won't create a file

```
codec encode -text *ascii_text* -form *format* --createfile *true/false*
```

#### Decoding encoded text

Use the command **decode** to decode encoded text.

Options:

- `-filepath`: path to the file with the encoded text in it 
- `-text`: text to decode if it's not in a file
- `-form`: the format of the encoded text (decimal | binary | octal | hecadecimal | base64)
- `-delimiter`: the delimiter used in the encoded text, space is default
- `--createfile`: true: will create a text file with the decoded text, false(defult): won't create a file

```
codec decode -text *encoded_text* -form *format* --createfile *true/false*
```
    
## Release & Changelog

Latest Relase: v1.0

Changelog:
- Added command **encode**
- Added command **decode**

## Libraries

- [Click](https://click.palletsprojects.com/en/7.x/) was used to make the CLI
- [Pyinstaller](https://www.pyinstaller.org/) was used to build the executable
- A customized version of [termynal](https://github.com/ines/termynal) by [Ines Montani](https://github.com/ines) was used on the [gh-pages website](https://araekiel.github.io/instahunter) to display the output 
 
## Contributing

Fork the repository and open a pull request to contribute.
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors

- **Araekiel** - [Github](https://github.com/Araekiel)

## License

[MIT](https://choosealicense.com/licenses/mit/)

<img alt="Codec" src="https://raw.githubusercontent.com/KSSBro/codec/gh-pages/public/images/logo.png" height="75">

# Codec
A CLI ASCII text encoder/decoder.

## Getting Started

### Prerequisites

To run the app from source - [Git](https://git-scm.com/) is needed to clone the repository on your machine. [Python](https://www.python.org/) and [Click](https://click.palletsprojects.com/en/7.x/) are required to run the app from the source.

### Installing

After installing **git**, clone the repository on your machine

```
git clone https://github.com/KSSBro/instahunter.git
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

Create an executable using pyinstaller:

```
pip install pyinstaller

pyinstaller codec.py --onefile
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

## Release

v1.0 has been released.

## Built with

- [Python](https://www.python.org/)
- [Click](https://click.palletsprojects.com/en/7.x/)
- [Pyinstaller](https://www.pyinstaller.org/)(Executable)

## Authors

- **KSSBro** - [Github](https://github.com/KSSBro)

## License

[MIT](https://choosealicense.com/licenses/mit/)
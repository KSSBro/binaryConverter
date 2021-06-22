<img alt="Codec" src="https://raw.githubusercontent.com/Araekiel/codec/gh-pages/public/images/logo.png" height="75">

# Codec
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)]() [![GitHub Release](https://img.shields.io/badge/release-v1.0.1-blue)]() [![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com) 

[Codec](https://arekiel.github.io/codec) is a CLI app that can encode and decode ASCII test to and from various formats.

Formats currently supported: 
- Base64
- Binary 
- Octal
- Hexadecimal
- Decimal 

<br/>
<img alt="Screenshot" src="https://raw.githubusercontent.com/Araekiel/codec/gh-pages/public/images/screenshot.JPG">

## Getting Started

### Prerequisites

To run the app from source - [Git](https://git-scm.com/) is needed to clone the repository on your machine. [Python](https://www.python.org/) and [Click](https://click.palletsprojects.com/en/7.x/) are required to run the app from the source.

### Installing

After installing **git**, clone the repository on your machine

```bash
git clone https://github.com/Araekiel/codec.git
```

After installing **Python**, install **Click** with **pip**

```bash
pip install click
```

### Usage

Running from the source:

```bash
python codec.py
```

To get help use **--help**:

```bash
codec --help
```

```bash
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

```bash
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

```bash
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

[MIT License](https://github.com/Araekiel/codec/blob/master/LICENSE) | Copyright (c) 2020 Kumar Shashwat

import json
with open("morse.json", 'r') as morseFile:
    morseData = json.load(morseFile)
    
def toMorse(value):
    return morseData[value.lower()]

def fromMorse(element):
    for key, value in morseData.items():
        if value == element.lower():
            return key

def controller(form, text, delim, type_):
    convertedList = []
    if type_ == "encode":
        elementList = list(text)
    else:
        elementList = text.split(delim)

    for element in elementList:
        if type_ == "encode":
            converted = encode(form, element)
        else:
            converted = decode(form, element)
        
        convertedList.append(converted)
    
    print(delim.join(convertedList))

def encode(form, raw):
    if form == "decimal":
        return str(ord(raw))
    elif form == "binary":
        return to_bin(ord(raw))
    elif form == "octal":
        return oct(ord(raw))[2:]
    elif form == "hexadecimal":
        return hex(ord(raw))[2:]
    else:
        return "Wrong input"

def decode(form, raw):
    pass


def to_bin(value):
    bin_value = ""
    counter = 0
    while value > 0:
        bin_value = str(int(value % 2)) + bin_value
        value = int(value / 2)
        counter += 1

    for count in range(8-counter):
        bin_value = "0" + bin_value
    
    return bin_value

def to_oct(value):
    oct_value = ""

    while value > 0:
        oct_value = str(int(value % 8)) + oct_value
        value = int(value / 8)

    return oct_value
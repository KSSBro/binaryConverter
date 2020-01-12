error = {
    "exists": False,
    "msg": "None"
}

def set_delimiter(delimiter):
    if delimiter != "space":
        return delimiter
    else:
        return " " 

def encode(form, raw, delimiter):
    if form == "base64":
        print("Working on base64")
    else:
        encodedList = []
        elementList = list(raw)
        for element in elementList:
            if form == "decimal":
                encodedList.append(str(ord(element)))
            elif form == "binary":
                encodedList.append(to_bin(ord(element)))
            elif form == "octal":
                encodedList.append(oct(ord(element))[2:])
            elif form == "hexadecimal":
                encodedList.append(hex(ord(element))[2:])
            else:
                error = True
                return print("Error")
        
        print(delimiter.join(encodedList))
        
    

def decode(form, raw, delimiter):
    if form == "base64":
        print("Working on base64")
    else:
        decodedList = []
        elementList = raw.split(delimiter)
        for element in elementList:
            if form == "decimal":
                decodedList.append(chr(int(element)))
            elif form == "binary":
                decodedList.append(from_bin(element))
            elif form == "octal":
                decodedList.append(chr(int(element, 8)))
            elif form == "hexadecimal":
                decodedList.append(chr(int(element, 16)))
        print("".join(decodedList))

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

def from_bin(value):
    reverseList = list(value[len(value)::-1])
    bitd = 1
    num = 0
    for char in reverseList:
        bit = int(char)
        if(bit == 1):
            num += bitd
        bitd *= 2
    return chr(num)

def to_oct(value):
    oct_value = ""

    while value > 0:
        oct_value = str(int(value % 8)) + oct_value
        value = int(value / 8)

    return oct_value
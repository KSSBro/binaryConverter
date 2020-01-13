error = {
    "exists": False,
    "msg": "None"
}

def setDelimiter(delimiter):
    if delimiter != "space":
        return delimiter
    else:
        return " " 

def createFile(result, name):
    file = open(name, "w+")
    file.write(result)
    print("File created! \nName: " + name)

def encode(form, raw, delimiter):
    if form == "base64":
       return to_base64(raw)
    else:
        encodedList = []
        elementList = list(raw)
        for element in elementList:
            if form == "decimal":
                encodedList.append(str(ord(element)))
            elif form == "binary":
                encodedList.append(toBin(ord(element)))
            elif form == "octal":
                encodedList.append(oct(ord(element))[2:])
            elif form == "hexadecimal":
                encodedList.append(hex(ord(element))[2:])
            else:
                error["exists"] = True
                error["msg"] = "Format error"
                return print("Error")
        
        return delimiter.join(encodedList)
        
    

def decode(form, raw, delimiter):
    if form == "base64":
        return from_base64(raw)
    else:
        decodedList = []
        elementList = raw.split(delimiter)
        for element in elementList:
            if form == "decimal":
                decodedList.append(chr(int(element)))
            elif form == "binary":
                decodedList.append(fromBin(element))
            elif form == "octal":
                decodedList.append(chr(int(element, 8)))
            elif form == "hexadecimal":
                decodedList.append(chr(int(element, 16)))
            else:
                error["exists"] = True
                error["msg"] = "Format error"
                return print("Error")
        return "".join(decodedList)

def to_base64(value):
    base64String = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    encodedList = []
    elementList = []
    a = 0
    b = 3
    while b < (len(value)+3):
        elementList.append(value[a:b])
        a = b
        b += 3
    for element in elementList:
        charList = list(element)
        prevBits = ""
        curBitLength = 6
        if len(element) < 3:
            endString = ""
            i = len(element)
            while i < 3:
                endString += "="
                i += 1
        for char in charList:
            charNum = int(ord(char))
            charBin = toBin(charNum)
            sixBits = prevBits + charBin[0:curBitLength]
            prevBits = charBin[curBitLength:]
            curBitLength -= 2
            encodedList.append(base64String[ord(fromBin(sixBits))])
        if len(prevBits) < 6:
            i = len(prevBits)
            while i < 6:
                prevBits += "0"
                i += 1
            encodedList.append(base64String[ord(fromBin(prevBits))]+endString)
        else:
            encodedList.append(base64String[ord(fromBin(prevBits))])
    return "".join(encodedList)

def from_base64(value):
    base64String = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    elementList = []
    decodedList = []
    a = 0
    b = 4
    while b <= len(value):
        elementList.append(value[a:b])
        a = b
        b += 4
    for element in elementList:
        charList = list(element)
        binaryList = []
        for char in charList:
            binaryList.append(toBin(base64String.find(char)))
        binaryList[0] = binaryList[0][2:] + binaryList[1][2:4]
        binaryList[1] = binaryList[1][4:] + binaryList[2][2:6]
        if binaryList[2] != "00000000":
            binaryList[2] = binaryList[2][6:] + binaryList[3][2:8]
        else:
            binaryList[2] = ""
        binaryList[3] = ""
        for binaryEl in binaryList:
            if binaryEl != "" and binaryEl != "00000000":
                decodedList.append(fromBin(binaryEl))
    return "".join(decodedList)

def toBin(value):
    bin_value = ""
    counter = 0
    while value > 0:
        bin_value = str(int(value % 2)) + bin_value
        value = int(value / 2)
        counter += 1

    for count in range(8-counter):
        bin_value = "0" + bin_value
    
    return bin_value

def fromBin(value):
    reverseList = list(value[len(value)::-1])
    bitd = 1
    num = 0
    for char in reverseList:
        bit = int(char)
        if(bit == 1):
            num += bitd
        bitd *= 2
    return chr(num)

# def to_oct(value):
#     oct_value = ""

#     while value > 0:
#         oct_value = str(int(value % 8)) + oct_value
#         value = int(value / 8)

#     return oct_value
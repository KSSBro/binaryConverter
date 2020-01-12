error = {
    "exists": False,
    "msg": "None"
}

def setDelimiter(delimiter):
    if delimiter != "space":
        return delimiter
    else:
        return " " 

def encode(form, raw, delimiter):
    base64String = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    encodedList = []
    if form == "base64":
        elementList = []
        a = 0
        b = 3
        while b < (len(raw)+3):
            elementList.append(raw[a:b])
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
        print("".join(encodedList))
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
        
        print(delimiter.join(encodedList))
        
    

def decode(form, raw, delimiter):
    if form == "base64":
        print("Working on base64 decoding")
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
        print("".join(decodedList))

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
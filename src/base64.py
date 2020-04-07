import binary 

def toBase64(value):
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
            charBin = binary.toBin(charNum)
            sixBits = prevBits + charBin[0:curBitLength]
            prevBits = charBin[curBitLength:]
            curBitLength -= 2
            encodedList.append(base64String[ord(binary.fromBin(sixBits))])
        if len(prevBits) < 6:
            i = len(prevBits)
            while i < 6:
                prevBits += "0"
                i += 1
            encodedList.append(base64String[ord(binary.fromBin(prevBits))]+endString)
        else:
            encodedList.append(base64String[ord(binary.fromBin(prevBits))])
    return "".join(encodedList)

def fromBase64(value):
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
            if char != "=":
                binaryList.append(binary.toBin(base64String.find(char)))
            else:
                binaryList.append(char)
        f = 2
        l = 4
        for i in range(4):
            if i < 3:
                if binaryList[i+1] != "=":
                    binaryList[i] = binaryList[i][f:] + binaryList[i+1][2:l]
                else:
                    binaryList[i] = ""
            else:
                binaryList[i] = ""
            f += 2
            l += 2
        for binaryEl in binaryList:
            if binaryEl != "":
                decodedList.append(binary.fromBin(binaryEl))
    return "".join(decodedList)
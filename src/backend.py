import base64
import binary

def encode(form, raw, delimiter):
    if form == "base64":
       return base64.toBase64(raw)
    else:
        encodedList = []
        elementList = list(raw)
        for element in elementList:
            if form == "decimal":
                encodedList.append(str(ord(element)))
            elif form == "binary":
                encodedList.append(binary.toBin(ord(element)))
            elif form == "octal":
                encodedList.append(oct(ord(element))[2:])
            elif form == "hexadecimal":
                encodedList.append(hex(ord(element))[2:])
            else:
                return print("Invalid format input!")
        
        return delimiter.join(encodedList)
        
    

def decode(form, raw, delimiter):
    if form == "base64":
        return base64.fromBase64(raw)
    else:
        decodedList = []
        elementList = raw.split(delimiter)
        for element in elementList:
            if form == "decimal":
                decodedList.append(chr(int(element)))
            elif form == "binary":
                decodedList.append(binary.fromBin(element))
            elif form == "octal":
                decodedList.append(chr(int(element, 8)))
            elif form == "hexadecimal":
                decodedList.append(chr(int(element, 16)))
            else:
                return print("Invalid format input!")
                
        return "".join(decodedList)



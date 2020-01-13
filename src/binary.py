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

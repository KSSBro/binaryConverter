def setDelimiter(delimiter):
    if delimiter != "space":
        return delimiter
    else:
        return " " 

def createFile(result, name):
    file = open(name, "w+")
    file.write(result)
    print("File created! \nName: " + name)

def readFile(filepath):
    file = open(filepath, "r+")
    return file.read()

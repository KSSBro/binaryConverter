def controller(form, text, delim, type_):
    convertedList = []
    if type_ == "encode":
        elementList = list(text)
    else:
        elementList = text.split(delim)

    print(elementList)

    for element in elementList:
        if type_ == "encode":
            converted = encoder(form, element)
        else:
            converted = decoder(form, element)
        
        convertedList.append(converted)

def encoder(form, raw):
    pass

def decoder(form, raw):
    pass

def to_oct(value):
    oct_value = ""

    while value > 0:
        oct_value = str(int(value % 8)) + oct_value
        value = int(value / 8)

    return oct_value
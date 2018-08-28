def atb(input):
	#print('ASCII to binary')
	#arr = (128, 64, 32, 16, 8, 4, 2, 1)
	#print(input)
	#return(arr)
	retString = ""
	error = "error"
	try:
		for i in range(0, len(input)): 
			bits = 128
			c = ord(input[i])
			while (bits >= 1):
				if(c - bits > 0 or c - bits == 0):
					retString += "1"
					c = c - bits
				else:
					retString += "0"
				bits = bits / 2
		return (retString, "Conversion Complete.")
	except:
		return (error, error)

def htb(input):
	print('HexaDecimal to binary')

def dtb(input):
	print('Decimal to binary')

def otb(input):
	print('OctaDecimal to binary')
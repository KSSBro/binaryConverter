err = "Error."
cc = "Conversion Complete."

def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

def atb(input):
	#print('ASCII to binary')
	#arr = (128, 64, 32, 16, 8, 4, 2, 1)
	#print(input)
	#return(arr)
	retString = ""	
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
		return (retString, cc)
	except:
		return (err, err)

def dtb(input):
	#print('Decimal to binary')
	retString = ""
	try:
		num = int(input)
		while num > 0:                                 
			if num == 1: 								
				retString += "1"
				num = 0							
			elif num%2 == 1:							
				retString += "1"
				num = int((num-1)/2)
			elif num%2 == 0: 								
				retString += "0"
				num = int(num/2)
			#print(num)
		return (reverse(retString), cc)
	except: 
		return (err, err)

def otb(input):
	print('OctaDecimal to binary')

def htb(input):
	print('HexaDecimal to binary')



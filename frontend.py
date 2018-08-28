from tkinter import *
import backend as back

def calc():
	type = menuOpt.get()
	input = conFromT.get()
	if(type == 'ASCII -> Bin'):
		rt, status = back.atb(input)
		#message.delete(0, END)
		messageT.set(status)
		ans.set(rt)
	elif(type == 'Hex -> Bin'):
		back.htb(input)
	elif(type == 'Dec -> Bin'):
		back.dtb(input)
	elif(type == 'Oct -> Bin'):
		back.otb(input)
	else:
		messageT.set("Select and option.")

def file(): 
	#print("Generate text file")
	text = ans.get()
	if(text != ""):
		t_file = open('Binary.txt', 'w')
		t_file.write(text)


window = Tk()
window.wm_title("Binary Converter")
img = PhotoImage(file = 'logo.png')
window.tk.call('wm', 'iconphoto', window._w, img)
window.geometry("270x200")
window.resizable(0,0)

conOption = Label(window, text = "Select your conversion:-")
conOption.grid(row = 0, column = 0)

options = ('ASCII -> Bin', 'Hex -> Bin', 'Dec -> Bin', 'Oct -> Bin')

menuOpt = StringVar()
menuOpt.set('Select')
#menu.get

menu = OptionMenu(window, menuOpt, *options)
menu.grid(row = 0, column = 1)

conFromT = StringVar()
conFrom = Entry(window, textvariable = conFromT)
conFrom.grid(row = 1, column = 0, pady = 10, padx = 5)

messageT = StringVar()
message = Entry(window, textvariable = messageT)
message.insert(0, 'Press Go! to convert')
message.config(state = 'readonly')
message.grid(row = 1, column = 1, pady = 10, padx = 5)

goBut = Button(window, text = "Go!", command = calc)
goBut.grid(row = 2 , column = 0, columnspan = 2)
 
ans = StringVar()
answer = Entry(window, textvariable =  ans)
answer.config(state = 'readonly')
answer.grid(row = 3, columnspan = 2, pady = 10)

printButton = Button(window, text = "Generate text file", command = file)
printButton.grid(row = 4, column = 0, columnspan = 2)

copy = Label(window, text = "Copyright © KSSBro 2018 | v0.1")
copy.grid(row = 5, column = 0, columnspan = 2, pady = 15)

window.mainloop()
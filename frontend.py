from tkinter import *
import functions as back


def calc():
	type = menuOpt.get()
	if(type == 'ASCII -> Bin'):
		back.atb()
	elif(type == 'Hex -> Bin'):
		back.htb()
	elif(type == 'Dec -> Bin'):
		back.dtb()
	elif(type == 'Oct -> Bin'):
		back.otb()
	else:
		print('Select an option')


window = Tk()
window.wm_title("Convertor")
img = PhotoImage(file = 'logo.png')
window.tk.call('wm', 'iconphoto', window._w, img)
window.geometry("270x150")
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

conToT = StringVar()
conTo = Entry(window, textvariable = conToT)
conTo.grid(row = 1, column = 1, pady = 10, padx = 5)

goBut = Button(window, text = "Go!", command = calc)
goBut.grid(row = 2 , column = 0, columnspan = 2)
 
ans = StringVar
answer = Entry(window, textvariable =  ans)
answer.config(state = 'readonly')
answer.grid(row = 3, columnspan = 2, pady = 10)

window.mainloop()
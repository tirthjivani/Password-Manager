from tkinter import *
import random
import string
import tkinter.messagebox

def one_character():

	lower_case = "abcdefghijklmnopqrstuvwxyz"
	upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	special_characters = "[];,./*-+!~@#$%^&*()_=-"

	return random.choice(string.digits + string.ascii_letters + lower_case + upper_case + special_characters)

def get_password():
	n = int(text2.get())
	name = text1.get()
	password = []
	for i in range(n):
		password.append(one_character())
	tkinter.messagebox._show("Generated Info", 'Password : ' + ''.join(password))
	#print("Your password is : " + ''.join(password))
	file = open("File.txt", 'a')
	file.readable()
	file.write("\n***************************\nAccount  : " + name)
	file.write("\nPassword : " + hash(''.join(password)))
	return ''.join(password)

def hash(string):
	q = ''
	p = 'gnflvo;mfnjk'
	r = 'xDtiEg3q!'
	q += p
	for i in string:
		q = q + str(i) + 'a'	
	q += r
	return q

root = Tk()

panel1 = Frame(root)
panel2 = Frame(root)

# *** Panel1 ***
text1 = StringVar()
text2 = StringVar()

text_name = Entry(panel1, textvariable=text1)
text_num = Entry(panel1, textvariable=text2)
label1 = Label(panel1, text="Enter account name ")
label2 = Label(panel1, text="Enter no. of digits of password ")

label1.grid(row=0, column=0)
text_name.grid(row=0, column=1)
label2.grid(row=1, column=0)
text_num.grid(row=1, column=1)


# *** Panel2 ***
okbutton = Button(panel2, text="Generate", command=get_password)
exitbutton = Button(panel2, text="Exit", command=root.quit)
okbutton.pack(side=LEFT)
exitbutton.pack(side=RIGHT)

panel1.pack()
panel2.pack(side=BOTTOM)

root.mainloop()

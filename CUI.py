import random
import string

def one_character():

	lower_case = "abcdefghijklmnopqrstuvwxyz"
	upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	special_characters = "[];,./*-+!~@#$%^&*()_=-"

	return random.choice(string.digits + string.ascii_letters + lower_case + upper_case + special_characters)

name = input("For what account this password is for?\nAnswer : ")
test = int(input("How many char password?\nAnswer : "))
password = []

for i in range(test):
	password.append(one_character())
print("Your password is : " + ''.join(password))

file = open("File.txt", 'a')
file.readable()
file.write("\n***************************\nAccount  : " + name)
file.write("\nPassword : " + ''.join(password))

print("\n\nThank you!\n")
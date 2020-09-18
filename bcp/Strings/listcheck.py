#Strings & Lists 3

#Write a function that checks whether an element occurs in a list.

set_list = [1, 2, 3, 4, 5, 6, 7 , 8, 9, 10]
user_input = int(input("Please enter a number to check within list: "))

def check_list():
	user_input
	try:
		print("Input is at position " + str(set_list.index(user_input)))
	except ValueError:
		print("Entered number not in list.")
		

check_list()


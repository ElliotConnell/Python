#basic coding problem number 5

#write a program that asks the user for a number n and prints the sum of the numbers 1 to n
#if the number is a multiple of three or five, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

#ask user for a number n
x = input("Please enter a number: ")

x = int(x)

#check if x is a multiple of 3 & 5
#if yes, create list of numbers for 1 to n
#work out sum of lists
#print result

if x % 3 == 0:
	a = (list(range(0, (x + 1))))
	result = (sum(a))
	print(result)
elif x % 5 == 0:
	a = (list(range(0, (x + 1))))
	result = (sum(a))
	print(result)
else:
	print("invalid entry")

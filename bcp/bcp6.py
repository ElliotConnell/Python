#basic coding problem number 6

#Write a program that asks the user for a number n and gives them the possibility to 
#choose between computing the sum and computing the product of 1,…,n.

#outline the guide

print("options:")
print("Enter 'sum' to calculate the sum of numbers 1, .., n")
print("Enter 'product' to calculate the product of numbers 1, .., n")

#ask user for a number n
x = input("Please enter a number: ")

x = int(x)

#ask the user if they want to calculate sum or product

user_input = input("Enter sum or product: ")

#if the user selects sum
if user_input == "sum":
#create list of 1 to n
	a = (list(range(0, (x + 1))))
	# calculate sum of 1 to n
	result = (sum(a))
	print(result)
#if the user select product
elif user_input == "product":
#create list of 1 to n
	a = (list(range(1, (x + 1))))
	#import math library
	import math
	#calculate product of 1 to n
	result = (math.prod(a))
	print(result)
#create output if invalid entry is entered
else:
	print("invalid entry")



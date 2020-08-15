#basic coding problem number 7

#Write a program that prints a multiplication table for numbers up to 12.

print("Multiplication Tables")

#ask the user which multiplication table they wish to display
#define user input as integer

num = int(input("Please enter the multiplication table you wish to diplay: "))

#create for loop for range 1 to 12


for i in range (1, 13):
	print(num, 'x', i, '=', num*i)
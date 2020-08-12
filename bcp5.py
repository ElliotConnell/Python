#basic coding problem number 5

#write a program that asks the user for a number n and prints the sum of the numbers 1 to n if the number is a multiple of three or five, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

#ask user for a number n
x = input("Please enter a number")

x = int(x)

#create list 1 to n 

#numbers = list(range(x + 1))
#print(numbers)

#check list for multiples of 3

a = list(range(0, (x + 1), 3))
#print(a)

#check list for multiples of 5

b = list(range(0, (x + 1), 5))
#print(b)

#combine lists

combined = a + b
#print(combined)

#sort list into order
#c = sorted(combined)
#print(c)

#remove duplicates

d = list(dict.fromkeys(combined))
d = sorted(d)
print(d)

#work out sum of combined lists

result = (sum(d))

#print result

print(result)
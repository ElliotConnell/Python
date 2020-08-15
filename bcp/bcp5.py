#basic coding problem number 5

#write a program that asks the user for a number n and prints the sum of the numbers 1 to n if the number is a multiple of three or five, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

#ask user for a number n
x = input("Please enter a number")

x = int(x)

#create list of multiples of 3 from 1 to n

a = list(range(0, (x + 1), 3))

#create list of multiples of 5 from 1 to n

b = list(range(0, (x + 1), 5))

#combine lists

combined = a + b

#remove duplicates

d = list(dict.fromkeys(combined))
d = sorted(d)
print(d)

#work out sum of combined lists

result = (sum(d))

#print result

print(result)
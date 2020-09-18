#Write a guessing game where the user has to guess a secret number. 
#After every guess the program tells the user whether their number was too large or too small. 
#At the end the number of tries needed should be printed. 
#It counts only as one try if they input the same number multiple times consecutively.


#generate and store random number

import random

number = random.randint(0,100)

query = int(input("Please select a number between 0 and 100: "))
count = 0

while query != number:
	if query <= number:
		print("Higher")
		query2 = int(input("Please select another number: "))
		if query2 != query:
			count += 1
			query = query2

	elif query >+ number:
		print("Lower")
		query2 = int(input("Please select another number: "))
		if query2 != query:
			count += 1
			query = query2

else:
	print("Correct!")
	count += 1


print("Nice Work! You took " + str(count) + " guesses")

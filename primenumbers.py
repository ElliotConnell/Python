#Write a program that prints all prime numbers. (Note: if your programming language does not support arbitrary size numbers, 
#printing all primes up to the largest number you can easily represent is fine too.)


#for statement runs for every number between the range 2 to 100

for num in range(2,101):
	if all(num%i!=0 for i in range(2, num)):
	#all() returns true if every iterable in the statement returns true
		#for every num devides by i with no remainder for range number 2 through the num
		print(num)
		#prints everything that returns true


for num in range(2,101):
#for statement runs through every number in range 2 through 101
    prime = True
    # sets the variable as true
    for i in range(2,num):
    #test for every number in range 2 through to num
        if (num%i==0):
        # divide num by i and works out if there is any remainder
            prime = False
            #sets the false number
    if prime:
    	#if the number turns out to be true it prints the number
       print (num)
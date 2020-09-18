# control flows

#besides a while statement just introduced, python uses control statements known from other languages

#if statements
x = int(input("Please enter an integer: "))

if x < 0:
	x = 0
	print('Nagative changed to zero')
elif x == 0:
	print('Zero')
elif x == 1:
	print('Single')
else:
	print('More')

# there can be zero or more elif parts, and the else part is optional. the word elif is short for 'else if',
# and is useful to avoid excessive indentation. An if ... elif ... elif ... sequence is a substitute for the switch
# or case statements found in other languages


# for statements

#the for statement iterates over the items of any sequence (a list or a string), in the order that they appear in a sequence

# measure some strings
words = ['cat', 'window', 'defenestrate']
for w in words:
	print(w, len(w))

#code that modifies a collection while iterating over that same collection can be tricky to get right
#instead, it is usually more straight forward to loop over a copy of the collection or to create a new collection

#strategy: iterate over a copy
for user, status in users.copy(). items():
	if status == 'inactive':
		del users[user]

#strategy: create a new collection
active_users = {}
for user, status in users.items():
	if status == 'active':
		active_users[user] = status

# the range() function

#if you need to iterate over a sequence of numbers, the built in function range() comes in handy. it generates arithmatic progressions

for i in range(5):
	print(i)

#the given end point is never part of the generated sequence; range(10) gerates 10 values, the legal indices for items of a sequence of length 10
#it is possible to let the range start at another number, or to specify a different increment (even negative; sometimes this is calle a step)

print(range(5, 10))
print(range(0, 10, 3))
print(range(-10, -100, -70))

#to iterate over the indices of a sequence, you can combine range() and len() as follows
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
	print(i, a[i])

#in most such cases, however, it is convenient to use the enumerate() function, see looping techniques

#a strange thing happens if you try to print a range

print(range(10))

# alist is an object which returns the successive items of the desired sequence when you iterate over it
# but it doesn't really make a list, thus saving space
# we say such an item iterable, that is, suitable as a target for functions and constructs that expect something
# from which they can obtain successive items until the supply is exhausted
# we have seen that the for statement is such a construct, while an example of a function that takes an iterable
# is sum()

print(sum(range(4)))


# break and continue statements, and else clauses on loops

#the break statement breaks out the innermost enclosing for or while loop
#loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the iterable
# (with for) or when the condition becomes false (with while), but not when the loop is terminated by a 
# break statement. this is exemplified by the following loop, which searches for primenumbers

for n in range (2, 10):
	for x in range (2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', n//x)
			break
		else:
			#loop fell through without finding a factor
			print(n, 'is a prime number')

# the else clause belongs to the for loop, not the if statement

# when used in a loop, the else clause has more in common with the else clause of a try statement that it
#does with that of an if statement
# a try statements else clause runs when no exception occurs and a loops else clause runs when no break occurs

# the continue statement continues withthe next iteration of a loop

for num in range (2, 10):
	if num % 2 == 0:
		print('found an even number', num)
		continue
	print('found a number', num)

# pass statements

# the pass statment does nothing. it can be used when a statement is required synactically but the program
# reuquires no action

while True:
	pass # busy-wait for keyboard interupt (Ctrl+C)

# this is commonly used for creating minimal classes

class MyEmptyClass:
	pass

# another place pass can be used is as a placeholder for a function or conditional body when you
# are working on new code, allowing you to keep thinking at a more abstract level. the pass is silently ignored

def initlog(*args):
	pass #remember to implement this

#defining functions

#create a function that writes a fibnacci series to an arbitrary boundary

def fib(n): # write a fibonacci series up to n
	"""Print an Fibonacci series up to n."""
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
		print()

#now call the function we just defined:
fib(2000)

# the keyword def intrduces a function definition. It must be followed by a function name and the parentheses
# list of formal parameters. the statements that form the body of the function start at the next line, must be indented

# the first statement of the function body can optionally be a string literal;
# this string literal is the funtions docstring

# the execution of a function introduces a new symbol table used for the local variables of the function
# all variable assignments ina function store the value in the local symbol table

# the actual parameters (arguments) to a function call are introduced in the local symbol table of the called
# function when it is called
# thus arguments are passedusing call by value (where the value is always an object reference, not value of the object)
# when a functioncalls another function, a new symbol table is created for that call

# a function definition associates the function name withthe function object in the current symbol table.
# the interpreter recognizes the object pointed to by that name as a user defined function
# other names can also point to that same function object and can also be used to access the function

fib
<function fib at 10042ed0>
f = fib
f(100)

# writing the value None is normally suppressed y the interpreter if it would be the oonly value written

>>> fib(0)
>>> print(fib(0))

#it is simple to write a function that returns a list of the number of the fibonacci series, instead of printing it

def fib2(n): #return Fibonacci series up to n
	"""Return a list containing the Fibonacci series up to n."""
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a) #see below
		a, b = b, a+b
		return result

f100 = fib2(100) 	#call it
f100				#write the result

# the return statement returns with a value from a function. return without an expression returns None.
# falling off the end of a function also returns None
# the statement result.append(a) calls a method of the list object result





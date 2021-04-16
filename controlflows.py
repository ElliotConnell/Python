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
# a mehtod of function that 'belongs' to an object and is named obj.methodname, where obj is some object (this may be an 
#expression), and methodname is the name of a method that is defined by the objects type. Different types define different
#methods. Methods od different types may have the same name withut causing ambiguity. (it is possible to define 
# your own method types and methods, using classes, see classes)
#the method append() shown in the equivelent to result = result + [a], but more efficient

#more on defining functions

#default argument values

def ask_ok(prompt, retries=4, reminder='Please try again!'):
	while True:
		ok = True:
		ok = input(prompt)
		if ok in ('y', 'ye', 'yes'):
			return True
		if ok in ('n', 'no', 'nop', 'nope'):
			return False
		retries = retries - 1
		if retries < 0:
			raise ValueError('invalid user response')
		print(reminder)

#this example intrsduces th in keyword. this test whether or not a sequence contains a certain value

#the default values are evacuated at the point of function definition in the defining scope, so that

i = 5

def f(arg=i):
	print(arg)

i = 6
f()

#will print 5

#the following function accumulates the arguments passed to it on subsequent calls. 

def f(a, L=[]):
	L.append(a)
	return L

print(f(1))
print(f(2))
print(f(3))

#this will print: 
[1]
[1, 2]
[1, 2, 3]

#if you don't want the default to be shared between subsequent calls, you can write the function like this instead

def f(a, L=None): 
	if L is None:
		L = []
	L.append(a)
	return L


#keyword arguments

#functions can also be called using keyword arguments of the form kwarg=value. for instance the following function:

def parrot(voltage, state='a stiff', action='voom', type='norwegian blue'):
	print("-- This parrot wouldn't", action, end=' ')
	print("if you put", voltage, "volts through it.")
	print("-- Lovely plumage, the ", type)
	print("-- It's", state, "!")

#accepts one required argument(voltage) and three optional arguments (state, action, and type). this function can be called 
#in any of the following ways

parrot(1000)										# 1 positional argument
parrot(voltage=1000)								# 1 keyword arguement
parrot(voltage=1000000, action='VOOOOOM')			# 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)			# 2 keyword arguements
parrot('a million', 'bereft of lie', 'jump')		# 3 positional arguments
parrot('a thousand', state='pushing up daisies')	# 1 positional, 1 keyword

#but all the following calls would be invalid:

parrot()											# required argument missing
parrot(voltage=5.0, 'dead')							# non keyword argument are a keyword argument
parrot(110, voltage=220)							# duplicate value for the same argument
parrot(actor = 'John Cleese')						# unknown keyword argument

# in a function call, keyword arguments must follow positional arguments. all the keyword arguments passed
# match one of the arguments accepted by the function (eg. actor is not a valid argument for the parrot
# function), and their order is not import. this also includes non-optional arguments (eg. 
# parrot(voltage=1000) is vaild too). no argument may receive a value more than once. here's an example
# that fails due to this function

def function(a):
	pass

function(0, a=0)

Traceback (most recent call call last):
	File"<stdin>" line 1, in <module>
TypeError: function() got multiple values for keyword argument 'a'

# when a final formal parameter of the form **name is present, it receives a dictionary (see mapping types - dict)
#containing all keyword arguments except for those corresponding to a formal parameter. this may be combined
# with a formal parameter of the form *name (described in the next subsection) which receives a tuple containing 
# the positional arguments beyod the formal parameter list (*name must occur before the name.) For example, if 
# define a function like this:

def cheeseshop(kind, *arguments, **keywords):
	print("-- Do you have any", kind, "?")
	for arg in arguments:
		print(arg)
	print("-" * 40)
	for kw in keywords:
		print(kw, ":", keywords[])

#it would be called like this

cheeseshop("Limburger", "It's very runny, sir", "It's really very, VERY runny, sir.", 
	shopkeeper="Michael Palin", 
	client="John Cleese",
	sketch="Cheese Shop Sketch")

# and of course it would print

#-- Do you have any Limburger ?
#-- I'm sorry, we're all out of Linburger
#It's very runny, sir.
#It's really very VERY runny sir.

#------------------
#shopkeeper : Michael Palin
#client : John Cleese
#sketch : Cheese Shop Sketch

# note the order in which keywords arguments are printed is guaranteed to match the order in which they
#were provided


# special parameters
#positional-or-keyword arguements 
# if / and * are not present in the function definition, arguments may be passed to a position or by keyword

#position-only parameters
#it is possible to mark certain parameters as positional only. 
#if positional only, the parmeters' order matters, and the paramter cannot be passed by keyword. 
#positional-only  paraters are placed before a / (forward slash). the /  is used to logically seperate the postional only
# from the rest of the parameters. if ter is no / in the function  definition, there are no positional parameters
#paramters following the/ may be positional-or-keyword or keyword-only

#keyword only arguments
# to mark paramters as keyword-only, indicating the paramters must eb passed by keyword argument, place an 
#* in the arguments list just before the firs keyword-only paramter

#function examples
#consider the following example funtion definitions paying cloase attention to the markers / and *

def standard_arg(arg):
	print(arg)

def pos_only_arg(arg, /):
	print(arg)

def kwd_only_arg(*, arg):
	print(arg)

def combined_example(pos_only, / , standard, *. kwd_only):
	print(pos_only, standard, kwd_only)

# the first function definition, standard_arg, the most familiar form, places no restrictions on the calling 
# convention and arguments may be passed by position or keyboard:

>>> standard_arg(2)
2

>>> standard_arg(arg=2)
2

#the second function pos_only_arg is restricted to only use positional parameters as there is a / in the function
# definition

>>> pos_only_arg(1)
1

>>> pos_only_arg(arg=1)
Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
TypeError: pos_only_arg() got an unexpected keyword argument 'arg'

# the third function kwd_only_args only allows keyword arguments as indicated by a * in the function definition

>>> kwd_only_arg(3)
Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
TypeError: combined_example() takes 2 positional arguments but 3 were given

>>> kwd_only_arg(arg=3)
1 2 3

# and the last uses all three calling conventions in the same function definition

>>> combined_example(1, 2, kwd_only=3)
Traceback (most recent call last): 
	File "<stdin>", line 1, in <module>:
TypeError: combined_example() takes 2 postional arguments but 3 were given

>>> combined_example(1,2, kwd_only=3)
1 2 3

>>> combined_example(1, standard=2, kwd_only=3)
1 2 3

>>> combined_example(pos_only=1, standard=2, kwd_only=3)
Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
TypeError: combined_example() got an unexpected keyword argument 'pos_only'

#finally consider this function definition which has a potential collision  between the positional argument name and **kwds which has name as a key;

def foo(name, **kwds):
	return 'name' in kwds

#there is no possibe call that will make it return True as the keyword 'name' will always bind to the first parameter

>>>foo(1, **{'name': 2})
Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
TypeError: foo() got multiple values for argument 'name'
>>>

#but using / (positional only arguments), it is possible since it allows name as a positional argument and 'name'
# as a keyword arguments:

def foo(name, /, **kwds)
>>> foo(1, **{'name': 2})
True

#in other words, the names of positional-only parameters can be used in **kwds without ambiguity

# recap

#the use case will determine which parameters to use in the function definition:

def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):

#as guidance:
	# -use positional-only if want the name of the paramters to not be available to the user. this is useful
	#	when parameter names have no real meaning, if you want to enforce the order of the arguments when the 
	#	function is called of if you need to take some positional paramters and arbitrary keywords
	# -use keyword-only when names have meaning and the function definitionis more understandable by being 
	#	exlpicit with names or you want to prevent users relying on the position of the argument being passed
	# - for an API, use positional-only to prevent breaking API changes if the parameters name is modified in the future


# arbitrary argument lists

# the lease frequently used option is to specify that a function can be called with an arbitrary number of arguments
# these arguments will be wrapped up in a tuple (see tuples and sequences). before the variable number of arguments
# zero or more normal arguments may occur

def write_multiple_items(file, seperatorm *args):
	file.write(seperator.join(args))

#normally these variadic argument s will be last in the list of formal parameters , because they scoop up all
# remaining input arguments that are passed to a function. any formal paramters which occur after the *args
# parameter are keyword-only arguements, meaning  that they can only be used as keywords rather than positional arguments

def concat(*args, sep="/"):
	return sep.join(args)

concat("earth", "mars", "venus")
'earth/mars/venus'

concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'

#unpacking argument lists

#the reverse situation occurs when when the arguments are already in a list or a tuple but need to be unpacked for a 
#function call requiring serperate positional arguments. for instance, the built-in range() function expects seperate
# start and stop arguments. if they are not available seperately, write the function call with the *-operator to
#unpack the arguments out of a list or tuple

>>> list(range(3, 6))		#normal call with seperate arguments
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))		# call with arguments unpackaed from a list
[3, 4, 5]

# in the same fashion, dictionaries can deliver keyword arguments with the **-operator:

def parrot(voltage, state=' a stiff', action='voom'):
	print("-- This parrot wouldn't", action, end=' ')
	print("if you put", voltage, "volts through it.", end=' ')
	print("E's", state, "!")

d = {"voltage": "four millon", "state": " bleedin' demised", "action": "VOOM"}
parrot(**d)
# This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !

# Lambda Expressions

# small anonymous function can be created with lambda keyword. this function returns the sum of its two
# arguments: lambda a, b: a+b. lambda functions can be used wherever function objects are required. they 
# are syntactically restricted to a single function. semantically, thay are just syntactic sugar for a normal 
# function definition. like nested function definitions, lambda functions can reference variables from the containing scope

def make_incrementor(n):
	return lambda x: x + n

f = make_incrementor(42)
f(0)
42
f(1)
43

# the above example uses a lambda expression to return a function. another use is to pass a small function as an argument

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs

[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]


# documentation strings

# some conventions about the content and formatting of documentation strings.

#the first line should always be a short, concise summary of the object's purpose. for brevity, it should not
# explicitly state the objects name or type, since these are available by other means.

# if there are more lines in the document string, the second line should be blank, visually seperating the summary
# from the rest of the documentation

def my_function():
	"""Do nothing, but document it.

	No, really, it doesn't do anything.
	"""
	pass

print(my_function.__doc__)
#Do nothing, but document it.

	#No, really, it doesn't do anything. 


# function annotations

# function annotations are completely optional metadata information about the types used by user-defined functions
# functions(see PEP3107 and PEP484 for more information)

# annotations are stored in the __annotations__ attribute of the function as a dictionary and have no effect on any 
# other part of the function. 
# paramter annotations are defined by a colon after the parameter name, followed by an expression evaluating to the
# value of the annotation. return annotationsare defined by a lteral ->, followed by an expression, between the parameter
# list and the colon denoting the end of the def statement. the following example has a positional argument, a 
# keyword argument, and the return value annotated

def f(ham: str, eggs: str = 'eggs') -> str:
	print ("Annotations:", f.__anotations__)
	print("Arguments:", ham, eggs)
	return ham + ' and ' + eggs

f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'


# intermezzo :coding style

# from PEP8 coding style:
#	- use 4 space indentation, and no tabs
# 		4 spaces are a good compromise between small indentation (allows for greater nesting depth) and large 
#		indentation (easier to read). tabs introduce confusion, and are best left out
#	- wrap lines so they don't exceed 79 characters
#		this helps users with small displays and makes it possible to have several code files side-by-side on 
#		larger displays
#	- use blank lines to seperate functions and classes, and larger blocks of code inside functions
#	- when possible, put comments on a line of their own
# 	- use docstrings
# 	- use spaces around operators and after commas, but not directly inside bracketing constructs: a = f(1, 2) + g (3, 4).
#	- name your classes and functions consistently; the convention is to UpperCamelCase for classes and
#		lowercase_with_underscores for functions and methods. always use self as the name for the first method argument
#		(see a first look at classes for more on classes and methods).
#	- don't use fancy encodings if your code is meant to be used in international environment. Python's default, 
#		UTF-8, or even plain ascii work best in any case
# 	- likewise, don't use non-ascii characters in identifiers if there is only the slightest chance people speaking 
#		a different language will read or maintain the code

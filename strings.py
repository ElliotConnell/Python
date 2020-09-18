#strings

print('spam eggs') #single quotes

print('doesn\'t') #use \' to escape the single quote

print("doesn't") #use double quotes instead

print('"yes," they said')

print("\"yes,\" they said")

print('"isn\'t" they said')


s = 'First line. \nSecond line.'
print(s)


print('C:\some\name') # here \n means new line
print(r'C:\some\name') #note the r before the quote


print("""\
Usage: thingy [OPTIONS]
	-h 				Display this usage message
	-H hostname		Hostname to connect to
""")

# 3 times 'un', follewed by 'ium'
print(3 * 'un' + 'ium')

print('py''thon')

text =('Put several strings within parentheses '
	'to have them joined together')
print(text)

#concatenate variables or a variable and a literal, use +
prefix = 'py'
print(prefix + 'thon')

#strings can also be indexed
word = 'Python'
print(word[0]) # character in position 0
print(word[5]) # character in position 5
#indices can also be negative numbers, to start counting from the right
print(word[-1]) # last character
print(word[-2]) # second last chacter
print(word[-6])

#slicing allows to obtain substring
print(word[0:2]) #characters from position 0 (included) to 2 (excluded)
print(word[2:5]) #characters from position 2 (included) to 5 (excluded)

#note that the start is always included and the end is always excluded. this makes sure that 
#s[:i] +s[i:] is always equal to s
print(word[:2] + word[2:])
print(word[:4] + word[4:])

#slice indices have useful defaults; an omitted first index defaults to zero, 
#an omitted second index defaults to the size of the string being sliced
print(word[:2]) #character fom the begining to position 2 (excluded)
print(word[4:]) #characters from position 4 (included) to the end
print(word[-2:]) #characters from the second-last (included) to the end
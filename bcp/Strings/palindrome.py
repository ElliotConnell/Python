#Strings & Lists 6

#Write a function that tests whether a string is a palindrome.

set_string = 'elle'


def palindrome():
	if set_string == set_string[::-1]:
		print('String is a palindrome')
	else:
		print('String is not a palindrome')

palindrome()
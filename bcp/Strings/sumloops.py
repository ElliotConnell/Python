#Strings & Lists 7

#Write three functions that compute the sum of the numbers in a list: using a for-loop, a while-loop and 
#recursion. (Subject to availability of these constructs in your language of choice.)


set_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def sum_for_loop():
	for x in set_list:
		print(sum(set_list[:x]))

sum_for_loop()

def sum_while_loop():
	x = 0
	y = set_list[-1]
	while x <= int(y):
		print(sum(set_list[:x]))
		x = x + 1

sum_while_loop()



def sum_recursion():
	z = set_list[-1]
	while z <= set_list[-1]:
		print(sum(set_list[:z]))
		z += 1

sum_recursion()


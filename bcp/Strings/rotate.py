#Strings & Lists 12

#Write a function that rotates a list by k elements. For example [1,2,3,4,5,6] rotated by two becomes [3,4,5,6,1,2]. 
#Try solving this without creating a copy of the list. How many swap or move operations do you need?

set_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
k = int(input("Please enter a number to rotate the list: "))

import collections

def rotate_list():
	d = collections.deque(set_list)
	d.rotate(k)
	print(d)


rotate_list()
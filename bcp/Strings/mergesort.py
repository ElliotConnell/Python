#Strings & Lists 11

#Write a function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6]. 
#You can do this quicker than concatenating them followed by a sort.

list_a = [1, 4, 2]
list_b = [5, 3, 6]

def merge_sort_a():
	result = list_a + list_b
	print(sorted(result))

merge_sort_a()


def merge_sort_b():
	print(sorted(list_a + list_b))

merge_sort_b()

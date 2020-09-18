#Strings & Lists 10

#Write a function that combines two lists by alternatingly taking elements, 
#e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].



def concatenate_alternate():
	list_a = [1, 2, 3, 4, 5]
	list_b = ['a', 'b', 'c', 'd', 'e']
	result = [None] * (len(list_a) + len(list_b))
	result[::2] = list_a
	result[1::2] = list_b
	print(result)

concatenate_alternate()
def arr(n): 
    try:
    	array = []
    	for x in range(n):
    		array.append(x)
    	return array
    except TypeError:
    	array = []
    	return array
    finally:
    	return array

arr(4)
arr(0)
arr()
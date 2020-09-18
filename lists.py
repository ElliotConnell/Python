#lists

squares = [1, 4, 9, 16, 25]

print(squares)

#like strings (and all other built-in sequence types), lists can be indexed and sliced

print(squares[0]) #indexing returns the item

print(squares[-1])

print(squares[-3:]) #slicing returns a new list

#all slice operations return a new list containing the requested elements. this means the following slice returns a shallow copy of the list

print(squares[:])

#lists also support concatenation

print(squares + [36, 49, 64, 81, 100])

# unlike strings, which are immutable, lists are a mutable type, i.e it is possible to change their content

cubes = [1, 8, 27, 65, 125] #something is wrong here
4 ** 3 # cube of 4 is 64, not 65

cubes[3] = 64 # replace the wrong value
print(cubes)

#you can also add new items at the end of the list, by using the append() method

cubes.append(216) #add the cube of 6
cubes.append(7 ** 3) # and the cube of 7

print(cubes)

#assignment to slices is also possible, and this can even change the size of the list or clear it entriely

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

#replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)

#now remove them
letters[2:5] = []
print(letters)

#clear the list by replacing all elements with an empty list
letters[:] = []
print(letters)

letters = ['a', 'b', 'c', 'd']
print(len(letters))

#it is possible to nest lists (create lists containing other lists)
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])
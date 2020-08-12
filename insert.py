#testing machine

#sets the first list
words = ["Python", "fun"]

#variables
index = 1
test = 3

#first call to print
print(words)

#second call to print. updates list
words.insert(index, "is")
print(words)

#final call to print. uses previous list
words.insert(test, "jokes")
print(words)
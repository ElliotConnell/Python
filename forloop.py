#while loop 

words = ["hello", "world", "spam", "eggs"] #list
counter = 0 #counter variable
max_index = len(words) - 1 #index. length of the list -1

while counter <= max_index: #while loop for while the counter is less than the index variable, the loop will run
   word = words[counter] #loop condition
   print(word + "!") #operation
   counter = counter + 1 #cycle


 #for loop equivelent
words = ["hello", "world", "spam", "eggs"] #list
for word in words: #for loop
  print(word + "!") #operation
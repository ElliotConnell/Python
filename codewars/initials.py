#Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

#The output should be two capital letters with a dot separating them.


name = "David mendieta" 

#divide into 2 strings

name_seperate = name.split()
  
#take the first letter of the first string
first_initial = name_seperate[0][0]
    
#take the first letter of the second string
second_initial = name_seperate[1][0]

#combine the two strings
print((first_initial + '.' + second_initial).upper())

#for loop runs for each word after the string is seperated
#word[0] pulls the first character from the string
#'.'.join then joins the 2 characters together
#.upper then converts all items in the string to uppercase

print('.'.join(word[0] for word in name_seperate).upper())
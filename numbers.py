#numbers

#the interpreter acts as a simple calculator: you can type an expression at it and it will write the value. 
#expression syntax is straightforward: the operators +, -, *, and / work just like most languages; 
#parentheses can be used for grouping

print(2 + 2)
#4

print(50 - 5 * 6)
#20

print((50 - 5*6) / 4)
#5.0

print(8 / 5) #division always returns a floating point number
#1.6

print (17 / 3) # classic division returns a float 
#5.666666666666667

print(17 // 3) # the floor division discards the fractional part
#5

print( 17 % 3) # the % operator returns the remainder of the division
#2

print(5 * 3 + 2) # result * divisor + remainder
#17

print( 5 ** 2) # 5 squared
#25

print(2 ** 7) #2 to the power of 7
#128

width = 20
height = 5 * 9

print(width * height)
#900

#operators with mixed type operands convert the integer operand to floating point
print(4 * 3.75 - 1)
#14.0

#in interactive mode, the last printed expression is assigned to the variable _. 
#This means that when you are using python as a desk calculator, 
#it is somewhat easier to continue calculations

#tax = 12.5 / 100
#price = 100.50
#price * tax
#12.5625
#price + _
#113.0625
#print(round(_, 2))
#113.06

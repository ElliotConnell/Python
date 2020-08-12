#a simple calculator

#overall menu
# this keeps on accepting user input until the user enters quit. so a while loop is used

while True:
    #user options
    print("options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to end the program")
    user_input = input(":")
    

    #the break staement is used to stop the while loop, in case the user inputs quit
    if user_input == "quit":
        break
    #while statement
    elif user_input == "add":
        #create the addition funtion
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 + num2)
    elif user_input == "subtract":
        #create the subtraction function
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 - num2)
    elif user_input == "multiply":
        #create the multiply funtion
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 * num2)
    elif user_input == "divide":
        #create the divide funtion
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 / num2)
    else:
        print("Unknown input")
        
    #output line dispalys the end result
    #the output lines is outside the if statement to omit repetition of code
    print ("The answer is " + result)
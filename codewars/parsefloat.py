
#Write function parse_float which takes a string/list and returns a number or 'none' 
#if conversion is not possible.

string = "test"


def parse_float(string):
    #try convert the string to a float
    try:
        print(float(string))
    # if there is a ValueError or TypeError print "None"
    except (ValueError, TypeError):
        print(None)

#run function
parse_float(string)


#Write function parse_float which takes a string/list and returns a number or 'none' 
#if conversion is not possible.

string = "test"


def parse_float(string):
    try:
        print(float(string))
    except (ValueError, TypeError):
        print(None)


parse_float(string)

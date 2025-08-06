# Task 2

# a (decorator) that takes one argument
def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator

# returns an integer, but it will be convert to be a string
@type_converter(str)
def return_int():
    return 5

#  returns a string that can't be converted to int as instraction said 
@type_converter(int)
def return_string():
    return "hello"

# Main program to print the test 
if __name__ == "__main__":
    y = return_int()
    print(type(y).__name__)  # "str"

    try:
        y = return_string()
        print("shouldn't get here!")
    except ValueError:
        print("can't convert that string to an integer!") 

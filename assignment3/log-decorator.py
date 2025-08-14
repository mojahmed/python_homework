# Task 1

import logging

# open("decorator.log", "w").close()

# Set up logger
logger = logging.getLogger("parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

# Decorator that logs function name, and parameters, 
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        

        log_message = (
            f"function: {func.__name__}\n"
            f"positional parameters: {args}\n"
            f"keyword parameters: {kwargs}\n"
            f"return: {result}\n"
        )

        logger.info(log_message)
        return result
    return wrapper

# Function 1:  with no parameters
@logger_decorator
def greet():
    print("Hello, World!")

# Function 2: this for Positional arguments
@logger_decorator
def show_numbers(*nums):
    for n in nums:
        print("Number:", n)
    return True

# Function 3:and this  Keyword arguments, and to  returns the decorator
@logger_decorator
def return_decorator(**info):
    for key in info:
        print(key + ":", info[key])
    return logger_decorator

# for main block to run functions
if __name__ == "__main__":
    greet()
    show_numbers(1, 5 , 3)
    return_decorator(name="Mohammed", age=30)

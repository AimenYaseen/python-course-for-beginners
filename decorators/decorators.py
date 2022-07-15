# Assigning Function to variables
from unittest import result


def increment(num):
    return num + 1

addition = increment

print(addition(5))

# Defining function nside another function
def plus_one(num):
    def add_one(num):
        return num + 1

    return add_one(num)

print(plus_one(55))

# Passing function as arguments
def plus(num):
    return num + 2

def func_pass(func):
    num = 76
    return func(num)

print("Function passed : ", func_pass(plus))

# function call func() with paranthesis
# Return a Function

def hello_func():
    def say_hi():
        return "Hello!"

    return say_hi

hello = hello_func()
print(hello())

# Nested And Enclosing Functions
def enclosing(str):
    def nested():
        print(str)

    nested()

enclosing("Nested function can use this string")

# Let's Create a Decorator
# Receives a function & Returns a function
def uppercase_decorator(function):
    def wrapper():
        func = function()
        return func.upper()

    return wrapper

def say_hi():
    return "hello world"

return_wrapper = uppercase_decorator(say_hi) # calls the func which returns a func
# But its not executed

print(return_wrapper())

# using @
@uppercase_decorator # calls the func with say_hi_2 which returns a func
def say_hi_2():
    return "hello world 2"

print(say_hi_2()) # Now executed the return function

# Multiple Decorators
def split_decorator(function):
    def wrapper():
        func = function()
        return func.split()

    return wrapper

@split_decorator
@uppercase_decorator # bottom_up approach
def say_hello():
    return "hello multiple decorators"

print(say_hello())
# first uppercase decorator will be called 
# returns wrapper with uppercase string which will then be passed to split decorator
# split also returns the wrapper

# print statement executes the wrapper of split -> uppercase wrapper -> say_hello

# ---------------------- Decorators with Arguments -----------------------
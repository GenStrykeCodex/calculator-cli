# functions module for calculator cli

""" |----------- Basic maths functions -----------| """

# add function
def add(a,b):
    return a + b

# subtract function
def subtract(a,b):
    return a - b

# multiply function
def multiply(a,b):
    return a * b

# divide function
def divide(a,b):
    return a / b

""" |----------- Advanced maths functions -----------| """

# square function
def square(a):
    return a**2

# square root function
def square_root(a):
    return a**0.5

# exponent function
def exponent(a,b):
    return a**b

""" |----------- Percent functions -----------| """

# percentage function
def percentage(a,b):
    return a*b/100

# increase % function
def percentage_increase(a,b):
    return a + a*b/100

# decrease % function
def percentage_decrease(a,b):
    return a - a*b/100
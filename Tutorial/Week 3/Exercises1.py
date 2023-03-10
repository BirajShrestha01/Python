# WAP to develop a simple calculator, defining each function for each calculation. [Include a welcome message]

# Function for welcome message using docstring
def welcome():
    """Welcome to my simple calculator"""

# Function for addition


def add(a, b):
    return a+b

# Function for subtraction


def subtract(a, b):
    return a-b

# Function for multiplication


def multiply(a, b):
    return a*b

# Function for division


def divide(a, b):
    return a/b


# Printing welcome message
print(welcome.__doc__)

# Taking numbers from user
x = int(input("Enter number 1:"))
y = int(input("Enter number 2:"))

# Calling functions for simple calculations
print("Sum:", add(x, y))
print("Difference:", subtract(x, y))
print("Product:", multiply(x, y))
print("Quotient:", divide(x, y))

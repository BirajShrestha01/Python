# WAP to develop a simple calculator, defining each function for each calculation. [Include a welcome message]

def welcome():
    """Welcome to my simple calculator"""


def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    return a/b


print(welcome.__doc__)

x = int(input("Enter number 1:"))
y = int(input("Enter number 2:"))

print("Sum:", add(x, y))
print("Difference:", subtract(x, y))
print("Product:", multiply(x, y))
print("Quotient:", divide(x, y))

# Develop a program to calculate the average marks of any 5 subjects by documenting your function (using doc string)

# Taking marks from the user
subject1 = int(input("Enter your marks in subject 1: "))
subject2 = int(input("Enter your marks in subject 2: "))
subject3 = int(input("Enter your marks in subject 3: "))
subject4 = int(input("Enter your marks in subject 4: "))
subject5 = int(input("Enter your marks in subject 5: "))


def avg(a, b, c, d, e):
    """This function takes marks from the user and outputs the average."""
    return (a+b+c+d+e)/5


# Calling the function avg() and printing the average marks
print("Average marks: ", avg(subject1, subject2, subject3, subject4, subject5))

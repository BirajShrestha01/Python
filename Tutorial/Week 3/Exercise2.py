# Develop a program to calculate the average marks of any 5 subjects by documenting your function (using doc string)

# Taking marks from the user
subject1 = float(input("Enter your marks in subject 1: "))
subject2 = float(input("Enter your marks in subject 2: "))
subject3 = float(input("Enter your marks in subject 3: "))
subject4 = float(input("Enter your marks in subject 4: "))
subject5 = float(input("Enter your marks in subject 5: "))


def avg(a, b, c, d, e):
    """
    This function takes marks from the user and outputs the average. 
    To get an average marks we should fiest take input marks from the user ther we stould get a sum of them and divide the sum by the no. of subjects we get average marks of subjects.
    """
    return (a+b+c+d+e)/5


# Calling the function avg() and printing the average marks
print("Average marks: ", avg(subject1, subject2, subject3, subject4, subject5))

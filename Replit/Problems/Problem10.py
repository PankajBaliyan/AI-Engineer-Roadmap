# Write a python program to find an average of two numbers entered by the user.

def Main():
    number1 = int(input("Enter a number : "))
    number2 = int(input("Enter a number : "))
    result = findAverage(number1,number2)
    print(result)

def findAverage(a,b):
    return (a+b)/2
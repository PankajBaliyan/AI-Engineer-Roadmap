# Use comparison operator to find out whether ‘a’ given variable a is greater than
# ‘b’ or not. Take a = 34 and b = 80

def Main():
    number1 = int(input("Enter a number : "))
    number2 = int(input("Enter a number : "))
    result = findReminderFunc(number1,number2)
    print(result)

def findReminderFunc(a,b):
    if a == b:
        return "A is equals to b"
    elif a > b:
        return "A is greater than b"
    return "A is smaller then b"
# Check the type of variable assigned using input () function.

def Main():
    inputNumber = int(input("Enter a number : "))
    result = findReminderFunc(inputNumber)
    print(result)
    inputString = input("Enter a word : ")
    result = findReminderFunc(inputString)
    print(result)

def findReminderFunc(number):
    return type(number)
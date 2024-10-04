# Write a program to fill in a letter template given below with name and date

# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

def Main():
    enteredName = input("Enter Name : ")
    enteredDate = input("Enter Date : ")
    print(f'''
    Dear {enteredName},
    You are selected!
    {enteredDate}''')
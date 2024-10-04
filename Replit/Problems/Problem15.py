# Replace the double space with single spaces.

def Main():
        enteredString = "This is a  good  man"
        result = changeDoubleSpaceToSingleSpace(enteredString)
        print(result)

def changeDoubleSpaceToSingleSpace(data):
    tempData = data.replace("  ", " ")
        

    return tempData
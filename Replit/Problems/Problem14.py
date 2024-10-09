# Write a program to detect double space in a string.

def Main():
        enteredString = "This is a  good  man"
        result = findDoubleSpace(enteredString)
        print(result)

def findDoubleSpace(data):
    first_occurrence = data.find("  ")  # Find the first occurrence
    total_occurrences = data.count("  ")  # Count total occurrences

    tempData = {
        "firstOccurrence": first_occurrence,
        "totalOccurrences": total_occurrences
    }

    return tempData
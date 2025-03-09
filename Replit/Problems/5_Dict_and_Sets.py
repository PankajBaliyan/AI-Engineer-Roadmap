# =========================================================================== #

# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up

# def Main():
#         myDict = {
#             "naam": "Name",
#             "kon": "Who"
#         }
#         inputWord = input("Enter a word : ")
#         print(myDict[inputWord])

# =========================================================================== #

# Write a program to input eight numbers from the user and display all the unique
# numbers (once).

# def Main():
#     mySet = set({})
#     for i in range(0,8):
#         inputNumber = int(input("Enter a number : "))
#         mySet.add(inputNumber)
#     print(mySet)

# =========================================================================== #

# Can we have a set with 18 (int) and '18' (str) as a value in it?

# def Main():
#     my_set = {18, '18'}
#     print(my_set)

# =========================================================================== #

# What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

# def Main():
#     s = set()
#     s.add(20)
#     s.add(20.0)
#     s.add('20')
#     print(s)
#     print(len(s))

# =========================================================================== #

# s = {} , What is the type of 's'?
# def Main():
#     s = {}
#     print(type(s))

# =========================================================================== #

# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

# def Main():
#     myDict = {}
#     for i in range(0,3):
#         inputStr = input("Enter  : ")
#         myDict[i] = inputStr
#     print(myDict)

# =========================================================================== #
# If the names of 2 friends are same; what will happen to the program in problem 6?
# def Main():
#     myDict = {}
#     for i in range(0,3):
#         name = input("Enter name : ")
#         word = input("Enter word : ")
#         myDict[name] = word
#     print(myDict)

# =========================================================================== #
# 8. If languages of two friends are same; what will happen to the program in problem 6?
# def Main():

# =========================================================================== #
# 9. Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}
# def Main():
#     s = {8, 7, 12, "Harry", (1,2)}  # Use a tuple (1,2) instead of [1,2]
#     print(s)
#     s.remove((1,2))  # Remove the tuple
#     print(s)

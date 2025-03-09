# 1. Write a program to print Twinkle twinkle little star poem in python.
# def Main():
#     print('''
#     Twinkle Twinkle little star
#     How are you wonder what you are''')

# # 2. Use REPL and print the table of 5 using it. 
# def Main():
#     for i in range(1,11):
#         print(f"5 x {i} = {5*i}")

# =========================================================================== #
# 3. Install an external module and use it to perform an operation of your interest.
# import requests


# def Main():
#     # Call the function
#     fetch_data()

# =========================================================================== #
# Function to fetch data from a public API
# def fetch_data():
#     url = 'https://jsonplaceholder.typicode.com/todos/1'
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()  # Parse JSON response
#         print('Fetched Data:', data)
#     else:
#         print(f'Failed to fetch data. Status code: {response.status_code}')

# =========================================================================== #
# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that
# import os

# def Main():
#     # Call the function to print the directory contents
#     print_directory_contents(directory_path)

# # Function to print the contents of a specified directory
# def print_directory_contents(directory_path):
#     try:
#         # Get the list of files and directories in the specified directory
#         contents = os.listdir(directory_path)
#         # print(contents) #it will return a list of dir

#         # Print the contents
#         print(f"Contents of '{directory_path}':")
#         for item in contents:
#             print(item)

#     except FileNotFoundError:
#         print(f"The directory '{directory_path}' does not exist.")
#     except PermissionError:
#         print(f"Permission denied to access the directory '{directory_path}'.")

# # Specify the directory path
# directory_path = '.'  # '.' refers to the current directory

# =========================================================================== #
# 5. Label the program written in problem 4 with comments. 

# def Main():
#     print("Types of comments")

#     """
#     This is a multi-line comment
#     written using a docstring.
#     """

#     # single line comment

#     # Multi line
#     # Comment


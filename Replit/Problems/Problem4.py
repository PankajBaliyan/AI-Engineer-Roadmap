# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that
import os

def Main():
    # Call the function to print the directory contents
    print_directory_contents(directory_path)

# Function to print the contents of a specified directory
def print_directory_contents(directory_path):
    try:
        # Get the list of files and directories in the specified directory
        contents = os.listdir(directory_path)
        # print(contents) #it will return a list of dir

        # Print the contents
        print(f"Contents of '{directory_path}':")
        for item in contents:
            print(item)

    except FileNotFoundError:
        print(f"The directory '{directory_path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{directory_path}'.")

# Specify the directory path
directory_path = '.'  # '.' refers to the current directory
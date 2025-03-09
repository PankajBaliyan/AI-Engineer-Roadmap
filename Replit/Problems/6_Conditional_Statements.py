
# =========================================================================== #
# Write a program to find the greatest of four numbers entered by the user.
# def Main():
#     def find_max(numbers):
#         if not numbers:  # Check if the list is empty
#             return None

#         max_num = numbers[0]  # Start with the first number
#         for num in numbers[1:]:  # Iterate through the rest of the list
#             if num > max_num:
#                 max_num = num
#         return max_num

#     # Example usage
#     numbers = [4, 9, 2, 15, 1, 7, 23, 8]
#     max_number = find_max(numbers)
#     print(f"The maximum number is: {max_number}")

# =========================================================================== #
# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.
# def calculate_result(marks, pass_percentage=40, subject_pass_percentage=33):
#     total_marks = sum(marks.values())
#     total_subjects = len(marks)
#     total_percentage = (total_marks / (100 * total_subjects)) * 100

#     if total_percentage < pass_percentage:
#         return "fail"

#     for subject, score in marks.items():
#         if (score / 100) * 100 < subject_pass_percentage:
#             return "fail"

#     return "pass"

# def Main():
#     student_marks = {
#         'Maths': 50,
#         'English': 20,
#         'Science': 90
#     }
#     result = calculate_result(student_marks)
#     print(f"Student result: {result}")

# =========================================================================== #
# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.
# def is_spam(comment, spam_keywords):
#     comment = comment.lower()
#     for keyword in spam_keywords:
#         if keyword.lower() in comment:
#             return True
#     return False

# def Main():
#     spam_keywords = [
#         "Make a lot of money", 
#         "buy now", 
#         "subscribe this", 
#         "click this"
#     ]

#     # For testing purposes
#     test_comments = [
#         "This is a normal comment.",
#         "You can Make a lot of money with this method!",
#         "Please subscribe this channel!",
#         "CLICK THIS link to win a prize!",
#         "BUY NOW and get 50% off!"
#     ]

#     for comment in test_comments:
#         result = "SPAM" if is_spam(comment, spam_keywords) else "NOT SPAM"
#         print(f"Comment: '{comment}' is {result}")

    # Uncomment the following lines to test with user input
    # user_comment = input("Enter your comment: ")
    # result = "SPAM" if is_spam(user_comment, spam_keywords) else "NOT SPAM"
    # print(f"Your comment is {result}")

# =========================================================================== #
# Write a program to find whether a given username contains less than 10
# characters or not.
# def Main():
#     # Get username input from the user
#     user_input = input("Please enter a username: ")
#     result = check_username_length(user_input)
#     print(result)


# def check_username_length(username):
#     if len(username) < 10:
#         return "The username contains less than 10 characters."
#     else:
#         return "The username contains 10 or more characters."

# =========================================================================== #
# Write a program which finds out whether a given name is present in a list or not.
# def Main():

#     # Predefined list of names
#     names = ["Alice", "Bob", "Charlie", "David", "Eve"]

#     # Get name input from the user
#     user_input = input("Please enter a name to check: ")
#     result = check_name_in_list(user_input, names)
#     print(result)

# def check_name_in_list(name, name_list):
#     if name in name_list:
#         return f"The name '{name}' is present in the list."
#     else:
#         return f"The name '{name}' is not present in the list."

# =========================================================================== #
# Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

# def calculate_grade(marks):
#     if 90 <= marks <= 100:
#         return "Ex"
#     elif 80 <= marks < 90:
#         return "A"
#     elif 70 <= marks < 80:
#         return "B"
#     elif 60 <= marks < 70:
#         return "C"
#     elif 50 <= marks < 60:
#         return "D"
#     elif marks < 50:
#         return "F"
#     else:
#         return "Invalid marks entered. Please enter marks between 0 and 100."

# def Main():
#     # Get marks input from the user
#     try:
#         user_marks = float(input("Please enter the marks obtained (0-100): "))
#         grade = calculate_grade(user_marks)
#         print(f"The grade is: {grade}")
#     except ValueError:
#         print("Invalid input. Please enter a numeric value for marks.")



# =========================================================================== #
# Write a program to find out whether a given post is talking about “Harry” or not.
# def check_post_for_harry(post):
#     if "Harry" in post:
#         return "The post is talking about 'Harry'."
#     else:
#         return "The post is not talking about 'Harry'."

# def Main():
#     # Get post input from the user
#     user_post = input("Please enter a post: ")
#     result = check_post_for_harry(user_post)
#     print(result)


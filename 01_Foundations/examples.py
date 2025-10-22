# ==============================================================================
# Module 01: Python Foundations - Code Examples
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Basic Syntax & Comments
# ------------------------------------------------------------------------------

# This is a single-line comment.
# Python uses indentation (usually 4 spaces) to define code blocks.
if True:
    print("Indentation is crucial in Python!") # This line is indented

"""
This is a multi-line comment (docstring).
It's often used for explaining functions or modules.
"""

# ------------------------------------------------------------------------------
# 2. Variables & Data Types
# ------------------------------------------------------------------------------

# Variable assignment
message = "Hello, Professor!" # String (str)
student_count = 25          # Integer (int)
average_score = 92.5        # Float (float)
is_enrolled = True          # Boolean (bool)

# You can check the type of a variable using the type() function
print(type(message))        # Output: <class 'str'>
print(type(student_count))  # Output: <class 'int'>
print(type(average_score))  # Output: <class 'float'>
print(type(is_enrolled))    # Output: <class 'bool'>

# ------------------------------------------------------------------------------
# 3. Type Casting
# ------------------------------------------------------------------------------

# Converting between types
num_str = "100"
num_int = int(num_str)       # Convert string to integer
print(num_int + 50)          # Output: 150

score_float = 85.7
score_int = int(score_float) # Convert float to integer (truncates)
print(score_int)             # Output: 85

age_int = 30
age_str = str(age_int)       # Convert integer to string
print("My age is " + age_str) # Output: My age is 30

# ------------------------------------------------------------------------------
# 4. Basic Input/Output (`print()`, `input()`)
# ------------------------------------------------------------------------------

# Using print()
print("Welcome to the Python Mastery Roadmap.")
subject = "Programming"
difficulty = "Intermediate"
print("Subject:", subject, "- Difficulty:", difficulty)

# Using f-strings (formatted string literals) - Recommended
print(f"Current Subject: {subject} (Difficulty: {difficulty})")

# Using input() to get user data (always returns a string!)
# Uncomment the following lines to run the input example:
# user_name = input("Please enter your name: ")
# birth_year_str = input(f"Hello {user_name}, please enter your birth year: ")

# # Perform type casting for calculations
# try: # Use try-except to handle potential errors if user enters non-numeric input
#     birth_year = int(birth_year_str)
#     current_year = 2025 # Assuming current year is 2025
#     user_age = current_year - birth_year
#     print(f"You are approximately {user_age} years old.")
# except ValueError:
#     print("Invalid input. Please enter a valid year.")

# ==============================================================================
# End of Module 01 Examples
# ==============================================================================
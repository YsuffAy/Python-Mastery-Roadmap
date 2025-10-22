# ==============================================================================
# Module 01: Python Foundations - Exercises
# ==============================================================================
# This file contains solved exercises to practice the concepts covered
# in the Foundations module (variables, data types, type casting, input/output).
# ==============================================================================

# ------------------------------------------------------------------------------
# EXERCISE 1: Simple Area Calculator
# ------------------------------------------------------------------------------
# Description: Calculate the area of a rectangle. Ask the user for the
#              length and width, convert them to floats, calculate the area,
#              and print the result.
# Source: Self-created

print("--- Exercise 1: Rectangle Area Calculator ---")
# Get input from the user (input always returns string)
# Uncomment the following lines to run this exercise interactively:
# length_str = input("Enter the length of the rectangle: ")
# width_str = input("Enter the width of the rectangle: ")

# # Use default values if running non-interactively for demonstration
length_str = "10.5"
width_str = "5.2"

try:
    # Convert input strings to float numbers for calculation
    length = float(length_str)
    width = float(width_str)

    # Calculate the area
    area = length * width

    # Print the result using an f-string
    print(f"The length is: {length}")
    print(f"The width is: {width}")
    print(f"The area of the rectangle is: {area}")

except ValueError:
    print("Invalid input. Please enter numeric values for length and width.")

# Expected Output (with default values):
# The length is: 10.5
# The width is: 5.2
# The area of the rectangle is: 54.6

print("-" * 40) # Separator line

# ------------------------------------------------------------------------------
# EXERCISE 2: String Repetition and Concatenation
# ------------------------------------------------------------------------------
# Description: Ask the user for their favorite word and a number (n).
#              Print the word repeated n times, separated by spaces.
# Source: Self-created

print("--- Exercise 2: Word Repeater ---")
# Get input from the user
# Uncomment the following lines to run this exercise interactively:
# favorite_word = input("Enter your favorite word: ")
# repeat_count_str = input("How many times should it be repeated? ")

# Use default values for demonstration
favorite_word = "Python"
repeat_count_str = "3"

try:
    # Convert repeat count to integer
    repeat_count = int(repeat_count_str)

    # Method 1: Using string multiplication and join (more Pythonic)
    repeated_words_list = [favorite_word] * repeat_count
    result_string = " ".join(repeated_words_list)

    # Method 2: Using a loop (more explicit)
    # result_string_loop = ""
    # for i in range(repeat_count):
    #     result_string_loop += favorite_word
    #     if i < repeat_count - 1: # Add space except for the last word
    #         result_string_loop += " "

    # Print the result
    print(f"Your word: {favorite_word}")
    print(f"Repeated {repeat_count} times: {result_string}")

except ValueError:
    print("Invalid input. Please enter a valid number for repetition count.")

# Expected Output (with default values):
# Your word: Python
# Repeated 3 times: Python Python Python

print("-" * 40) # Separator line

# ------------------------------------------------------------------------------
# EXERCISE 3: Boolean Logic Check
# ------------------------------------------------------------------------------
# Description: Check if a given number is positive AND even.
# Source: Self-created

print("--- Exercise 3: Positive and Even Check ---")
number_to_check = 10

# Check conditions using logical operators
is_positive = number_to_check > 0
is_even = number_to_check % 2 == 0

# Combine conditions with 'and'
is_positive_and_even = is_positive and is_even

# Print the results
print(f"Number to check: {number_to_check}")
print(f"Is it positive? {is_positive}")
print(f"Is it even? {is_even}")
print(f"Is it positive AND even? {is_positive_and_even}")

# Try with another number
number_to_check_2 = -7
is_positive_2 = number_to_check_2 > 0
is_even_2 = number_to_check_2 % 2 == 0
is_positive_and_even_2 = is_positive_2 and is_even_2
print(f"\nNumber to check: {number_to_check_2}")
print(f"Is it positive AND even? {is_positive_and_even_2}")


# Expected Output:
# Number to check: 10
# Is it positive? True
# Is it even? True
# Is it positive AND even? True
#
# Number to check: -7
# Is it positive AND even? False

print("-" * 40) # Separator line

# ==============================================================================
# End of Module 01 Exercises
# ==============================================================================
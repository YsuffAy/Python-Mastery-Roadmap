# ==============================================================================
# Module 03: Data Structures / Tuples - Exercises
# ==============================================================================
# This file contains solved exercises to practice the concepts covered in the
# Tuples submodule, including immutability, unpacking, and use cases.
# ==============================================================================

# ------------------------------------------------------------------------------
# EXERCISE 1: Returning Multiple Values from a Function
# ------------------------------------------------------------------------------
# Description: Create a function that takes a list of numbers and returns the
#              minimum, maximum, and sum of the list. Then, "unpack" the
#              returned tuple into separate variables.
# This demonstrates tuple packing (on return) and unpacking (on assignment).
# Source: Self-created

print("--- Exercise 1: Multiple Return Values ---")

def calculate_stats(data_list):
    """Calculates the min, max, and sum of a list of numbers."""
    if not data_list:
        return None, None, None # Return a tuple of Nones if the list is empty

    minimum = min(data_list)
    maximum = max(data_list)
    total = sum(data_list)
    return minimum, maximum, total # Python automatically "packs" these into a tuple

# Sample data
scores = [88, 95, 72, 100, 65]

# Call the function and "unpack" the resulting tuple into three variables
min_score, max_score, sum_of_scores = calculate_stats(scores)

print(f"Data list: {scores}")
print(f"Minimum value returned: {min_score}")
print(f"Maximum value returned: {max_score}")
print(f"Sum of values returned: {sum_of_scores}")

# Expected Output:
# Data list: [88, 95, 72, 100, 65]
# Minimum value returned: 65
# Maximum value returned: 100
# Sum of values returned: 420

print("-" * 40)


# ------------------------------------------------------------------------------
# EXERCISE 2: Using Tuples as Dictionary Keys
# ------------------------------------------------------------------------------
# Description: Create a dictionary to store student grades for different courses.
#              Use a tuple `(student_id, course_code)` as the key for each grade.
# This demonstrates a key use case where lists cannot be used.
# Source: Self-created

print("--- Exercise 2: Tuples as Dictionary Keys ---")
# Using tuples as keys to store compound information
grade_book = {
    (101, "PHYS-101"): 95,
    (101, "MATH-101"): 88,
    (102, "PHYS-101"): 91,
    (102, "CS-101"): 99,
}

# Add a new entry
grade_book[(101, "CS-101")] = 85

# Look up a specific grade
student_to_lookup = 102
course_to_lookup = "PHYS-101"
lookup_key = (student_to_lookup, course_to_lookup)

if lookup_key in grade_book:
    grade = grade_book[lookup_key]
    print(f"Grade for Student ID {student_to_lookup} in Course {course_to_lookup} is: {grade}")
else:
    print(f"No grade found for Student ID {student_to_lookup} in Course {course_to_lookup}.")

# Expected Output:
# Grade for Student ID 102 in Course PHYS-101 is: 91

print("-" * 40)


# ------------------------------------------------------------------------------
# EXERCISE 3: Unpacking for Data Records
# ------------------------------------------------------------------------------
# Description: A function returns a data record as a tuple. Unpack this tuple
#              to extract specific pieces of information.
# This demonstrates selective unpacking.
# Source: Self-created

print("--- Exercise 3: Unpacking Data Records ---")

def get_file_record():
    """Returns a sample file record as a tuple."""
    return ("main.py", "1.2 KB", "2025-10-30", "Read-Only")

# Get the record
file_info = get_file_record()

# Unpack the tuple to get specific information
# We only care about the filename and the date, so we can use `_` to ignore the others.
filename, _, modification_date, _ = file_info

print(f"Full record received: {file_info}")
print(f"Extracted Filename: {filename}")
print(f"Extracted Modification Date: {modification_date}")


# Expected Output:
# Full record received: ('main.py', '1.2 KB', '2025-10-30', 'Read-Only')
# Extracted Filename: main.py
# Extracted Modification Date: 2025-10-30

print("-" * 40)

# ==============================================================================
# End of Module 03/Tuples Exercises
# ==============================================================================
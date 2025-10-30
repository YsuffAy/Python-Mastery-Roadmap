# ==============================================================================
# Module 03: Data Structures / Lists - Exercises
# ==============================================================================
# This file contains solved exercises to practice the concepts covered in the
# Lists submodule, including list creation, manipulation, and iteration.
# ==============================================================================

# ------------------------------------------------------------------------------
# EXERCISE 1: Filter and Transform
# ------------------------------------------------------------------------------
# Description: Given a list of numbers, create a new list that contains the
#              square of only the odd numbers from the original list.
# Source: Self-created

print("--- Exercise 1: Filter and Transform ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_of_odds = []

# Iterate through each number in the original list
for number in numbers:
    # Check if the number is odd
    if number % 2 != 0:
        # If it is, calculate its square and append to the new list
        squares_of_odds.append(number ** 2)

print(f"Original list: {numbers}")
print(f"Squares of odd numbers: {squares_of_odds}")

# --- Alternative Solution using List Comprehension ---
# This is a more "Pythonic" way to achieve the same result in one line.
squares_of_odds_comp = [number ** 2 for number in numbers if number % 2 != 0]
print(f"Result with List Comprehension: {squares_of_odds_comp}")

# Expected Output:
# Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Squares of odd numbers: [1, 9, 25, 49, 81]
# Result with List Comprehension: [1, 9, 25, 49, 81]

print("-" * 40)


# ------------------------------------------------------------------------------
# EXERCISE 2: Find Common Elements
# ------------------------------------------------------------------------------
# Description: Given two lists, find and create a new list containing only the
#              elements that are present in both lists, without duplicates.
# Source: Self-created

print("--- Exercise 2: Find Common Elements ---")
list_a = [1, 2, 3, 4, 5, 5, 6]
list_b = [4, 5, 6, 7, 8, 8, 5]
common_elements = []

# Iterate through each item in the first list
for item in list_a:
    # Check if the item is in the second list AND not already in our result list
    if item in list_b and item not in common_elements:
        common_elements.append(item)

print(f"List A: {list_a}")
print(f"List B: {list_b}")
print(f"Common elements (no duplicates): {common_elements}")

# --- Alternative Solution using Sets ---
# This is a much more efficient way to solve this problem.
common_elements_set = list(set(list_a) & set(list_b))
print(f"Result with Sets: {common_elements_set}")

# Expected Output:
# List A: [1, 2, 3, 4, 5, 5, 6]
# List B: [4, 5, 6, 7, 8, 8, 5]
# Common elements (no duplicates): [4, 5, 6]
# Result with Sets: [4, 5, 6] (Order may vary with sets)

print("-" * 40)


# ------------------------------------------------------------------------------
# EXERCISE 3: Remove Duplicates from a List
# ------------------------------------------------------------------------------
# Description: Given a list with duplicate entries, create a new list that
#              contains only the unique elements, preserving the original order.
# Source: Self-created

print("--- Exercise 3: Remove Duplicates (Preserving Order) ---")
inventory_tags = ["A-01", "B-02", "A-01", "C-03", "B-02", "D-04"]
unique_tags = []

# Iterate through the original list
for tag in inventory_tags:
    # If the tag is not already in our new list, add it
    if tag not in unique_tags:
        unique_tags.append(tag)

print(f"Original tags: {inventory_tags}")
print(f"Unique tags (order preserved): {unique_tags}")

# --- Note on using sets for this ---
# Converting to a set and back to a list is faster but DOES NOT preserve order.
# unique_tags_unordered = list(set(inventory_tags))
# print(f"Unique tags (order NOT preserved): {unique_tags_unordered}")


# Expected Output:
# Original tags: ['A-01', 'B-02', 'A-01', 'C-03', 'B-02', 'D-04']
# Unique tags (order preserved): ['A-01', 'B-02', 'C-03', 'D-04']

print("-" * 40)

# ==============================================================================
# End of Module 03/Lists Exercises
# ==============================================================================
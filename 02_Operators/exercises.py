# ==============================================================================
# Module 02: Python Operators - Exercises
# ==============================================================================
# This file contains solved exercises to practice the concepts covered in the
# Operators module, including arithmetic, comparison, and logical operators.
# ==============================================================================

import math # We'll need this for the value of PI in Exercise 1

# ------------------------------------------------------------------------------
# EXERCISE 1: Circle Calculator
# ------------------------------------------------------------------------------
# Description: Calculate the area and circumference of a circle given its radius.
# This exercise uses arithmetic operators (`*`, `**`).
# Formulas: Area = π * r², Circumference = 2 * π * r
# Source: Self-created

print("--- Exercise 1: Circle Calculator ---")
radius = 7.5

# Calculate area using the exponentiation operator (**)
area = math.pi * (radius ** 2)

# Calculate circumference using the multiplication operator (*)
circumference = 2 * math.pi * radius

# Print the results, formatted to show 2 decimal places
print(f"Given a circle with radius: {radius}")
print(f"The calculated area is: {area:.2f}")
print(f"The calculated circumference is: {circumference:.2f}")

# Expected Output:
# Given a circle with radius: 7.5
# The calculated area is: 176.71
# The calculated circumference is: 47.12

print("-" * 40)

# ------------------------------------------------------------------------------
# EXERCISE 2: Admission Eligibility Check
# ------------------------------------------------------------------------------
# Description: Check if a candidate is eligible for a program. Eligibility
#              requires a score of 80 or higher AND an age between 18 and 25 (inclusive).
# This exercise uses comparison (`>=`, `<=`) and logical (`and`) operators.
# Source: Self-created

print("--- Exercise 2: Admission Eligibility Check ---")
candidate_score = 85
candidate_age = 22

# Check each condition separately
is_score_sufficient = candidate_score >= 80
is_age_valid = (candidate_age >= 18) and (candidate_age <= 25)

# Combine the conditions to determine final eligibility
is_eligible = is_score_sufficient and is_age_valid

# Print the results
print(f"Candidate Score: {candidate_score}")
print(f"Candidate Age: {candidate_age}")
print(f"Score is sufficient (>= 80)? {is_score_sufficient}")
print(f"Age is valid (between 18 and 25)? {is_age_valid}")
print(f"Final Eligibility: {is_eligible}")

# Expected Output:
# Candidate Score: 85
# Candidate Age: 22
# Score is sufficient (>= 80)? True
# Age is valid (between 18 and 25)? True
# Final Eligibility: True

print("-" * 40)

# ------------------------------------------------------------------------------
# EXERCISE 3: Inventory Update and Boxing
# ------------------------------------------------------------------------------
# Description: Update an inventory count and then calculate how many full boxes
#              can be packed and how many items are left over.
# This exercise uses assignment (`+=`) and modulus (`%`) operators.
# Source: Self-created

print("--- Exercise 3: Inventory Update and Boxing ---")
inventory_count = 125
items_per_box = 10

print(f"Initial inventory: {inventory_count}")

# A new shipment arrives, add it to the inventory
new_shipment = 38
inventory_count += new_shipment # Using the assignment operator
print(f"Inventory after receiving {new_shipment} new items: {inventory_count}")

# Calculate how many full boxes can be packed using floor division
full_boxes = inventory_count // items_per_box

# Calculate how many items are left over using the modulus operator
remaining_items = inventory_count % items_per_box

# Print the packaging results
print(f"With {items_per_box} items per box, we can pack {full_boxes} full boxes.")
print(f"There will be {remaining_items} items left over.")

# Expected Output:
# Initial inventory: 125
# Inventory after receiving 38 new items: 163
# With 10 items per box, we can pack 16 full boxes.
# There will be 3 items left over.

print("-" * 40)

# ==============================================================================
# End of Module 02 Exercises
# ==============================================================================
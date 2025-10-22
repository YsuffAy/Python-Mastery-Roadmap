# ==============================================================================
# Module 02: Python Operators - Code Examples
# ==============================================================================
# This file provides working examples for the operators covered in the
# Operators module.
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Arithmetic Operators
# ------------------------------------------------------------------------------
print("--- 1. Arithmetic Operators ---")
a = 10
b = 3

print(f"{a} + {b}  = {a + b}")    # Addition
print(f"{a} - {b}  = {a - b}")    # Subtraction
print(f"{a} * {b}  = {a * b}")    # Multiplication
print(f"{a} / {b}  = {a / b}")    # Division (always returns a float)
print(f"{a} % {b}  = {a % b}")    # Modulus (returns the remainder)
print(f"{a} ** {b} = {a ** b}")   # Exponentiation (a to the power of b)
print(f"{a} // {b} = {a // b}")   # Floor Division (discards the fractional part)

# ------------------------------------------------------------------------------
# 2. Assignment Operators
# ------------------------------------------------------------------------------
print("--- 2. Assignment Operators ---")
x = 10
print(f"Initial x: {x}")

x += 5  # Equivalent to x = x + 5
print(f"After x += 5: {x}")

x -= 3  # Equivalent to x = x - 3
print(f"After x -= 3: {x}")

x *= 2  # Equivalent to x = x * 2
print(f"After x *= 2: {x}")

x /= 4  # Equivalent to x = x / 4
print(f"After x /= 4: {x}")
print("-" * 40)

# ------------------------------------------------------------------------------
# 3. Comparison Operators
# ------------------------------------------------------------------------------
print("--- 3. Comparison Operators ---")
val1 = 10
val2 = 5

print(f"{val1} == {val2}: {val1 == val2}")   # Equal to
print(f"{val1} != {val2}: {val1 != val2}")   # Not equal to
print(f"{val1} > {val2}: {val1 > val2}")    # Greater than
print(f"{val1} < {val2}: {val1 < val2}")    # Less than
print(f"{val1} >= 10: {val1 >= 10}")     # Greater than or equal to
print(f"{val2} <= 5: {val2 <= 5}")      # Less than or equal to
print("-" * 40)

# ------------------------------------------------------------------------------
# 4. Logical Operators
# ------------------------------------------------------------------------------
print("--- 4. Logical Operators ---")
age = 25
has_license = True

# 'and' operator: checks if a person can legally drive a car
can_drive = age >= 18 and has_license
print(f"Age: {age}, Has License: {has_license}")
print(f"Can drive? (age >= 18 and has_license): {can_drive}")

# 'or' operator: checks for a discount
is_student = False
is_senior = False
gets_discount = is_student or is_senior
print(f"\nIs student? {is_student}, Is senior? {is_senior}")
print(f"Gets discount? (is_student or is_senior): {gets_discount}")

# 'not' operator: inverts a boolean value
is_active = False
is_inactive = not is_active
print(f"\nIs active? {is_active}")
print(f"Is inactive? (not is_active): {is_inactive}")
print("-" * 40)

# ------------------------------------------------------------------------------
# 5. Identity Operators
# ------------------------------------------------------------------------------
print("--- 5. Identity Operators ---")
list_a = [1, 2, 3]
list_b = list_a      # list_b is just another name for list_a
list_c = [1, 2, 3]   # list_c has the same values but is a different object

print(f"list_a: {list_a}")
print(f"list_b: {list_b}")
print(f"list_c: {list_c}")

# 'is' operator checks if they are the SAME object in memory
print(f"list_a is list_b: {list_a is list_b}")   # True, they point to the same object

# 'is not' operator checks if they are DIFFERENT objects
print(f"list_a is not list_c: {list_a is not list_c}") # True, they are different objects

# Compare with '==' which checks if the VALUES are the same
print(f"list_a == list_c: {list_a == list_c}")   # True, their content is identical
print("-" * 40)

# ------------------------------------------------------------------------------
# 6. Membership Operators
# ------------------------------------------------------------------------------
print("--- 6. Membership Operators ---")
my_frameworks = ["Django", "Flask", "FastAPI"]
my_name = "Nikola Tesla"

# 'in' operator
print(f"Is 'Flask' in {my_frameworks}? {'Flask' in my_frameworks}")   # True
print(f"Is 'React' in {my_frameworks}? {'React' in my_frameworks}")   # False

# 'not in' operator
print(f"Is 'Ruby' not in {my_frameworks}? {'Ruby' not in my_frameworks}") # True
print(f"Is 'Tesla' in the name '{my_name}'? {'Tesla' in my_name}")       # True
print("-" * 40)

# ==============================================================================
# End of Module 02 Examples
# ==============================================================================
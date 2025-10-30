# ==============================================================================
# Module 03: Data Structures / Tuples - Code Examples
# ==============================================================================
# This file provides working examples for the concepts covered in the Tuples
# submodule README.md.
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Creating Tuples
# ------------------------------------------------------------------------------
print("--- 1. Creating Tuples ---")
# An empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}, type: {type(empty_tuple)}")

# A tuple of numbers
numbers = (1, 5, -2, 10, 5)
print(f"Tuple of numbers: {numbers}")

# A tuple with mixed data types
mixed_tuple = (1, "Hello", 3.14, True)
print(f"Mixed-type tuple: {mixed_tuple}")

# CRITICAL: Creating a single-item tuple requires a trailing comma
single_item_tuple = (5,)
not_a_tuple = (5) # This is just the integer 5
print(f"Single-item tuple: {single_item_tuple}, type: {type(single_item_tuple)}")
print(f"This is NOT a tuple: {not_a_tuple}, type: {type(not_a_tuple)}")

# Tuple packing (creating a tuple without parentheses)
packed_tuple = 10, "Twenty", 30.0
print(f"Packed tuple: {packed_tuple}, type: {type(packed_tuple)}")
print("-" * 40)


# ------------------------------------------------------------------------------
# 2. Accessing Elements: Indexing & Slicing
# ------------------------------------------------------------------------------
print("--- 2. Accessing Elements ---")
coordinates = (1920, 1080, "RGB", 60) # (x, y, color_mode, refresh_rate)

# --- Indexing ---
print("Indexing:")
print(f"First element (index 0): {coordinates[0]}")   # 1920
print(f"Last element (index -1): {coordinates[-1]}")  # 60

# --- Slicing ---
print("\nSlicing:")
# Get the resolution (x, y) as a new tuple
resolution = coordinates[0:2]
print(f"Resolution slice [0:2]: {resolution}") # (1920, 1080)

# Get all elements except the first one
other_info = coordinates[1:]
print(f"Other info slice [1:]: {other_info}") # (1080, 'RGB', 60)

# --- IMMUTABILITY DEMONSTRATION ---
print("\nAttempting to change a tuple (will cause an error):")
try:
    coordinates[0] = 1024 # This line will raise a TypeError
except TypeError as e:
    print(f"Error caught as expected: {e}")
print("-" * 40)


# ------------------------------------------------------------------------------
# 3. Tuple Methods
# ------------------------------------------------------------------------------
print("--- 3. Tuple Methods ---")
grades = ('A', 'B', 'C', 'B', 'A', 'A')
print(f"Grades tuple: {grades}")

# .count() method
count_of_A = grades.count('A')
print(f"Number of 'A' grades: {count_of_A}")

# .index() method
index_of_first_B = grades.index('B')
print(f"Index of the first 'B' grade: {index_of_first_B}")
print("-" * 40)


# ------------------------------------------------------------------------------
# 4. Use Cases for Tuples
# ------------------------------------------------------------------------------
print("--- 4. Use Cases ---")
# --- As Dictionary Keys ---
# Lists are mutable and cannot be keys, but tuples can.
location_data = {
    (40.7128, -74.0060): "New York City", # A tuple as a key
    (34.0522, -118.2437): "Los Angeles"
}
nyc_coords = (40.7128, -74.0060)
print(f"Data for {nyc_coords}: {location_data[nyc_coords]}")
print("-" * 40)


# ------------------------------------------------------------------------------
# 5. Tuple Packing and Unpacking
# ------------------------------------------------------------------------------
print("--- 5. Tuple Packing and Unpacking ---")

# --- Returning multiple values from a function ---
# The function actually returns a single tuple, which can then be unpacked.
def get_user_info():
    name = "Nikola"
    surname = "Tesla"
    birth_year = 1856
    return name, surname, birth_year # Tuple packing happens here

# Unpacking the returned tuple into separate variables
user_name, user_surname, user_birth_year = get_user_info()

print(f"Unpacked info: Name={user_name}, Surname={user_surname}, Year={user_birth_year}")

# --- Swapping variables in a single line ---
a = 10
b = 20
print(f"\nBefore swap: a = {a}, b = {b}")
a, b = b, a # Packing (b, a) into a tuple, then unpacking into a, b
print(f"After swap: a = {a}, b = {b}")
print("-" * 40)

# ==============================================================================
# End of Module 03/Tuples Examples
# ==============================================================================
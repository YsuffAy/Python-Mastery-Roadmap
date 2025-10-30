# ==============================================================================
# Module 03: Data Structures / Sets - Code Examples
# ==============================================================================
# This file provides working examples for the concepts covered in the Sets
# submodule README.md.
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Creating Sets
# ------------------------------------------------------------------------------
print("--- 1. Creating Sets ---")

# Creating a set from a list with duplicates.
# Note how duplicates are automatically removed.
numbers_list = [1, 2, 3, 4, 4, 2]
numbers_set = {1, 2, 3, 4, 4, 2}
print(f"Creating a set from {numbers_list}: {numbers_set}")

# CRITICAL: Creating an empty set
empty_set = set()
empty_dict = {} # This creates an empty DICTIONARY, not a set!
print(f"An empty set: {empty_set}, type: {type(empty_set)}")
print(f"This is an empty dictionary: {empty_dict}, type: {type(empty_dict)}")

# A set cannot contain mutable items like lists
# The following line would raise a TypeError if uncommented:
# invalid_set = {1, 2, [3, 4]}

# A set can contain immutable items like tuples
valid_set = {1, 2, (3, 4)}
print(f"A set with a tuple inside: {valid_set}")
print("-" * 40)


# ------------------------------------------------------------------------------
# 2. Set Methods
# ------------------------------------------------------------------------------
print("--- 2. Set Methods ---")
elements = {'Hydrogen', 'Helium'}
print(f"Initial set: {elements}")

# --- Adding Elements ---
elements.add('Lithium') # Add a single element
print(f"After add('Lithium'): {elements}")
elements.add('Helium') # Adding an existing element does nothing
print(f"After add('Helium') again: {elements}")

more_elements = {'Beryllium', 'Boron', 'Lithium'}
elements.update(more_elements) # Add all elements from another set
print(f"After update() with another set: {elements}")

# --- Removing Elements ---
# .discard() is safe: it does nothing if the element is not found
elements.discard('Carbon')
print(f"After discard('Carbon') (not in set): {elements}")

# .remove() is unsafe: it raises a KeyError if the element is not found
elements.remove('Helium')
print(f"After remove('Helium'): {elements}")
# The following line would raise a KeyError:
# elements.remove('Carbon')

# .pop() removes and returns an ARBITRARY element
popped_element = elements.pop()
print(f"Popped an arbitrary element: {popped_element}")
print(f"Set after pop(): {elements}")
print("-" * 40)


# ------------------------------------------------------------------------------
# 3. Mathematical Set Operations
# ------------------------------------------------------------------------------
print("--- 3. Mathematical Set Operations ---")
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Union: all unique elements from both sets
union_set = set_a | set_b
print(f"Union (A | B): {union_set}")
print(f"Union (A.union(B)): {set_a.union(set_b)}")

# Intersection: only elements common to both sets
intersection_set = set_a & set_b
print(f"Intersection (A & B): {intersection_set}")
print(f"Intersection (A.intersection(B)): {set_a.intersection(set_b)}")

# Difference: elements in A but not in B
difference_set = set_a - set_b
print(f"Difference (A - B): {difference_set}")
print(f"Difference (B - A): {set_b.difference(set_a)}")

# Symmetric Difference: elements in either A or B, but not both
symmetric_diff_set = set_a ^ set_b
print(f"Symmetric Difference (A ^ B): {symmetric_diff_set}")
print("-" * 40)


# ------------------------------------------------------------------------------
# 4. Use Cases
# ------------------------------------------------------------------------------
print("--- 4. Use Cases ---")

# --- Use Case 1: Removing Duplicates from a List ---
print("Removing duplicates from a list:")
messy_list = ['apple', 'banana', 'orange', 'apple', 'grape', 'banana']
print(f"Original messy list: {messy_list}")
unique_items_list = list(set(messy_list)) # Convert to set to remove duplicates, then back to list
print(f"List with unique items: {unique_items_list}")
print("(Note: The original order is not guaranteed)")

# --- Use Case 2: Fast Membership Testing ---
print("\nFast membership testing:")
# For a large number of items, checking 'in' a set is much faster than 'in' a list.
# This example demonstrates the syntax; the speed difference is noticeable on large datasets.
permissions = {'read', 'write', 'execute'}
user_permission = 'write'
print(f"User permissions: {permissions}")
if user_permission in permissions:
    print(f"User has '{user_permission}' permission. Access granted.")
else:
    print(f"User does not have '{user_permission}' permission. Access denied.")
print("-" * 40)

# ==============================================================================
# End of Module 03/Sets Examples
# ==============================================================================
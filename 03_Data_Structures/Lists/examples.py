# ==============================================================================
# Module 03: Data Structures / Lists - Code Examples
# ==============================================================================
# This file provides working examples for the concepts covered in the Lists
# submodule README.md.
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Creating Lists
# ------------------------------------------------------------------------------
print("--- 1. Creating Lists ---")
empty_list = []
numbers = [1, 5, -2, 10, 5]  # A list with duplicate elements
mixed_list = [1, "Hello", 3.14, True, [10, 20]] # A list with different data types

print(f"An empty list: {empty_list}")
print(f"A list of numbers: {numbers}")
print(f"A mixed-type list: {mixed_list}")
print("-" * 40)


# ------------------------------------------------------------------------------
# 2. Accessing Elements: Indexing & Slicing
# ------------------------------------------------------------------------------
print("--- 2. Accessing Elements ---")
colors = ["red", "blue", "green", "yellow", "purple"]

# --- Indexing ---
print("Indexing:")
print(f"First element (index 0): {colors[0]}")   # Accessing the first item
print(f"Third element (index 2): {colors[2]}")   # Accessing the third item
print(f"Last element (index -1): {colors[-1]}")  # Negative indexing for the last item
print(f"Second to last (index -2): {colors[-2]}")# Negative indexing

# --- Slicing ---
print("\nSlicing:")
print(f"From index 1 to 4 (exclusive): {colors[1:4]}") # ['blue', 'green', 'yellow']
print(f"From the beginning to index 3 (exclusive): {colors[:3]}") # ['red', 'blue', 'green']
print(f"From index 2 to the end: {colors[2:]}") # ['green', 'yellow', 'purple']
print(f"A full copy of the list: {colors[:]}")
print(f"Every second element: {colors[::2]}") # ['red', 'green', 'purple']
print(f"Reversed list: {colors[::-1]}")
print("-" * 40)


# ------------------------------------------------------------------------------
# 3. List Methods: Modifying and Managing Lists
# ------------------------------------------------------------------------------
print("--- 3. List Methods ---")
planets = ["Mercury", "Venus", "Earth"]
print(f"Initial list of planets: {planets}")

# --- Adding Items ---
planets.append("Mars") # Adds "Mars" to the end
print(f"After append('Mars'): {planets}")

planets.insert(1, "Planet X") # Inserts "Planet X" at index 1
print(f"After insert(1, 'Planet X'): {planets}")

outer_planets = ["Jupiter", "Saturn"]
planets.extend(outer_planets) # Adds all items from another list
print(f"After extend(['Jupiter', 'Saturn']): {planets}")

# --- Removing Items ---
planets.remove("Planet X") # Removes the first occurrence of "Planet X"
print(f"After remove('Planet X'): {planets}")

last_planet = planets.pop() # Removes and returns the last item
print(f"Popped item: {last_planet}")
print(f"List after pop(): {planets}")

del planets[0] # Deletes the item at index 0 ("Mercury")
print(f"After 'del planets[0]': {planets}")

# --- Other Useful Methods ---
planets_copy = planets.copy() # Create a shallow copy
planets_copy.sort() # Sorts the copy in-place
print(f"Sorted copy: {planets_copy}")

planets.reverse() # Reverses the original list in-place
print(f"Original list reversed: {planets}")

print(f"Count of 'Earth' in the list: {planets.count('Earth')}")
print(f"Index of 'Venus' in the list: {planets.index('Venus')}")
print("-" * 40)


# ------------------------------------------------------------------------------
# 4. Built-in Functions with Lists
# ------------------------------------------------------------------------------
print("--- 4. Built-in Functions ---")
scores = [95, 88, 72, 95, 100]
print(f"Scores: {scores}")

print(f"Number of scores (len): {len(scores)}")
print(f"Highest score (max): {max(scores)}")
print(f"Lowest score (min): {min(scores)}")
print(f"Sum of scores (sum): {sum(scores)}")

# 'sorted()' returns a new sorted list, leaving the original unchanged
sorted_scores = sorted(scores)
print(f"New sorted list (sorted()): {sorted_scores}")
print(f"Original scores list is unchanged: {scores}")
print("-" * 40)


# ------------------------------------------------------------------------------
# 5. Strategic Note: Mutability Demonstration
# ------------------------------------------------------------------------------
print("--- 5. Mutability Demonstration ---")

def modify_list(some_list):
    """This function modifies the list it receives."""
    print(f"  Inside function, received list: {some_list}")
    some_list.append(999) # This change will affect the original list
    print(f"  Inside function, list is now: {some_list}")

original_data = [10, 20, 30]
print(f"Before function call, original_data: {original_data}")

modify_list(original_data) # Pass the list to the function

print(f"After function call, original_data HAS CHANGED: {original_data}")

# ==============================================================================
# End of Module 03/Lists Examples
# ==============================================================================
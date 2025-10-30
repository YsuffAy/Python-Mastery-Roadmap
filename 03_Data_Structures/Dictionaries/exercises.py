# ==============================================================================
# Module 03: Data Structures / Dictionaries - Exercises
# ==============================================================================
# This file contains solved exercises to practice the concepts covered in the
# Dictionaries submodule, focusing on data modeling, lookups, and aggregation.
# ==============================================================================

# ------------------------------------------------------------------------------
# EXERCISE 1: Modeling Project Data
# ------------------------------------------------------------------------------
# Description: Use a dictionary to model the data for a project. Then, access,
#              update, and add new information to the project dictionary.
# This demonstrates using a dictionary to represent a structured object.
# Source: Self-created

print("--- Exercise 1: Modeling Project Data ---")

# 1. Create a dictionary to represent a TEKNOFEST project
teknofest_project = {
    "project_name": "Autonomous Drone Navigation System",
    "category": "Unmanned Aerial Vehicles",
    "team_members": ["Mert Ateş", "Nikola Tesla"],
    "status": "In Development"
}

print(f"Initial Project Data:\n{teknofest_project}\n")

# 2. Access and print the project's category
print(f"Project Category: {teknofest_project.get('category')}")

# 3. Update the status of the project
teknofest_project["status"] = "Testing Phase"
print(f"Updated Status: {teknofest_project['status']}")

# 4. Add a new team member to the team_members list
# Note: We access the list inside the dictionary and then use a list method.
teknofest_project["team_members"].append("Tony Stark")
print(f"Updated Team Members: {teknofest_project['team_members']}")

# Expected Output:
# Initial Project Data:
# {'project_name': 'Autonomous Drone Navigation System', 'category': 'Unmanned Aerial Vehicles', 'team_members': ['Mert Ateş', 'Nikola Tesla'], 'status': 'In Development'}
#
# Project Category: Unmanned Aerial Vehicles
# Updated Status: Testing Phase
# Updated Team Members: ['Mert Ateş', 'Nikola Tesla', 'Tony Stark']

print("-" * 40)


# ------------------------------------------------------------------------------
# EXERCISE 2: Aggregating Sales Data
# ------------------------------------------------------------------------------
# Description: You are given a list of sales records as (product, amount) tuples.
#              Calculate the total sales for each product.
# This demonstrates using a dictionary to aggregate (group and sum) data.
# Source: Self-created

print("--- Exercise 2: Aggregating Sales Data ---")
sales_data = [
    ("Laptop", 1500),
    ("Mouse", 25),
    ("Laptop", 1350),
    ("Keyboard", 75),
    ("Mouse", 30)
]

# Create an empty dictionary to store total sales per product
product_totals = {}

# Iterate through each sale record
for product, amount in sales_data:
    # Use .get(key, 0) to get the current total, or 0 if it's a new product.
    # Then add the new amount and update the dictionary.
    product_totals[product] = product_totals.get(product, 0) + amount

print(f"Sales Data: {sales_data}")
print(f"Total sales per product: {product_totals}")

# Expected Output:
# Sales Data: [('Laptop', 1500), ('Mouse', 25), ('Laptop', 1350), ('Keyboard', 75), ('Mouse', 30)]
# Total sales per product: {'Laptop': 2850, 'Mouse': 55, 'Keyboard': 75}

print("-" * 40)


# ------------------------------------------------------------------------------
# EXERCISE 3: Simple Status Code Translator
# ------------------------------------------------------------------------------
# Description: Create a dictionary that acts as a fast lookup table to translate
#              HTTP status codes into their meanings.
# This demonstrates using a dictionary for efficient lookups (like a switch-case).
# Source: Self-created

print("--- Exercise 3: Simple Status Code Translator ---")

http_status_codes = {
    200: "OK",
    301: "Moved Permanently",
    404: "Not Found",
    500: "Internal Server Error"
}

def translate_status(code):
    """Translates an HTTP status code to its meaning using the dictionary."""
    # Use .get() with a default value for codes that are not in our dictionary
    return http_status_codes.get(code, "Unknown Status Code")

# Test the function with known and unknown codes
code1 = 404
code2 = 200
code3 = 418 # An unknown code

print(f"The meaning of code {code1} is: '{translate_status(code1)}'")
print(f"The meaning of code {code2} is: '{translate_status(code2)}'")
print(f"The meaning of code {code3} is: '{translate_status(code3)}'")

# Expected Output:
# The meaning of code 404 is: 'Not Found'
# The meaning of code 200 is: 'OK'
# The meaning of code 418 is: 'Unknown Status Code'

print("-" * 40)

# ==============================================================================
# End of Module 03/Dictionaries Exercises
# ==============================================================================
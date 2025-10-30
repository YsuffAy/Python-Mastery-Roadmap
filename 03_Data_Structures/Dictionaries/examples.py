# ==============================================================================
# Module 03: Data Structures / Dictionaries - Code Examples
# ==============================================================================
# This file provides working examples for the concepts covered in the
# Dictionaries submodule README.md.
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Creating Dictionaries
# ------------------------------------------------------------------------------
print("--- 1. Creating Dictionaries ---")
# An empty dictionary
empty_dict = {}
print(f"Empty dictionary: {empty_dict}, type: {type(empty_dict)}")

# A dictionary for a simple profile
student_profile = {
    "name": "Nikola Tesla",
    "student_id": 1856,
    "major": "Electrical Engineering",
    "is_active": False
}
print(f"Student profile dictionary: {student_profile}")

# A dictionary with different key types (string, int, tuple)
mixed_key_dict = {
    "name": "Project Apollo",
    11: "First Moon Landing",
    (1969, 7, 20): "Landing Date"
}
print(f"Dictionary with mixed key types: {mixed_key_dict}")
print("-" * 40)


# ------------------------------------------------------------------------------
# 2. Accessing and Modifying Values
# ------------------------------------------------------------------------------
print("--- 2. Accessing and Modifying Values ---")
rocket = {
    "name": "Saturn V",
    "stages": 3,
    "height_meters": 111
}
print(f"Initial rocket data: {rocket}")

# --- Accessing Values ---
# Using square brackets (raises KeyError if key doesn't exist)
print(f"Rocket name: {rocket['name']}")

# Using .get() method (safe way, returns None if key doesn't exist)
thrust = rocket.get("thrust_kn")
print(f"Thrust value (key does not exist): {thrust}") # Output: None

# .get() with a default value
payload_capacity = rocket.get("payload_kg", "Not Specified")
print(f"Payload capacity: {payload_capacity}") # Output: Not Specified

# --- Adding or Updating Values ---
# Updating an existing value
rocket["height_meters"] = 110.6
print(f"Updated rocket data: {rocket}")

# Adding a new key-value pair
rocket["manufacturer"] = "Boeing / North American / Douglas"
print(f"Data after adding a new key: {rocket}")

# Using .update() to add/modify multiple items
rocket.update({"status": "Retired", "stages": 3.0})
print(f"Data after .update(): {rocket}")
print("-" * 40)


# ------------------------------------------------------------------------------
# 3. Deleting Items
# ------------------------------------------------------------------------------
print("--- 3. Deleting Items ---")
system_config = {
    "hostname": "server-01",
    "ip_address": "192.168.1.10",
    "port": 8080,
    "temp_key": "to be deleted"
}
print(f"Initial config: {system_config}")

# Using del
del system_config["port"]
print(f"Config after 'del system_config[\"port\"]': {system_config}")

# Using .pop() - removes the item and returns its value
removed_value = system_config.pop("temp_key")
print(f"Value of popped item 'temp_key': {removed_value}")
print(f"Config after pop(): {system_config}")

# Using .popitem() - removes the last inserted item (LIFO)
last_item = system_config.popitem()
print(f"Last item popped: {last_item}")
print(f"Config after popitem(): {system_config}")
print("-" * 40)


# ------------------------------------------------------------------------------
# 4. Iterating Over Dictionaries
# ------------------------------------------------------------------------------
print("--- 4. Iterating Over Dictionaries ---")
sensor_readings = {
    "temperature": 25.5,
    "humidity": 45.8,
    "pressure": 1013.25
}

# --- Iterating over keys (default behavior) ---
print("\nIterating over keys:")
for key in sensor_readings:
    # Use the key to access the value
    print(f"  Key: {key}, Value: {sensor_readings[key]}")

# --- Iterating over values ---
print("\nIterating over values:")
for value in sensor_readings.values():
    print(f"  Value: {value}")

# --- Iterating over key-value pairs (most common and powerful) ---
print("\nIterating over items (key, value pairs):")
for key, value in sensor_readings.items():
    print(f"  The {key} is {value}")
print("-" * 40)


# ------------------------------------------------------------------------------
# 5. Use Case: Frequency Counting
# ------------------------------------------------------------------------------
print("--- 5. Use Case: Frequency Counting ---")
data_stream = ['signal_A', 'signal_B', 'signal_A', 'signal_C', 'signal_B', 'signal_A']
frequency_counter = {}

for signal in data_stream:
    # .get(key, 0) returns 0 if the key is not found
    frequency_counter[signal] = frequency_counter.get(signal, 0) + 1

print(f"Data stream: {data_stream}")
print(f"Frequency of each signal: {frequency_counter}")
print("-" * 40)

# ==============================================================================
# End of Module 03/Dictionaries Examples
# ==============================================================================
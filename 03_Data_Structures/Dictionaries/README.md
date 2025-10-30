# Dictionaries

Dictionaries are one of the most flexible and widely used data structures in Python. They work like a real-world dictionary: you use a "key" (the word) to instantly access its corresponding "value" (the definition).

Instead of a simple ordered sequence, they store related data in **key-value pairs**.

## 1. Core Properties

* **Historically Unordered / Modernly Ordered:** In Python 3.7 and later, dictionaries maintain the insertion order of their items. However, their fundamental philosophy is to access items by key, not by index. Therefore, it's better to think of them as a "mapping" structure rather than relying on their order.
* **Mutable:** Key-value pairs can be added, modified, or deleted after the dictionary is created.
* **Key-Value Pairs:** Each element consists of two parts:
    * **Key:** A unique identifier used to access a value.
    * **Value:** The data associated with the key. Values can be duplicates.
* **Notation:** Defined by enclosing a comma-separated sequence of `key: value` pairs in curly braces `{}`.
    * `empty_dict = {}`
    * `student = {"name": "Ahmet", "age": 21, "major": "Engineering"}`

### Critical Rules (for Keys)

1.  **Keys Must Be Unique:** A dictionary cannot have two identical keys. If you add a new value with an existing key, the old value will be overwritten.
2.  **Keys Must Be Immutable:** Only **immutable** data types can be used as dictionary keys.
    * **Valid Key Types:** Numbers (`int`, `float`), Strings (`str`), Tuples (`tuple`).
    * **Invalid Key Types:** Lists (`list`), Sets (`set`), other Dictionaries (`dict`).

## 2. Accessing and Modifying Values

Items in dictionaries are accessed directly by their **keys**, **not** by an index number.

### 1. Accessing a Value
* **Method 1: Square Brackets `[]`**
    * `student["name"]` -> `"Ahmet"`
    * **Risk:** If the specified key does **not** exist in the dictionary, it raises a **`KeyError`** and crashes the program.

* **Method 2: The `.get()` Method (The Safe Way)**
    * `student.get("age")` -> `21`
    * **Advantage:** If the key does **not** exist, it **does not raise an error**; instead, it returns `None` by default.
    * You can provide a second argument to specify a default value to return if the key is not found:
        * `student.get("university", "Unknown")` -> `"Unknown"` (because the "university" key does not exist)

### 2. Adding or Updating a Value
The same syntax is used for changing the value of an existing key or adding a new key-value pair.

* `student["age"] = 22` (Updates the value of the existing "age" key)
* `student["student_id"] = 12345` (Adds a new "student_id" key and value)
* **The `.update()` Method:** Used to update a dictionary with the key-value pairs from another dictionary.
    * `student.update({"age": 23, "city": "Istanbul"})`

## 3. Deleting Items

* `del my_dict[key]`: Deletes the key-value pair with the specified key. Raises a `KeyError` if the key is not found.
    * `del student["major"]`
* `my_dict.pop(key)`: Removes the pair with the specified key and **returns its value.** This is useful when you want to use the value and then delete it. Raises an error if the key is not found (a default value can be provided).
    * `removed_age = student.pop("age")`
* `my_dict.popitem()`: Removes and returns the **last inserted** key-value pair as a tuple `(key, value)` (LIFO - Last-In, First-Out logic).
* `my_dict.clear()`: Deletes all content from the dictionary.

## 4. Iterating Over Dictionaries

There are several ways to loop through the contents of a dictionary.

* **Iterating Over Keys (Default):**
    ```python
    for key in student:
        print(key)
        # Output: "name", "age", "city"...
    ```
    * This is the same as iterating over `student.keys()`.

* **Iterating Over Values (`.values()`):**
    ```python
    for value in student.values():
        print(value)
        # Output: "Ahmet", 23, "Istanbul"...
    ```

* **Iterating Over Both Keys and Values (`.items()` - The Most Common and Powerful Method):**
    The `.items()` method returns each key-value pair as a `(key, value)` tuple. This is very useful in combination with "unpacking".
    ```python
    for key, value in student.items():
        print(f"{key}: {value}")
        # Output:
        # name: Ahmet
        # age: 23
        # city: Istanbul
    ```

## 5. Why and When to Use Dictionaries?

* **1. Fast Lookups:** This is the greatest strength of dictionaries. Accessing an element by its key is **orders of magnitude faster** than searching for that element in a list. This is because they use a "hash table" structure, similar to sets. Even with millions of items, access is nearly instantaneous.
* **2. Data Modeling:** They are perfect for modeling real-world objects or structures. Anything with "properties," such as a user, a product, or a configuration file, can be represented with a dictionary. The JSON format (the standard for data exchange on the web) is fundamentally based on dictionaries.
* **3. Flexible Data Storage:** Because keys are often strings and values can be lists, other dictionaries, or any data type, they allow for the creation of very complex and nested data structures.
* **4. Frequency Counting:** They are ideal for counting the occurrences of each element in a list.
    ```python
    letters = ['a', 'b', 'a', 'c', 'b', 'a']
    frequency = {}
    for letter in letters:
        frequency[letter] = frequency.get(letter, 0) + 1
    # Result: {'a': 3, 'b': 2, 'c': 1}
    ```
# 01 - Python Foundations

This module covers the most fundamental building blocks of the Python programming language. These are the first concepts that need to be understood before starting to write any Python code.

## 1. Basic Syntax & Comments

* **Syntax:** These are the rules of a programming language. In Python, these rules often resemble English words and are easy to read.
* **Indentation:** In Python, spaces (usually 4 spaces) are used to define code blocks (e.g., the body of an `if` statement or a function). This replaces the `{}` braces found in other languages and is **mandatory**. Incorrect indentation will cause errors.
* **Comments:** Used to explain what the code does or to temporarily disable a part of the code. They are ignored by the Python interpreter.
    * Single-line comments start with the `#` symbol.
    * Multi-line comments (often used for function or class documentation, called docstrings) are enclosed in triple quotes (`""" ... """` or `''' ... '''`).

## 2. Variables & Data Types

* **Variable:** A named "container" used to store a value (data) in memory. Creating a variable in Python simply requires giving it a name and assigning a value using the `=` operator.
    * `message = "Hello World"`
    * `age = 30`
* **Data Type:** Specifies the type of data a variable holds (e.g., number, text). Python is a **dynamically typed** language, meaning you don't explicitly declare the variable's type; Python automatically infers it when you assign a value.
    * **Basic Data Types:**
        * **String (`str`):** Sequences of characters enclosed in single (`'...'`) or double (`"..."`) quotes.
            * `name = "Ahmet"`
        * **Integer (`int`):** Whole numbers without a fractional part.
            * `count = 10`
        * **Float (`float`):** Numbers with a fractional part.
            * `pi_value = 3.14`
        * **Boolean (`bool`):** Can only hold two values: `True` or `False`. Heavily used in conditional statements.
            * `is_active = True`

## 3. Type Casting

Sometimes, it's necessary to convert one data type to another.

* `int(value)`: Converts the value to an integer.
    * `int("10")` -> `10` (numeric)
    * `int(3.14)` -> `3` (truncates the decimal part)
* `float(value)`: Converts the value to a float.
    * `float("3.14")` -> `3.14` (numeric)
    * `float(10)` -> `10.0`
* `str(value)`: Converts the value to a string.
    * `str(10)` -> `"10"` (text)
    * `str(True)` -> `"True"` (text)

## 4. Basic Input/Output (`print()`, `input()`)

* **`print()` Function:** Used to display values or the content of variables on the screen (console).
    * `print("Your age:", age)`
    * **f-string (Formatted String Literal):** The modern way to easily embed variables within strings. Start the string with `f` and place variables inside curly braces `{}`.
        * `print(f"Hello, {name}! Your age is {age}.")`
* **`input()` Function:** Used to get data (input) from the user via the keyboard. It **always returns a string**. If numerical operations are needed, type casting (`int()`, `float()`) must be performed.
    * `username = input("Please enter your name: ")`
    * `birth_year_str = input("Enter your birth year: ")`
    * `birth_year_int = int(birth_year_str)`
    * `current_age = 2025 - birth_year_int`
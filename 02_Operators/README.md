# 02 - Operators in Python

Operators are special symbols or keywords used to perform operations on variables and values. Python has several different types of operators.

## 1. Arithmetic Operators

These are used to perform basic mathematical operations.

* **`+` (Addition):** Adds two numbers.
    * `5 + 3` results in `8`
* **`-` (Subtraction):** Subtracts one number from another.
    * `5 - 3` results in `2`
* **`*` (Multiplication):** Multiplies two numbers.
    * `5 * 3` results in `15`
* **`/` (Division):** Divides one number by another and returns the result as a **float**.
    * `10 / 2` results in `5.0`
    * `7 / 2` results in `3.5`
* **`%` (Modulus / Remainder):** Returns the remainder of a division.
    * `10 % 3` results in `1` (the remainder when 10 is divided by 3 is 1)
    * `7 % 2` results in `1`
* **`**` (Exponentiation):** Raises a number to the power of another (left side is the base, right side is the exponent).
    * `2 ** 3` results in `8` (as in $2^3$)
* **`//` (Floor Division):** Divides one number by another and returns the **integer part** of the result (discards the fractional part).
    * `10 // 3` results in `3` (Normally 3.33... but the decimal is dropped)
    * `7 // 2` results in `3` (Normally 3.5 but the decimal is dropped)

## 2. Assignment Operators

These are used to assign values to variables. The most basic one is `=`. Others are shortcuts for performing an operation and assigning the result in one step.

* **`=` (Simple Assignment):** Assigns the value on the right to the variable on the left.
    * `x = 5`
* **`+=` (Add and Assign):** Adds the right value to the left variable's value and reassigns the result to the left variable.
    * `x += 3` is the same as `x = x + 3`
* **`-=` (Subtract and Assign):** `x -= 3` is the same as `x = x - 3`
* **`*=` (Multiply and Assign):** `x *= 3` is the same as `x = x * 3`
* **`/=` (Divide and Assign):** `x /= 3` is the same as `x = x / 3`
* **`%=` (Modulus and Assign):** `x %= 3` is the same as `x = x % 3`
* **`**=` (Exponentiate and Assign):** `x **= 3` is the same as `x = x ** 3`
* **`//=` (Floor Divide and Assign):** `x //= 3` is the same as `x = x // 3`

## 3. Comparison Operators

These are used to compare two values. They return a **Boolean** value (`True` or `False`) and are fundamental to conditional statements like `if`.

* **`==` (Is equal to?):** `True` if two values are equal, `False` otherwise.
    * `5 == 5` -> `True`
    * `5 == 3` -> `False`
* **`!=` (Is not equal to?):** `True` if two values are different, `False` if they are equal.
    * `5 != 3` -> `True`
    * `5 != 5` -> `False`
* **`>` (Is greater than?):** `True` if the left value is greater than the right one.
    * `5 > 3` -> `True`
* **`<` (Is less than?):** `True` if the left value is less than the right one.
    * `3 < 5` -> `True`
* **`>=` (Is greater than or equal to?):** `True` if the left value is greater than or equal to the right one.
    * `5 >= 5` -> `True`
    * `5 >= 3` -> `True`
* **`<=` (Is less than or equal to?):** `True` if the left value is less than or equal to the right one.
    * `3 <= 5` -> `True`
    * `5 <= 5` -> `True`

## 4. Logical Operators

These are used to operate on Boolean values (`True`, `False`) or to combine multiple conditions.

* **`and`:** Returns `True` only if both conditions are `True`, otherwise returns `False`.
    * `(5 > 3) and (2 < 4)` -> `True and True` -> `True`
    * `(5 > 3) and (2 > 4)` -> `True and False` -> `False`
* **`or`:** Returns `True` if at least one of the conditions is `True`, returns `False` only if both are `False`.
    * `(5 > 3) or (2 > 4)` -> `True or False` -> `True`
    * `(5 < 3) or (2 > 4)` -> `False or False` -> `False`
* **`not`:** Inverts a Boolean value. It makes `True` become `False`, and `False` become `True`.
    * `not (5 > 3)` -> `not True` -> `False`

## 5. Identity Operators

These check if two variables point to the **exact same object** in memory. This is different from `==`, which compares the *values* of the objects.

* **`is`:** Returns `True` if two variables are the same object.
    * `x = [1, 2]`
    * `y = x`
    * `z = [1, 2]`
    * `x is y` -> `True` (y points to the exact same list as x)
    * `x is z` -> `False` (x and z have the same values but are different list objects in memory)
    * `x == z` -> `True` (Their values are the same)
* **`is not`:** Returns `True` if two variables are different objects.
    * `x is not z` -> `True`

## 6. Membership Operators

These check if a value is present in a sequence (like a list, tuple, string, set, etc.).

* **`in`:** Returns `True` if the value is found in the sequence.
    * `my_list = [1, 2, 3]`
    * `2 in my_list` -> `True`
    * `5 in my_list` -> `False`
    * `"a" in "Merhaba"` -> `True`
* **`not in`:** Returns `True` if the value is not found in the sequence.
    * `5 not in my_list` -> `True`

# Tuples

Tuples are another built-in, ordered data structure in Python. They are very similar to lists, but with one **critical difference**: tuples are **immutable**. This means that once a tuple is created, its contents cannot be changed.

## 1. Core Properties

* **Ordered:** Items are stored in the order they were created, and each item has a specific index (just like lists).
* **Immutable:** The contents (adding, removing, or changing items) **cannot be modified** after creation. This is their most important characteristic.
* **Can Contain Different Data Types:** They can hold numbers, strings, lists, or even other tuples.
* **Allows Duplicate Members:** The same item can appear multiple times in a tuple.
* **Notation:** Defined by enclosing a comma-separated sequence of items in parentheses `()`.
    * `empty_tuple = ()`
    * `numbers = (1, 5, -2, 10)`
    * `single_item_tuple = (5,)` **Critical Note:** When creating a tuple with a single item, a trailing comma is mandatory. Otherwise, Python interprets it as a regular parenthesized expression (`(5)` is just the number 5).
    * Parenthesis-free definition is also possible (tuple packing): `my_tuple = 1, "two", 3.0`

## 2. Accessing Elements (Indexing and Slicing)

Since tuples are ordered, their elements can be accessed via indexing and slicing, just like lists.

* **Indexing:** Used to access a single item at a specific position (starts from 0, negative indexing works).
    * `colors = ("red", "blue", "green")`
    * `colors[0]` -> `"red"`
    * `colors[-1]` -> `"green"`

* **Slicing:** Used to get a subset of the tuple (as a new **tuple**) (`start:stop:step`).
    * `numbers = (0, 1, 2, 3, 4, 5)`
    * `numbers[1:4]` -> `(1, 2, 3)`

**The Most Important Difference:** Unlike lists, you **cannot change or delete** an item in a tuple using indexing or slicing. The following code will raise a `TypeError`:
```python
my_tuple = (1, 2, 3)
# my_tuple[0] = 5  # ERROR!
# del my_tuple[1]  # ERROR!
````

## 3\. Tuple Methods

Because tuples are immutable, they **do not have** methods that modify the content, such as `append`, `insert`, or `remove`, which are found on lists. They only have two basic methods for retrieving information:

  * `tuple.count(value)`: Counts how many times the specified `value` occurs in the tuple.
  * `tuple.index(value)`: Returns the index of the **first** occurrence of the specified `value`.

## 4\. Why Use Tuples? (Advantages Over Lists)

  * **Data Integrity:** Guarantees that a collection of data is not accidentally or intentionally **changed** during the program's execution. This makes the code safer and more predictable. For example, coordinate information `(x, y)` that a function should never alter should be stored as a tuple.
  * **Dictionary Keys:** Dictionary keys **must be immutable**. For this reason, lists cannot be used as dictionary keys, whereas tuples can.
      * `my_dict = {(1, 2): "value"}` -\> Valid
      * `# my_dict = {[1, 2]: "value"}` -\> Invalid (Raises TypeError)
  * **Performance:** Tuples are generally slightly **faster** and use **less memory** than lists. Python can apply optimizations because it knows the size of a tuple is fixed.

## 5\. Tuple Packing & Unpacking

This is a powerful feature frequently used in Python.

  * **Packing:** When we write comma-separated values, Python automatically creates a tuple.
      * `my_packed_tuple = 10, "Twenty", 30.0`
  * **Unpacking:** The process of assigning the items of a tuple to individual variables in sequence. The number of variables must **be the same** as the number of items in the tuple.
      * `coordinates = (3, 5)`
      * `x, y = coordinates` (Now the variable `x` holds 3, and `y` holds 5)
      * This feature is often used to return multiple values from a function.
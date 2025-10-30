# Lists

Lists are one of the most fundamental and versatile data structures in Python. We can think of a list as an **ordered** and **mutable** collection that can hold various types of items (numbers, strings, and even other lists).

## 1. Core Properties

* **Ordered:** Items are stored in the order you add them. Each item has a specific position (index).
* **Mutable:** You can change its content (add, remove, or modify items) after it has been created.
* **Can Contain Different Data Types:** A list can hold numbers, strings, and other lists all at the same time.
* **Allows Duplicate Members:** The same item can appear multiple times in a list.
* **Notation:** Defined by enclosing a comma-separated sequence of items in square brackets `[]`.
    * `empty_list = []`
    * `numbers = [1, 5, -2, 10]`
    * `mixed_list = [1, "Hello", 3.14, True, [10, 20]]`

## 2. Accessing Elements: Indexing & Slicing

Because lists are ordered, we can access their items using their positions (indexes).

* **Indexing:** Used to access a single item at a specific position.
    * **Rule:** Indexing starts from **0!** The first item in a list is at index 0.
    * **Negative Indexing:** Used to start from the end of the list. `-1` refers to the last item, `-2` to the second-to-last item, and so on.
    * *Example:* `colors = ["red", "blue", "green"]`
        * `colors[0]` -> `"red"`
        * `colors[1]` -> `"blue"`
        * `colors[-1]` -> `"green"`
        * `colors[-2]` -> `"blue"`

* **Slicing:** Used to get a subset of the list (as a new list).
    * **Notation:** `list[start:stop:step]`
    * **`start`:** The index where the slice begins (inclusive). If omitted, it defaults to the beginning (0).
    * **`stop`:** The index where the slice ends (**exclusive!**). If omitted, it goes to the very end.
    * **`step`:** The interval to skip (defaults to 1). Can be negative for reversing.
    * *Example:* `numbers = [0, 1, 2, 3, 4, 5, 6, 7]`
        * `numbers[2:5]` -> `[2, 3, 4]` (Starts at index 2, up to but not including index 5)
        * `numbers[:3]` -> `[0, 1, 2]` (From the beginning up to index 3)
        * `numbers[4:]` -> `[4, 5, 6, 7]` (From index 4 to the end)
        * `numbers[:]` -> Returns a full copy of the list.
        * `numbers[::2]` -> `[0, 2, 4, 6]` (From start to end, skipping every other item)
        * `numbers[::-1]` -> `[7, 6, 5, 4, 3, 2, 1, 0]` (Reverses the list)

## 3. List Methods: Modifying and Managing Lists

Since lists are mutable, they have many built-in methods for adding, removing, or sorting items. These methods often modify the list **in-place** (meaning they don't create a new list).

* **Adding Items:**
    * `list.append(item)`: Adds an item to the **end** of the list.
    * `list.insert(index, item)`: Inserts an item at the specified **index**, shifting other items to the right.
    * `list.extend(other_list)`: Appends all the items from another list (or any other iterable) to the end of the current list. (The `+` operator does a similar job but creates a new list).

* **Removing Items:**
    * `list.remove(value)`: Removes the **first** item from the list with the specified `value`. Raises an error if the value is not found.
    * `list.pop(index=-1)`: Removes and **returns** the item at the specified index. If no index is specified, it removes and returns the **last** item by default.
    * `del list[index]`: Removes the item at the specified index (returns nothing). Can also be used with slicing (`del list[2:4]`).
    * `list.clear()`: Removes all items from the list, making it an empty list.

* **Other Useful Methods:**
    * `list.index(value)`: Returns the index of the **first** item with the specified `value`. Raises an error if the value is not found.
    * `list.count(value)`: Returns the number of times the specified `value` appears in the list.
    * `list.sort()`: Sorts the list **in-place** (numerically or alphabetically).
    * `list.reverse()`: Reverses the order of the elements in the list **in-place**.
    * `list.copy()`: Returns a **shallow copy** of the list. This is important for working on a copy without modifying the original. (Slicing with `new_list = old_list[:]` does the same thing).

## 4. Built-in Functions with Lists

* `len(list)`: Returns the number of items (length) in the list.
* `min(list)`: Returns the smallest item in the list (items must be comparable).
* `max(list)`: Returns the largest item in the list.
* `sum(list)`: Returns the sum of all numeric items in the list.
* `sorted(list)`: Returns a **new sorted copy** of the list (does not modify the original list).

## 5. Strategic Notes

* Lists are the most common data structure you will encounter in Python. A deep understanding of their methods and indexing/slicing logic is critical.
* Paying attention to whether a method modifies a list "in-place" or "returns a new list" is crucial for preventing unexpected bugs (e.g., `sort()` vs `sorted()`).
* The mutability of lists provides flexibility but also carries the risk of the list's content being unintentionally changed later in the program (especially when passed as an argument to functions).
# Sets

Sets are an **unordered** data structure in Python that contain only **unique** elements. They are a direct implementation of the mathematical concept of a set. You can think of a set like a bag where you throw in objects; each object can only be in the bag once, and they don't have a specific order inside.

## 1. Core Properties

* **Unordered:** Items are not kept in any particular order as they are added. Therefore, sets **cannot be accessed** using an index or slicing.
* **Unique Elements:** A set **does not allow** duplicate items. If you try to add an item that already exists, nothing happens.
* **Mutable:** Sets are mutable, meaning you can add or remove elements after the set has been created.
* **Items Must Be Immutable:** A set can only contain immutable data types (such as numbers, strings, and tuples). You **cannot** put mutable items like lists or other sets inside a set.
* **Notation:** Defined by enclosing a comma-separated sequence of items in curly braces `{}`.
    * `numbers = {1, 2, 3, 4, 4, 2}` -> Result: `{1, 2, 3, 4}` (Duplicates are automatically removed)
    * `letters = {"a", "b", "c"}`
* **Critical Note (Empty Set):** You **cannot** use `{}` to create an empty set, as this creates an empty dictionary. To create an empty set, you must use the `set()` function.
    * `empty_set = set()`

## 2. Key Differences from Lists/Tuples

| Property        | List `[]`     | Tuple `()`       | Set `{}`          |
| :-------------- | :------------ | :--------------- | :---------------- |
| **Ordering** | Ordered       | Ordered          | **Unordered** |
| **Mutability** | Mutable       | **Immutable** | Mutable           |
| **Duplicates** | Allows        | Allows           | **Does not allow**|
| **Indexing** | Yes           | Yes              | **No** |

## 3. Set Methods: Managing the Set

* **Adding Elements:**
    * `set.add(item)`: Adds a single item to the set. If the item is already present, it does nothing.
    * `set.update(other_set_or_list)`: Adds all items from another set, list, or other iterable to the set.

* **Removing Elements:**
    * `set.remove(value)`: Removes the specified `value` from the set. Raises a **`KeyError`** if the value is **not** found.
    * `set.discard(value)`: Removes the specified `value` from the set. If the value is **not** found, it does nothing and **does not raise an error.** This is the life-saving difference between it and `remove`.
    * `set.pop()`: Removes and returns an **arbitrary** element from the set. Since sets are unordered, you cannot know which element will be popped.
    * `set.clear()`: Removes all elements from the set.

## 4. Mathematical Set Operations (The Strategic Advantage)

The real power of sets is their ability to perform mathematical set operations very efficiently. (See: `[[07_Kumeler.md]]`)

For sets `A = {1, 2, 3, 4}` and `B = {3, 4, 5, 6}`:

* **Union:** Creates a new set containing all unique elements from both sets.
    * **Operator:** `A | B` -> `{1, 2, 3, 4, 5, 6}`
    * **Method:** `A.union(B)`

* **Intersection:** Creates a new set containing only the elements that are common to both sets.
    * **Operator:** `A & B` -> `{3, 4}`
    * **Method:** `A.intersection(B)`

* **Difference:** Creates a new set containing elements that are in the first set but not in the second set.
    * **Operator:** `A - B` -> `{1, 2}`
    * **Method:** `A.difference(B)`
    * (Note: `B - A` would result in `{5, 6}`)

* **Symmetric Difference:** Creates a new set containing elements that are in either set, but not in their intersection (only in A or only in B).
    * **Operator:** `A ^ B` -> `{1, 2, 5, 6}`
    * **Method:** `A.symmetric_difference(B)`

## 5. Why and When to Use Sets?

* **1. Removing Duplicates (Most Common Use):** The fastest and most "Pythonic" way to remove duplicate elements from a list is to convert it to a set and then back to a list.
    * `my_list = [1, 2, 2, 3, 4, 4, 4]`
    * `unique_list = list(set(my_list))` -> `[1, 2, 3, 4]`

* **2. Fast Membership Testing:** Checking if an element exists in a collection is **much faster** in sets than in lists. This is because sets store data in a special structure called a "hash table". If you are querying for the existence of an item in a collection with thousands or millions of elements, using a set will dramatically speed up your program.
    * The operation `element in my_set` is much more efficient than `element in my_list`.

* **3. Mathematical Operations:** If you need to perform mathematical operations like finding common elements, differences, or unions between two collections, sets are the right tool designed for the job.
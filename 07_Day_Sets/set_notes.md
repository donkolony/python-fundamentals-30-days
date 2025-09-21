# Set Properties

- **Unordered** → No guaranteed order of elements (not chronological)
- **Un-indexed** → Elements cannot be accessed by index
- **Unique elements only** → Duplicates are not allowed

---

# Common Operations

- `len(set)` → Return the number of elements
- `in` operator → Check if an item exists in the set

---

# Set Methods

## 🟢 Methods that **modify the set (in place)**

- `add(item)` → Add a single item
- `update(iterable)` → Add multiple items or combine with another set (changes the original set)
- `remove(item)` → Remove item (raises **error** if not found)
- `discard(item)` → Remove item (does **not raise error** if not found)
- `pop()` → Remove and return a random item (no arguments)
- `clear()` → Empty the set
- `del set_name` → Delete the entire set object

---

## 🔵 Methods that **return a new set**

- `union(other_set)` → Combine sets (no duplicates). Returns a **new set**.
- `intersection(other_set)` → Common elements between sets. Returns a **new set**.
- `difference(other_set)` → Elements in current set but not in the other. Returns a **new set**.
- `symmetric_difference(other_set)` → Elements not shared between sets. Returns a **new set**.

---

## 🟣 Methods that **return information**

- `issubset(other_set)` → Returns `True` if current set is inside another
- `issuperset(other_set)` → Returns `True` if current set contains another
- `isdisjoint(other_set)` → Returns `True` if two sets have no elements in common

---

# Quick Tip

- ✅ Use `union()`, `intersection()`, `difference()`, etc. when you need **a new set**.
- ✅ Use `update()`, `add()`, `remove()` when you want to **change the existing set**.
- ⚠️ Sets are unordered → you cannot rely on the position of elements.

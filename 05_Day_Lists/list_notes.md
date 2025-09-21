# List Properties

- **Ordered** → Elements maintain insertion order
- **Mutable** → Elements can be changed after creation
- **Allow duplicates** → Same value can appear multiple times
- **Allow multiple data types** → (e.g., `str`, `int`, `float`, `dict`, etc.)

---

# Indexing & Slicing

- Access single item: `list[index]`
- Slice: `list[start:end:step]`

---

# List Methods

## 🟢 Methods that **modify the list**

- `append(item)` → Add item at the end
- `insert(index, item)` → Add item at a specific index
- `remove(item)` → Remove the first occurrence of item
- `pop(index)` → Remove item at specified index (or last item if index not provided)
- `del list_name[index]` → Delete item at index (or entire list if no index)
- `clear()` → Empty the list
- `extend(iterable)` → Append all elements from another list/iterable
- `reverse()` → Reverse the list in place
- `sort(reverse=False)` → Sort list in place (default ascending, `reverse=True` for descending)

---

## 🔵 Methods that **do not modify the list**

- `copy()` → Return a shallow copy of the list
- `count(item)` → Return number of times an item appears
- `index(item)` → Return index of the first occurrence of item
- `sorted(list, reverse=False)` → Return a **new sorted list** (original unchanged)
- `+` (plus operator) → Concatenate two lists and return a new one

---

# Quick Tip

- ✅ Use `sorted()` when you want to keep the original list intact/unchanged. Create a new list
- ✅ Use `sort()` when you want to update the list itself. Changes the original list

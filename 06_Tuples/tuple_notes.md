# Tuple Properties

- **Ordered** → Elements maintain insertion order
- **Immutable** → Cannot be changed after creation
- **Allow duplicates** → Same value can appear multiple times

---

# Indexing & Slicing

- Access single item: `tuple[index]`
- Slice: `tuple[start:end:step]`

---

# Tuple Methods & Operations

## 🔵 Methods that **return information (not a tuple)**

- `count(item)` → Return the number of times an item appears (**integer**)
- `index(item)` → Return the index of the first occurrence (**integer**)

---

## 🟢 Operations that **create a new tuple**

- `+` (concatenation) → Join two or more tuples into a new tuple

---

## 🔴 Operations that **remove the entire tuple**

- `del tuple_name` → Delete the entire tuple object from memory  
  _(⚠️ You cannot delete individual items, since tuples are immutable)_

---

# Quick Tip

- Tuples are like “read-only lists”: you can look at them and combine them, but you **cannot modify individual elements**.

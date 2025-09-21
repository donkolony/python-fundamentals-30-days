# Dictionary Properties

- **Collection of key:value pairs**
- **Unordered** (insertion order preserved since Python 3.7, but not indexed)
- **Mutable** → can be changed after creation
- **Unique keys** → duplicate keys are not allowed (values can repeat)

---

# Common Operations

- `len(dict)` → Return number of key:value pairs

---

# Dictionary Methods

## 🟢 Methods that **modify the dictionary (in place)**

- `update({key:value})` → Add or update key:value pairs
- `pop(key)` → Remove the item with the specified key and return its value
- `popitem()` → Remove and return the **last inserted item** (key, value)
- `clear()` → Remove all items
- `del dict_name[key]` → Delete the item with the specified key
- `del dict_name` → Delete the entire dictionary

---

## 🔵 Methods that **return a new dictionary / view**

- `copy()` → Return a shallow copy (useful to avoid changing the original)
- `keys()` → Return a view object of dictionary keys
- `values()` → Return a view object of dictionary values
- `items()` → Return a view object of dictionary key:value pairs (as tuples)

---

# Accessing Dictionary Items

- `dict["key"]` → Access value by key (❌ raises **KeyError** if key doesn’t exist)
- `dict.get("key")` → Access value by key (✅ returns `None` if key doesn’t exist — safe method)

---

# Adding Items to a Dictionary

- Add new key:value pairs:
  ```python
  dct["new_key"] = "new_value"
  dct.update({"keyName": "valueName"})
  ```

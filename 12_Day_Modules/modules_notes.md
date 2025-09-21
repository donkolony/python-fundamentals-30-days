# What is a Module

# Creating a Module

# Import Functions from a Module

# Import Functions from a Module and Renaming

# Import Built-in Modules

- Common built-in modules
  - math
  - datetime
  - os
  - sys
  - random
  - statistic
  - collections
  - json
  - re

# OS Module

- perform operating system tasks
- functions to create, change current working dir, removing a dir, fetching its contents, changing and identifying the current dir

# Sys Module

# Statistics Module

- mean
- median
- mode
- stdev (standard deviation)

# Math Module

- pi
- sqrt (square root)
- pow
- floor (always round down)
- ceil (always round up)
- log10

# String Module

- `ascii_letters` → abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ (both lower and upper letters of the alphabet)
- `ascii_lowercase` → abcdefghijklmnopqrstuvwxyz (only lower letters of the alphabet)
- `ascii_uppercase` → ABCDEFGHIJKLMNOPQRSTUVWXYZ (only upper letters of the alphabet)
- `digits` → 0123456789
- `hexdigits` → 0123456789abcdefABCDEF

# 🎲 Random Module

The `random` module offers several methods for generating random values or making random selections from sequences such as:

- Lists
- Tuples
- Strings

## Commonly Used Methods

- `choices(sequence)` [returns a single, random element from the sequence]
  - choices[population, weights=None, cum-weights=None, k=1]
- `shuffle` → accepts a sequence and modifies the sequence
- `sample` → accepts a sequence and does not modify the sequence, keeping the original intact. Requires 2 args. sample(sequence, k), where k is the size of the returned list
- `randint` → accepts two parameters and returns a random number between the two given range, both lower and upper values are inclusive (3, 9)
- `randrange` → same as _randint_, but here the upper value is exclusive (3, 9). 9 will never be included in the random selection

👉 Rule of thumb:

- Use `shuffle()` if you’re okay with modifying the list itself.
- Use `sample()` if you want a shuffled copy while keeping the original list safe.

👉 Rule of thumb:

- Use `choices` → duplicates allowed
- Use `sample` → unique values only

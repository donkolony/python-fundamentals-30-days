# link: https: // youtu.be/DUnY6l482Lk


########## Example 1 ##########
# Method 1: For Loop
# nums = [1, 2, 3, 4, 5]

# nums_squared = []
# for num in nums:
#     square = num**2
#     nums_squared.append(square)

# print(nums_squared)

# Method 1: List Comprehension
"""
[Part 1, Part 2, Part 3] = [operation, for var in, existing/original_list]
- Work backwards
- Part 3: existing list
- Part 2: for var in
- Part 1: operation
"""
# nums_squared = [num**2 for num in nums]
# print(nums_squared)

########## Example 2 ##########


import time
tv_shows = ["friends", "PARKS AND RECREATION",
            "the Office", "30 rock", "modern FAMILY"]

# Method 1: For Loop
# tv_shows_cap = []
# for show in tv_shows:
#     show_cap = show.title()
#     tv_shows_cap.append(show_cap)

# print(tv_shows_cap)

# Method 2: List Comprehension
# tv_shows_cap = [show.title() for show in tv_shows]
# print(tv_shows_cap)


"""Working with Conditions"""
# Method 1: For Loop (same as prev. example)
# tv_shows_cap = []
# for show in tv_shows:
#     if len(show) >= 10:
#         show_cap = show.title()
#         tv_shows_cap.append(show_cap)

# print(f"For Loop With Condition: {tv_shows_cap}")

# Method 2: List Comprehension (same as prev. example)
# tv_shows_cap = [show.title() for show in tv_shows if len(show) >= 10]
# print(tv_shows_cap)

"""Generate a List From Scratch"""
# Squaring numbers inside a list without manually creating a list
# square = [n**2 for n in range(1, 11)]
# print(square)

"""Speed Comparison: For Loop vs List Comprehension"""
# Method 1: For Loop Run Time
start = time.time()
squares = []
for n in range(1, 100000001):
    squares.append(n**2)
end = time.time()

print(f"For Loop + append run time: {end - start}")

# Method 2: List Comprehension Run Time
# start = time.time()
# [n**2 for n in range(1, 100000001)]
# end = time.time()
# print(f"List Comprehension rum time: {end - start}")

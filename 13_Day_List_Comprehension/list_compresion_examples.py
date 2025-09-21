"""Example 1: If we want to change a string to a list of characters. You can use a couple of methods"""

# Method 1: Using The Built-in List Function
language = 'Python'
# lst = list(language)
# print(type(language))
# print(lst)
# print(type(lst))

# Method 2: Using For Loop
lst = []
for lang in language:
    lst.append(lang)
# print(lst)

# Method 3: Using List Comprehension
lst = [lang for lang in language]
# print(lst)
# print(type(lst))

"""Example 2: Generating a List Of Numbers With Operations"""
# Generating numbers
numbers = [i for i in range(11)]
# print(numbers)

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
# print(squares)

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
# print(numbers)

"""Example 3: List Comprehension With Condition Statement"""
# Generating even numbers
# to generate even numbers list in range 0 to 21
even_numbers = [i for i in range(21) if i % 2 == 0]
# print(even_numbers)

# Generating odd numbers
# to generate odd numbers in range 0 to 21
odd_numbers = [i for i in range(21) if i % 2 != 0]
# print(odd_numbers)

# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
# print(positive_even_numbers)

# Flattening a three dimensional array: List Comp
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
# print(flattened_list)

# Flattening a three dimensional array: For Loop
flat_list = []
for i in list_of_lists:
    for y in i:
        flat_list.append(y)

# print(flat_list)

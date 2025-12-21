numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [num for num in numbers if num % 2 == 0 and num > 0]

# Flattening a 3D array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened_list_fl = []
for row in list_of_lists:
    for col in row:
        flattened_list_fl.append(col)

print(f"Flattened List Using For Loop: {flattened_list_fl}")

flattened_list_lc = [col for row in list_of_lists for col in row]
print(f"Flattened List Using List Comprehension:{flattened_list_lc}")


def power(x):
    return lambda y: x ** y


print(power(2)(3))

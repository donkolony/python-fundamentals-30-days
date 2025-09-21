# 💻 Exercises: Day 12

########## Exercises: Level 1 ##########
# 1
import random
from string import *
from random import *


def random_user_id(random):
    user_id = ("".join(choices(ascii_letters + digits, k=random)))

    return user_id


# print(random_user_id(5))
# print(random_user_id(6))
# print(random_user_id(8))

# 2


def user_id_gen_by_user():
    num_of_char = int(input("enter number of characters: "))
    num_of_ids = int(input("enter number of IDs: "))

    generated_ids = []

    for _ in range(num_of_ids):
        user_id = ''.join(choices(ascii_letters + digits,  k=num_of_char))
        generated_ids.append(user_id)

    # print(generated_ids)
    return generated_ids


# print(user_id_gen_by_user())


# 3
def rgb_color_gen():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb = f"rgb({r}, {g}, {b})"

    return rgb


# print(rgb_color_gen())


########## Exercises: Level 2 ##########
# 1
def list_of_hexa_colors(n=1):
    hexa_colors = []

    for _ in range(n):
        hexa = "".join(choices(hexdigits, k=6))
        hexa_colors.append(f"#{hexa}")

    return hexa_colors


# print(list_of_hexa_colors(3))
# print(list_of_hexa_colors(5))
# print(list_of_hexa_colors(8))

# 2
def list_of_rgb_colors(n=1):
    rgb_colors = []

    for _ in range(n):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        rgb = f"rgb{(r, g, b)}"
        rgb_colors.append(rgb)

    return rgb_colors


# print(list_of_rgb_colors(2))
# print(list_of_rgb_colors(4))
# print(list_of_rgb_colors(6))


# 3
# Method 1: Accepting a string name "hexa" or "rgb"

def generate_colors(color_type, n=1):
    if color_type == "hexa":
        return list_of_hexa_colors(n)
    elif color_type == "rgb":
        return list_of_rgb_colors(n)
    else:
        return "Invalid color type. Choose 'hexa' or 'rgb'"


# print(generate_colors("hexa", 3))
# print(generate_colors("hexa", 1))
# print(generate_colors("hexa"))
# print(generate_colors("don", 2))
# print(generate_colors("rgb", 3))
# print(generate_colors("rgb", 1))
# print(generate_colors("rgb"))
# print(generate_colors("don", 2))

# Method 2: Accepting a function as a parameter
def generate_colors(func, n=1):
    return func(n)


# print(generate_colors(list_of_hexa_colors, 3))
# print(generate_colors(list_of_hexa_colors))
# print(generate_colors(list_of_rgb_colors, 3))
# print(generate_colors(list_of_rgb_colors))


########## Exercises: Level 3 ##########
# 1
def shuffle_list(n):
    shuffle(n)
    return n


# print(shuffle_list([2, 5, 6, 2, 5, 6]))
# print(shuffle_list(["banana", "watermelon", "mango", "grapes"]))
# print(shuffle_list(["don", "peso", "lyle", "cuppuccino"]))


# 2
_chocies = choices(range(10), k=7)  # allows duplicates
_sample = sample(range(10), 7)  # does not allow duplicates
# print(_chocies)
# print(_sample)


def seven_random_numbers():
    return sample(range(10), 7)


# print(seven_random_numbers())

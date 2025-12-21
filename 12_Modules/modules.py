import random
import string


"""Day 12: Modules"""

# Exercises: Day 12


print("--------------------------------------")
print("Exercises: Level 1")
print("--------------------------------------")


# 1.1 Writ a function which generates a six digit/character random_user_id.
print("\nQuestion 1.1")


def random_user_id() -> str:
    ids = string.ascii_letters + string.digits
    return "".join(random.sample(ids, k=6))


print(random_user_id())

"""
# 1.2 Modify the previous task. Declare a function named user_id_gen_by_user.
It doesn't take any parameters but it takes two inputs using input().
One of the inputs is the number of characters and the second input is the
number of IDs which are supposed to be generated.
"""
print("\nQuestion 1.2")


def user_id_gen_by_user():
    num_of_char = int(input("Enter number of characters: "))
    num_of_ids = int(input("Enter number of ids: "))

    for _ in range(num_of_ids):
        print("".join(random.sample(string.ascii_letters +
                                    string.digits, k=num_of_char)))


# user_id_gen_by_user()

# 1.3 Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
print("\nQuestion 1.3")


def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return f"rgb({r}, {g}, {b})"


print(rgb_color_gen())


print("\n--------------------------------------")
print("Exercises: Level 2")
print("--------------------------------------")

"""
# 2.1 Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after 
# #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
"""
print("\nQuestion 2.1")


def list_of_hexa_colors(n):
    hexa = []
    for _ in range(n):
        hexa.append(f"#{"".join(random.choices("0123456789ABCDEF", k=6))}")

    return hexa


""" REFACTOR """


def list_of_hexa_colors(n):

    return ["#" + ''.join(random.choices("0123456789ABCDEF", k=6)) for _ in range(n)]


print(list_of_hexa_colors(3))


# 2.2 Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
print("\nQuestion 2.2")


def list_of_rgb_colors(n):
    rgb = []
    for _ in range(n):
        rgb.append(
            f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})")

    return rgb


""" REFACTOR """


def list_of_rgb_colors(n):
    return [f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})" for _ in range(n)]


print(list_of_rgb_colors(3))


"""
# 2.3 Write a function generate_colors which can generate any number of hexa or rgb colors.
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
"""
print("\nQuestion 2.3")


def generate_colors(f, n):
    f = f.lower()
    if f == "hexa":
        return list_of_hexa_colors(n)
    elif f == "rgb":
        return list_of_rgb_colors(n)
    else:
        raise ValueError("Color type must be 'hexa' or 'rgb'")


""" REFACTOR """


def generate_colors(color_type, n):
    color_type = color_type.lower()
    if color_type == "hexa":
        return ["#" + ''.join(random.choices("0123456789ABCDEF", k=6)) for _ in range(n)]
    elif color_type == "rgb":
        return [f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})" for _ in range(n)]
    else:
        raise ValueError("color_type must be 'hexa' or 'rgb'")


print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))


print("\n--------------------------------------")
print("Exercises: Level 3")
print("--------------------------------------")


# 3.1 Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
print("\nQuestion 3.1")


def shuffle_list(lst: list) -> list:
    return random.sample(lst, len(lst))


print(shuffle_list([1, 2, 3, 4, 5]))
print(shuffle_list(['a', 'b', 'c', 'd', 'e']))


# 3.2 Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
print("\nQuestion 3.2")


def random_unique_numbers() -> list[int]:
    return random.sample(range(10), k=7)


print(random_unique_numbers())

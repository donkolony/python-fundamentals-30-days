# 💻 Exercises: Day 13

# 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

negative_nums = [num for num in numbers if num <= 0]
# print(negative_nums)

neg_num = []
for num in numbers:
    if num <= 0:
        neg_num.append(num)

# print(neg_num)

negative_nums2 = list(filter(lambda num: num <= 0, numbers))
# print(negative_nums2)

# 2
# list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

# flattened_list = [z for i in list_of_lists for y in i for z in y]
# print(f"List comprehension: {flattened_list}")

# my_list = []
# for i in list_of_lists:
#     # print(i)
#     for y in i:
#         # print(y)
#         for z in y:
#             # print(z)
#             my_list.append(z)

# print(f"Normal Loop: {my_list}")

3
my_test = [(0, 1, 0, 0, 0, 0, 0),
           (1, 1, 1, 1, 1, 1, 1),
           (2, 1, 2, 4, 8, 16, 32),
           (3, 1, 3, 9, 27, 81, 243),
           (4, 1, 4, 16, 64, 256, 1024),
           (5, 1, 5, 25, 125, 625, 3125),
           (6, 1, 6, 36, 216, 1296, 7776),
           (7, 1, 7, 49, 343, 2401, 16807),
           (8, 1, 8, 64, 512, 4096, 32768),
           (9, 1, 9, 81, 729, 6561, 59049),
           (10, 1, 10, 100, 1000, 10000, 100000)]

tup = [(n, 1, n, n**2, n**3, n**4, n**5) for n in range(11)]
# print(tup)
# print(tup == my_test)


new_tup = []
for n in range(11):
    x = (n, 1, n, n**2, n**3, n**4, n**5)
    new_tup.append(x)

# print(new_tup)
# print(my_test == new_tup)


# 4
countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# new_countries = [[name.upper(), name[:3].upper(), capital.upper()]
#                  for country in countries for name, capital in country]

# print(new_countries)


# new_count = []
# for country in countries:
#     name, capital = country[0]
#     # print(name)
#     # print(capital)
#     # print(country)
#     abbr = name[:3]
#     new_count.append([name.upper(), abbr.upper(), capital.upper()])

# print(new_count)

# 5
# new_countries = [{"country": name.upper(), "city": capital.upper()}
#                  for country in countries for name, capital in country]

# print(new_countries)


# tup_list = [('Finland', 'Helsinki')]
# # Destructing the list of tuple(s)
# name, cap = tup_list[0]
# print(name)
# print(cap)

# new_count = []
# for country in countries:
#     name, capital = country[0]
#     dct = {"country": name.upper(), "city": capital.upper()}
#     new_count.append(dct)

# print(new_count)


# 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],
         [('Donald', 'Trump')], [('Bill', 'Gates')]]

# new_names = [name + " " +
#              surname for inner in names for name, surname in inner]

# print(new_names)

# new_lst = []
# tup_list = [('Asabeneh', 'Yetayeh')]
# name, surname = tup_list[0]
# new_lst.append(f"{name} {surname}")
# print(new_lst)

# new_names = []
# for name in names:
#     name, surname = name[0]
#     # new_names.append(name + " " + surname)
#     new_names.append(f"{name} {surname}")

# print(new_names)

# 7


def slope_or_y_intercept(calc_type, x, y):
    nominator = y[1] - x[1]
    denominator = y[0] - x[0]

    if denominator == 0:
        raise ValueError("Slope is undefined for vertical line")

    slope = nominator / denominator
    y_intercept = x[1] - slope * x[0]

    if calc_type == "slope":
        return slope
    elif calc_type == "y-intercept":
        return y_intercept
    else:
        raise ValueError("calc_type must be 'slope' or y-intercept")


# print(slope_or_y_intercept("slope", (10, 2), (-9, 7)))
# print(slope_or_y_intercept("y-intercept", (10, 2), (-9, 7)))
# print(slope_or_y_intercept("slope", (-16, 11), (-19, -12)))
# print(slope_or_y_intercept("y-intercept", (-16, 11), (-19, -12)))
# print(slope_or_y_intercept("test", (-16, 11), (-19, -12)))


"""
slope_or_intercept = lambda calc_type, x, y: (
    (y[1] - x[1]) / (y[0] - x[0])
    if calc_type == "slope"
    else y[1] - ((y[1] - x[1]) / (y[0] - x[0])) * y[0]
)
"""

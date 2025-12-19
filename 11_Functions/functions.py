from countries_data import countries_data

"""Day 11: Functions"""

# Exercises: Day 11


print("--------------------------------------")
print("Exercises: Level 1")
print("--------------------------------------")


# 1 Declare a function add_two_numbers. It takes two parameters and it returns a sum.
print("\nQuestion 1")


def add_two_numbers(num1, num2):
    return num1 + num2


print(add_two_numbers(2, 2))

# 2 Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
print("\nQuestion 2")


def area_of_circle(r):
    return 3.14 * r * r


print(area_of_circle(10))


# 3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
print("\nQuestion 3")


def add_all_nums(*args):
    for i in args:
        if not isinstance(i, (int, float)):
            return "Error"

    return sum(args)


print(add_all_nums(-5, 10))
print(add_all_nums(-5, -10))
print(add_all_nums("5", 5))

# 4 Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
print("\nQuestion 4")


def convert_celsius_to_fahrenheit(c):

    return f"{(c * 9/5) + 32} fahrenheit degrees"


print(convert_celsius_to_fahrenheit(30))

# 5 Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
print("\nQuestion 5")


def check_season(month):

    season = {
        "January": "Winter",
        "February": "Winter",
        "March": "Spring",
        "April": "Spring",
        "May": "Spring",
        "June": "Summer",
        "July": "Summer",
        "August": "Summer",
        "September": "Autumn",
        "October": "Autumn",
        "November": "Autumn",
        "December": "Winter",
    }

    return season.get(month.capitalize())


print(check_season("december"))


# 6 Write a function called calculate_slope which return the slope of a linear equation
print("\nQuestion 6")


def calculate_slope(point1, point2):

    return (point2[1] - point1[1]) / (point2[0] - point1[0])


print(calculate_slope((2, 3), (-4, 6)))

# 7 Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
print("\nQuestion 7")


def solve_quadratic_eqn(a, b, c):
    square_root = (b**2 - (4 * a * c)) ** 0.5
    denominator = 2 * a

    if square_root < 0:
        return "No Real Roots"

    x1 = round((-b + square_root) / denominator, 2)
    x2 = round((-b - square_root) / denominator, 2)

    print(square_root)
    print(denominator)

    return (x1, x2)


print(solve_quadratic_eqn(2, 3, -4))


# 8 Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
print("\nQuestion 8")


def print_list(items):
    for item in items:
        print(item)


print_list([2, 3, 4])
print_list(["Don", "Peso", "Lyle"])


# 9 Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
print("\nQuestion 9")


# def reverse_list(arr):
#     reverse = []
#     for i in arr[::-1]:
#         reverse.append(i)

#     return reverse

def reverse_list(arr):

    return [i for i in arr[::-1]]


print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))


# 10 Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
print("\nQuestion 10")


def capitalize_list_items(arr):

    return [i.capitalize() for i in arr]


print(capitalize_list_items(['potato', 'tomato', 'mango', 'milk']))
print(capitalize_list_items(["a", "b", "c", "d"]))

# 11 Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
print("\nQuestion 11")


def add_item(arr, item):
    arr.append(item)
    return arr


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]
print(add_item(food_staff, "Meat"))
print(add_item(numbers, 5))

# 12 Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
print("\nQuestion 12")


def remove_item(arr, item):
    arr.remove(item)
    return arr


print(remove_item(food_staff, "Mango"))
print(remove_item(numbers, 3))


# 13 Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
print("\nQuestion 13")


def sum_of_numbers(num):

    return sum(range(num + 1))


print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10))  # 55
print(sum_of_numbers(100))  # 5050


# 14 Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
print("\nQuestion 14")


def sum_of_odds(num):

    return sum(range(1, num + 1, 2))


print(sum_of_odds(13))


# 15 Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
print("\nQuestion 15")


def sum_of_even(num):

    return sum(range(2, num + 1, 2))


print(sum_of_even(13))


print("--------------------------------------")
print("Exercises: Level 2")
print("--------------------------------------")


# 2.1 Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
print("\nQuestion 2.1")


def evens_and_odds(num):
    even = 0
    odd = 0
    for i in range(1, num + 1):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return f"even count {even}, odd count {odd}"


print(evens_and_odds(16))


# 2.2 Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
print("\nQuestion 2.2")


def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i

    return fact


print(factorial(5))


# 2.3 Call your function is_empty, it takes a parameter and it checks if it is empty or not
print("\nQuestion 2.3")


def is_empty(paramter):
    return "Empty" if len(paramter) == 0 else "Not Empty"


print(is_empty("   "))


# 2.4 Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
print("\nQuestion 2.4a")


def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


print(calculate_mean([1, 2, 3, 4, 5]))

print("\nQuestion 2.4b")


def calculate_median(numbers):
    length = len(numbers)
    if length % 2 == 0:
        return (numbers[(length // 2) - 1] + numbers[length // 2]) / 2
    return numbers[length // 2]


print(calculate_median([1, 2, 3, 4, 5, 6]))

print("\nQuestion 2.4c")


def calculate_mode(numbers):
    num_dict = {}
    for num in numbers:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] = numbers.count(num)
    mode = sorted(num_dict.items(),
                  key=lambda mode: mode[1], reverse=True)[:1][0]

    return mode


print(calculate_mode([1, 2, 3, 3, 4, 5, 5, 5, 6]))


print("\nQuestion 2.4d")


def calculate_range(numbers):
    return max(numbers) - min(numbers)


print(calculate_range([-6, 2, 3, 3, 4, 5, 5, 5, 6]))

print("\nQuestion 2.4e")


# def calculate_variance(numbers):
#     mean = calculate_mean(numbers)
#     sample_mean_squared = 0
#     population_size = len(numbers)

#     for num in numbers:
#         sample_mean_squared += (num - mean)**2

#     return sample_mean_squared / population_size


""" REFACTOR """


def calculate_variance(numbers, variance_type):
    mean = calculate_mean(numbers)
    length = len(numbers)

    return sum((num - mean)**2 for num in numbers) / length if variance_type == "population" else sum((num - mean)**2 for num in numbers) / (length - 1)


print(calculate_variance([1, 2, 15, 3, 4, 5, 11], "population"))
print(calculate_variance([1, 2, 15, 3, 4, 5, 11], "sample"))


print("\nQuestion 2.4f")


def calculate_std(numbers):
    standard_variance = (calculate_variance(numbers, "sample")) ** 0.5

    return standard_variance


print(calculate_std([1, 2, 15, 3, 4, 5, 11]))


print("--------------------------------------")
print("Exercises: Level 3")
print("--------------------------------------")


# 3.1 Write a function called is_prime, which checks if a number is prime.
print("\nQuestion 3.1")


def is_prime(number):
    if number <= 1:
        return False
    for num in range(2, int(number**0.5 + 1)):
        if number % num == 0:
            return False

    return True


prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

print(is_prime(90))

# 3.2 Write a functions which checks if all items are unique in the list.
print("\nQuestion 3.2")


def unique_list(items):
    return len(items) == len(set(items))


print(unique_list([1, 2, 3, 4, 5]))  # True NO Duplicates
print(unique_list([1, 2, 3, 4, 5, 5, 5]))  # False Duplicates


# 3.3 Write a function which checks if all the items of the list are of the same data type.
print("\nQuestion 3.3")


def same_data_type(items):
    first_type = type(items[0])
    return all(type(item) == first_type for item in items)


print(same_data_type([1, 2, 3]))  # True SAME Data Type(int)
print(same_data_type([1, 2, "3"]))  # False DIFFERENT Data Type(int and str)

# 3.4 Write a function which check if provided variable is a valid python variable
print("\nQuestion 3.4")


def valid_python_variable(item):
    # return "Valid" if item[0].isalpha() else "Not Valid"  # ignores _ only issue
    return item.isidentifier()


print(valid_python_variable("python"))  # True
print(valid_python_variable("_python"))  # False
print(valid_python_variable("1python"))  # False


# 3.5 Go to the data folder and access the countries-data.py file.
# 3.5.1 Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
print("\nQuestion 3.5.1")


def most_spoken_languages(top_n):
    total_languages = []
    for country in countries_data:
        total_languages.extend(country["languages"])

    most_spoken_languages = {}
    for lang in total_languages:
        most_spoken_languages[lang] = total_languages.count(lang)

    top_spoken_languages = sorted(most_spoken_languages.items(),
                                  key=lambda language: language[1], reverse=True)[:top_n]

    return top_spoken_languages


print(most_spoken_languages(20))


# 3.5.2 Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
print("\nQuestion 3.5.2")


def most_populated_countries(top_n):
    populated_countries = {}
    for population in countries_data:
        populated_countries[population["name"]] = population["population"]

    most_populated = sorted(
        populated_countries.items(), key=lambda population: population[1], reverse=True)[:top_n]

    return most_populated


print(most_populated_countries(10))

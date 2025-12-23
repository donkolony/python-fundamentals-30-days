
from pprint import pprint
from countries_data import countries_data
import itertools
from countries import countries as c
from functools import reduce

""" Day 14: Higher Order Functions """

# Exercises: Day 14


print("--------------------------------------")
print("Exercises: Level 1")
print("--------------------------------------")

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
numbers = [-2, -1, 0, 1, 2, 3, 4, 5]
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

# 1.1 Explain the difference between map, filter, and reduce.
print("Question 1.1")
"""
map():      A function in Python applies a given function to each element of an iterable (list, tuple, set, etc.)

filter():   A function used to extract elements from an iterable (like a list, tuple or set) that satisfy a
            given condition   It works by applying a function to each element and keeping only those for which
            function returns True.

reduce():   A function from (functools) applies a function cumulatively to an iterable,
            reducing it to a single value. It's handy for concise tasks like summing, multiplying
            (factorial), finding max/min, concatenating strings or flattening lists.
"""


# 1.2 Explain the difference between higher order function, closure and decorator

# 1.3 Define a call function before map, filter or reduce, see examples.
print("\nQuestion 1.3")


def cube(n):
    return n**3


def even_num(n):
    return n % 2 == 0


def add(a, b):
    return a + b


result_map = list(map(cube, numbers))
print(result_map)

result_filter = list(filter(even_num, numbers))
print(result_filter)

result_reduce = reduce(add, numbers)
print(result_reduce)

# 1.4 Use for loop to print each country in the countries list.
print("\nQuestion 1.4")
print([country for country in countries])

# 1.5 Use for to print each name in the names list.
print("\nQuestion 1.5")
print([name for name in names])

# 1.6 Use for to print each number in the numbers list.
print("\nQuestion 1.6")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([number for number in numbers])


print("--------------------------------------")
print("Exercises: Level 2")
print("--------------------------------------")

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
numbers = [-2, -1, 0, 1, 2, 3, 4, 5]
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

# 2.1 Use map to create a new list by changing each country to uppercase in the countries list
print("\nQuestion 2.1")
countries_uppercase = list(map(lambda country: country.upper(), countries))
print(countries_uppercase)

# 2.2 Use map to create a new list by changing each number to its square in the numbers list
print("\nQuestion 2.2")
squared_numbers = list(map(lambda number: number**2, numbers))
print(squared_numbers)

# 2.3 Use map to change each name to uppercase in the names list
print("\nQuestion 2.3")
names_uppercase = list(map(lambda name: name.upper(), names))
print(names_uppercase)

# 2.4 Use filter to filter out countries containing 'land'.
print("\nQuestion 2.4")
countries_with_land = list(
    filter(lambda country: "land" in country, countries))
print(countries_with_land)

# 2.5 Use filter to filter out countries having exactly six characters.
print("\nQuestion 2.5")
countries_length_six = list(
    filter(lambda country: len(country) == 6, countries))
print(countries_length_six)

# 2.6 Use filter to filter out countries containing six letters and more in the country list.
print("\nQuestion 2.6")
countries_length_six_or_more = list(
    filter(lambda country: len(country) >= 6, countries))
print(countries_length_six_or_more)

# 2.7 Use filter to filter out countries starting with an 'E'
print("\nQuestion 2.7")
countries_starting_with_e = list(
    filter(lambda country: country.startswith("E"), countries))
print(countries_starting_with_e)

# 2.8 Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
print("\nQuestion 2.8")
squared_even_numbers = reduce(lambda a, b: a + b, filter(lambda number: number %
                                                         2 == 0, map(lambda number: number**2, numbers)))
print(squared_even_numbers)


# 2.9 Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
print("\nQuestion 2.9")


def get_string_lists(lst):
    strings_only = list(
        filter(lambda item: isinstance(item, str), lst))

    return strings_only


items = ["hello", 5, 3.2, "world", True, "Python"]
print(get_string_lists(items))


# 2.10 Use reduce to sum all the numbers in the numbers list.
print("\nQuestion 2.10")
sum_numbers = reduce(lambda num1, num2: num1 + num2, numbers)
print(sum_numbers)


# 2.11 Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
print("\nQuestion 2.11")
concatenate_countries = reduce(lambda a, b: a + ", " + b, countries[:-1])
sentence = f"{concatenate_countries}, and {countries[-1]} are north European countries"

print(sentence)

# 2.12 Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
print("\nQuestion 2.12")


def categorize_countries(countries, pattern):
    pattern = pattern.lower()
    end_with_suffix = list(
        filter(lambda country: country.lower().endswith(pattern), countries))

    return end_with_suffix


print(categorize_countries(c, "land"))
print(categorize_countries(c, "ia"))
print(categorize_countries(c, "island"))
print(categorize_countries(c, "stan"))

# 2.13 Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
print("\nQuestion 2.13")


def country_starting_letter(countries):
    result = {}
    for country in countries:
        first_letter = country[0]
        if first_letter in result:
            result[first_letter] += 1
        else:
            result[first_letter] = 1

    return result


print(country_starting_letter(c))


# 2.14 Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
print("\nQuestion 2.14")


def get_first_ten_countries(countries, n=10):
    return countries[:n]


print(f"\nUsing Normal Slicing")
print(get_first_ten_countries(c, 10))


""" REFACTOR USING BUILT-IN MODULES (ITERTOOLS) """


def get_first_ten_countries(countries, n=10):
    return list(itertools.islice(countries, n))




print(f"\nUsing Built-in Module (Itertools)")
print(get_first_ten_countries(c, 10))


# 2.15 Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
print("\nQuestion 2.15")


def get_last_ten_countries(countries, n=10):
    return countries[-n:]


print(get_last_ten_countries(c, 10))


print("--------------------------------------")
print("Exercises: Level 3")
print("--------------------------------------")


# 3.1 Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:

# 3.1.1 Sort countries by name, by capital, by population
print("\nQuestion 3.1.1")


def sort_countries(countries, sort_type):
    sorted_country = sorted(
        countries, key=lambda item: item.get(sort_type))

    return sorted_country


print(sort_countries(countries_data, "name"))
print(sort_countries(countries_data, "capital"))
print(sort_countries(countries_data, "population"))

# 3.1.2 Sort out the ten most spoken languages by location.
print("\nQuestion 3.1.2")


def most_spoken_languages(countries, top_n=10):
    language_count = {}
    for country in countries:
        for language in set(country["languages"]):
            language_count[language] = language_count.get(language, 0) + 1

    top_spoken_languages = sorted(
        language_count.items(), key=lambda item: item[1], reverse=True)[:top_n]

    return top_spoken_languages


print(most_spoken_languages(countries_data, 10))


# 3.1.3 Sort out the ten most populated countries.
print("\nQuestion 3.1.3")


def most_populated_countries(countries, top_n):
    top_populated_countries = sorted(
        countries, key=lambda country: country.get("population", 0), reverse=True
    )[:top_n]

    # Return list of tuples
    return [(country["name"], country["population"]) for country in top_populated_countries]


print(most_populated_countries(countries_data, 5))

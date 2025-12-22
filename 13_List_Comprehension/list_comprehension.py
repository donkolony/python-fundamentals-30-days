from pprint import pprint

"""Day 13: List Comprehension"""

# Exercises: Day 13


print("--------------------------------------")
print("Exercises: Level 1")
print("--------------------------------------")


# 1.1 Filter only negative and zero in the list using list comprehension
print("Question 1.1")
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
zero_and_negative_numbers = [num for num in numbers if num <= 0]
print(zero_and_negative_numbers)

# 1.2 Flatten the following list of lists of lists to a one dimensional list :
print("\nQuestion 1.2")
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [z for x in list_of_lists for y in x for z in y]
print(flattened_list)

"""
# 1.3 Using list comprehension create the following list of tuples:

[(0, 1, 0, 0, 0, 0, 0),
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
"""
print("\nQuestion 1.3")
list_of_tuples = [(n, 1, n, n**2, n**3, n**4, n**5) for n in range(11)]
pprint(list_of_tuples)

# 1.4 Flatten the following list to a new list:
print("\nQuestion 1.4")
countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flattened_countries_lc = [
    [name.upper(), name[:3].upper(), cap.upper()] for country in countries for name, cap in country]

print(flattened_countries_lc)


"""
# 1.5 Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output:
    [{'country': 'FINLAND', 'city': 'HELSINKI'},
    {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
    {'country': 'NORWAY', 'city': 'OSLO'}]
"""
print("\nQuestion 1.5")
countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

list_dictionaries = [{"country": name.upper(), "city": city.upper()}
                     for country in countries for name, city in country]

print(list_dictionaries)

"""
# 1.6 Change the following list of lists to a list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

output
    ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
"""
print("\nQuestion 1.6")
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],
         [('Donald', 'Trump')], [('Bill', 'Gates')]]
list_of_concatenated_strings = [
    (firstname + " " + lastname) for name in names for firstname, lastname in name]

print(list_of_concatenated_strings)

from countries_data import countries_data
from countries import countries


"""Day 10: Loops"""

# Exercises: Day 10


print("--------------------------------------")
print("Exercises: Level 1")
print("--------------------------------------")

# 1 Iterate 0 to 10 using for loop, do the same using while loop.
print("\nQuestion 1")

print("\nnUsing For Loop:")
for num in range(11):
    print(num)

print("\nUsing While Loop:")
count = 0
while count < 11:
    print(count)
    count += 1


# 2 Iterate 10 to 0 using for loop, do the same using while loop.
print("\nQuestion 2")

print("\nnUsing For Loop: ")
for num in range(11):
    print(10 - num)

print("\nUsing While Loop:")
count = 10
while count >= 0:
    print(count)
    count -= 1

"""
# 3 Write a loop that makes seven calls to print(), so we get on the output the following triangle:

#
##
###
####
#####
######
#######
"""
print("\nQuestion 3")

print("\nnUsing For Loop:")
for i in range(1, 8):
    print(i * "#")

print("\nUsing While Loop:")
count = 0
while count < 8:
    print(count * "#")
    count += 1

"""
# 4 Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

"""
print("\nQuestion 4")

print("\nnUsing For Loop:")
for row in range(8):
    for col in range(8):
        print("#", end=" ")
    print()

print("\nUsing While Loop:")
row = 0
while row < 8:
    col = 0
    while col < 8:
        print("#", end=" ")
        col += 1
    print()  # prints a new line
    row += 1

"""
# 5 Print the following pattern:

0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100


"""
print("\nQuestion 5")

print("\nnUsing For Loop:")
for i in range(11):
    print(f"{i} x {i} = {i * i}")

print("\nUsing While Loop:")
count = 0
while count <= 10:
    print(f"{count} x {count} = {count * count}")
    count += 1

# 6 Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
print("\nQuestion 5")
frameworks = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

print("\nUsing For Loop: ")
for i in frameworks:
    print(i)


print("\nUsing While Loop:")
count = 0
while count < len(frameworks):
    print(frameworks[count])
    count += 1

# 7 Use for loop to iterate from 0 to 100 and print only even numbers
print("\nQuestion 5")

print("\nUsing For Loop:")
for i in range(2, 101, 2):
    print(i)

print("\nUsing While Loop:")
count = 2
while count <= 100:
    print(count)
    count += 2

# 8 Use for loop to iterate from 0 to 100 and print only odd numbers
print("\nUsing For Loop:")
for i in range(1, 101, 2):
    print(i)

print("\nUsing While Loop:")
count = 1
while count <= 100:
    print(count)
    count += 2


print("--------------------------------------")
print("Exercises: Level 2")
print("--------------------------------------")

# 1 Use for loop to iterate from 0 to 100 and print the sum of all numbers.
print("\nQuestion 1")

print("\nUsing For Loop:")
total = 0
for i in range(101):
    total += i
print(f"Sum using for loop: {total}")


print("\nUsing While Loop:")
i = 0
total = 0
while i <= 100:
    total += i
    i += 1
print(f"Sum using while loop: {total}")


# 2 Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
print("\nQuestion 2")

print("\nUsing For Loop:")
even_total = 0
odd_total = 0
for i in range(101):
    if i % 2 == 0:
        even_total += i
    else:
        odd_total += i

print(
    f"The sum of all evens is {even_total}. And the sum of all odds is {odd_total}.")


print("\nUsing While Loop:")
even_total = 0
odd_total = 0
i = 0
while i <= 100:
    if i % 2 == 0:
        even_total += i
    else:
        odd_total += i
    i += 1

print(
    f"The sum of all evens is {even_total}. And the sum of all odds is {odd_total}.")


print("--------------------------------------")
print("Exercises: Level 3")
print("--------------------------------------")


# 1 Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
print("\nQuestion 1")

print("\nUsing For Loop:")
land = []
for country in countries:
    if "land" in country:
        land.append(country)

print(land)


print("\nUsing While Loop:")
land = []
i = 0
while i < len(countries):
    if "land" in countries[i]:
        land.append(countries[i])
    i += 1

print(land)

# 2 This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']

print("\nQuestion 1")

print("\nUsing For Loop:")
reverse = []
for fruit in fruits[::-1]:
    reverse.append(fruit)

print(reverse)


print("\nUsing While Loop:")
reverse = []
i = 0
last_index = len(fruits) - 1
while i < len(fruits):
    reverse.append(fruits[len(fruits) - 1 - i])
    i += 1

print(reverse)

"""
# 3 Go to the data folder and use the countries_data.py file.
"""
# 3a What are the total number of languages in the data
print("\nQuestion 3a")
total_languages = []

for country in countries_data:
    total_languages.extend(country["languages"])


unique_languages = set(total_languages)
print(
    f"Total languages in the countries data (non-unique): {len(total_languages)}")
print('\n')
print(
    f"Total languages in the countries data (unique): {len(unique_languages)}")


# 3b Find the ten most spoken languages from the data
print("\nQuestion 3b")
most_spoken_languages = {}
for lang in total_languages:
    most_spoken_languages[lang] = total_languages.count(lang)

top_spoken_languages = sorted(most_spoken_languages.items(),
                              key=lambda language: language[1], reverse=True)[:10]

print(top_spoken_languages)


# 3c Find the 10 most populated countries in the world
print("\nQuestion 3c")
most_populated_countries = {}
for population in countries_data:
    most_populated_countries[population["name"]] = population["population"]

most_populated_countries = sorted(
    most_populated_countries.items(), key=lambda population: population[1], reverse=True)[:10]

print(most_populated_countries)

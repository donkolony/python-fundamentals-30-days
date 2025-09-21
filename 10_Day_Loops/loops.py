# 💻 Exercises: Day 10

# Exercises: Level 1

# #1
# for i in range(10):
#     print(f"Count using a for loop {i}")

# count = 0
# while count < 10:
#     print(f"Count using a while loop: {count}")
#     count += 1
 
#2
# for i in range(10):
#     print(f"Count down using for loop: {10 - i}")

# count = 10
# while count > 0:
#     print(f"Count down using while loop: {count}")
#     count -= 1

#3
# for i in range(8):
#     print("#" * i)

#4
# for rows in range(9):
#     for cols in range(9):
#         print("#", end=" ")
#     print("#") 

#5
# for i in range(11):
#     print(f" {i} x {i} = {i * i}")

#6
# languages = ['Python', 'Numpy','Pandas','Django', 'Flask'] 
# for language in languages:
#     print(language)

#7
# for i in range(101):
#     if i % 2 == 0:
#         print(i)

#8
# for i in range(101):
#     if i % 2 != 0:
#         print(i)

# # using the continue keyword
# for i in range(101):
#     if i % 2 == 0:
#         continue
#     print(i)

########## Exercises: Level 2 ########## 

#1
# total = 0
# for num in range(101):
#         total +=  num
        
# print(f"Sum of all numbers: {total}")

#2
# even_total = 0
# odd_total = 0

# for num in range(101):
#     if num % 2 == 0:
#         even_total += num
#     else:
#         odd_total += num
    
# print(f"The sum of all evens is {even_total}. And the sum of all odds is {odd_total}.")

########## Exercises: Level 3 ########## 

#1
# import countries as c

# land = []

# for country in c.countries:
#     if "land" in country:
#         land.append(country)

# print(land)

#2
# fruits = ['banana', 'orange', 'mango', 'lemon']

# for fruit in reversed(fruits):
#     print(fruit)


# 3 (i) What are the total number of languages in the data
import countries_data as cd

all_languages = []
unique_languages = set()
countries_list = []
population_list = []


for country in cd.countries:
    all_languages.extend(country["languages"])
    unique_languages.update(country["languages"])
    countries_list.append(country["name"])
    
# print(countries_list)

# print(f"There are {len(cd.countries)} items in the list") 
# print(f"Using list (with duplicates), there are {len(all_languages)} languages in the data.")
# print(f"Using set (without duplicates), there are {len(unique_languages)} languages in the data.")


"""
English - 91
French - 45
Arabic - 25
Spanish - 24
Portuguese - 9
German - 7
Chinese - 5
"""
# 3 (ii) - Mike used the import counter
import countries_data as cd
from collections import Counter

languages_list = []
unique_languages = set()
countries_list = [] #name of country
population_list = [] #population

for country in cd.countries:
    languages_list.extend(country['languages'])
    countries_list.append(country['name'])
    population_list.append(country['population'])
    unique_languages.update(country['languages'])


print(Counter(languages_list).most_common(10))

print(countries_list)
print(population_list)

# 3 (iii)






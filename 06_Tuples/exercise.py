"""Day 06: Tuples"""

# Exercises: Day 6

# Exercises: Level 1


print("--------------------------------------")
print("Exercises: Level 1")
print("--------------------------------------")


# 1 Create an empty tuple
print("\nQuestion 1")
empty_tuple = tuple()

# 2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Herve', 'Peter', 'Victor')
sisters = ('Blondelle', 'Grace', 'Roseline')
print("\nQuestion 2")

# 3 Join brothers and sisters tuples and assign it to siblings
print("\nQuestion 3")
siblings = brothers + sisters

# 4 How many siblings do you have?
print("\nQuestion 4")
amount_of_siblings = len(siblings)
print(
    f"I have {amount_of_siblings} siblings.")

# 5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
print("\nQuestion 5")
parents = ['Dieudonne', 'Rose']
list_of_siblings = list(siblings)
family_members = parents + list_of_siblings

print(f"My family members: {family_members}")


print("\n\n\n")
print("--------------------------------------")
print("Exercises: Level 2")
print("--------------------------------------")


# 1 Unpack siblings and parents from family_members
print("\nQuestion 1")
dad, mom, *siblings = family_members

print(f"Dad {dad}")
print(f"Mom {mom}")
print(f"Siblings {siblings}")

# 2 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
print("\nQuestion 2")
fruits = ('water-melon', 'mango', 'peach', 'banana')
vegetables = ('cucumber', 'beetroot', 'carrot', 'pepper')
animal_products = ('beef', 'chicken', 'pork', 'fish')
food_stuff_tp = fruits + vegetables + animal_products

# 3 Change the about food_stuff_tp tuple to a food_stuff_lt list
print("\nQuestion 3")
food_stuff_lt = list(food_stuff_tp)

# 4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print("\nQuestion 4")
print(food_stuff_tp)
middle1 = len(food_stuff_tp) // 2 - 1
middle2 = len(food_stuff_tp) // 2
middle_item = food_stuff_tp[middle1: middle2 + 1]

print(f"Middle Item: {middle_item}")

# 5 Slice out the first three items and the last three items from food_staff_lt list
print("\nQuestion 5")
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]

print(f"Food Stuff List: {food_stuff_lt}")
print(f"First three items: {first_three_items}")
print(f"Last three items: {last_three_items}")

# 6 Delete the food_staff_tp tuple completely
print("\nQuestion 6")
del food_stuff_tp


# 7 Check if an item exists in tuple:
print("\nQuestion 7")
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print(nordic_countries)

# 7a  Check if 'Estonia' is a nordic country
estonia_exist = "Estonia" in nordic_countries
print(f"Does Estonia exist inside nordic countries tuple? {estonia_exist}")


# 7b Check if 'Iceland' is a nordic country
iceland_exist = "Iceland" in nordic_countries
print(f"Does Iceland exists in nordic countries tuple? {iceland_exist}")

# Exercise: Level 1

#1
empty_tuple = ()

#2
brothers = ("Peter", "Victor", "Herve")
sisters = ("Blondelle", "Grace", "Rosie")

# print(f"Brothers: {brothers}")
# print(f"Sisters: {sisters}")

#3
siblings = brothers + sisters
# print(f"Siblings: {siblings}")

#4
amount_of_siblings = len(siblings)
# print(f"I have {amount_of_siblings} siblings")

#5
parents = ["Dieudonne", "Rose"]
list_of_siblings = list(siblings)
family_members = list_of_siblings + parents

# print(f"List of my family members: {family_members}")


# Exercise: Level 2

#1 
sib1, sib2, sib3, sib4, sib5, sib6, par1, par2 = family_members

# print(f"Sibling 1: {sib1}")
# print(f"Sibling 2: {sib2}")
# print(f"Sibling 3: {sib3}")
# print(f"Sibling 4: {sib4}")
# print(f"Sibling 5: {sib5}")
# print(f"Sibling 6: {sib6}")
# print(f"Parent 1: {par1}")
# print(f"Parent 2: {par2}")
 

#2
fruits = ("apple", "banana", "orange", "mango", "grapes")
vegetables = ("potato", "tomato", "onion")
animal_products = ("milk", "eggs", "beef")

food_stuff_tp = fruits + vegetables + animal_products 

# print(type(fruits))
# print(type(vegetables))
# print(type(animal_products))
# print(food_stuff_tp)

#3
food_stuff_lt = list(food_stuff_tp)

# print(food_stuff_lt)
# print(type(food_stuff_lt))

#4
food_stuff_lt[5:6]
# print(food_stuff_lt)

#5
# print(food_stuff_lt[0:3])
# print(food_stuff_lt[-3:-1])

#6
del food_stuff_tp

#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)
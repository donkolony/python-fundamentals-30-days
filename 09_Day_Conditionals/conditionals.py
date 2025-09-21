# 💻 Exercises: Day 9

## Exercises: Level 1

#1
# age = int(input("Enter your age: ")) #15

# if age >= 18:
#     print("You are old enough to drive :)")
# else:
#     years_remaining = 18 - age 
#     print(f"You need {years_remaining} more years to learn to drive")

#2
# my_age = int(input("Enter age: "))
# your_age = int(input("Enter age: "))

# if my_age > your_age:
#     if my_age - your_age == 1:
#         print("year")
#     elif my_age - your_age > 1:
#         print("years")
#     else:
#         print("No difference in age")
# else:
#     age_diff = your_age - my_age
#     print(f"You are {age_diff} years older than me")

#3
# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))

# if a > b:
#     print(f"{a} is greater than {b}")
# elif a < b:
#     print(f"{a} is smaller than {b}")
# else:
#     print("equal")


## Exercises: Level 2

#1
# while True:
#     score = int(input("Enter score: "))
#     if score >= 80 and score <= 100:
#         print("A")
#     elif score >= 70 and score <= 79:
#         print("B")
#     elif score >= 60 and score <= 69:
#         print("C")
#     elif score >= 50 and score <= 59:
#         print("D")
#     elif score >= 0 and score <= 49:
#         print("F")
#     else:
#         print("Invalid")

#2
# month = input("Enter month: ")

# if month == "September" or month == "October" or month == "November":
#     print("Autumn")
# elif month == "December" or month == "January" or month == "February":
#     print("Winter")
# elif month == "March" or month == "April" or month == "May":
#     print("Spring")
# elif month == "June" or month == "July" or month == "August":
#     print("Summer")
# else:
#     print("Invalid")

# if month in ["September", "October", "November"]:
#     print("Autumn")
# elif month in ["December", "January",  "February"]:
#     print("Winter")
# elif month in["March", "April", "May"]:
#     print("Spring")
# elif month in["June", "July",  "August"]:
#     print("Summer")
# else:
#     print("Invalid")

#3
# all_fruits = [ "Apple","Bananas","Oranges", "Grapes" ,"Strawberries", "Blueberries", "Mangoes","Pineapples", "Watermelons", "Pears" ]

#Level 3

# person = {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
#     }

#1
# if person["skills"]:
#     print(person["skills"][2])

#2
# if "Python" in person["skills"]:
#     print(True)
# else:
#     print(False)

#3

# skill_1 = input("Enter a skill: ")
# skill_2 = input("Enter a skill: ")

# if skill_1 and skill_2 in person["skills"]:
#     print("You are a frontend developer!")
# else:
#     print("None")

"""
* If a person skills has only JavaScript and React, print('He is a front end developer'), 
if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
else print('unknown title') - for more accurate results more conditions can be nested!
"""

#convert the skill list into a set for better comparison
# then use if statements to check



######################################################################################


## 💻 Exercises: Day 9

# Exercises: Level 1

#1
# age = int(input("enter your age: "))

# if age >= 18:
#     print("You are old enough to drive")
# else:
#     years_left = 18 - age
#     print(f"You need {years_left} more years to learn to drive ")

#2
# my_age = 23
# your_age = int(input("enter your age: "))

# if my_age > your_age:
#     if my_age - your_age == 1:
#         print("year")
#     elif my_age - your_age > 1:
#         print("years")
# else:
#     age_diff = your_age - my_age
#     print(f"You are {age_diff} years old than me")

#3
# a = int(input("enter number: "))
# b = int(input("enter number: "))

# if a > b:
#     print(f"{a} is greater than {b}")
# elif a < b:
#     print(f"{a} is smaller than {b}")
# else:
#     print("equal")

## Exercises: Level 2

#1
# score = int(input("enter grade: "))
# if score >= 80 and score <= 100:
#     print("A")
# elif score >= 70 and score <= 79:
#      print("B")
# elif score >= 60 and score <= 69:
#     print("C")
# elif score >= 50 and score <= 59:
#     print("D")
# elif score >= 0 and score <= 49:
#     print("F")
# else:
#     print("invalid")

#2
# month = input("enter month: ")

# if month in ["September", "October", "November"]:
#     print("Autumn")
# elif month in ["December", "January", "February"]:
#     print("Winter")
# elif month in ["March", "April", "May"]:
#     print("Spring")
# elif month in ["June", "July", "August"]:
#     print("Summer")
# else:
#      print("Month does not exists")

#3
# fruits = ['banana', 'orange', 'mango', 'lemon']
# user_fruit = input("enter a fruit: ")

# if user_fruit not in fruits:
#     fruits.append(user_fruit)
#     print(fruits)
# elif user_fruit in fruits:
#     print("That fruit already exists in the list")

## Exercises: Level 3
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

#1
# if person["skills"]:
#     middle_skill = (len(person['skills'] ) // 2)
#     print(person['skills'][middle_skill])

#2
# if "Python" in person["skills"]:
#     print("Python skill exist")
# else:
#     print("Python skill does not exist")


#3
# skill_set = set(person['skills'])

# if {"React", "Node", "MongoDB"} <= skill_set:
#     print("You are a fullstack developer")
# elif {"Node", "Python", "MongoDB"} <= skill_set:
#     print("You are a backend developer")
# elif {"JavaScript", "React"} <= skill_set:
#     print("You are a frontend developer")
# else:
#     print("unknown title, are you sure you are a programmer?")

#4
# if person['is_marred'] == True and person['country'] == "Finland":
#     print(f"{person['first_name']} {person['last_name']} lives in {person['country']} and is married")

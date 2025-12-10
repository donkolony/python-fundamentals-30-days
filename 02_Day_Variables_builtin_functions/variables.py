# Variables in Python

# Exercises - Day 2


# Exercises: Level 1
# Day2: 30 Days of python programming
first_name = "Don"
last_name = "Kolony"
fullname = "Don Kolony"
country = "France"
city = "Lyon"
age = 250
year = 2025
is_married = False
is_true = True
is_light_on = False
favorite_color, occupation, height, race, can_code = "orange", "student", 1.81, "african", True


# Exercises: Level 2
print(f"first name data type: {type(first_name)}")
print(f"length of first name: {len(first_name)}")
print(
    f"length of first name is: {len(first_name)} and length of last name is: {len(last_name)} ")
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_two / num_one
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
radius = 30
area_of_circle = 3.14 * radius**2
circum_of_circle = 2 * 3.14 * radius
user_radius = int(input("Enter radius: "))
user_area_of_circle = 3.14 * user_radius**2
print(
    f"user radius = {user_radius} area of circle: (3.14 * {user_radius} ** 2) = {3.14 * user_radius**2}  ")

user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")
user_country = input("Enter your country: ")
user_age = int(input("Enter your age: "))

print(f"user first name: {user_first_name}")
print(f"user last name: {user_last_name}")
print(f"user country: {user_country}")
print(f"user age: {user_age}")

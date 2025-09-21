## valid variable names

firstname
lastname
age
country
city
first_name
last_name
capital_city
\_if # if we want to use reserved word as a variable
year_2021
year2021
current_year_2021
birth_year
num1
num2

## Invalid variable names

first-name
first@name
first$name
num-1
1num

# Variables in Python

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
'firstname':'Asabeneh',
'lastname':'Yetayeh',
'country':'Finland',
'city':'Helsinki'
}

## Built-in functions

print() functions takes unlimited number of arguments
len() function only take sone argument

print('Hello, World!') # The text Hello, World! is an argument
print('Hello',',', 'World','!') # it can take multiple arguments, four arguments have been passed
print(len('Hello, World!')) # it takes only one argument

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

## Declaring Multiple Variables in a Line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

## Casting - When converting one data type fo another

# int to float

num_int = 10
print('num_int',num_int) # 10
num_float = float(num_int)
print('num_float:', num_float) # 10.0

# float to int

gravity = 9.81
print(int(gravity)) # 9

# int to str

num_int = 10
print(num_int) # 10
num_str = str(num_int)
print(num_str) # '10'

# str to int or float

num_str = '10.6'
num_float = float(num_str)
print('num_float', float(num_str)) # 10.6
num_int = int(num_float)
print('num_int', int(num_int)) # 10

# str to list

first_name = 'Asabeneh'
print(first_name) # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list) # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']

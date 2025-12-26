try:
    print(10 + '5')
except:
    print('Something went wrong')

try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')


try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occurred')
except ValueError:
    print('Value error occurred')
except ZeroDivisionError:
    print('zero division error occurred')


try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)


""" Packing and Unpacking Arguments in Python """


def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e


lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))

numbers = range(2, 7)
print(list(numbers))
args = [2, 7]
numbers = list(range(*args))
print(numbers)

# UNPACKING a List/Tuple
countries = ["Denmark", "Sweden", "Norway", "Finland", "Iceland"]
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']

numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)  # 1 [2, 3, 4, 5, 6] 7

# Unpacking Dictionaries


def unpacking_person_info(name, country, city, age):
    return f"{name} lives in {country}, {city}. He is {age} years old."


dct = {"name": "Don", "country": "South Africa", "city": "Cape Town", "age": 23}
print(unpacking_person_info(**dct))


# Packing Lists
def sum_all(*args):
    s = 0
    for i in args:
        s += i

    return s


print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5, 6, 7))

# Packing Dictionaries


def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")

    return kwargs


print(packing_person_info(name="Don",
      country="South Africa", city="Cape Town", age=23))


# Spreading in Python
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [*lst_one, *lst_two]
print(lst)

country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)

# Enumerate
for index, item in enumerate([20, 30, 40]):
    print(index, item)

for index, i in enumerate(countries):
    print("Hi")
    if i == "Finland":
        print(f"The country {i} has been found at index {index}")

# Zip
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit': f, 'veg': v})

print(fruits_and_veges)

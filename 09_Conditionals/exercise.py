"""Day 09: Conditionals"""

# Exercises: Day 9


print("--------------------------------------")
print("Exercises: Level 1")
print("--------------------------------------")

"""
1 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: 
You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.

Output:
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
"""
print("\nQuestion 1")
user_age = int(input("Enter your age: "))
if user_age >= 18:
    print('You are old enough to drive.')
else:
    print(f'You need {18 - user_age} more year(s) to learn to drive.')

"""
2 Compare the values of my_age and your_age using if … else. Who is older (me or you)? 
Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to 
print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom 
text if my_age = your_age. Output:

Enter your age: 30
You are 5 years older than me.
"""
print("\nQuestion 2")
your_age = int(input("Enter your age: "))
my_age = 23
if your_age > my_age:
    if your_age - my_age == 1:
        print('year')
    elif your_age - my_age > 1:
        print('years')
    print(f'You are {your_age - my_age} years older than me')
elif your_age < my_age:
    print(f'You are {my_age - your_age} years younger than me.')
else:
    print('You are the same age as me')

"""
3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b,
if a is less b return a is smaller than b, else a is equal to b. Output:

Enter number one: 4
Enter number two: 3
4 is greater than 3
"""
print("\nQuestion 3")
num1 = int(input('Enter number one: '))
num2 = int(input('Enter number two: '))
if num1 > num2:
    print(f'{num1} is greater than {num2}')
elif num1 < num2:
    print(f'{num1} is less than {num2}')
else:
    print(f'{num1} is equal to {num2}')


print("--------------------------------------")
print("Exercises: Level 2")
print("--------------------------------------")


"""
1 Write a code which gives grade to students according to theirs scores:

80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
"""
print("\nQuestion 1")
user_grade = int(input('Enter your grade: '))
if user_grade > 100:
    print('Invalid grade')
elif user_grade >= 80 and user_grade <= 100:
    print('A')
elif user_grade >= 70 and user_grade < 80:
    print('B')
elif user_grade >= 60 and user_grade < 70:
    print('C')
elif user_grade >= 50 and user_grade < 60:
    print('D')
else:
    print('F')


"""
2 Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November,
the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is 
Spring June, July or August, the season is Summer
"""
print("\nQuestion 2")
user_month = input('Enter month: ').capitalize()
if user_month in ['September', 'October', 'November']:
    print('Autumn')
elif user_month in ['December', 'January', 'February']:
    print('Winter')
elif user_month in ['March', 'April', 'May']:
    print('Spring')
elif user_month in ['June', 'July', 'August']:
    print('Summer')
else:
    print('Invalid month')


"""
3 The following list contains some fruits:

```sh
fruits = ['banana', 'orange', 'mango', 'lemon']
```

If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
If the fruit exists print('That fruit already exist in the list')
"""

print("\nQuestion 3")
fruits = ['banana', 'orange', 'mango', 'lemon']
user_fruit = input('Enter a fruit: ').lower()

if user_fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(user_fruit)
    print('That fruit has been added to the list')
    print(fruits)


print("--------------------------------------")
print("Exercises: Level 3")
print("--------------------------------------")

"""
1 Here we have a person dictionary. Feel free to modify it!
"""

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python', 'SQL'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1a Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
print("\nQuestion 1a")
if 'skills' in person:
    length = len(person['skills'])
    if length % 2 != 0:
        middle = person['skills'][length // 2]
        print(middle)
    else:
        middle1 = person['skills'][length // 2]
        middle2 = person['skills'][length // 2 - 1]
        print(f'{middle1} and {middle2}')
else:
    print('Skill does not exist')


# 1b Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
print("\nQuestion 1b")
if 'skills' in person:
    if 'Python' in person['skills']:
        print('Python exist')
    else:
        print('Python does not exist')
else:
    print('Person has no skills list')


""" 
# 1c If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills 
has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, 
Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can 
be nested!
"""
print("\nQuestion 1c")
if 'skills' in person:
    skill_list = person['skills']
    if "Node" in skill_list and "MongoDB" in skill_list and "React" in skill_list:
        print('He is a fullstack developer')
    elif 'Node' in skill_list and 'Python' in skill_list and 'MongoDB' in skill_list:
        print('He is a backend developer')
    elif 'JavaScript' in skill_list and 'React' in skill_list:
        print('He is a front end developer')
    else:
        print('unknown title')
else:
    print('Person has no skills')


"""
# 1d If the person is married and if he lives in Finland, print the information in the following format:
    Asabeneh Yetayeh lives in Finland. He is married.:
"""
print("\nQuestion 1d")
marital_status = input('Enter marital status: ')
country = input('Enter country: ').capitalize()
if marital_status == 'married' and country == "Finland":
    print(f'Asabeneh Yetayeh lives in {country}. He is {marital_status}.')
else:
    print("Hmmm")

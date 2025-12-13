"""
Formating Styles
% --->  (%s, %d, %f)

"{} {}".format(variable1, variable2)

f-strings
"""

first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
language = 'Python'


# print("\n")
# print("String Formatting Using % Operator Python <3")
# print("I am %s %s, I am %d years old and I teach %s" %
#       (first_name, last_name, age, language))

# print("\n")
# print("String Formatting Using Str.format Python 3")
# print("I am {} {}, I am {} years old and I teach {}".format(
#     first_name, last_name, age, language))

# print("\n")
# print("String Formatting Using F-Strings Python 3.6+")
# print(f"I am {first_name} {last_name}, I am {age} years old and I teach {language}")

"""Unpacking String Characters"""
# language = 'Python'
# a, b, c, d, e, f = language  # unpacking sequence characters into variables
# print(a)  # P
# print(b)  # y
# print(c)  # t
# print(d)  # h
# print(e)  # o
# print(f)  # n


language = 'ABCDEFGHI abcdefghi'


print(language.swapcase())

def square(num):
    """
    Applying square on every number
    """
    return num**2


"""
By default map returns a map object (just the memory object). If we want to use the result we have to convert the result into a list
map(square, a) applies square() to each element in a 
list() converts the map object to a list
"""

#  Example: Converting map object into a list
a = [1, 2, 3, 4, 5]
res = list(map(square, a))
print(res)


#  Example: map() with lambda
"""
We cna use lambda function instead of a custom function with map() to make code shorter and easier.
Lambda function = Anonymous Function
"""
a = [1, 2, 3, 4, 5]
res = list(map(lambda x: x ** 3, a))
print(f"lambda function: {res}")

# Example: map() with multiple iterables
c = [1, 2, 3]
d = [4, 5, 6]
res = list(map(lambda x, y: x * y, c, d))
print(f"map with multiple iterables: {res}")


# Example: Converting strings to Uppercase
fruits = ["apple", "banana", "cherry"]
res = list(map(str.upper, fruits))
print(f"converting strings to Uppercase: {res}")


# Example: Extracting first character from strings
words = ["apple", "banana", "cherry"]
res = list(map(lambda s: s[0], words))
print(f"extracting first characters from strings: {res}")

# Example: Removing whitespaces from strings
s = ['  hello  ', '  world ', ' python  ']
res = list(map(str.strip, s))
print(f"removing whitespaces from strings: {res}")


# Example: Converting fahrenheit from celsius
celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(f"converting fahrenheit from celsius: {fahrenheit}")

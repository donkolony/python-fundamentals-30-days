"""Day 03: Operators"""

# Declare your age as integer variable
print("\nQuestion 1")
age = 23

# Declare your height as a float variable
print("\nQuestion 2")
height = 1.81

# Declare a variable that store a complex number
print("\nQuestion 3")
com = 1 - 2j


# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
print("\nQuestion 4")
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area_of_triangle = int(0.5 * base * height)
print(f"The area of the triangle is {area_of_triangle}")

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
print("\nQuestion 5")
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
perimeter_of_triangle = int(a + b + c)
print(f"The perimeter of the triangle is {perimeter_of_triangle}")

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
print("\nQuestion 6")
length = int(input("Enter length: "))
width = int(input("Enter width: "))
area_of_rectangle = int(length * width)
perimeter_of_triangle = int((length + width) * 2)
print(
    f"Area of the rectangle is {area_of_rectangle} and perimeter of the rectangle is {perimeter_of_triangle}")

# 7 Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
print("\nQuestion 7")
radius = int(input("Enter radius: "))
# area = pi * r * r
area_of_circle = 3.14 * radius ** 2
# circumference = 2 * pi * r
circumference_of_circle = 2 * 3.14 * radius
print(
    f"area of a circle is {area_of_circle:.2f} and circumference of a circle is {circumference_of_circle:.2f}")


# 8 Calculate the slope, x-intercept and y-intercept of y = 2x -2
print("\nQuestion 8")
# y = mx + c
y = "2x - 2"
m = 2
c = -2

# y-intercept: let x = 0
x = 0
y_intercept = m * x + c

# x-intercept: ley y = 0
y = 0
x_intercept = (y - c) / m

print(f"Slope: {m}")
print(f"y-int-intercept: {y_intercept}")
print(f"x-int-intercept: {x_intercept}")


# 9 Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
print("\nQuestion 9")
point_1 = (2, 2)
point_2 = (6, 10)
slope = (point_2[1] - point_1[1]) / (point_2[0] - point_1[0])
euclidean_dis = ((point_2[0] - point_1[0]) ** 2 +
                 (point_2[1] - point_1[1]) ** 2) ** 0.5

print(f"slope: {slope}")
print(f"euclidean_distance: {euclidean_dis:.2f}")

# 10 Compare the slopes in tasks 8 and 9.
print("\nQuestion 10")
print(f"slope Q8 == slope Q9? {m == slope}")

# 11 Calculate the value of y (y = x**2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
print("\nQuestion 11")
a, b, c = 1, 6, 9
d = (b**2) - (4*a*c)
eqn_pos = (- b + d**0.5) / (2 * a)
eqn_neg = (- b - d**0.5) / (2 * a)

print(f"y is 0 when x is: {eqn_pos} and {eqn_neg}")

for x in range(-20, 21):   # check x from -20 to 20
    y = x**2 + 6*x + 9
    if y == 0:
        print("y is 0 when x is:", x)


# 12 Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print("\nQuestion 12")
python = "python"
dragon = "dragon"

print(len(python) != len(dragon))  # falsy comparison -> they are NOT equal

# 13 Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("\nQuestion 13")
print("on" in python and "on" in dragon)

# 14 I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("\nQuestion 14")
sentence = "I hope this course is not full of jargon"
print("jargon" in sentence)

# 15 There is no 'on' in both dragon and python
print("\nQuestion 15")
print("on" not in python and "on" not in dragon)

# 16 Find the length of the text python and convert the value to float and convert it to string
print("\nQuestion 16")
python = "python"
print(f"Length of python as a float: {float(len(python))}")
print(f"Length of python as a string: {str(len(python))}")


# 17 Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
print("\nQuestion 17")
num = 10
is_even = num % 2 == 0
print(f" is {num} even? {is_even}")

# 18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print("\nQuestion 18")
floor_division = 7 // 3
float_to_int = int(2.7)
print(floor_division == float_to_int)

# 19 Check if type of '10' is equal to type of 10
print("\nQuestion 19")
num_str = "10"
num_int = 10
print(type(num_str) == type(num_int))


# 20 Check if int('9.8') is equal to 10
print("\nQuestion 20")
gravity_str = "9.8"
num_10 = 10
print(int(float(gravity_str)) == num_10)

# 21 Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
print("\nQuestion 21")
hours = float(int(input("Enter hours: ")))
rate = float(int(input("Enter rate per hour: ")))
earning = hours * rate
print(f"Your weekly earning is R{earning}")

#  22 Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
print("\nQuestion 22")
years_lived = int(input("Enter years lived: "))
days_per_year = 365.25
seconds_per_day = 24 * 60 * 60
years_lived_in_secs = years_lived * days_per_year * seconds_per_day
print(f"You have lived for {years_lived_in_secs} seconds")

# 23 Write a Python script that displays the following table
print("\nQuestion 23")
"""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")

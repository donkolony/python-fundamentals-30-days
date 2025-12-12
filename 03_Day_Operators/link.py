

"""Day 03: Operators"""

"""
Question: Calculate the value of y (y = x**2 + 6x + 9).
Try to use different x values and figure out at what x value y is going to be 0.
"""


a, b, c = 1, 6, 9
d = (b**2) - (4 * a * c)

x1 = (- b + d**0.5) / (2 * a)
x2 = (- b - d**0.5) / (2 * a)

print(f"y is 0 when x is: {x1} and {x2}")

# Advanced Method Using Loops :)

for x in range(-20, 21):   # check x from -20 to 20
    y = x**2 + 6 * x + 9
    if y == 0:
        print("y is 0 when x is:", x)






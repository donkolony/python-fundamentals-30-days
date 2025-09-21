"""Function as a Parameter"""


def sum_numbers(nums):
    return sum(nums)

# print(sum_numbers([2, 5, 6, 43]))


def higher_order_function_1(f, lst):
    total = f(lst)
    return total


# Passing the function as an argument
# print(higher_order_function_1(sum_numbers, [2, 5, 6, 43]))


"""Function as a Return Value"""


def square(x):          # a square function
    return x ** 2


def cube(x):            # a cube function
    return x ** 3


def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)


def higher_order_function_2(f_type):
    if f_type == "square":
        return square
    elif f_type == "cube":
        return cube
    elif f_type == "absolute":
        return absolute
    else:
        return "Please enter either square, cube or absolute"


result = higher_order_function_2('square')
print(result(3))
result = higher_order_function_2('cube')
print(result(3))
result = higher_order_function_2('absolute')
print(result(-3))
result = higher_order_function_2('normal')
print(result)

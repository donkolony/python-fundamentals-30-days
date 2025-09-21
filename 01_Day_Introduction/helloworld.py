# The print() built-in function takes one or more arguments as follows print("argument1", "argument2", "argument3")

# Day 1 - 30DaysOfPython Challenge
print(2 + 3)    # addition(+)
print(3 -1)     # subtraction(-)
print(2 * 3)    # multiplication(*)
print(3 / 2)    # division(/)
print(3 ** 2)   # exponential(**)
print(3 % 2)    # modulus(%)
print(3 // 2)   # Floor division operator(//)

# Checking data types
print(type(10))                     # Int
print(type(3.14))                   # Float
print(type(1 + 3j))                 # Complex number     
print(type("Don"))                  # String
print(type([4,5,6]))                # List  
print(type({"name": "Don"}))        # Dictionary    
print(type({9.8, 3.14, 2.7}))       # Set      
print(type((9.8, 3.14, 2.7)))       # Tuple   

# # Level 3
_int = 20
_float = 1.05
_complex = 1 - 4j
_string = "Don and Mike"
_bool = True
my_list = [5, 4, 3, 2, 1]
my_tuple = (4, 5, 6, 7)
my_set = {4, 5, 4 , "Don"}
my_dict = {
    "name_1": "Don",
    "name_2": "Mike"
}

print(type(my_dict))

pointA = (2,3)
pointB = (10,8)
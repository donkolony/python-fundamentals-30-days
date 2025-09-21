# Normal import
import math
"""
we have to call the modules name every time we want to use ots function/method
"""
# print(math.pi)           
# print(math.sqrt(2))     
# print(math.pow(2, 3))    
# print(math.floor(9.81))
# print(math.ceil(9.81))   
# print(math.log10(100))

# Import a single function
from math import pi
# print(pi)

# Import multiple functions (only importing the functions we want)
"""
We can call the function name directly instead of calling the module (math) every time we want to use its function
"""
from math import pi, sqrt, pow, floor, ceil, log10
# print(pi)                 
# print(sqrt(2))           
# print(pow(2, 3))          
# print(floor(9.81))        
# print(ceil(9.81))         
# print(math.log10(100))   

# Importing all functions from the module
"""
We can call the function name directly instead of calling the module (math) every time we want to use its function
"""
from math import *
# print(pi)                  
# print(sqrt(2))            
# print(pow(2, 3))           
# print(floor(9.81))         
# print(ceil(9.81))          
# print(math.log10(100)) 

# Import but renaming the function/method
from math import pi as PI
# print(PI)

from random import random, randint
# print(random())
# print(randint(5, 20))


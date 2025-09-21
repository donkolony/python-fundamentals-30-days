# 💻 Exercises: Day 11

################# Exercises: Level 1 ################# 
#1
def add_two_numbers(num1, num2):
    return num1 + num2

# print(add_two_numbers(-99, 8))

#2
def area_of_circle(radius):
    pi = 3.141592653589793
    area = int(pi * radius**2)
    return area

# print(f"Area of circle is: {area_of_circle(10)}")

#3
def add_all_nums(*args):
    for item in args:
        if not isinstance(item, (int, float)):
            return "Error"

    return sum(args)
        
# print(add_all_nums(3,54,6))
# print(add_all_nums(3,"54",6))

#4
def convert_celsius_to_fahrenheit(deg):
    fahrenheit = (deg * 9/5) + 32
    return f"{int(fahrenheit)} degrees celsius"

# print(convert_celsius_to_fahrenheit(30))
# print(convert_celsius_to_fahrenheit(-15))

#5
def check_season(month):
    if month in ["September", "October", "November"]:
        return "It is Autumn 🍂"
    elif month in ["December", "January",  "February"]:
        return "It is Winter 🥶"
    elif month in ["March", "April", "May"]:
        return "It is Spring 🌴"
    elif month in ["June", "July",  "August"]:
        return "It is Summer 😍"
    else:
        return "Month does not exist"
    
# print(check_season("December"))
# print(check_season("November"))
# print(check_season("July"))
# print(check_season("March"))

#6
def calculate_slope(point1, point2):
    upper = point2[1] - point1[1]
    lower = point2[0] - point1[0]
    slope = int(upper / lower)
    return slope
    
# print(f"The slope is: {calculate_slope((2,4), (3,7))}")
# print(f"The slope is: {calculate_slope((2,3), (4,7))}")
 
#7
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return "No real roots"
    
    x1 = int((-b + discriminant**0.5) / (2*a))
    x2 = int((-b - discriminant**0.5) / (2*a))

    return {x1, x2}

# print(solve_quadratic_eqn(1, -2, -15))
# print(solve_quadratic_eqn(1, 3, 6))

#8
def print_list(my_list):
    for item in my_list:
        print(item)
    
# print_list([1,2,3,4])
# print_list(["Don", "Mike", "Mbasa"])

# 9
def reverse_list(my_lists):
    reversed_list = []
    for item in my_lists:
        reversed_list.insert(0, item)
    return reversed_list
    
# print(reverse_list([1,2,4,5,3,8]))
# print(reverse_list(["Don", "Mike", "Mbasa"]))

#10
def capitalize_list_items(lists):
    cap_list = []
    for item in lists:
        cap_list.append(item.capitalize())
        
    return cap_list

# print(capitalize_list_items(["apple", "banana"]))
# print(capitalize_list_items(["orange", "mango"]))

#11
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
def add_item(food_staff, item):
    new_list = food_staff.copy()
    new_list.append(item)
    return new_list

# print(add_item(food_staff, "Peach"))
# print(add_item(food_staff, "Banana"))
# print(food_staff)

#12
companies = ['Microsoft', 'Amazon', 'Google', 'IBM']
def remove_item(my_list, item):
    new_list = my_list.copy()
    if item in new_list:
        new_list.remove(item)
    return new_list

# print(remove_item(companies, "IBM"))
# print(remove_item(companies, "Google"))
# print(companies)

# 13
def sum_of_numbers(number):
    total = 0
    for num in range(number + 1):
        total += num
    
    return total

# print(f"Sum of all numbers in that range is: {sum_of_numbers(5)}")
# print(f"Sum of all numbers in that range is: {sum_of_numbers(10)}")
# print(f"Sum of all numbers in that range is: {sum_of_numbers(100)}")

#14
def sum_of_odds(numbers):
    sum_of_odds = 0
    for number in range(numbers + 1):
        if number % 2 != 0:
            sum_of_odds += number

    return sum_of_odds

# print(sum_of_odds(10))
# print(sum_of_odds(15))
# print(sum_of_odds(20))

"""Improved Version (from chat)"""
def sum_of_odds(numbers):
    return sum(range(1, numbers + 1, 2))

# print(sum_of_odds(10))
# print(sum_of_odds(15))
# print(sum_of_odds(20))

#15
def sum_of_even(numbers):
    sum_of_even = 0
    for number in range(numbers + 1):
        if number % 2 == 0:
            sum_of_even += number

    return sum_of_even

# print(sum_of_even(10))
# print(sum_of_even(15))
# print(sum_of_even(20))

"""Improved version (from chat)"""
def sum_of_even(numbers):
    return sum(range(0, numbers + 1, 2))

# print(sum_of_even(10))
# print(sum_of_even(15))
# print(sum_of_even(20))


#################  Exercises: Level 2 ################# 
#1
def evens_and_odds(number):
    even_num = 0
    odd_num = 0

    for num in range(number + 1):
        if num % 2 == 0:
            even_num += 1

        else:
            odd_num += 1
    
    return f"The number of odds are {odd_num} \nThe number of evens are {even_num}"

# print(evens_and_odds(5))
# print(evens_and_odds(10))
# print(evens_and_odds(100))


#2
"""For Testing Purpose"""
from math import factorial
# print(f"Factorial using math import: {factorial(10)}")


def factorial(number):
    fact = 1

    for num in (range(1, number + 1)):
        fact *= num

    return fact
        
# print(f"Factorial using general knowledge: {factorial(2)}")
# print(f"Factorial using general knowledge: {factorial(5)}")
# print(f"Factorial using general knowledge: {factorial(7)}")

#3
def is_empty(collection):
    if len(collection) == 0:
        return "Empty"
    else:
        return "Not Empty"
    
# print(is_empty(()))
# print(is_empty((2,)))
# print(is_empty([]))
# print(is_empty([1,2,3]))


#4
""" 4 (i) Mean - average of a set"""
def calculate_mean(numbers):
    mean = sum(numbers) / len(numbers)

    return mean

# print(calculate_mean([1, 2, 3, 4, 5]))
# print(calculate_mean([1, -2, 13, 4, 11]))


""" 4 (ii) Median - middle number"""
def calculate_median(numbers):
    lst_sorted  = sorted(numbers)
    lst_len = len(lst_sorted)

    if lst_len % 2 == 0:
        mid1 = lst_sorted[lst_len//2 - 1]
        mid2 = lst_sorted[lst_len//2]
        median = (mid1 + mid2) / 2
    else:
        median = lst_sorted[lst_len//2]

    return median

# print(calculate_median([1, 2, 3, 4, 5]))  # 3
# print(calculate_median([1, 2, 3, 4, 5, 9])) # 3.5
 

""" 4 (iii) Mode - number that appears the most"""
import statistics
x = [1, 2, 1, 2, 2, 5, 7, 7]
# print(f"Element with highest freq is: {statistics.multimode(x)}")

import collections
occurrence_count = collections.Counter(x)
# Find highest freq
max_freq = max(occurrence_count.values())
# Find all numbers that appear this many times
modes = []
for number, count in occurrence_count.items():
    if count == max_freq:
        modes.append(number)

# print(f"Frequencies: {occurrence_count}")
# print(f"Modes: {modes}")

"""
List:      [1, 2, 2, 3, 3, 3]

Counter:   {
    1: 1,   # 1 appears once
    2: 2,   # 2 appears twice
    3: 3    # 3 appears three times
}

- .values() → [1, 2, 3] (the counts)
- .keys() → [1, 2, 3] (the unique elements)
- .items() → [(1,1), (2,2), (3,3)]
"""


""" Manually Method 1: """
def calculate_mode(numbers):
    freq_element = max(set(numbers),  key=numbers.count)
    return freq_element

# print(calculate_mode([1, 2, 1, 2, 5, 7]))
# print(calculate_mode((1, 2, 1, 2, 7, 7, 7)))


""" Manually Method 2: """
def calculate_mode(numbers):
    counter = 0
    act_num = numbers[0]

    for num in numbers:
        occurrence_count = numbers.count(num) #(i=1) = 1 (i=2) = 3
        if occurrence_count > counter: #(i=1): 1>0 (i=2): 3>1
            counter = occurrence_count  #(i=1) = 1 (i=2) = 3
            act_num = num #(i=1) = 14 (i=2) = 7
        
    return act_num

# print(calculate_mode([1, 2, 1, 2, 5, 7]))
# print(calculate_mode((1, 2, 1, 2, 7, 7, 7)))


""" 4 (iv) Range - max - min"""
def calculate_range(numbers):
    return max(numbers) - min(numbers)

# print(calculate_range([19, 4, 8, 10, 17]))
# print(calculate_range((3, -10, 11, 6))) 
# print(calculate_range({4, 8, 7, 3, 15}))
 

""" 4 (v) Variance - how spread out the data is from the mean"""
y = [1, 2, 15, 3, 4, 5, 11]
# print(f"Variance using import: {statistics.variance(y)}")

def calculate_variance(numbers):
    sample_mean_squared = 0
    mean = calculate_mean(numbers)

    for num in numbers:
        sample_mean_squared += (num - mean)**2
    
    sample_variance = sample_mean_squared / (len(numbers) - 1)
    return sample_variance
    
 
# print(calculate_variance([1, 2, 15, 3, 4, 5, 11]))
# print(calculate_variance([1, 2, 15, 3, 4, 5]))
# print(calculate_variance([4, -7, 8, 6, 23, 7, 3, 5, -11]))



""" 4 (vi) Standard deviation - square root of th e variance"""
import math
# print(math.sqrt(26.80952380952381))
# print(math.sqrt(26.0))
# print(math.sqrt(92.19444444444444))

import statistics
# print(statistics.stdev([1, 2, 15, 3, 4, 5, 11]))

def calculate_std(numbers):
    variance = calculate_variance(numbers)
    standard_deviation = (variance)**0.5
    return standard_deviation

# print(calculate_std([1, 2, 15, 3, 4, 5, 11]))
# print(calculate_std([1, 2, 15, 3, 4, 5]))
# print(calculate_std([4, -7, 8, 6, 23, 7, 3, 5, -11]))


################# Exercises: Level 3 ################# 
#1
def is_prime (number):
    if number <= 1:
        return False
    for num in range(2, int(number/2) + 1):
        if number % num == 0:
            return f"{number} is not a prime number"
        
    return f"{number} is a prime number"
    
# print(is_prime(1))
# print(is_prime(7))
# print(is_prime(8))
# print(is_prime(9))

#2
def unique_list(items):
    if len(items) == len(set(items)):
        return "Items are unique"
    else:
        return "Items not unique"

# print(unique_list([3,4,2,3,5,3]))
# print(unique_list([1, 2, 3, 5, 4]))


#3
def same_data_type(items):
    if not items:
        return True
    first_item_type = type(items[0])
    return all(type(item) is first_item_type for item in items)

# print(same_data_type([4, -7, 8, 6, 23, 7, 3]))
# print(same_data_type([4, -7, "8", 6, 23, 7, 3]))
# print(same_data_type(["apple", "banana", "peach"]))


#4
def valid_python_variable(variable):
    return variable.isidentifier()

# print(valid_python_variable("string"))
# print(valid_python_variable("_list"))
# print(valid_python_variable("2my_data"))
# print(valid_python_variable("my-data"))
# print(valid_python_variable("myData"))


#5 (i) - same question as one in the loop section
"""
APPROACH
- Loop through all countries and collect all languages.
- Count the frequency of each language.
- Sort by frequency.
- Return top n (10 or 20).
"""
from collections import Counter
import countries_data as cd


unique_lang_set = set()
countries_list = []
population_list = []

def most_spoken_languages(top_n=10):
    all_languages = []

    for country in cd.countries:
        all_languages.extend(country["languages"])

    language_counts = Counter(all_languages)

    most_common_languages = language_counts.most_common(top_n)

    top_languages = []
    for lang_tuple in most_common_languages:
        language_name = lang_tuple[0]
        top_languages.append(language_name)


    return top_languages

# print(most_spoken_languages(5))
# print(most_spoken_languages(10))
# print(most_spoken_languages(20))

#5 (ii) same question as one in the loop section
def most_populated_countries(top_n=10):
    country_pop_list = []
    for country in cd.countries:
        # Adds the name of country and its population as a tuple inside the list
        country_pop_list.append((country["name"], country["population"]))

    # Sort the list by population in descending order
    country_pop_list.sort(key=lambda x: x[1], reverse=True)


    # Get the top `top_n` countries
    top_countries = country_pop_list[:top_n]

    top_countries_name = []
    # Extract only the country names from the tuples
    for country in top_countries:
        top_countries_name.append(country[0])
        
    return top_countries_name
    
# print(most_populated_countries(5))
# print(most_populated_countries(10))
# print(most_populated_countries(20))




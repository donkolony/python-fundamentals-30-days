from person_account import PersonAccount
from stats import Statistics

"""Day 21: Classes and Objects"""

print("--------------------------------------")
print("Exercises: Level 1")
print("--------------------------------------")


"""
# 1.1   Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make
        function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, 
        mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, 
        and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations 
        as methods for the Statistics class.
"""
print("Question 1.1")


ages = [
    31,
    26,
    34,
    37,
    27,
    26,
    32,
    32,
    26,
    27,
    27,
    24,
    32,
    33,
    27,
    25,
    26,
    38,
    37,
    31,
    34,
    24,
    33,
    29,
    26,
]

data = Statistics(ages)

print(f"Count {data.count()}")
print(f"Sum {data.sum()}")
print(f"Min {data.min()}")
print(f"Max {data.max()}")
print(f"Range {data.range()}")
print(f"Mean {data.mean()}")
print(f"Median {data.median()}")
print(f"Mode {data.mode()}")
print(f"Variance {data.var()}")
print(f"Standard Deviation {data.std()}")
print(f"Frequency {data.freq_dist()}")

"""
# 1.2   Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, 
        account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for 
        expenses.
"""
print("\nQuestion 1.2")
person = PersonAccount("Don", "Kolony")

person.add_income("Salary", 5000)
person.add_income("Freelance", 1500)

person.add_expense("Rent", 2000)
person.add_expense("Food", 800)

print(person.account_info())

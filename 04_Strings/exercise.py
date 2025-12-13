"""Day 04: String"""


# 1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print("\nQuestion 1")
thirty = 'Thirty', 'Days', 'Of', 'Python'
print(" ".join(thirty))

# 2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print("\nQuestion 2")
coding = 'Coding', 'For', 'All'
print(" ".join(coding))

# 3 Declare a variable named company and assign it to an initial value "Coding For All".
print("\nQuestion 3")
company = "Coding For All"

# 4 Print the variable company using print().
print("\nQuestion 4")
print(company)

# 5 Print the length of the company string using len() method and print().
print("\nQuestion 5")
print(f"length of word {company} is: {len(company)}")

# 6 Change all the characters to uppercase letters using upper() method.
print("\nQuestion 6")
print(company.upper())

# 7 Change all the characters to lowercase letters using lower() method.
print("\nQuestion 7")
print(company.lower())

# 8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print("\nQuestion 8")
print(f"Formatting using capitalize: {company.capitalize()}")
print(f"Formatting using title: {company.title()}")
print(f"Formatting using swapcase: {company.swapcase()}")

# 9 Cut(slice) out the first word of Coding For All string.
print("\nQuestion 9")
print(company[:6])

# 10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
print("\nQuestion 10")
print(company.index("Coding"))
print(company.find("Coding"))

# 11 Replace the word coding in the string 'Coding For All' to Python.
print("\nQuestion 11")
print(company.replace("Coding", "Python"))

# 12 Change Python for Everyone to Python for All using the replace method or other methods.
python = "Python For Everyone"
print("\nQuestion 12")
print(python.replace("Everyone", "All"))

# 13 Split the string 'Coding For All' using space as the separator (split()) .
print("\nQuestion 13")
print(company.split())

# 14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("\nQuestion 14")
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_companies.split(","))

# 15 What is the character at index 0 in the string Coding For All.
print("\nQuestion 15")
print(company[0])

# 16 What is the last index of the string Coding For All.
print("\nQuestion 16")
print(company[-1])

# 17 What character is at index 10 in "Coding For All" string.
print("\nQuestion 17")
print(company[10])

# 18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
print("\nQuestion 18")
words = python.split()
acronym = words[0][0] + words[1][0] + words[2][0]
print(acronym)

# 19 Create an acronym or an abbreviation for the name 'Coding For All'.
print("\nQuestion 19")
words = company.split()
acronym = words[0][0] + words[1][0] + words[2][0]
print(acronym)

# 20 Use index to determine the position of the first occurrence of C in Coding For All.
print("\nQuestion 20")
print(
    f"position of the first occurrence of C in Coding For All is {company.index("C")}")

# 21 Use index to determine the position of the first occurrence of F in Coding For All.
print("\nQuestion 21")
print(
    f"position of the first occurrence of F in Coding For All is {company.index("F")}")

# 22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
print("\nQuestion 22")
coding_for_all_people = "Coding For All People"
print(
    f"position of the last occurrence of l in Coding For All People is {company.rfind("l")}")


# 23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("\nQuestion 23")
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index("because"))
print(sentence.find("because"))

# 24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("\nQuestion 24")
print(sentence.rfind("because"))


# 25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("\nQuestion 25")
print(sentence[31:54])

# 26 Does ''Coding For All' start with a substring Coding?
print("\nQuestion 26")
print(company.startswith("Coding"))

# 27 Does 'Coding For All' end with a substring coding?
print("\nQuestion 27")
print(company.endswith("coding"))

# 28 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print("\nQuestion 28")
coding_for_all = '   Coding For All      '
print(coding_for_all.strip())

"""
# 29 Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python
"""
variable_1 = "30DaysOfPython"
variable_2 = "thirty_days_of_python"
print("\nQuestion 29")
print(variable_1.isidentifier())  # False
print(variable_2.isidentifier())  # True

# 30 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
print("\nQuestion 30")
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("#".join(python_libraries))

# 31 Use the new line escape sequence to separate the following sentences.
"""
I am enjoying this challenge.
I just wonder what is next.
"""
print("\nQuestion 31")
print("I am enjoying this challenge.\nI just wonder what is next.")

# 32 Use a tab escape sequence to write the following lines
"""
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
"""
print("\nQuestion 32")
print("Name\t\tAge\tCountry\t\tCity")
print("Asabeneh\t250\tFinland\t\tHelsinki")

# 33 Use the string formatting method to display the following:
print("\nQuestion 33")
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, area))

# 34 Make the following using string formatting methods:
"""
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
"""
num_1 = 8
num_2 = 6
print("\nQuestion 34")
print(f"{num_1} + {num_2} = {num_1 + num_2}")
print(f"{num_1} - {num_2} = {num_1 - num_2}")
print(f"{num_1} * {num_2} = {num_1 * num_2}")
print(f"{num_1} / {num_2} = {num_1 / num_2:.2f}")
print(f"{num_1} % {num_2} = {num_1 % num_2}")
print(f"{num_1} // {num_2} = {num_1 // num_2}")
print(f"{num_1} ** {num_2} = {num_1 ** num_2}")

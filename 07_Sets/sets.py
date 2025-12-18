"""Day 07: Sets"""

# Exercises: Day 7


print("--------------------------------------")
print("Exercises: Level 1")
print("--------------------------------------")
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1 Find the length of the set it_companies
print("\nQuestion 1")
print(f"Length of the set it_companies: {len(it_companies)}")


# 2 Add 'Twitter' to it_companies
print("\nQuestion 2")
it_companies.add("Twitter")


# 3 Insert multiple IT companies at once to the set it_companies
print("\nQuestion 3")
it_companies.update({"BBD", "Tesla", "Meta"})

# 4 Remove one of the companies from the set it_companies
print("\nQuestion 4")
removed_company = it_companies.pop()


# 5 What is the difference between remove and discard
print("\nQuestion 5")
"""
remove(): removes an element from a set, it must be a member. Raises a KeyError if element not a member 
discard(): removes an element from a set if it is a member. Unlike remove(), discard() does not raise a KeyError if element not a member
"""

print("--------------------------------------")
print("Exercises: Level 2")
print("--------------------------------------")


A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}


# 1 Join A and B
print("\nQuestion 1")
AB = A.union(B)

# 2 Find A intersection B
print("\nQuestion 2")
print(f"common elements between A and B:{A.intersection(B)}")


# 3 Is A subset of B
print("\nQuestion 3")
print(f"Is A subset of B? {A.issubset(B)}")

# 4 Are A and B disjoint sets
print("\nQuestion 4")
print(
    f"Are A and B disjoint sets (Does A and B have something in common)? {A.isdisjoint(B)}")

# 5 Join A with B and B with A
print("\nQuestion 5")
A.update(B)
B.update(A)

print(A)
print(B)

# 6 What is the symmetric difference between A and B
print("\nQuestion 6")
print(f"Symmetric difference between A and B: {A.symmetric_difference(B)}")

# 7 Delete the sets completely
print("\nQuestion 6")
del A, B


print("--------------------------------------")
print("Exercises: Level 3")
print("--------------------------------------")

age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print("\nQuestion 1")
age_set = set(age)
print(f"Length of list {len(age)} vs Length of set {len(age_set)}")

# 2 Explain the difference between the following data types: string, list, tuple and set
print("\nQuestion 2")
print(""" 
String:  
List: A data collection that is ordered, indexable and mutable
Tuple: A data collection that is ordered, indexable and immutable
Set: A data collection that is unordered, un-indexed and stores unique elements
""")

# 3 I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
print("\nQuestion 3")
sentence = "I am a teacher and I love to inspire and teach people."
print(f"There are {len(set(sentence.split()))} unique words in the sentence")

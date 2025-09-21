# Exercises: Level 1

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


#1
# print(len(it_companies))

#2
# it_companies.add("Twitter")
# print(it_companies)

#3
# it_companies.update(["Bash", "Netflix"])
# print(it_companies)

#4
# it_companies.remove("Google")
# print(it_companies)

#5
# it_companies.discard("Bash")
# print(it_companies)


# Exercises: Level 2
#1
# print(A.union(B))

#2
# print(A.intersection(B))

#3
# print(A.issubset(B))

#4
# print(A.isdisjoint(B))

#5
# print(A.update(B))
# print(B.update(A))

#6
# print(A.symmetric_difference(B))

#7
# del it_companies
# del A
# del B
# del age

# Exercises: Level 3

#1
age_set = set(age)
# print(age_set)
# print(len(age) == len(age_set))

#2
"""
string: 
list
tuple
set
"""

unique_words = "I am a teacher and I love to inspire and teach people"
str_to_lst = unique_words.split()
lst_to_set = set(str_to_lst)
 
# print(unique_words)
# print(str_to_lst)
# print(f"There are {len(lst_to_set)} words")



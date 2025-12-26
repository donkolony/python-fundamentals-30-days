""" Day 17: Exception Handling """


print("--------------------------------------")
print("Exercises: Level 1")
print("--------------------------------------")

# 1.1 Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
print("Question 1.1")
names = ['Finland', 'Sweden', 'Norway',
         'Denmark', 'Iceland', 'Estonia', 'Russia']


*nordic_countries, es, ru = names

print(nordic_countries)
print(es)
print(ru)

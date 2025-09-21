# Examples

"""
1. Union → “Everything in both, no duplicates.”
"""
# a = {1, 2, 3}
# b = {3, 4, 5}
# a.union(b)  # {1, 2, 3, 4, 5}

"""
2. Intersection → “Only the stuff we share.”
"""
# a = {1, 2, 3}
# b = {3, 4, 5}
# a.intersection(b)  # {3}

"""
3. Difference → “What I have, but you don't.”
"""
# a = {1, 2, 3}
# b = {3, 4, 5}
# a.difference(b)  # {1, 2}  (from a only)
# b.difference(a)  # {4, 5}  (from b only)


"""
4. Symmetric Difference → “What's different in each, no sharing - What we don't have in common.”
"""
# a = {1, 2, 3}
# b = {3, 4, 5}
# a.symmetric_difference(b)  # {1, 2, 4, 5}

"""
5. Subset → “I'm inside you.”
"""
# a = {1, 2}
# b = {1, 2, 3}
# a.issubset(b)  # True


"""
6. Superset → “I contain you.”
"""
a = {1, 2, 3}
b = {2, 3}
print(a.issuperset(b))  # True


"""
7. Disjoint → “We have nothing in common.”
"""
# a = {1, 2}
# b = {3, 4}
# a.isdisjoint(b)  # True

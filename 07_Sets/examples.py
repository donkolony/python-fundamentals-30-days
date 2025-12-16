A = {'item1', 'item2', 'item3', 'item4'}
B = {'item3', 'item2'}

common = A.intersection(B)
diff = A.difference(B)  # What exists in A but NOT in B
sym_diff = A.symmetric_difference(B)

print(A)
print(B)
print(f"common elements between A and B: {common}")
print(f"difference between A and B: {diff}")
print(f"symmetric difference between A and B: {sym_diff}")


"""
1. Difference
Difference is one-way

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A - B   # or A.difference(B) -> {1, 2} 
B - A   # or B.difference(A) -> {5, 6}

👉 Meaning:
“What exists in A but NOT in B”

So:

A - B ≠ B - A


2. Symmetric Difference
Symmetric difference is two-way
A ^ B     # or A.symmetric_difference(B) -> {1, 2, 5, 6}

👉 Meaning:
“What's unique across both sets”

It removes anything they share and keeps:

    things only in A
    things only in B
    
"""

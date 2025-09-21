"""
nested loop = A loop within another loop (outer, inner)
    outer_loop:
        inner_loop:
            # code for inner_loop
        #code for outer loop
"""

"""
# Outer loop iterates 3 times
# Inner loop iterates 9 times
# for every iteration in the outer loop, the inner loop iterates 9 times. Thats one cycle
# It repeats the process until the outer loop completes its iteration (e.g range of 3, which iterates 3 times)
"""

# for outer in range(3):
#     for inner in range(1, 10):
#         print(inner, end="")
#     print()

# Example : Create a Square
# rows = int(input("enter the # of rows: "))
# cols = int(input("enter the # of cols: "))
# symbol = input("enter a symbol to use: ")

# for row in range(rows):
#     for col in range(cols):
#         print(symbol, end="")
#     print()

# x = (1,2,3,4,5,6,7,8,9,10)


# credit_card = "1234-5678-9012-3456"

# for i in credit_card:
#     if i == "-":
#         i = "#"
#     print(i)


lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

# for x in lst1:
#     for y in lst2:
#         print(x, y, end="\t")
#     print()
 
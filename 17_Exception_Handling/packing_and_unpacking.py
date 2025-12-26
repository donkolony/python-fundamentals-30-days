""" 
Packing (putting things INTO a box)
Meaning:
    "Put many things into one box"

Example (Real Life)
    You throw all your toys into one toy box.
"""

# Packing in code example


def play(*toys):
    print(toys)


# All toys are packed into one box called toys
# ["teddy", "car", "dino"]
play("teddy", "car", "dino")


def plays(**toys):
    print(toys)


# All toys are packed into one box (dictionary)
# {'teddy': 1, 'car': 1, 'dino': 1}
plays(teddy=1, car=1, dino=1)


""" 
Unpacking (taking things OUT of the box) 
Means:
    "Take things OUT of the box (dictionary)"

Example (Real Life)
    You open the toy box and put each toy on the floor
"""
toys = ["teddy", "car", "dino"]

print("\nList Unpacking Example")
play(*toys)  # Toys are taken out of the box


toys = {"teddy": 1, "car": 1}

print("\nDictionary Unpacking Example")
plays(**toys)

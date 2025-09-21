# Mastery Loops With ChatGPT

"""
Day 1 - Loop Basics
Focus: for and while loops.

Exercises
1. Print numbers from 1 to 10 using a for loop.
2. Print numbers from 1 to 10 using a while loop.
3. Print only even numbers between 1 and 20.
4. Count down from 10 to 1.
"""
#1
# for i in range(1, 11):
#     print(i)

#2 
# counter = 1
# while counter < 11:
#     print(counter)
#     counter += 1

#3
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)
#     else:
#         continue

"""
for i in range(2, 21, 2):
    print(i)

"""

#4
# for i in reversed(range(1, 11)):
#     print(i)

"""
for i in range(10, 0, -1):
    print(i)
"""

# counter = 10
# while counter >= 1:
#     print(counter)
#     counter -= 1


"""
Day 2 - Break & Continue
Focus: Controlling loop flow.

Exercises
1. Print numbers 1-10, but stop when you hit 5 (break).
2. Print numbers 1-10, but skip number 5 (continue).
3. Ask the user to enter a password until they get it right.
"""
#1 
# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)

# counter = 1
# while counter <= 10:
#     if counter == 5:
#         break 
#     print(counter)
#     counter += 1

#2
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)


# counter = 1
# while counter <= 10:
#     if counter == 5:
#         counter += 1
#         continue
#     print(counter)
#     counter += 1

#3
password = "$vscodE"
user_password = input("enter password: ")

while True:
    if user_password == password:
        print("Successful")
        break
    else:
        print("Incorrect, try again.")

"""
Pro tips for Day 2
- You almost never need else: after a break or continue check — it just adds extra indentation.
- When using continue, make sure counters still increment, otherwise you can create infinite loops.
- In infinite loops (while True:), make sure there’s a break path.
"""
 


    
   





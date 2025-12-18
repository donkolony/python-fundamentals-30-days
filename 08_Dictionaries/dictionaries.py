"""Day 08: Dictionary"""

# Exercises: Day 8

print("--------------------------------------")
print("Exercises: Level 1")
print("--------------------------------------")

# 1 Create an empty dictionary called dog
print("\nQuestion 1")
dog = {}

# 2 Add name, color, breed, legs, age to the dog dictionary
print("\nQuestion 2")
dog["name"] = "Whoofy"
dog["color"] = "brown"
dog["breed"] = "Congolese shepherd"
dog["legs"] = 4
dog["age"] = 12

print(dog)

# 3 Create a student dictionary and add required keys  •
print("\nQuestion 3")
student = {
    "first_name": "Don",
    "last_name": "Pablo",
    "gender": "male",
    "age": 23,
    "marital_status": "single",
    "skills": ["Python", "HTML", "CSS", "JavaScript", "React"],
    "country": "DR Congo",
    "city": "Kinshasa",
    "address": {
        "street": "123 Cape Town",
        "post_code": 7538
    }
}

# 4 Get the length of the student dictionary
print("\nQuestion 4")
student_length = len(student)
print(f"Length of student dictionary is {student_length}")

# 5 Get the value of skills and check the data type
print("\nQuestion 5")
student_skills = student["skills"]
print(f"Data type of skills: {type(student_skills)}")

# 6 Modify the skills values by adding one or two skills
print("\nQuestion 6")
student_skills.append("NodeJS")
student_skills.append("Java")

print(student)

# 7 Get the dictionary keys as a list
print("\nQuestion 7")
student_keys = list(student.keys())
print(f"Dictionary keys as a list: {student_keys}")

# 8 Get the dictionary values as a list
print("\nQuestion 8")
student_values = list(student.values())
print(f"Dictionary values as a list: {student_values}")

# 9 Change the dictionary to a list of tuples using items() method
print("\nQuestion 9")
student_items = list(student.items())
print(f"Dictionary to a list of tuples: {student_items}")

# 10 Delete one of the items in the dictionary
print("\nQuestion 10")
del student["skills"]

# 11 Delete one of the dictionaries
del student

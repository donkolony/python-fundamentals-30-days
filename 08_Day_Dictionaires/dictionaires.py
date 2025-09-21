# 💻 Exercises: Day 8

#1
dog = {}

#2
dog["name"] = "Tesla"
dog["color"] = "white"
dog["breed"] = "pitbull"
dog["legs"] = 4
dog["age"] = 10

#3
student = {
    "first_name" : "Don",
    "last_name" : "Kolony",
    "gender" : "male",
    "age" : 25,
    "marital_status" : "single",
    "skills" : ["python", "html", "css", "javascript"],
    "country" : "DR Congo",
    "city" : "Kinshaha",
    "address" :"Cape Town"
}

#4
# print(f"Length of student dict: {len(student)}")

#5
# print(type(student["skills"]))

#6
student["skills"].append("react")
# print(student)

#7
# print(student.keys())

#8
# print(student.values())

#9
# print(student.items())

#10
# print(student.pop("first_name")) #Don
# print(student.popitem()) #("address", "Cape Town")
# del student["skills"] 

#11
# del dog

education = student.update({"education": "civil engineering"})
print(student)
 

 




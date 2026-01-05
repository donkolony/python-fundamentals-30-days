# =========================
# PARENT CLASS
# =========================
# Think of a class as a "blueprint"
# Just like a blueprint for a house 🏠


class Person:
    def __init__(
        self,
        firstname="Don",
        lastname="Kolony",
        age=23,
        country="DR Congo",
        city="Kinshasa",
    ):
        # These are things every Person has
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

        # Each person starts with an empty list of skills 🎒
        self.skills = []

    def person_info(self):
        # This function tells us information about the person
        return (
            f"{self.firstname} {self.lastname} is {self.age} years old. "
            f"He lives in {self.city}, {self.country}"
        )

    def add_skills(self, skill):
        # This function adds a new skill to the person's skill list
        self.skills.append(skill)


"""
STUDENT CLASS (CHILD CLASS)

A Student IS A Person 👨‍🎓
So Student can use everything Person has.
"""


class Student(Person):
    """
    We are NOT writing __init__ here.

    This means:
    - Student will AUTOMATICALLY use Person's __init__
    - Student gets all properties and methods from Person

    This is called INHERITANCE 👪
    """

    pass  # "pass" means: nothing extra for now


# =========================
# USING THE STUDENT CLASS
# =========================

# Creating student objects (objects are real things made from a class)
s1 = Student("Ben", "Doe", 30, "France", "Paris")
s2 = Student("Jake", "Paul", 46, "France", "Lyon")

print(s1.person_info())

# Adding skills to s1
s1.add_skills("JavaScript")
s1.add_skills("React")
s1.add_skills("Python")

print(s1.skills)

print(s2.person_info())

# Adding skills to s2
s2.add_skills("Organizing")
s2.add_skills("Marketing")
s2.add_skills("Digital Marketing")

print(s2.skills)


# =========================
# METHOD OVERRIDING
# =========================
# Now we want a Student with EXTRA info (gender)
# And we want to CHANGE how person_info works


class Student1(Person):
    def __init__(
        self,
        firstname="Don",
        lastname="Kolony",
        age=23,
        country="DR Congo",
        city="Kinshasa",
        gender="male",
    ):
        # This property belongs ONLY to Student1
        self.gender = gender

        # super() calls the parent (Person) __init__
        # This gives us firstname, lastname, age, country, city
        super().__init__(firstname, lastname, age, country, city)

    def person_info(self):
        # Change "He" or "She" depending on gender
        gender_word = "He" if self.gender == "male" else "She"

        return (
            f"{self.firstname} {self.lastname} is {self.age} years old. "
            f"{gender_word} lives in {self.city}, {self.country}."
        )


print("\n")

# Creating Student1 objects
s1 = Student1("Mark", "Petersen", 45, "France", "Paris", "male")
s2 = Student1("Maree", "Lopez", 28, "South Africa", "Cape Town", "female")

print(s1.person_info())

# Adding skills to s1
s1.add_skills("JavaScript")
s1.add_skills("React")
s1.add_skills("Python")

print(s1.skills)

print(s2.person_info())

# Adding skills to s2
s2.add_skills("Organizing")
s2.add_skills("Marketing")
s2.add_skills("Digital Marketing")

print(s2.skills)

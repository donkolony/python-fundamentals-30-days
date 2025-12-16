from pprint import pprint


person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}


person["job_title"] = "Python Instructor"
person["skills"].append("HTML")


print(person)

# Removes the item with the specified key name inside a dictionary
removed_pop = person.pop("skills")
print("\n")
pprint(removed_pop)

# Remove the last item inside dictionary
removed_popitem = person.popitem()
print("\n")
print(removed_popitem)

# Del an item with specified key name
del person['age']
print("\n")
pprint(person)

# Changing Dictionary to a List of Items
person_list = person.items()
print('\n')
print(person_list)

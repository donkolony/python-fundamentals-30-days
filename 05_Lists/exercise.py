"""Day 05: Lists"""

# Exercises: Day 5

# Exercises: Level 1


print("--------------------------------------")
print("Exercises: Level 1")
print("--------------------------------------")

# 1 Declare an empty list
print("\nQuestion 1")
empty_list = list()
print(f"Length of of list is = {len(empty_list)}")

# 2 Declare a list with more than 5 items
print("\nQuestion 2")
subjects = ["Mathematics", "Applied Mechanics", "Civil Technology",
            "Engineering Drawing", "Structural Design"]
print(subjects)

# 3 Find the length of your list
print("\nQuestion 3")
print(f"Length of the subject list is {len(subjects)}")

# 4 Get the first item, the middle item and the last item of the list
print("\nQuestion 4")
first_item = subjects[0]
middle_item = subjects[len(subjects) // 2]
last_item = subjects[-1]

print(f"First item in the subjects list is: {first_item}")
print(f"Middle item in the subjects list is: {middle_item}")
print(f"Last item in the subjects list is: {last_item}")

# 5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
print("\nQuestion 5")
mixed_data_types = ["Don", 23, 1.81, "Single", "123 Cape Town"]


# 6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
print("\nQuestion 6")
it_companies = ["Facebook", "Google", "Microsoft",
                "Apple", "IBM", "Oracle", "Amazon"]


# 7 Print the list using print()
print("\nQuestion 7")
print(f"Mixed data types list >>> {mixed_data_types}")
print(f"List of IT-Companies >>> {it_companies}")

# 8 Print the number of companies in the list
print("\nQuestion 8")
print(f"Number of companies = {len(it_companies)}")

# 9 Print the first, middle and last company
print("\nQuestion 9")
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]

print(f"First company: {first_company}")
print(f"Middle company: {middle_company}")
print(f"Last company: {last_company}")

# 10 Print the list after modifying one of the companies
print("\nQuestion 10")
it_companies[-3] = "Twitter"
print(it_companies)

# 11 Add an IT company to it_companies
print("\nQuestion 11")
it_companies.append("BBD")
print(it_companies)

# 12 Insert an IT company in the middle of the companies list
print("\nQuestion 12")
it_companies.insert(len(it_companies) // 2, "Alphabet")
print(it_companies)


# 13 Change one of the it_companies names to uppercase (IBM excluded!)
print("\nQuestion 13")
it_companies[0] = "FACEBOOK"
print(it_companies)


# 14 Join the it_companies with a string '#;  '
print("\nQuestion 14")
print(f"Companies joined with # >>> {"#".join(it_companies)}")

# 15 Check if a certain company exists in the it_companies list.
print("\nQuestion 15")
print(f"Does Apple exit inside it_companies? {"Apple" in it_companies}")

# 16 Sort the list using sort() method
print("\nQuestion 16")
it_companies.sort()
print(it_companies)

# 17 Reverse the list in descending order using reverse() method
print("\nQuestion 17")
it_companies.reverse()
print(it_companies)

# 18 Slice out the first 3 companies from the list
print("\nQuestion 18")
print(f"First 3 companies >>> {it_companies[:4]}")

# 19 Slice out the last 3 companies from the list
print("\nQuestion 19")
print(f"Last 3 companies >>> {it_companies[-3:]}")

# 20 Slice out the middle IT company or companies from the list
print("\nQuestion 20")
print(f"Middle company >>> {it_companies[len(it_companies) // 2]}")


# 21 Remove the first IT company from the list
print("\nQuestion 21")
it_companies.remove('Twitter')
print(it_companies)

# 22 Remove the middle IT company or companies from the list
print("\nQuestion 22")
it_companies.remove(it_companies[len(it_companies) // 2])
print(it_companies)

# 23 Remove the last IT company from the list
print("\nQuestion 23")
it_companies.remove(it_companies[-1])
print(it_companies)

# 24 Remove all IT companies from the list
print("\nQuestion 24")
it_companies.clear()
print(it_companies)

# 25 Destroy the IT companies list
print("\nQuestion 25")
del it_companies


# 26 Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

print("\nQuestion 26")
fullstack = front_end + back_end
print(f"Fullstack original >>> {fullstack}")

# 27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux
print("\nQuestion 27")
full_stack = fullstack.copy()
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")

print(f"Fullstack copy >>> {full_stack}")


print("\n\n\n")
print("--------------------------------------")
print("Exercises: Level 2")
print("--------------------------------------")

# 1 The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1a Sort the list and find the min and max age
print("\nQuestion 1a")
ages.sort()
min_age, *rest, max_age = ages

print(f"Min age = {min_age}")
print(f"Rest of ages = {rest}")
print(f"Max age = {max_age}")


# 1b Add the min age and the max age again to the list
print("\nQuestion 1b")
ages.append(min_age)
ages.append(max_age)

print(f"Min and max ages added again >> {ages}")

# 1c Find the median age (one middle item or two middle items divided by two)
print("\nQuestion 1c")

ages.sort()
middle1 = ages[len(ages) // 2 - 1]
middle2 = ages[len(ages) // 2]
median = (middle1 + middle2) / 2

print(f"Median age is {median}")

# 1d Find the average age (sum of all items divided by their number)
print("\nQuestion 1d")
average_age = sum(ages) / len(ages)

print(f"Average age: {average_age}")

# 1e Find the range of the ages (max minus min)
print("\nQuestion 1e")
min_age, *rest, max_age = ages
age_range = max_age - min_age

print(f"Range: {age_range}")

# 1f Compare the value of (min - average) and (max - average), use abs() method
print("\nQuestion 1f")
min_and_average = (min_age - average_age)
max_and_average = (max_age - average_age)

print(
    f"min - average = {min_age} - {average_age} = {abs(min_age - average_age)}")
print(
    f"max - average = {max_age} - {average_age} = {abs(max_age - average_age)}")

# 1g Find the middle country(ies) in the countries list
countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombi',
    'Comoros',
    'Congo (Brazzaville)',
    'Congo',
    'Costa Rica',
    "Cote d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor Timur)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia, The',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia and Montenegro',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe',
]
print("\nQuestion 1g")
middle = len(countries) // 2

print(f"Middle countries: {countries[middle]}")

# 1h Divide the countries list into two equal lists if it is even if not one more country for the first half.
print("\nQuestion 1h")

first_half = countries[:middle + 1]
second_half = countries[middle + 1:]

print(f"{first_half}, length = {len(first_half)}")
print(f"{second_half}, length = {len(second_half)}")

# 1i Unpack the first three countries and the rest as scandic countries.
print("\nQuestion 1i")
countries = ['China', 'Russia', 'USA',
             'Finland', 'Sweden', 'Norway', 'Denmark']

first_country, second_country, third_country, *scandinavian_countries = countries

print(f"First country: {first_country}")
print(f"Second country: {second_country}")
print(f"Third country: {third_country}")
print(f"Scandic countries: {scandinavian_countries}")

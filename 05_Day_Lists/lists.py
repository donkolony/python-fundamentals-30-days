#1
# empty_list = []

#2
fruits = ["apple", "mango", "water-melon", "strawberry", "orange"]

# #3
# print(len(fruits))

#4
# print(f"First item: {fruits[0]}")
# print(f"Second item: {fruits[(len(fruits) // 2)]}")
# print(f"Third item {fruits[len(fruits) -1]}")

#5
# mixed_data_types =  ["Don", 25, 1.81, "single", "donkolony@gmail.com"]

#6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7
# print(it_companies)

#8
# print(len(it_companies))

#9
# print(it_companies[0]) #Facebook
# print(it_companies[len(it_companies) // 2]) #Apple
# print(it_companies[len(it_companies) - 1]) # Amazon

#10
# it_companies[5] = "Bash"
# print(it_companies)

#11
# it_companies.append("Bash")
# print(it_companies)

#12
# it_companies.insert((len(it_companies) // 2), "Netflix")
# print(it_companies)

#13
# print(it_companies[1].upper())

#14
# print("#".join(it_companies))

#15
# print("Facebook" in it_companies) #True
# print("Bash" in it_companies) #False

#16
# it_companies.sort()
# print(it_companies)

#17
# it_companies.sort(reverse=True)
# print(it_companies)

#18
# print(it_companies[3:])

#19
# print(it_companies[0:4])

#20
# print(it_companies[(len(it_companies) // 2)])

#21
# it_companies.remove("Facebook")
# print(it_companies)

#22
# it_companies.remove("Apple")
# print(it_companies)

#23
it_companies.remove("Amazon")
# print(it_companies)

#24 
it_companies.clear()
# print(it_companies)

#25
del it_companies

#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
# print(front_end + back_end)
# print(front_end)

#27
full_stack = front_end.copy()
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")

# print(f"Copied List: {full_stack}")


# Exercise 2: Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#1
ages.sort()
# print(f"Sorted list in ascending order: {ages}")
min_age = min(ages)
max_age = max(ages)
# print(f"Minimum age is: {min_age}")
# print(f"Maximum age is: {max_age}")

#2
# ages.append(min_age)
# ages.append(max_age)
# print(ages)

#3
median_age = int((ages[4]  + ages[5]) / 2)
# print(f"The median age is: {median_age}")

#4
_sum = sum(ages)
_len = len(ages)
average_num = int(_sum / _len)
# print(f"Sum is {_sum}")
# print(f"length is {_len}")
# print(f"The average is: {average_num}")

#5
_range = max(ages) - min(ages)
# print(f"The range is: {_range}")

#6
min_vs_avg = abs(min(ages) - average_num)
max_vs_avg = abs(max(ages) - average_num)

# print(f"Difference between the min and average value is: {min_vs_avg}")
# print(f"Difference between the max and average value is: {max_vs_avg}")


#7
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
];

# print(countries[len(countries) // 2])
# print(countries[int(len(countries) / 2)])

#8
first_half = countries[0:97]
second_half = countries[97:]
# print(first_half)
# print(second_half)

# Unpacking (Destructing a list)
new_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
country1, country2, country3, *scandic_countries = new_countries

# print(country1)
# print(country2)
# print(country3)
# print(scandic_countries)


 




import xml.etree.ElementTree as ET
# import xlrd
import csv
import json


""" Changing JSON to Dictionary """
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''

person_dct = json.loads(person_json)
print('\n--------------------------------------------------------')
print('Changing JSON to Dictionary  >> ')
print(type(person_dct))
print(person_dct)
print(person_dct['name'])
print('--------------------------------------------------------')

""" Changing Python Dictionary to JSON """
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}

person_json = json.dumps(person, indent=4)
print('\n--------------------------------------------------------')
print('Changing Python Dictionary to JSON >> ')
print(type(person_json))
print(person_json)
print('--------------------------------------------------------')

""" Saving as JSON FILE """

person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}

with open('./19_File_Handling/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)


""" CSV (Common Separated Values) """
with open('./19_File_Handling/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{', '.join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines: {line_count}')


""" XLSX Extension >> Module needs to be installed using PIP """
# excel_book = xlrd.open_workbook('./19_File_Handling/xls_example.xls')
# print(excel_book.nsheets)
# print(excel_book.sheet_names)


""" XML Files """
tree = ET.parse('./19_File_Handling/xml_example.xml')
root = tree.getroot()
print('\n--------------------------------------------------------')
print('Reading XML files >> ')
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)
print('\n--------------------------------------------------------')

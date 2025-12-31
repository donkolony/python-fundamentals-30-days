import csv
from text_similarity import (read_text_source, preprocess_text,
                             remove_stop_words, jaccard_similarity, cosine_similarity)
import math
import stop_words
import pprint
import re
import json
import collections
import functools


""" Day 19: File Handling """


print("--------------------------------------")
print("Exercises: Level 1")
print("--------------------------------------")


"""
# 1.1 Write a function which count number of lines and number of words in a text.
All the files are in the data the folder:
a) Read obama_speech.txt file and count number of lines and words
b) Read michelle_obama_speech.txt file and count number  of lines and words
c) Read donald_speech.txt file and count number of lines and words
d) Read melina_trump_speech.txt file and count number of lines and words
"""
print("Question 1.1")


def num_of_lines_and_words(file_path):
    with open(file_path) as f:
        content = f.read()
        lines = content.splitlines()
        words = content.split()
        return f'length of lines: {len(lines)} and amount of words: {len(words)}'


obama_speech = './data/obama_speech.txt'
michelle_obama_speech = './data/michelle_obama_speech.txt'
donald_speech = './data/donald_speech.txt'
melina_trump_speech = './data/melina_trump_speech.txt'

print(num_of_lines_and_words(obama_speech))
print(num_of_lines_and_words(michelle_obama_speech))
print(num_of_lines_and_words(donald_speech))
print(num_of_lines_and_words(melina_trump_speech))


"""
# 1.2 Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
# Your output should look like this
print(most_spoken_languages(filename='./data/countries_data.json', 10))
[(91, 'English'),
(45, 'French'),
(25, 'Arabic'),
(24, 'Spanish'),
(9, 'Russian'),
(9, 'Portuguese'),
(8, 'Dutch'),
(7, 'German'),
(5, 'Chinese'),
(4, 'Swahili'),
(4, 'Serbian')]

# Your output should look like this
print(most_spoken_languages(filename='./data/countries_data.json', 3))
[(91, 'English'),
(45, 'French'),
(25, 'Arabic')]
"""
print("\nQuestion 1.2")


def most_spoken_languages(file_path, top_n=10):
    with open(file_path, encoding='utf-8') as f:
        # Convert JSON to Python dictionary
        countries = json.loads(f.read())

        language_count = {}

        for country in countries:
            for language in set(country['languages']):
                language_count[language] = language_count.get(language, 0) + 1

        sorted_languages = sorted([(count, language)
                                  for language, count in language_count.items()], reverse=True)

        return sorted_languages[:top_n]


countries_data = './data/countries_data.json'
# print(most_spoken_languages(countries_data, 3))

# 1.3 Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
print("\nQuestion 1.3")


def most_populated_countries(file_path, top_n=10):
    with open(file_path, encoding='utf-8') as f:
        countries = json.loads(f.read())

        sorted_countries = sorted(
            countries, key=lambda country: country['population'], reverse=True)

        result = [{
            'country': country['name'],
            'population': country['population']
        }
            for country in sorted_countries[:top_n]
        ]

        return result


countries_data = './data/countries_data.json'
# print(most_populated_countries(countries_data, 3))


print("--------------------------------------")
print("Exercises: Level 2")
print("--------------------------------------")


# 2.4 Extract all incoming email addresses as a list from the email_exchange_big.txt file.
print("\nQuestion 2.4")


def extract_emails(file_path):
    with open(file_path, encoding='utf-8', errors='ignore') as f:
        contents = f.read()
        # pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        # more strict ⬇️
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        emails = re.findall(pattern, contents)
        return sorted(set(emails))


path = './data/email_exchange_big.txt'
emails = extract_emails(path)
for idx, email in enumerate(emails, 1):
    print(idx, email)

"""
2.5Find the most common words in the English language. Call the name of your function find_most_common_words,
it will take two parameters - a string or a file and a positive integer, indicating the number of words.
Your function will return an array of tuples in descending order. Check the output
e.g.
  [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and'),
    (4, 'a'),
    (4, 'in'),
    (3, 'that'),
    (2, 'have'),
    (2, 'I')
"""
print("\nQuestion 2.5")


def find_most_common_words(text_or_file, n=10):
    if text_or_file.endswith('.txt'):
        with open(text_or_file, encoding='utf-8', errors='ignore') as f:
            text = f.read()
    else:
        text = text_or_file

    pattern = r'\b[a-zA-Z]+\b'
    words = re.findall(pattern, text)
    words = [word.lower() if word != "I" else word for word in words]
    counter = collections.Counter(words)

    return [(count, word) for word, count in counter.most_common(n)]


sample = './data/romeo_and_juliet.txt'
common_words = find_most_common_words(sample, 5)
# pprint.pprint(common_words)


"""
# 2.6 Use the function, find_most_frequent_words to find:
a) The ten most frequent words used in Obama's speech
b) The ten most frequent words used in Michelle's speech
c) The ten most frequent words used in Trump's speech
d) The ten most frequent words used in Melina's speech
"""
print("\nQuestion 2.6")
ten_most_frequent_words_obama_speech = './data/obama_speech.txt'
ten_most_frequent_words_michelle_speech = './data/michelle_obama_speech.txt'
ten_most_frequent_words_trump_speech = './data/donald_speech.txt'
ten_most_frequent_words_melina_speech = './data/melina_trump_speech.txt'

# print("\nTop words from Obama's Speech")
# pprint.pprint(find_most_common_words(ten_most_frequent_words_obama_speech, 10))
# print("\nTop words from Michelle's Speech")
# pprint.pprint(find_most_common_words(
#     ten_most_frequent_words_michelle_speech, 10))
# print("\nTop words from Trump Speech")
# pprint.pprint(find_most_common_words(ten_most_frequent_words_trump_speech, 10))
# print("\nTop words from Melina Speech")
# pprint.pprint(find_most_common_words(
#     ten_most_frequent_words_melina_speech, 10))


"""
# 2.7 Write a python application that checks similarity between two texts.
It takes a file or a string as a parameter and it will evaluate the similarity of the two texts.
For instance check the similarity between the transcripts of Michelle's and Melina's speech.
You may need a couple of functions, function to clean the text(clean_text), function to
remove support words(remove_support_words) and finally to check the similarity(check_text_similarity).
List of stop words are in the data directory
"""
print("\nQuestion 2.7")
file1 = './data/michelle_obama_speech.txt'
file2 = './data/melina_trump_speech.txt'
file3 = './data/obama_speech.txt'
file4 = './data/donald_speech.txt'

text1 = read_text_source(file2)
text2 = read_text_source(file4)

words1 = remove_stop_words(preprocess_text(text1), stop_words.stop_words)
words2 = remove_stop_words(preprocess_text(text2), stop_words.stop_words)

# print('Jaccard Similarity:', jaccard_similarity(words1, words2))
# print('Cosine Similarity:', cosine_similarity(words1, words2))


# 2.8 Find the 10 most repeated words in the romeo_and_juliet.txt
print("\nQuestion 2.8")

romeo_and_juliet = './data/romeo_and_juliet.txt'
most_repeated_words_romeo_and_juliet = find_most_common_words(
    romeo_and_juliet, 10)
# pprint.pprint(most_repeated_words_romeo_and_juliet)


"""
# 2.9 Read the hacker news csv file and find out:
a) Count the number of lines containing python or Python
b) Count the number lines containing JavaScript, javascript or Javascript
c) Count the number lines containing Java and not JavaScript
"""


def count_matching_lines(csv_path, pattern):
    count = 0
    with open(csv_path, encoding='utf-8', errors='ignore') as f:
        reader = csv.reader(f)
        for row in reader:
            line = ' '.join(row)
            if re.search(pattern, line, re.IGNORECASE):
                count += 1

        return count


csv_path = './data/hacker_news.csv'

# 2.9a Count the number of lines containing python or Python
print("\nQuestion 2.9a")
python_pattern = r'\bpython\b'
# print('Python:', count_matching_lines(csv_path, python_pattern))

# 2.9b Count the number lines containing JavaScript, javascript or Javascript
print("\nQuestion 2.9b")
javascript_pattern = r'\bjavascript\b'
# print('JavaScript:', count_matching_lines(csv_path, javascript_pattern))

# 2.9c c) Count the number lines containing Java and not JavaScript
print("\nQuestion 2.9c")
java_not_js_pattern = r'\bjava\b(?!script)'
# print('Java (not JavaScript):', count_matching_lines(
#     csv_path, java_not_js_pattern))

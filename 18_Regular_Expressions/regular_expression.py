""" Day 18: Regular Expression """

import re
import collections

print("--------------------------------------")
print("Exercises: Level 1")
print("--------------------------------------")

# 1.1 What is the most frequent word in the following paragraph?
print("Question 1.1")
paragraph = '''I love teaching.
If you do not love teaching what else can you love.
I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''

print('\n')
pattern = r'\b\w+\b'  # ignores spaces better than .split()
most_frequent_word = {}
matches = [word.lower() for word in re.findall(pattern, paragraph)]
for word in matches:
    most_frequent_word[word] = most_frequent_word.get(word, 0) + 1
sorted_words = dict(sorted(most_frequent_word.items(),
                    key=lambda word: word[1], reverse=True))

print(sorted_words)


print('\nMethod Using Counter from collections module')
pattern = r'\b\w+\b'
matches = collections.Counter(re.findall(
    pattern, paragraph))  # does not sort items
# sorts item when we call most_common method. Faster sorting method and optimized in C
most_common = matches.most_common()

print(most_common)


"""
# 1.2   The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.
        Extract these numbers from this whole text and find the distance between the two furthest particles.

Example
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points = [-12, -4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 - (-12)
"""
print("--------------------------------------")
print("Exercises: Level 2")
print("--------------------------------------")
print("\nQuestion 2.1")
sentence = """The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.
Extract these numbers from this whole text and find the distance between the two furthest particles.
"""
pattern = r'-?\d+\.?\d*'
points = re.findall(pattern, sentence)
points = [int(point) for point in points]  # convert to integers
sorted_points = sorted(points)  # sort numerically
# distance between furthest points
distance = sorted_points[-1] - sorted_points[0]

print("Extracted points:", points)
print("Sorted points:", sorted_points)
print("Distance:", distance)  # 20

# 2.2 Write a pattern which identifies if a string is a valid python variable
"""
is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True
"""
print("\nQuestion 2.2")


def is_valid_variable(name):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.fullmatch(pattern, name))


print(is_valid_variable('first_name'))  # True
print(is_valid_variable('first-name'))  # False
print(is_valid_variable('1first_name'))  # False
print(is_valid_variable('firstname'))  # True


print("--------------------------------------")
print("Exercises: Level 3")
print("--------------------------------------")

# 3.1 Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
print("\nQuestion 3.1")
pattern1 = r"[^a-zA-Z0-9\s.,!?']"
pattern2 = r"\b\w+(?:'\w+)?\b"
stop_words = {'i', 'a', 'as', 'to', 'be', 'the',
              'and', 'is', 'there', 'any', 'this', 'you'}

cleaned_sentence = re.sub(pattern1, "", sentence).lower()
words = re.findall(pattern2, cleaned_sentence)
filtered_words = [word for word in words if word not in stop_words]
frequent = collections.Counter(filtered_words)
most_frequent_words = frequent.most_common(3)

print("Top 3 most frequent words:", most_frequent_words)

import statistics
import requests
import re
from collections import Counter

print("--------------------------------------")
print("Exercises: Level 1")
print("--------------------------------------")


"""
# 1.1 Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
 
"""
print("Question 1.1")


def most_frequent_words(url, top_n, stop_words=None):
    if stop_words is None:
        stop_words = {
            "i",
            "a",
            "as",
            "to",
            "be",
            "the",
            "and",
            "is",
            "there",
            "any",
            "this",
            "you",
            "of",
            "in",
            "for",
            "on",
            "at",
        }

    pattern1 = r"[^a-z\s']"
    pattern2 = r"\b[a-z]+(?:'[a-z]+)?\b"

    response = requests.get(url)
    text = response.text.lower()

    # Remove unwanted characters
    cleaned_text = re.sub(pattern1, " ", text)

    # Extract words + contractions
    words = re.findall(pattern2, cleaned_text)

    # Remove stop words
    filtered_words = [word for word in words if word not in stop_words]

    # Count frequencies
    counts = Counter(filtered_words)

    return counts.most_common(top_n)


url = "http://www.gutenberg.org/files/1112/1112.txt"
result = most_frequent_words(url, 10)
print(result)

"""
# 1.2 Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
    1.2.1 the min, max, mean, median, standard deviation of cats' weight in metric units.
    1.2.2 the min, max, mean, median, standard deviation of cats' lifespan in years.
    1.2.3 Create a frequency table of country and breed of cats
"""


def fetch_cat_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


url = "https://api.thecatapi.com/v1/breeds"


# 1.2.1 the min, max, mean, median, standard deviation of cats' weight in metric units.


def cat_weight_stats(breeds):
    weights = []

    for breed in breeds:
        weight_str = breed["weight"]["metric"]
        min_w, max_w = map(float, weight_str.split(" - "))
        weights.append((min_w + max_w) / 2)

    return {
        "min": min(weights),
        "max": max(weights),
        "mean": statistics.mean(weights),
        "median": statistics.mode(weights),
        "std_dev": statistics.stdev(weights),
    }


# 1.2.2 the min, max, mean, median, standard deviation of cats' lifespan in years.


def cats_lifespan_stats(breeds):
    lifespan = []

    for breed in breeds:
        life_str = breed["life_span"]
        min_l, max_l = map(float, life_str.split(" - "))
        lifespan.append((min_l + max_l) / 2)

    return {
        "min": min(lifespan),
        "max": max(lifespan),
        "mean": statistics.mean(lifespan),
        "median": statistics.median(lifespan),
        "std_dev": statistics.stdev(lifespan),
    }


# 1.2.3 Create a frequency table of country and breed of cats


def country_breed_frequency(breeds):
    countries = []

    for breed in breeds:
        country = breed.get("origin")
        if country:
            countries.append(country)

    return Counter(countries)


# Rub All Three Questions
url = "https://api.thecatapi.com/v1/breeds"
breeds = fetch_cat_data(url)


print("\nQuestion 1.2.1 - Cat Weight Stats")
print(cat_weight_stats(breeds))

print("\nQuestion 1.2.2 - Cat Lifespan Stats")
print(cats_lifespan_stats(breeds))

print("\nQuestion 1.2.3 - Country & Breed Frequency")
print(country_breed_frequency(breeds))


"""
# 1.3 Read the countries API and find countries_api = 'https://restcountries.eu/rest/v2/all'
    1.3.1 the 10 largest countries
    1.3.2 the 10 most spoken languages
    1.3.3 the total number of languages in the countries API
"""


def fetch_country_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


# 1.3.1 the 10 largest countries
print("\nQuestion 1.3.1")


def largest_countries(data, top_n=10):
    countries_with_area = [
        (country["name"], country["area"])
        for country in data
        if country.get("area") is not None
    ]

    countries_with_area.sort(key=lambda x: x[1], reverse=True)

    return countries_with_area[:top_n]


# 1.3.2 the 10 most spoken languages
def most_spoken_language(data, top_n=10):
    languages = []

    for country in data:
        for lanaguage in country["lanaguages"]:
            languages.append(lanaguage["name"])

    language_counts = Counter(languages)

    return language_counts.most_common(top_n)


# 1.3.3 the total number of languages in the countries API
def total_number_of_langauge(data):
    unique_languages = set()

    for country in data:
        for language in country["languages"]:
            unique_languages.add(language["name"])

    return len(unique_languages)


# Debugger
countries_api = "https://restcountries.com/v3.1/all"
data = fetch_cat_data(countries_api)

print("\nQuestion 1.3.1 - 10 Largest Countries")
for country, area in largest_countries(data):
    print(country, area)


print("\nQuestion 1.3.2 – 10 Most Spoken Languages")
for language, count in most_spoken_language(data):
    print(language, count)


print("\nQuestion 1.3.3 – Total Number of Languages")
print(total_number_of_langauge(data))

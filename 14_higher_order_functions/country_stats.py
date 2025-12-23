"""
country_stats.py

A small module for analyzing countries data:
- Most populated countries
- Most spoken languages

Dependencies:
- `countries_data` dictionary/list imported from your data file
- `functools.reduce` (for functional style counting)
"""

from functools import reduce
from countries_data import countries_data


def most_populated_countries(countries, top_n=10):
    """
    Returns the top N most populated countries.

    Pythonic and concise:
    - Sorts the list of country dictionaries by population
    - Takes the top N countries
    - Returns a list of tuples (country_name, population)

    Parameters:
        countries (list): List of dictionaries, each with 'name' and 'population' keys
        top_n (int): Number of top countries to return

    Returns:
        list of tuples: Each tuple is (country_name, population), sorted descending by population
    """

    # Step 1: Sort the countries by population descending and slice top N
    top_populated_countries = sorted(
        countries,
        key=lambda country: country.get("population", 0),
        reverse=True
    )[:top_n]

    # Step 2: Return a list of tuples (name, population)
    return [(country["name"], country["population"]) for country in top_populated_countries]


def most_spoken_languages(countries, top_n=10):
    """
    Returns a dictionary of the top N most spoken languages.

    Parameters:
        countries (list): List of country dictionaries, each with a 'languages' key
        top_n (int): Number of top languages to return (default 10)

    Returns:
        dict: Keys are languages, values are the number of countries where the language is spoken
    """

    # Step 1: Use reduce to count languages across all countries
    language_count = reduce(
        lambda acc, country: {
            **acc,  # previous accumulated counts
            **{
                # Count each language once per country using set
                lang: acc.get(lang, 0) + 1
                for lang in set(country["languages"])
            }
        },
        countries,  # iterate through all countries
        {}  # initial empty dictionary
    )

    # Step 2: Sort by count descending and take top N
    top_spoken_languages = dict(
        sorted(
            language_count.items(),
            key=lambda item: item[1],
            reverse=True
        )[:top_n]
    )

    return top_spoken_languages

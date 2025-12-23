from functools import reduce
from countries_data import countries_data


def most_spoken_languages(countries, top_n=10):
    """
    Returns a dictionary of the top N most spoken languages.

    This is a **manual frequency-count algorithm** and is foundational for problems like:
        - Most spoken languages
        - Word frequency counting
        - Vote counting
        - Log analysis

    Notes:
    - We count each language **once per country** using set() to avoid duplicates.
    - Sorting is used to find the top N languages by frequency.
    - The .get(key, 0) + 1 pattern is used to increment counts safely without KeyError.
    - For numeric values like population, you don't need this pattern because you are not counting occurrences.

    Parameters:
        countries (list): List of country dictionaries, each with a 'languages' key
        top_n (int): Number of top languages to return (default 10)

    Returns:
        dict: Keys are languages, values are number of countries where the language is spoken
    """

    # -------------------------
    # Step 1: Initialize empty dictionary to hold counts
    # -------------------------
    language_count = {}

    # -------------------------
    # Step 2: Loop over all countries
    # -------------------------
    for country in countries:
        # Convert to set to avoid counting duplicates within the same country
        for language in set(country["languages"]):
            # Increment count safely: start at 1 if language not yet in dictionary
            language_count[language] = language_count.get(language, 0) + 1

    # -------------------------
    # Step 3: Sort the dictionary by counts in descending order and keep top N
    # -------------------------
    top_spoken_languages = dict(
        sorted(
            language_count.items(),      # Convert dict to list of tuples (language, count)
            key=lambda item: item[1],   # Sort by count
            reverse=True                # Highest count first
        )[:top_n]                        # Slice top N items
    )

    # -------------------------
    # Step 4: Return the result as a dictionary
    # -------------------------
    return top_spoken_languages


""" Most Spoken Languages Using REDUCE """


def most_spoken_languages(countries, top_n=10):
    """
    Returns a dictionary of the top N most spoken languages.

    Parameters:
        countries (list): List of country dictionaries, each with a 'languages' key
        top_n (int): Number of top languages to return (default 10)

    Parameters of reduce
    reduce(function, iterable, initializer)
    - function → a function with two parameters: (accumulator, current_item)
    - iterable → the list we are processing (here: countries)
    - initializer → starting value of the accumulator (here: {} empty dict)

    Returns:
        dict: Keys are languages, values are the number of countries where the language is spoken
    """

    # -----------------------------------
    # Step 1: Use reduce to accumulate language counts
    # -----------------------------------
    language_count = reduce(
        # This lambda will be called for each country in the list
        lambda acc, country: {
            # Merge the current accumulator 'acc' with updated counts for this country
            **acc,  # existing accumulated language counts
            **{
                # For each language in this country (use set to avoid duplicates)
                # increment count by 1, start at 1 if not exists
                lang: acc.get(lang, 0) + 1
                for lang in set(country["languages"])
            }
        },
        countries,  # The list we are reducing over (each country dictionary)
        {}  # Initial accumulator: an empty dictionary
    )

    # -----------------------------------
    # Step 2: Sort the dictionary by count in descending order and take top N
    # -----------------------------------
    top_spoken_languages = dict(
        sorted(
            language_count.items(),           # convert dict to list of (language, count) tuples
            # sort by the count (second item in tuple)
            key=lambda item: item[1],
            # descending order (highest count first)
            reverse=True
        )[:top_n]                             # slice to keep only top N languages
    )

    # Step 3: Return the result as a dictionary
    return top_spoken_languages


# ========== Example: First 3 countries (simplified) ==========
countries = [
    {"name": "Finland", "languages": ["Finnish", "Swedish"]},
    {"name": "Sweden",  "languages": ["Swedish"]},
    {"name": "Norway",  "languages": ["Norwegian", "Swedish"]}
]

# We want to count number of countries per language.

# Step 0: Initial accumulator
acc = {}  # empty dictionary

# Step 1: Process Finland
country = {"name": "Finland", "languages": ["Finnish", "Swedish"]}

# Inside Lambda:
new_counts = {lang: acc.get(lang, 0) + 1 for lang in set(country["languages"])}
# set(["Finnish", "Swedish"]) → {"Finnish", "Swedish"}
# acc.get(lang, 0) → 0 for both, because acc is empty
# new_counts = {"Finnish": 1, "Swedish": 1}

# Merge with acc:
acc = {**acc, **new_counts}  # {} merged with {"Finnish":1, "Swedish":1}
# acc after step 1 = {"Finnish": 1, "Swedish": 1}

# Step 2: Process Sweden
country = {"name": "Sweden", "languages": ["Swedish"]}

# Inside Lambda:
new_counts = {lang: acc.get(lang, 0) + 1 for lang in set(country["languages"])}
# set(["Swedish"]) → {"Swedish"}
# acc.get("Swedish", 0) → 1
# new_counts = {"Swedish": 2}

# Merge with acc:
acc = {**acc, **new_counts}
# acc after step 2 = {"Finnish": 1, "Swedish": 2}

# Step 3: Process Norway
country = {"name": "Norway", "languages": ["Norwegian", "Swedish"]}

# Inside lambda:
new_counts = {lang: acc.get(lang, 0) + 1 for lang in set(country["languages"])}
# set(["Norwegian", "Swedish"]) → {"Norwegian", "Swedish"}
# acc.get("Norwegian",0) → 0
# acc.get("Swedish",0) → 2
# new_counts = {"Norwegian": 1, "Swedish": 3}

# Merge with acc:
acc = {**acc, **new_counts}
# acc after step 3 = {"Finnish": 1, "Swedish": 3, "Norwegian": 1}

# ✅ Final accumulator after 3 countries. This is exactly how reduce builds up the counts.
{"Finnish": 1, "Swedish": 3, "Norwegian": 1}

# Step 4: Sorting and taking top N
# If we take top 2:
top_2 = dict(sorted(acc.items(), key=lambda item: item[1], reverse=True)[:2])
# top_2 = {"Swedish": 3, "Finnish": 1}

"""
Key insight from this animation
    - acc grows with each country
    - set() ensures we don't double-count a language within the same country
    - **acc, **new_counts merges old + new → always up-to-date
"""

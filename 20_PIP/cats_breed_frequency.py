from collections import Counter
import statistics
import requests
import matplotlib.pyplot as plt


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


############################################################


# Bar Chart: Country vs Numbers of Cat Breeds
def plot_country_breed_bar(freq_table, top_n=10):
    countries = dict(freq_table.most_common(top_n))
    plt.figure()
    plt.bar(countries.keys(), countries.values())
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Country")
    plt.ylabel("Number of Breeds")
    plt.title(f"Top {top_n} Countries by Number of Cat Breeds")
    plt.tight_layout()
    plt.show()


def plot_weight_histogram(breeds):
    weights = []
    for breed in breeds:
        min_w, max_w = map(float, breed["weight"]["metric"].split(" - "))
        weights.append((min_w + max_w) / 2)
    plt.figure()
    plt.hist(weights, bins=10)
    plt.xlabel("Average Weight (kg)")
    plt.ylabel("Frequency")
    plt.title("Distribution of Cat Weights (Metric)")
    plt.show()


def plot_lifespan_histogram(breeds):
    lifespan = []
    for breed in breeds:
        min_l, max_l = map(float, breed["life_span"].split(" - "))
        lifespan.append((min_l + max_l) / 2)

    plt.figure()
    plt.hist(lifespan, bins=10)
    plt.xlabel("Average Lifespan (Years)")
    plt.ylabel("Frequency")
    plt.title("Distribution of Cat Lifespans")
    plt.show()


# Debugger
url = "https://api.thecatapi.com/v1/breeds"
breeds = fetch_cat_data(url)

# Frequency table
country_freq = country_breed_frequency(breeds)

# Plots
plot_country_breed_bar(country_freq)
plot_weight_histogram(breeds)
plot_lifespan_histogram(breeds)

import requests
from bs4 import BeautifulSoup
import json


print("--------------------------------------")
print("Exercises: Level 1")
print("--------------------------------------")


"""
# 1.1 Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
"""
print("Question 1.1")


url = "http://www.bu.edu/president/boston-university-facts-stats/"
response = requests.get(url)
content = response.content

# Parse HTML
soup = BeautifulSoup(content, "html.parser")

# Extract data
headings = [h.get_text(strip=True) for h in soup.find_all(["h1", "h2", "h3"])]
paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]

# Store data in dictionary
data = {"url": url, "headings": headings, "paragraphs": paragraphs}

# Save as JSON
file_path = "./22_Web_Scraping/data.json"
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)


print("Data saved successfully!")


"""
# 1.2 Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file
"""
print("\nQuestion 1.2")

url = "https://archive.ics.uci.edu/dataset/759/glioma+grading+clinical+and+mutation+features+dataset"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# Find ALL tables
tables = soup.find("table")

rows = tables.find_all("tr")[1:]  # skip header row

datasets = []
for row in rows:
    cols = row.find_all("td")

    if len(cols) >= 6:
        dataset = {
            "name": cols[0].get_text(strip=True),
            "data_types": cols[1].get_text(strip=True),
            "default_task": cols[2].get_text(strip=True),
            "attribute_types": cols[3].get_text(strip=True),
            "instances": cols[4].get_text(strip=True),
            "attributes": cols[5].get_text(strip=True),
        }

        datasets.append(dataset)

file_path = "./22_Web_Scraping/uci_datasets.json"
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(datasets, f, indent=4)

print("JSON file created successfully")

"""
# 1.3   Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). 
        The table is not very structured and the scrapping may take very long time.
"""
print("\nQuestion 1.3")
url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Find ALL wikitable tables
tables = soup.find_all("table", class_="wikitable")

print(f"Found {len(tables)} wikitable tables")

# Pick the largest table (presidents table)
table = max(tables, key=lambda t: len(t.find_all("tr")))

rows = table.find_all("tr")[1:]  # skip header

presidents = []

for row in rows:
    cols = row.find_all(["td", "th"])

    if len(cols) >= 5:
        president = {
            "number": cols[0].get_text(strip=True),
            "name": cols[2].get_text(" ", strip=True),
            "term": cols[3].get_text(" ", strip=True),
            "party": cols[5].get_text(strip=True),
        }
        presidents.append(president)

# Save to JSON
file_path = "./22_Web_Scraping/us_president.json"
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(presidents, f, indent=4)

print("US Presidents data saved successfully!")

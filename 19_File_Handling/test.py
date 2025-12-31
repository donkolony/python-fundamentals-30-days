import json

file_path = './data/countries_data.py'

with open(file_path, errors='ignore') as f:
    contents = json.loads(f.read())

    language_count = {}
    for country in contents:
        for language in set(country['languages']):
            language_count[language] = language_count.get(language, 0) + 1

    top_spoken_languages = sorted(
        language_count.items(), key=lambda item: item[1], reverse=True)[:10]

    print(top_spoken_languages)

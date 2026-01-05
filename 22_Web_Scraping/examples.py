import requests
from bs4 import BeautifulSoup

url = "https://www.w3schools.com/java/"


response = requests.get(url)
content = response.content  # we get all the content from the website
soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.body)
# print(response.status_code)

# for link in soup.find_all("a"):
#     print(link.get("href"))

print(soup.get_text())

tables = soup.find_all("table", {"cellpadding": "3"})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class, or HTML tag, for more information check the beatifulsoup doc
# table = tables[0]

# for td in table.find("tr").find_all("td"):
#     print(td.text)

import requests
from bs4 import BeautifulSoup

url = "https://es.wikipedia.org/wiki/Sistema_solar"
req = requests.get(url).text

soup = BeautifulSoup(req, "lxml")
#print(soup.prettify())

table = soup.find("table", {"class": "wikitable mw-datatable sortable center"})
print(table.findAll("th"))




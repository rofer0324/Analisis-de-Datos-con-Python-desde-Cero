import urllib3
from bs4 import BeautifulSoup

url = "https://www.python.org/events/python-events/"
req = urllib3.PoolManager()
res = req.request('GET', url)

soup = BeautifulSoup(res.data, "html.parser")
#print(soup)

events = soup.find("ul", {"class": "list-recent-events menu"}).findAll("li")

for event in events:
    detalles = {}
    detalles["name"] = event.find("h3").find("a").text
    detalles["Location"] = event.find("span", {"class": "event-location"}).text
    detalles["time"] = event.find("time").text
    print(detalles)

import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/events/python-events/"
req = requests.get(url)

#print(req.text) # Imprime el contenido de la pagina web en bruto.

soup = BeautifulSoup(req.text, "lxml")

events = soup.find("ul", {"class": "list-recent-events menu"}).findAll("li")
#print(events)

for event in events:
    detalles = {}
    detalles["name"] = event.find("h3").find("a").text
    detalles["Location"] = event.find("span", {"class": "event-location"}).text
    detalles["time"] = event.find("time").text
    print(detalles)
import requests
from lxml import html, etree

url = "https://es.wikipedia.org/wiki/Sistema_solar"
req = requests.get(url).text

tree = html.fromstring(req)
#print(tree)

for element in tree.xpath("/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[5]/tbody/tr"):
    print(etree.tostring(element))
import requests
from bs4 import BeautifulSoup

url = "https://es.wikipedia.org/wiki/Historia_de_Python"
req = requests.get(url).text
soup = BeautifulSoup(req, "lxml")

imagen_tag = soup.find("img")

imagen_url = f'https:{imagen_tag["src"]}'
#print(imagen_url)

image = requests.get(imagen_url)

def guardar_imagen(nombre, extension):
    with open(f"{nombre}.{extension}", "wb") as file:
        for fragmento in image.iter_content(chunk_size=1024):
            file.write(fragmento)


if imagen_url.endswith(".jpg"):
    guardar_imagen("Img_python", ".jpg")
elif imagen_url.endswith(".png"):
    guardar_imagen("Img_python", ".png")
elif imagen_url.endswith(".jpeg"):
    guardar_imagen("Img_python", ".jpeg")
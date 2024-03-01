import requests
from bs4 import BeautifulSoup
from PIL import Image
import io

url = "https://www.udemy.com/"
req = requests.get(url).text

soup = BeautifulSoup(req, "lxml")

imagen_tag = soup.find("div", {"class": "wide-hero-banner-slide-module--image-container--jU9nN"}).find("img")
#print(imagen_tag)

imagen_url = imagen_tag["src"]
#print(imagen_url)

image = requests.get(imagen_url).content
#print(image) # Imagen en bytes

def miniatura_imagen(bytes, ancho, alto, nombre):
    imagen = Image.open(io.BytesIO(bytes))
    imagen.thumbnail( (ancho, alto) )
    imagen.save(f"{nombre}.png")
    
miniatura_imagen(image, 500, 500, "img_udemy")

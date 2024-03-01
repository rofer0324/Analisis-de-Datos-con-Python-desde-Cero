from bs4 import BeautifulSoup
import requests
import pandas as pd

def obtener_planetas():
    url = "https://es.wikipedia.org/wiki/Sistema_solar"
    req = requests.get(url).text
    soup = BeautifulSoup(req, "lxml")
    
    planetas = soup.find("table", {"class": "wikitable mw-datatable sortable center"}).find_all("tr")
    #print(planetas)
    
    def diccionario(tr):
        datos_planetas = {}
        td = tr.findAll("td")
        try:
            datos_planetas["Satelite"] = td[0].text.strip()
            datos_planetas["Planeta"] = td[1].text.strip()
            datos_planetas["Diametro"] = td[2].text.strip()
            datos_planetas["Periodo_Orbital"] = td[3].text.strip()
            
            datos_planetas["imagen"] = f'https:{td[4].find("img")["src"]}'
            
            return datos_planetas
        except:
            pass
        
    
    return [diccionario(tr) for tr in planetas][1: ]
    
if __name__ == "__main__":
   planetas = obtener_planetas()
   #print(planetas)
   
   dataframe = pd.DataFrame(planetas)
   print(dataframe)
   
   dataframe.to_json("planetas.json")
   dataframe.to_csv("planetas.csv", index=False)


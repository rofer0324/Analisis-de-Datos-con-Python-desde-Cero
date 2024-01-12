from abc import ABC, abstractmethod

class Celular(ABC): #Clase padre
    
    def __init__(self, color, almacenamiento):
        self.color =  color
        self.almacenamiento =  almacenamiento
        
    def info(self):
        print(f"Color: {self.color}")
        print(f"Almacenamiento: {self.almacenamiento}Gb")
        
    def encender(self):
        print("Encender")
        
    def apagar(self):
        print("Apagar")

class android(Celular): #SubClase
    
    def __init__(self, color, almacenamiento):
        super(android, self).__init__(color, almacenamiento) 
    
    def expandir_almacenamiento(self):
        print("Expandiendo almacenamiento del celular")
        
class iphone(Celular): #SubClase
    
    def airdrop(self):
        print("Transfiriendo archivos")

#obj = Celular("Blanco", 16)
celular_android = android("Rojo", 64)
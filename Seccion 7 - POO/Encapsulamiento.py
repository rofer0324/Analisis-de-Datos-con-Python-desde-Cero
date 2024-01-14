from abc import ABC, abstractmethod

#---Clase padre---#
class Celular(ABC): 
    @abstractmethod
    def __init__(self, color, almacenamiento):
        self.__color =  color
        self.__almacenamiento =  almacenamiento #El doble guion indica que el atributo es privado
        self.__volumen = 5
    
    @abstractmethod
    def info(self):
        print(f"Color: {self.__color}")
        print(f"Almacenamiento: {self.__almacenamiento}Gb")
        print(f"Volumen: {self.__volumen}")
        
    @abstractmethod   #abstraccion del metodo 
    def encender(self):
        print("Encender")
        
    @abstractmethod   
    def apagar(self):
        print("Apagar")
        
    def subir_volumen(self):
        self.__volumen += 1
        print(f"Nivel de volumen actual: {self.__volumen}")
        
    def bajar_volumen(self):
        self.__volumen -= 1
        print(f"Nivel de volumen actual: {self.__volumen}")
        
#---Clase padre---#

class android(Celular): #SubClase
    
    def __init__(self, color, almacenamiento):
        super(android, self).__init__(color, almacenamiento) 
    
    def encender(self):
        super(android, self).encender() #Hace referencia a la clase padre y por eso aparece en la impresion
        print("Mostrando logo de ANDROID")
        
    def apagar(self):
        super(android, self).apagar()
    
    def info(self):
        super(android, self).info()
    
    def expandir_almacenamiento(self):
        super(android, self).expandir_almacenamiento()
        print("Expandiendo almacenamiento del celular")
        
class iphone(Celular): #SubClase
    
    def __init__(self, color, almacenamiento):
        super(iphone, self).__init__(color, almacenamiento)
    
    def encender(self):
        super(iphone, self).encender()
        print("Mostrando logo de IPHONE")
    
    def apagar(self):
        super(android, self).apagar()
    
    def info(self):
        super(android, self).info()
    
    def airdrop(self):
        super(iphone, self).airdrop()
        print("Transfiriendo archivos")

#obj = Celular("Blanco", 16)
celular_android = android("Rojo", 64)
celular_android.info()
celular_android.subir_volumen()
celular_android.bajar_volumen()
celular_android.bajar_volumen()

#celular_iphone = iphone("Gris", 128)
#celular_iphone.encender()
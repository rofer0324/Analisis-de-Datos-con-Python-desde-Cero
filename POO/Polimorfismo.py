from abc import ABC, abstractmethod

class Celular(ABC): #Clase padre
    @abstractmethod
    def __init__(self, color, almacenamiento):
        self.color =  color
        self.almacenamiento =  almacenamiento
    
    @abstractmethod
    def info(self):
        print(f"Color: {self.color}")
        print(f"Almacenamiento: {self.almacenamiento}Gb")
        
    @abstractmethod   #abstraccion del metodo 
    def encender(self):
        print("Encender")
        
    @abstractmethod   
    def apagar(self):
        print("Apagar")

class android(Celular): #SubClase
    
    def __init__(self, color, almacenamiento):
        super(android, self).__init__(color, almacenamiento) 
    
    def encender(self):
        super(android, self).encender() #Hace referencia a la clase padre y por eso aparece en la impresion
        print("Mostrando logo de ANDROID")
    
    #se puede agregar el metodo apagar, info del metodo subclase
    
    def expandir_almacenamiento(self):
        super(android, self).expandir_almacenamiento()
        print("Expandiendo almacenamiento del celular")
        
class iphone(Celular): #SubClase
    
    def __init__(self, color, almacenamiento):
        super(iphone, self).__init__(color, almacenamiento)
    
    def encender(self):
        super(iphone, self).encender()
        print("Mostrando logo de IPHONE")
    
    #se puede agregar las sub clases de info, apagar de la super clase.
    
    def airdrop(self):
        super(iphone, self).airdrop()
        print("Transfiriendo archivos")

#obj = Celular("Blanco", 16)
celular_android = android("Rojo", 64)
celular_android.encender()

celular_iphone = iphone("Gris", 128)
celular_iphone.encender()
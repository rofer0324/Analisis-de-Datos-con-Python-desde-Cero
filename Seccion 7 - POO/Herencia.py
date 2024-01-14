class Celular: #Clase padre
    
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
    
    def expandir_almacenamiento(self):
        print("Expandiendo almacenamiento del celular")
        
class iphone(Celular): #SubClase
    
    def airdrop(self):
        print("Transfiriendo archivos")
 

cel_android = android("Negro", 64)
cel_android.expandir_almacenamiento()
cel_android.info()

cel_iphone = iphone("blanco", 16)
cel_iphone.airdrop()
cel_iphone.encender()

obj_cel = Celular("Gris", 256)
obj_cel.info()
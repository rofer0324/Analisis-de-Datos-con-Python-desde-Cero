class Celular:
    variable_ejemplo = "Ejemplo"
    
    def __init__(self, color):
        self.color =  color 
    
    def encender(self, contrasena):
        print(f"Encendiendo Telefono {contrasena}")
        #print(self.color)
    
    def apagar(self):
        print("Apagado")
        
objeto_celular = Celular("blanco")
print(objeto_celular.color)
objeto_celular.encender("0324")


    

    

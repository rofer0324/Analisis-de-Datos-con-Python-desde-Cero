from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
import sys

class AplicacionHelloWorld(QWidget):
    def __init__(self):
        super(AplicacionHelloWorld, self).__init__()
        self.emptywindow()
        
    def emptywindow(self):
        self.setGeometry(100, 100, 600, 1000)
        self.setWindowTitle('Aplicacion Hello World')
        self.displaylabels()
        
    def displaylabels(self):
        texto = QLabel(self)
        texto.setText("Hola Mundo")
        texto.move(250, 25)
        
        image = r"Seccion 15 - PyQt\World.jpg"
        try:
            with open(image):
                labelimage = QLabel(self)
                pixmap = QPixmap(image)
                labelimage.setPixmap(pixmap)
                labelimage.move(0, 100)
        
        except:
            print("No se pudo abrir la imagen")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = AplicacionHelloWorld()
    ventana.show()
    sys.exit(app.exec_()) # Metodo de salida limpia
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
import sys

class VentanaBoton(QWidget):
    def __init__(self):
        super(VentanaBoton, self).__init__()
        self.intialize()
        
    def intialize(self):
        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle('Ventana con Boton')
        self.mostrarBotones()
        
    def mostrarBotones(self):
        label = QLabel(self)
        label.setText("Presiona el Boton")
        label.move(100, 20)
        
        boton = QPushButton('Presioname', self)
        boton.move(105, 50)
        
        boton.clicked.connect(self.botonPresionado) 
        
    def botonPresionado(self):
        print("Boton Presionado - Se cierra la ventana")
        self.close()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaBoton()
    window.show()
    sys.exit(app.exec_()) # Metodo de salida limpia
        

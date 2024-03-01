from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import sys

class Grafica(FigureCanvasQTAgg):
    def __init__(self):
        figura = Figure()
        super(Grafica, self).__init__(figura)
        
        self.g1 = figura.add_subplot(111)
        
class Aplication(QWidget):
    def __init__(self):
        super(Aplication, self).__init__()
        self.mostrar_widgets()
        
    def mostrar_widgets(self):
        self.lned_x = QLineEdit(self) # Campo de texto para el eje x
        self.lned_y = QLineEdit(self) # Campo de texto para el eje y
        self.btn_graficar = QPushButton("Graficar", self)
        self.btn_limpiar = QPushButton("Limpiar", self)
        
        # Diseño de botones y campos
        hlyt = QHBoxLayout()
        hlyt.addWidget(self.lned_x)
        hlyt.addWidget(self.lned_y)
        hlyt.addWidget(self.btn_graficar)
        hlyt.addWidget(self.btn_limpiar)
        
        # Grafica
        self.grafica = Grafica()
        
        vlyt = QVBoxLayout(self)
        vlyt.addLayout(hlyt)
        vlyt.addWidget(self.grafica)
        
        self.btn_limpiar.clicked.connect(self.limpiar_grafica)
        self.btn_graficar.clicked.connect(self.graficar)
        
    def limpiar_grafica(self):
        self.grafica.g1.cla()
        self.grafica.draw()
        
    def graficar(self):
        x = int(self.lned_x.text())
        y = int(self.lned_y.text())
        
        self.grafica.g1.scatter(x, y)
        self.grafica.draw()
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Aplication()
    window.show()
    sys.exit(app.exec_()) # Metodo de salida limpia
        
        
import matplotlib.pyplot as plt
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFrame
import numpy as np


class Grafica(FigureCanvasQTAgg):
    def __init__(self):
        figura = plt.figure()
        super(Grafica, self).__init__(figura)
        self.grafica1 = figura.add_subplot(221)
        self.grafica2 = figura.add_subplot(222)
        self.grafica3 = figura.add_subplot(223)
        self.grafica4 = figura.add_subplot(224)

class Aplication(QMainWindow):
    def __init__(self):
        super(Aplication, self).__init__()
        grafica = Grafica()
        ###--- Graficas con Numeros Random ---###
        grafica.grafica1.scatter(np.random.randint(1, 15, size=5), np.random.randint(1, 26, size=5))
        grafica.grafica2.pie(np.random.randint(1, 100, size=5))
        grafica.grafica3.bar(np.random.randint(1, 50, size=5), np.random.randint(1, 26, size=5))
        grafica.grafica4.plot(np.random.randint(100, 200, size=5))
        
        # Objeto de barra de navegacion
        barra_navegacion = NavigationToolbar2QT(grafica, self)
        
        #Agregando Diseño
        vlyt = QVBoxLayout()
        vlyt.addWidget(barra_navegacion)
        vlyt.addWidget(grafica)
        
        # Agregar el diseño al frame
        contenedor = QFrame()
        contenedor.setLayout(vlyt)
        
        self.setCentralWidget(contenedor)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Aplication()
    window.show()
    sys.exit(app.exec_()) # Metodo de salida limpi
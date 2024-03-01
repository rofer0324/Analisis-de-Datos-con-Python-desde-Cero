from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt5.QtCore import QThread
import sys
import math
import time

class Hilo(QThread):
    def __init__(self, grafica):
        super(Hilo, self).__init__()
        self.grafica = grafica
        self.oscilacion = 50
        self.x = list(range(50))
        self.y = [self.funcion_graficar(valor) for valor in range(self.oscilacion)]
        
    def run(self):
        while True:
            self.graficar()
            time.sleep(.020)
    
    def funcion_graficar(self, valor):
        amplitud = 2
        frecuencia = 0.8
        resultado = amplitud * math.sin((2 * math.pi) * (frecuencia * valor) + valor)
        return resultado
    
    def graficar(self):
        self.grafica.g1.cla()
        self.grafica.g1.plot(self.x, self.y)
        self.oscilacion += 1
        self.y = self.y[1:] + [self.funcion_graficar(self.oscilacion)]
        self.grafica.draw()

class Grafica(FigureCanvasQTAgg):
    def __init__(self):
        figura = Figure()
        super(Grafica, self).__init__(figura)
        
        self.g1 = figura.add_subplot(111)
        
class Aplication(QMainWindow):
    def __init__(self):
        super(Aplication, self).__init__()
        self.mostrar_widget()
        
    def mostrar_widget(self):
        self.grafica = Grafica()
        self.setCentralWidget(self.grafica)
        
        # Instancia del Hilo
        self.hilo = Hilo(self.grafica)
        self.hilo.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Aplication()
    window.show()
    sys.exit(app.exec_()) # Metodo de salida limpia

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from .boton import BotonAnimado

class VentanaGrafica(QWidget):

    def __init__(self):
        super().__init__()

    # Layout de la ventana
        layout = QVBoxLayout(self)

    # Widge de la ventana
        contenedor_principal = QWidget()
        layout.addWidget(contenedor_principal)

    #Layout para botones
        layout_boton = QHBoxLayout(contenedor_principal)

    # Figura y área de dibujo
        self.fig = Figure(figsize=(8, 5))
        self.ax = self.fig.add_subplot(111)

    # Datos
        turnos = ["0", "1", "2", "3", "4"]
        probabilidades = [20,42, 23, 5, 4]

    # Gráfica
        self.ax.plot(turnos, probabilidades, marker="o")
        self.ax.set_title("RESULTADOS: PROBABILIDAD RELATIVA")
        self.ax.set_xlabel("TURNO")
        self.ax.set_ylabel("Probabilidad de ganar (%)")
        self.fig.tight_layout()

    # Integración con PySide6
        self.canvas = FigureCanvasQTAgg(self.fig)

    #Botones
        boton_reiniciar = BotonAnimado("Reiniciar",300,50)
        boton_menu = BotonAnimado("Menu",300,50)
        boton_salir = BotonAnimado("Salir",300,50)

        layout.addWidget(self.canvas)
        layout.addWidget(contenedor_principal)

        layout_boton.addWidget(boton_reiniciar)
        layout_boton.addWidget(boton_menu)
        layout_boton.addWidget(boton_salir)

    # Forzar el primer dibujo
        self.canvas.draw()

        print("Canvas creado:", self.canvas)
        print("Tamaño del canvas:", self.canvas.size())
        print("Widgets en el layout:", layout.count())




from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure



class VentanaGrafica(QWidget):

    def __init__(self):
        super().__init__()

        # Layout de la ventana
        layout = QVBoxLayout(self)

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
        layout.addWidget(self.canvas)

        # Forzar el primer dibujo
        self.canvas.draw()

        print("Canvas creado:", self.canvas)
        print("Tamaño del canvas:", self.canvas.size())
        print("Widgets en el layout:", layout.count())



from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QGridLayout
from PySide6.QtWidgets import QPushButton
from pathlib import Path
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, Signal
class SelectorCartas(QDialog): #ventana secundaria

    carta_selecionad = Signal(object)

    def __init__(self, mazo, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Seleccionar carta")
        self.resize(700, 500)

        self.mazo = mazo

        BASE_DIR = Path(__file__).resolve().parent.parent.parent

        # Organizar las cartas en filas y columnas
        self.layout_principal = QGridLayout(self)
        self.layout_principal.setSpacing(10)

        columnas = 12

        for indice, carta in enumerate(self.mazo): #Iteramos entre la posicion de la carta y la carta
            self.boton_carta = QPushButton()

            carta_path = (
                BASE_DIR
                / "resources"
                / "componentes"
                / "cartas"
                / carta.fotocarta
            )

            self.boton_carta.setIcon(QIcon(str(carta_path)))
            self.boton_carta.setIconSize(QSize(70, 100))
            self.boton_carta.setFixedSize(85, 115)

            self.boton_carta.clicked.connect(
                lambda checked=False, c=carta:
                self.seleccionar_carta(c)
            )

            fila = indice // columnas
            columna = indice % columnas

            self.layout_principal.addWidget(
                self.boton_carta, fila, columna
            ) #Coloca el boton en esta fila y esta columna

    def seleccionar_carta(self, carta):
        print("Carta seleccionada:", carta.fotocarta)
        self.carta_seleccionada.emit(carta)


